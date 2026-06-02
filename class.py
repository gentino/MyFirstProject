# Simple Python Quiz Test

score = 0

print("Welcome to the Python Quiz!\n")

# Question 1
answer = input("1. What keyword is used to define a function in Python? ")
if answer.lower() == "def":
    score += 1

# Question 2
answer = input("2. What data type is used to store True or False values? ")
if answer.lower() == "boolean" or answer.lower() == "bool":
    score += 1

# Question 3
answer = input("3. Which function is used to display output in Python? ")
if answer.lower() == "print":
    score += 1

# Question 4
answer = input("4. What symbol is used for comments in Python? ")
if answer == "#":
    score += 1

# Question 5
answer = input("5. What keyword is used to create a loop that repeats while a condition is true? ")
if answer.lower() == "while":
    score += 1

print("\nQuiz Completed!")
print(f"Your score: {score}/5")

if score == 5:
    print("Excellent! 🎉")
elif score >= 3:
    print("Good job! 👍")
else:
    print("Keep practicing! 📚")