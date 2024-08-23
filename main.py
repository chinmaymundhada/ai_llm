from pdf_parser import extract_text_from_pdf
from qa_system import answer_questions
from slack_bot import post_to_slack
from utils import load_questions, load_pdf_path
import dotenv
import os

# Load environment variables from .env file
dotenv.load_dotenv()

# Verify that the API key is loaded
if not os.getenv("OPENAI_API_KEY"):
    print("Error: OpenAI API key not found!")
    exit(1)  # Exit the script if the API key is not found

def main():
    # Load inputs
    questions = load_questions()
    pdf_path = load_pdf_path()

    # Extract text from PDF
    document_text = extract_text_from_pdf(pdf_path)

    # Get answers from the LLM
    answers = answer_questions(document_text, questions)

    # Post results to Slack
    post_to_slack(answers)

if __name__ == "__main__":
    main()
