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