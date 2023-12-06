import json
from difflib import get_close_matches
import os

def load_knowledge_base() -> dict:
    print('Loading knowledge base...')
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_path, 'knowledge_base.json')

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            print('Knowledge base loaded.')
            return json.load(file)
    else:
        return {}

def save_knowledge_base(file_path: str, data: dict):
    print(f'Saving knowledge base to {file_path}...')
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_path, file_path)
    with open(file_path, 'w') as file:
        print('Knowledge base saved.')
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base['questions']:
        if q['question'] == question:
            return q['answer']
        

def chat_bot():
    knowledge_base: dict = load_knowledge_base()
    print('Bot: Hello, I am a chatbot. I will answer your questions about the chatbot.')
    while True:
        user_question: str = input('You: ')
        if user_question.lower() == 'bye':
            print('Bot: See you later!')
            break

        best_match: str | None = find_best_match(user_question, [q["question"] for q in knowledge_base["questions"]])
        if best_match:
            print(f'Bot: {get_answer_for_question(best_match, knowledge_base)}')
        else:
            print('Bot: Sorry, I do not understand. Please teach me.')
            new_answer: str = input('Type the answer or "skip" to skip this question: ')
            if new_answer.lower() == 'skip':
                continue

            knowledge_base['questions'].append({
                'question': user_question,
                'answer': new_answer
            })
            save_knowledge_base('knowledge_base.json', knowledge_base)
            print('Bot: Thank you for teaching me!')

if __name__ == '__main__':
    chat_bot()