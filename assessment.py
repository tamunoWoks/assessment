from sys import exit


class EngineeringTest:
    def __init__(self):
        # Initialize the score to zero
        self.score = 0


        def main(self):
            print("Welcome to the Engineering Internship assessment Test!\n")

            # Ask if the user is ready for the test
            play = input("Are you ready for your test? ").strip()
            self.ready(play)

            # Ask the user for their field of engineering
            dept = input("\nWhat is your field of Engineering? ").strip()
            field_name = self.field(dept)
            print(
                f"welcome to your {field_name} Engineering Assessment Test!!!"
                "Choose the correct option among options A, B, C and D"
            )

            # Direct to the appropriate department based on user input
            if dept.lower() == "civil":
                self.civil()
            elif dept.lower() == "electrical":
                self.electrical()
            elif dept.lower() == "computer":
                self.computer()
            elif dept.lower() == "mechanical":
                self.mechanical()
            else:
                print("Invalid department. Exiting the test.")
                exit()

            # Calculate and display the final score
            final_score = self.calculate_score()
            print(f"\nYou got {self.score} correct")
            print(f"Your score is {final_score}%")
            print(self.grade(final_score))


        def ready(self, playing):
            # Check if user is ready for test
            while True:
                if playing.lower() in ("no", "n"):
                    print("Come back when you are ready!!")
                    exit()
                elif playing.lower() in ("yes", "y"):
                    return "Okay! Let's begin, Goodluck!"
                else:
                    print("Answer yes or no")
                    playing = input("Are you ready for your test? ").strip()


        def field(self, dept):
            # Validate user's engineering field
            while True:
                if dept.lower() in ("computer", "electrical", "mechanical", "civil"):
                    return dept.capitalize()
                else:
                    print(
                        "This test accomodates only Computer, Electrical, Mechanical and Civil Engineering"
                    )
                dept = input("What is your field of Engineering? ").strip()


        def ask_question(self, question, correct_answer):
            # Ask a question and validate the answer
            while True:
                answer = input(question + "Your answer: ").strip().lower()
                if answer in ("a", "b", "c", "d"):
                    if answer == correct_answer:
                        print("Correct!")
                        self.score += 1
                    else:
                        print(f"Incorrect. The correct answer is {correct_answer.upper()}.")
                    break
                else:
                    print("Invalid option")
