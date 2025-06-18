import sys
from datetime import datetime

# Global dictionary to store quiz questions
quiz_data = {}

# File path for logging
log_file = "quiz_log.txt"

# Function to log all transactions
def log_transaction(action):
    with open(log_file, "a") as file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f"[{timestamp}] {action}\n")

# Get valid input from user
def get_valid_option(prompt, valid_options):
    while True:
        choice = input(prompt).strip()
        if choice in valid_options:
            return choice
        print("❌ Invalid input. Please try again.")

# Add question to quiz
def add_question():
    try:
        question_id = input("Enter unique Question ID: ").strip()
        if question_id in quiz_data:
            print("❌ Question ID already exists.")
            return
        question = input("Enter the question: ").strip()
        options = []
        for i in range(4):
            option = input(f"Enter Option {i+1}: ").strip()
            options.append(option)
        answer = input("Enter the correct answer: ").strip()

        quiz_data[question_id] = {
            'question': question,
            'options': options,
            'answer': answer
        }
        print("✅ Question added successfully.")
        log_transaction(f"Added Question ID: {question_id}")
    except Exception as e:
        print(f"❌ Error occurred: {e}")

# View all questions
def view_questions():
    if not quiz_data:
        print("⚠️ No questions available.")
        return
    for qid, qdata in quiz_data.items():
        print(f"\nID: {qid}")
        print(f"Q: {qdata['question']}")
        for idx, opt in enumerate(qdata['options'], 1):
            print(f"{idx}. {opt}")
        print(f"Answer: {qdata['answer']}")

# Delete a question
def delete_question():
    qid = input("Enter Question ID to delete: ").strip()
    if qid not in quiz_data:
        print("❌ Question ID not found.")
        return
    confirm = input("Are you sure you want to delete this question? (Y/N): ").strip().lower()
    if confirm == 'y':
        del quiz_data[qid]
        print("✅ Question deleted.")
        log_transaction(f"Deleted Question ID: {qid}")
    else:
        print("ℹ️ Deletion cancelled.")

# Quiz Cracker - attempt the quiz
def start_quiz():
    if not quiz_data:
        print("⚠️ No questions to display.")
        return
    score = 0
    for qid, qdata in quiz_data.items():
        print(f"\nQ: {qdata['question']}")
        for i, opt in enumerate(qdata['options'], 1):
            print(f"{i}. {opt}")
        try:
            choice = int(input("Enter your choice (1-4): ").strip())
            if 1 <= choice <= 4:
                selected = qdata['options'][choice - 1]
                if selected.lower() == qdata['answer'].lower():
                    print("✅ Correct!")
                    score += 1
                else:
                    print(f"❌ Wrong. Correct answer: {qdata['answer']}")
            else:
                print("❌ Invalid option. Skipping question.")
        except:
            print("❌ Invalid input. Skipping question.")
    print(f"\n🎯 Quiz finished. Your score: {score}/{len(quiz_data)}")
    log_transaction(f"Quiz attempted. Score: {score}/{len(quiz_data)}")

# Quiz Master menu
def quiz_master_menu():
    while True:
        print("\n--- Quiz Master Menu ---")
        print("1. Add Question")
        print("2. View Questions")
        print("3. Delete Question")
        print("4. Exit to Main Menu")
        choice = get_valid_option("Enter choice (1-4): ", ['1', '2', '3', '4'])
        if choice == '1':
            add_question()
        elif choice == '2':
            view_questions()
        elif choice == '3':
            delete_question()
        elif choice == '4':
            break

# Main menu
def main_menu():
    while True:
        print("\n========== Quiz Game ==========")
        print("1. Quiz Master")
        print("2. Quiz Cracker")
        print("3. Exit")
        choice = get_valid_option("Enter choice (1-3): ", ['1', '2', '3'])
        if choice == '1':
            quiz_master_menu()
        elif choice == '2':
            start_quiz()
        elif choice == '3':
            print("👋 Exiting the game. Goodbye!")
            sys.exit()

# Entry point
if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        log_transaction(f"Error: {e}")
