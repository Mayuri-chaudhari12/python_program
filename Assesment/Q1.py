import questions_data
import log_operations

def add_question():
    question_id = input("Enter Question ID: ").strip()
    question = input("Enter Question: ").strip()
    options = {}
    for i in range(1, 5):
        options[f"Option {i}"] = input(f"Enter Option {i}: ").strip()
    correct_answer = input("Enter the Correct Answer: ").strip()

    new_question = {
        'question': question,
        'options': options,
        'correct_answer': correct_answer
    }

    questions_data.questions[question_id] = new_question
    log_operations.log_action("Added", question_id)

    print(f"Question with ID {question_id} added successfully!")

def view_questions():
    if not questions_data.questions:
        print("No questions available.")
        return
 
    print("\n--- Available Questions ---")
    for question_id, data in questions_data.questions.items():
        print(f"ID: {question_id} - {data['question']}")
        for option, option_text in data['options'].items():
            print(f"{option}: {option_text}")
        print(f"Correct Answer: {data['correct_answer']}")
        print("-" * 30)

def delete_question():
    question_id = input("Enter the Question ID you want to delete: ").strip()

    if question_id not in questions_data.questions:
        print(f"No question found with ID {question_id}")
        return

    confirm = input(f"Are you sure you want to delete question ID {question_id}? (Y/N): ").strip().lower()
    if confirm == 'y':
        del questions_data.questions[question_id]
        log_operations.log_action("Deleted", question_id)
        print(f"Question ID {question_id} deleted successfully!")
    else:
        print("Deletion canceled.")

