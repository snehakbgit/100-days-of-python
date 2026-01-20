import random

score = 0
streak = 0
level = 1

print("🎮 Welcome to the Calculator Game!")
print("Solve math problems to earn points.")
print("Type 'q' anytime to quit.\n")

while True:
    # Increase difficulty with level
    max_num = level * 10
    num1 = random.randint(1, max_num)
    num2 = random.randint(1, max_num)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    print(f"Level {level} | Score: {score} | Streak: {streak}")
    user_input = input(f"What is {num1} {operator} {num2}? ")

    if user_input.lower() == 'q':
        print("\n👋 Game Over!")
        print(f"Final Score: {score}")
        break

    try:
        user_answer = int(user_input)
    except ValueError:
        print("❌ Invalid input! Numbers only.\n")
        continue

    if user_answer == correct_answer:
        streak += 1
        points = 10 + (streak * 2)
        score += points
        print(f"✅ Correct! +{points} points\n")
    else:
        print(f"❌ Wrong! Correct answer was {correct_answer}\n")
        streak = 0

    # Level up condition
    if score >= level * 50:
        level += 1
        print(f"🔥 Level Up! You are now Level {level}\n")
