#using tuples and lists to create a quiz game
questions = ("How many continents are there on Earth? ",
             "How many elements are there in the periodic table? ",
             "What is the most abudant gas in the Earth's atmosphere? ",
             "How many bones are there in the human body? ",
             "What is the largest planet in our solar system? ")

options = (("A. 5", "B. 6", "C. 7", "D. 8"),
           ("A. 108", "B. 118", "C. 128", "D. 138"),
           ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 208", "C. 210", "D. 212"),
           ("A. Earth", "B. Jupiter", "C. Saturn", "D. Neptune"))

answers = ("C", "B", "B", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("\n" + question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
        print(f"The correct answer was: {answers[question_num]}")
    question_num += 1