import random

QUESTIONS = [
    {"q": "What is the capital of France?", "options": ["Berlin","Madrid","Paris","Rome"], "answer": "Paris"},
    {"q": "What is 12 x 12?", "options": ["124","144","132","148"], "answer": "144"},
    {"q": "Which planet is closest to the Sun?", "options": ["Venus","Earth","Mars","Mercury"], "answer": "Mercury"},
    {"q": "Who wrote Romeo and Juliet?", "options": ["Dickens","Shakespeare","Hemingway","Poe"], "answer": "Shakespeare"},
    {"q": "What is H2O?", "options": ["Oxygen","Hydrogen","Water","Salt"], "answer": "Water"},
    {"q": "How many continents are there?", "options": ["5","6","7","8"], "answer": "7"},
    {"q": "What is the largest ocean?", "options": ["Atlantic","Indian","Arctic","Pacific"], "answer": "Pacific"},
    {"q": "What year did World War II end?", "options": ["1943","1944","1945","1946"], "answer": "1945"},
    {"q": "What is the speed of light (approx)?", "options": ["300km/s","3000km/s","300000km/s","30km/s"], "answer": "300000km/s"},
    {"q": "What is the chemical symbol for gold?", "options": ["Ag","Fe","Au","Gd"], "answer": "Au"},
]

def play():
    print("=== Python Quiz Game ===")
    name = input("Enter your name: ").strip() or "Player"
    questions = random.sample(QUESTIONS, min(5, len(QUESTIONS)))
    score = 0

    for i, q in enumerate(questions, 1):
        print(f"
Q{i}: {q['q']}")
        opts = q["options"][:]
        random.shuffle(opts)
        for j, opt in enumerate(opts, 1):
            print(f"  {j}. {opt}")
        while True:
            ans = input("Your answer (1-4): ").strip()
            if ans in ["1","2","3","4"]:
                break
            print("Please enter 1, 2, 3, or 4")
        chosen = opts[int(ans)-1]
        if chosen == q["answer"]:
            print("  ✅ Correct!")
            score += 1
        else:
            print(f"  ❌ Wrong! Answer was: {q['answer']}")

    print(f"
🎉 {name}, your score: {score}/{len(questions)}")
    if score == len(questions):
        print("Perfect score! Amazing!")
    elif score >= len(questions) // 2:
        print("Good job!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    play()
    while input("
Play again? (y/n): ").lower() == "y":
        play()
