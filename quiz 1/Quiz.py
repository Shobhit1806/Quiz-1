users = []  # List to store user dictionaries (username, password, scores)
questions = [ 
    {
        "question": "Which of the following is a valid SQL statement to retrieve all rows from a table?",
        "options": ["SELECT * FROM table_name;", "GET ALL FROM table_name;", "FETCH * FROM table_name;", "EXTRACT * FROM table_name;"],
        "correct": "A"
    },
    {
        "question": "What does the term 'normalization' in DBMS refer to?",
        "options": ["Ensuring the database runs faster.",
                    "Dividing the database into smaller tables and eliminating redundancy.",
                    "Backing up the database.",
                    "Adding more data to the database."],
        "correct": "B"
    },
    {
        "question": "In an ER diagram, an entity set is represented by:",
        "options": ["Rectangle", "Ellipse", "Diamond", "Triangle"],
        "correct": "A"
    },
    {
        "question": "A transaction in DBMS must follow which set of properties?",
        "options": ["ACID (Atomicity, Consistency, Isolation, Durability)",
                    "BASE (Basically Available, Soft State, Eventual Consistency)",
                    "CRUD (Create, Read, Update, Delete)",
                    "DML (Data Manipulation Language)"],
        "correct": "A"
    },
    {
        "question": "What is the primary purpose of an index in a database?",
        "options": ["To increase data redundancy.",
                    "To speed up query processing.",
                    "To secure the data.",
                    "To store a backup of the data."],
        "correct": "B"
    }
]

def register():
    """Register a new user."""
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    
    for user in users:
        if user["username"] == username:
            print("Username already exists. Please try a different one.")
            return

    users.append({"username": username, "password": password, "scores": []})
    print("Registration successful!")


def login():
    """Log in an existing user."""
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    
    for user in users:
        if user["username"] == username and user["password"] == password:
            print("Login successful!")
            return user

    print("Invalid credentials. Please try again.")
    return None


def attempt_quiz(user):
    """Allow the user to attempt the quiz."""
    score = 0

    for idx, question in enumerate(questions):
        print(f"\nQuestion {idx + 1}: {question['question']}")
        print(f"A. {question['options'][0]}")
        print(f"B. {question['options'][1]}")
        print(f"C. {question['options'][2]}")
        print(f"D. {question['options'][3]}")

        answer = input("Enter your answer (A/B/C/D): ").upper()
        if answer == question["correct"]:
            score += 10  # Assume each question is worth 10 points

    print(f"\nYou scored: {score}")
    user["scores"].append(score)  


def view_results(user):
    """View the user's quiz results."""
    if user["scores"]:
        print("\nYour Scores:")
        for idx, score in enumerate(user["scores"], 1):
            print(f"Attempt {idx}: {score} points")
    else:
        print("\nNo scores found. You haven't attempted any quizzes yet.")


def view_all_users():
    """Admin function to view all registered users and their scores."""
    print("\n--- All Registered Users ---")
    if not users:
        print("No users registered yet.")
        return

    for user in users:
        print(f"Username: {user['username']}, Scores: {user['scores']}")


def main():
    while True:
        print("\n--- Quiz App Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. View All Users (Admin)")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                while True:
                    print("\n--- User Menu ---")
                    print("1. Attempt Quiz")
                    print("2. View Results")
                    print("3. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        attempt_quiz(user)
                    elif user_choice == "2":
                        view_results(user)
                    elif user_choice == "3":
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == "3":
            view_all_users()
        elif choice == "4":
            print("Thank you for using the Quiz App!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()