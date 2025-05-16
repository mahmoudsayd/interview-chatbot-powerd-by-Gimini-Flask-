# gemini_utils.py
from dotenv import load_dotenv
import os
import google.generativeai as genai
from google.api_core import exceptions as google_exceptions
import re
from typing import List
from config import Parameters

# ---- ADD THIS LINE AT THE TOP ----
load_dotenv()  # Load environment variables from .env file
# ----------------------------------

# --- Gemini API Key Configuration ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
    except Exception as e:
        print(f"Error configuring Gemini API: {e}. Ensure GEMINI_API_KEY is set correctly.")
else:
    print("Warning: GEMINI_API_KEY environment variable not found. The API will not be functional.")


def get_completion_gemini(complete_prompt: str, model_name: str = Parameters.MODEL_GEMINI, temperature: float = 0.1) -> str:
    """
    Send a message to the Google Gemini API to get a response.
    Allows specifying temperature.
    """
    if not GEMINI_API_KEY:
        error_msg = "Error: Gemini API key not configured. Please set the GEMINI_API_KEY environment variable."
        print(error_msg)
        return error_msg

    try:
        model = genai.GenerativeModel(model_name)
        generation_config = genai.types.GenerationConfig(
            temperature=temperature # Use the passed temperature
        )

        response = model.generate_content(
            complete_prompt,
            generation_config=generation_config,
        )

        if not response.candidates: # Check if response.candidates is empty or None
            block_reason = "Unknown"
            block_reason_message = "No message"
            if response.prompt_feedback: # This might also be None if candidates is None
                block_reason = response.prompt_feedback.block_reason or "Unknown"
                block_reason_message = response.prompt_feedback.block_reason_message or "No message"
            return f"Error: Content generation blocked or no candidates returned. Reason: {block_reason}. Message: {block_reason_message}"
        
        # Ensure there's content in the first candidate
        if not response.candidates[0].content or not response.candidates[0].content.parts:
            return "Error: Received an empty response from the API (no content parts)."
            
        return response.text # .text will access candidates[0].content.parts[0].text

    except google_exceptions.InvalidArgument as e:
        print(f"Encountered an InvalidArgument error (often due to prompt issues or model compatibility): {e}")
        return "Error: Input too long or invalid for model, or prompt issue."
    except google_exceptions.ResourceExhausted as e:
        print(f"Encountered a ResourceExhausted error: {e}")
        return "Error: API quota exceeded or rate limit hit."
    except google_exceptions.GoogleAPIError as e:
        print(f"A Google API error occurred: {e}")
        return f"Error: A Google API error occurred: {e.args[0] if e.args else str(e)}"
    except AttributeError as e:
        if "'NoneType' object has no attribute 'parts'" in str(e) or "'NoneType' object has no attribute 'text'" in str(e) or "candidates" in str(e).lower():
            return "Error: Received an empty or malformed response from the API."
        print(f"An unexpected AttributeError occurred: {e}")
        return "Error: An unexpected attribute error occurred during API call."
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "Error: An unexpected error occurred during API call."


def get_questions_from_text(text_questions: str) -> List[str]:
    """
    Extract all questions from the concatenated_questions string using regular expressions.
    Expects questions to be formatted as "1. Question text"
    """
    if not text_questions or text_questions.startswith("Error:"):
        return [] # Return empty list if input is an error or empty
    question_list = re.findall(r'^\s*\d+\.\s*(.+?)\s*$', text_questions, re.MULTILINE)
    return [q.strip() for q in question_list if q.strip()]