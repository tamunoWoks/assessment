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
                        print(
                            f"Incorrect. The correct answer is {correct_answer.upper()}."
                        )
                    break
                else:
                    print("Invalid option")

        def civil(self):
            # Questions for Civil Engineering
            questions = [
                (
                    "\nQ1. What is the primary purpose of reinforcement in concrete?\n"
                    "A. To reduce the weight of the concrete structure.\n"
                    "B. To improve its tensile strength.\n"
                    "C. To increase its compressive strength.\n"
                    "D. To enhance its aesthetic appearance.\n",
                    "b",
                ),
                (
                    "\nQ2. What is the primary purpose of a soil compaction test?\n"
                    "A. To determine the soil's moisture content.\n"
                    "B. To test the soil's permeability.\n"
                    "C. To determine the soil's mineral content.\n"
                    "D. To increase the soil's density.\n",
                    "d",
                ),
                (
                    "\nQ3. What is Manning's equation used for?\n"
                    "A. Calculating the velocity of flow in an open channel.\n"
                    "B. Calculating the velocity of flow in a closed pipe.\n"
                    "C. Determining the pressure in a water distribution system.\n"
                    "D. Estimating the flow rate in a sewer system.\n",
                    "a",
                ),
                (
                    "\nQ4. What information does a hydrograph provide?\n"
                    "A. The velocity of flow in a river.\n"
                    "B. The water quality parameters of a river.\n"
                    "C. The rate of flow (discharge) versus time past a specific point.\n"
                    "D. The temperature variations in a water body.\n",
                    "c",
                ),
                (
                    "\nQ5. What does the Level of Service (LOS) in traffic engineering describe?\n"
                    "A. The maximum speed limit on a road.\n"
                    "B. The capacity of a parking lot.\n"
                    "C. The number of traffic signals on a road.\n"
                    "D. The operational conditions of a roadway or intersection.\n",
                    "d",
                ),
            ]
            for question, correct_answer in questions:
                self.ask_question(question, correct_answer)

        def electrical(self):
            # Questions for Electrical Engineering
            questions = [
                (
                    "\nQ1. What is Ohm's Law?\n"
                    "A. V = IR\n"
                    "B. P = IV\n"
                    "C. P = IRV\n"
                    "D. V = IRP\n",
                    "a",
                ),
                (
                    "\nQ2. What is the unit of magnetic flux?\n"
                    "A. Tesla.\n"
                    "B. Weber.\n"
                    "C. Gauss.\n"
                    "D. Henry.\n",
                    "b",
                ),
                (
                    "\nQ3. What is the function of a transformer?\n"
                    "A. To convert AC to DC.\n"
                    "B. To store electrical energy.\n"
                    "C. To increase the frequency of AC.\n"
                    "D. To step up or step down AC voltage.\n",
                    "d",
                ),
                (
                    "\nQ4. What is a three-phase power system primarily used for?\n"
                    "A. Reducing energy consumption.\n"
                    "B. Improving power factor.\n"
                    "C. Efficient transmission of electrical power.\n"
                    "D. Converting AC to DC.\n",
                    "c",
                ),
                (
                    "\nQ5. What is the purpose of a diode in an electrical circuit?\n"
                    "A. To amplify signals.\n"
                    "B. To store electrical energy.\n"
                    "C. To resist changes in current.\n"
                    "D. To allow current to flow in one direction only.\n",
                    "d",
                ),
            ]
            for question, correct_answer in questions:
                self.ask_question(question, correct_answer)

        def computer(self):
            # Questions for Computer Engineering
            questions = [
                (
                    "\nQ1. Which sorting algorithm has the best average time complexity?\n"
                    "A. Bubble Sort\n"
                    "B. Quick Sort\n"
                    "C. Selection Sort\n"
                    "D. Insertion Sort\n",
                    "b",
                ),
                (
                    "\nQ2. What does GUI stand for?\n"
                    "A. Graphical User Interface.\n"
                    "B. General User Interface.\n"
                    "C. Global User Interface.\n"
                    "D. Guided User Interface.\n",
                    "a",
                ),
                (
                    "\nQ3. In a network, what is the function of a router?\n"
                    "A. To store data.\n"
                    "B. To provide a wireless signal.\n"
                    "C. To translate domain names into IP addresses.\n"
                    "D. To manage network traffic.\n",
                    "d",
                ),
                (
                    "\nQ4.Which of the following is not a type of computer bus?\n"
                    "A. Data Bus.\n"
                    "B. Address Bus.\n"
                    "C. Output Bus.\n"
                    "D. Control Bus.\n",
                    "c",
                ),
                (
                    "\nQ5. Which of the following is an example of an operating system?\n"
                    "A. Python.\n"
                    "B. MySQL.\n"
                    "C. Ethernet.\n"
                    "D. Windows.\n",
                    "d",
                ),
            ]
            for question, correct_answer in questions:
                self.ask_question(question, correct_answer)

        def mechanical(self):
            # Questions for Mechanical Engineering
            questions = [
                (
                    "\nQ1. What is the SI unit of stress?\n"
                    "A. Pascal\n"
                    "B. Quick Sort\n"
                    "C. Selection Sort\n"
                    "D. Insertion Sort\n",
                    "a",
                ),
                (
                    "\nQ2. What is the first law of thermodynamics also known as?\n"
                    "A. Law of conservation of mass.\n"
                    "B. Law of conservation of energy.\n"
                    "C. Law of entropy.\n"
                    "D. Law of action and reaction.\n",
                    "b",
                ),
                (
                    "\nQ3. Which type of heat transfer occurs due to the movement of fluid?\n"
                    "A. Conduction.\n"
                    "B. Convection.\n"
                    "C. Radiation.\n"
                    "D. None of the above.\n",
                    "b",
                ),
                (
                    "\nQ4. Which of the following materials has the highest thermal conductivity?\n"
                    "A. Copper.\n"
                    "B. Aluminum.\n"
                    "C. Steel.\n"
                    "D. Glass.\n",
                    "a",
                ),
                (
                    "\nQ5. What is the primary purpose of a flywheel in an engine?\n"
                    "A. To cool the engine.\n"
                    "B. To reduce friction.\n"
                    "C. To increase speed.\n"
                    "D. To store rotational energy.\n",
                    "d",
                ),
            ]
            for question, correct_answer in questions:
                self.ask_question(question, correct_answer)

        def calculate_score(self):
            # Calculate the percentage score
            percentage = (self.score / 5) * 100
            return round(percentage)

        def grade(self, final_score):
            # Assign a grade based on the final score
            if final_score >= 80:
                return "Excellent!!!"
            elif final_score >= 70:
                return "Good!!!"
            elif final_score >= 60:
                return "Pass!!!"
            else:
                return "Fail, Resit the exam!!!"


if __name__ == "__main__":
    # Create an instance of the test and start the main function
    test = EngineeringTest()
    test.main()
