import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def answer_questions(document_text, questions):
    answers = {}
    for question in questions:
        response = openai.Completion.create(
            engine="gpt-4o-mini",
            prompt=f"{document_text}\n\nQuestion: {question}\nAnswer:",
            max_tokens=100
        )
        answer = response.choices[0].text.strip()
        if not answer or "Data Not Available" in answer:
            answer = "Data Not Available"
        answers[question] = answer
    return answers
