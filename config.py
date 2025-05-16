# config.py

class Parameters:
    """
    Configurable parameters for the application.
    """

    # --- Model Configuration ---
    # For Gemini, common models: 'gemini-pro' (text), 'gemini-1.5-flash-latest', 'gemini-1.5-pro-latest'
    MODEL_GEMINI = 'gemini-1.5-flash-latest'  # Choose your preferred Gemini model

    # --- Prompts ---
    # Updated to guide Gemini for better parsing by get_questions_from_text
    QUESTIONS_PROMPT_TEMPLATE = """Job description: {job_description}

Based on the given job description, kindly formulate exactly ten relevant interview questions.
Each question should be a maximum of 30 words.
These questions should aim to assess the candidate's competency for the job role.
List the questions one per line, each starting with a number followed by a period and a space (e.g., "1. Your question here.").
Do not generate any other text before or after the list of questions."""

    EVALUATION_PROMPT_TEMPLATE = """
Job description: {job_description}

Candidate's Interview Transcript:
{interview_text}

As an AI interview assistant, your task is to evaluate the quality and depth of the candidate's responses based on the provided job description and their answers. Consider the following:

1.  **Relevance and Depth:** Does the candidate provide detailed answers that directly address the questions and demonstrate their understanding and expertise relevant to the job description?
2.  **Tangible Examples:** Are there specific, tangible examples in their responses that illustrate their skills and experiences as they relate to the tasks and qualifications mentioned in the job description?
3.  **Problem Solving & Achievement:** Does the candidate elaborate on how they have used necessary skills or experiences to overcome challenges or achieve results?
4.  **Role Fit:** Do the responses suggest the candidate has the ability to perform well in the role's complexities and challenges?

Based on your evaluation:

If the candidate's responses are inadequate, vague, or don't clearly demonstrate the needed skills or experiences for this specific role, tactfully communicate this by starting your response with: "Thank you for your responses. However, based on the answers provided, it appears there may be a misalignment with the requirements of the role we're seeking to fill. At this time, we cannot extend an offer. We appreciate your time and effort and wish you the best in your future endeavors." Then, you can optionally add a brief, constructive summary of why.

If the responses indicate a strong fit for the role, acknowledge the candidate's suitability by starting your response with: "Thank you for your thoughtful responses. Based on your answers, it appears that your skills, experience, and understanding align well with the requirements of the role. We will be in touch with the next steps." Then, you can optionally add a brief summary of their strengths.

Provide only the evaluation message.
"""