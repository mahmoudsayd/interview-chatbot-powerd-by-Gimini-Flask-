import uuid
from flask import Flask, request, render_template, redirect, url_for, session, flash
from gemini_utils import get_completion_gemini, get_questions_from_text, GEMINI_API_KEY
from config import Parameters
from job_descriptions import get_job_description
import os # for job role list

app = Flask(__name__)
app.secret_key = os.urandom(24) # More secure secret key for sessions

# Helper to get available job roles for the dropdown
def get_available_job_roles():

    return [
        "Data Scientist", "Backend Developer", "Frontend Developer",
        "AI/ML Engineer", "DevOps Engineer", "Mobile App Developer",
        "Cybersecurity Analyst",
        "Cloud Architect",
        "Data Engineer", 
        "UI/UX Designer",
        "Product Manager (Tech)", 
        "Full Stack Developer",
        "Game Developer",
        "QA Engineer (Software Tester)",
        "Network Engineer",
        "Database Administrator (DBA)",
        "Solutions Architect",
        "Marketing Manager",
        "Sales Representative",
        "Human Resources Manager",
        "Business Analyst",
        "Operations Manager",
        "Project Manager (General)",
        "Financial Analyst",
        "Customer Success Manager",
        "Supply Chain Manager",
        "Graphic Designer",
        "Content Writer / Copywriter",
        "Video Editor",
        "Social Media Manager",
        "Registered Nurse (RN)",
        "Medical Researcher",
        "Lab Technician",
        "Technical Writer",
        "Recruiter / Talent Acquisition Specialist",
        "Systems Administrator",
        "Customer Support Specialist"
    ]

def _handle_api_error(response_text: str, context: str) -> bool:
    """Checks for error string and flashes a message if an error occurred."""
    if response_text and response_text.startswith("Error:"):
        session['error_message'] = f"API Error during {context}: {response_text}"
        flash(session['error_message'], 'danger') # Using Flask's flash messaging
        return True
    session.pop('error_message', None) # Clear previous error
    return False

def _generate_uuid() -> str:
    return str(uuid.uuid4())

@app.route('/', methods=['GET'])
def index():
    # Clear previous interview session data if any
    session.pop('job_role', None)
    session.pop('questions', None)
    session.pop('answers', None)
    session.pop('current_question_index', None)
    session.pop('evaluation', None)
    session.pop('error_message', None)
    
    available_roles = get_available_job_roles()
    return render_template('index.html', available_roles=available_roles)

@app.route('/start_interview', methods=['POST'])
def start_interview_route():
    job_role = request.form.get('job_role')
    if not job_role:
        flash("Please select a job role.", "warning")
        return redirect(url_for('index'))

    session['job_role'] = job_role
    session['questions'] = []
    session['answers'] = [] # list of tuples (answer_text, question_uuid_it_answers)
    session['current_question_index'] = 0
    session['evaluation'] = None
    session.pop('error_message', None) # Clear any previous errors

    job_description = get_job_description(job_role)
    if "No job description available" in job_description:
        flash(f"No job description found for '{job_role}'. Please select another role.", "danger")
        return redirect(url_for('index'))

    prompt = Parameters.QUESTIONS_PROMPT_TEMPLATE.format(job_description=job_description)
    
    # Use temperature 0.1 for question generation as per original config
    raw_questions_text = get_completion_gemini(prompt, temperature=0.7)

    if _handle_api_error(raw_questions_text, "question generation"):
        return redirect(url_for('index')) # Redirect to start if questions fail

    generated_questions = get_questions_from_text(raw_questions_text)

    if not generated_questions:
        err_msg = "No questions were extracted from the AI's response. The response might have been empty or improperly formatted."
        session['error_message'] = err_msg
        flash(err_msg, 'danger')
        return redirect(url_for('index'))

    # Store questions with UUIDs
    session['questions'] = [(q, _generate_uuid()) for q in generated_questions]
    session.modified = True # Important when modifying mutable types in session
    
    return redirect(url_for('interview_page'))


@app.route('/interview', methods=['GET', 'POST'])
def interview_page():
    if 'job_role' not in session or 'questions' not in session:
        flash("Interview not started. Please select a job role first.", "info")
        return redirect(url_for('index'))

    job_role = session['job_role']
    questions = session.get('questions', []) # List of (question_text, uuid)
    answers = session.get('answers', [])     # List of (answer_text, question_uuid_it_answers, original_question_text)
    current_q_idx = session.get('current_question_index', 0)

    if request.method == 'POST':
        answer_text = request.form.get('answer')
        if answer_text and current_q_idx < len(questions):
            current_question_text, current_question_uuid = questions[current_q_idx]
            # Store answer with the UUID of the question it answers and the question text itself
            answers.append((answer_text, current_question_uuid, current_question_text))
            session['answers'] = answers
            session['current_question_index'] = current_q_idx + 1
            session.modified = True
            # Redirect to GET to prevent form resubmission issues
            return redirect(url_for('interview_page'))
        elif not answer_text:
            flash("Please provide an answer.", "warning")
        # If no answer_text or already past last question, just re-render (or redirect to GET)
        return redirect(url_for('interview_page'))


    # Prepare display data
    past_q_and_a = []
    # Answers are stored as (answer_text, question_uuid, original_question_text)
    # Questions are stored as (question_text, question_uuid)
    # We need to match them carefully. A simpler way is to just iterate through submitted answers.
    for ans_text, q_uuid, q_text in answers:
         past_q_and_a.append({'question': q_text, 'answer': ans_text})
    
    current_question_text = None
    if current_q_idx < len(questions):
        current_question_text = questions[current_q_idx][0]

    all_questions_answered = current_q_idx >= len(questions) and len(questions) > 0
    evaluation_result = session.get('evaluation')

    if all_questions_answered and not evaluation_result:
        # Perform evaluation
        interview_parts = []
        for i, (ans_text, q_uuid, q_text) in enumerate(answers):
            interview_parts.append(f"Question {i+1}: {q_text}\nAnswer {i+1}: {ans_text}")
        
        interview_text_for_eval = "\n\n".join(interview_parts)
        job_description = get_job_description(job_role)

        eval_prompt = Parameters.EVALUATION_PROMPT_TEMPLATE.format(
            job_description=job_description,
            interview_text=interview_text_for_eval
        )
        # Use temperature 0.0 for evaluation for more deterministic output
        evaluation_result = get_completion_gemini(eval_prompt, temperature=0.0)
        
        if _handle_api_error(evaluation_result, "candidate evaluation"):
            # Error already flashed, evaluation_result will contain the error message
             pass # Let the template display the error from session['error_message']
        session['evaluation'] = evaluation_result
        session.modified = True

    return render_template('interview.html',
                           job_role=job_role,
                           current_question=current_question_text,
                           past_q_and_a=past_q_and_a,
                           all_questions_answered=all_questions_answered,
                           evaluation=session.get('evaluation'), # Use the potentially updated evaluation
                           error_message=session.get('error_message'))


@app.route('/reset', methods=['GET'])
def reset_interview():
    session.clear()
    flash("Interview reset. Please start a new one.", "info")
    return redirect(url_for('index'))

if __name__ == '__main__':
    if not GEMINI_API_KEY:
        print("CRITICAL: GEMINI_API_KEY is not set. The application will not function correctly.")
        print("Please set it in your environment or in a .env file.")
    app.run(debug=True)

    get_available_job_roles