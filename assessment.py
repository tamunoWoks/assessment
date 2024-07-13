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