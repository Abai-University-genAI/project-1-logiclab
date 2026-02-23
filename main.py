import random

# ===== Логикалық функциялар =====
def logic_and(a, b):
    return a and b

def logic_or(a, b):
    return a or b

def logic_not(a):
    return not a

# ===== Truth Table =====
def print_truth_table():
    print("\nTRUTH TABLE (A AND B)")
    print("A B | Result")
    for a in [0, 1]:
        for b in [0, 1]:
            result = logic_and(bool(a), bool(b))
            print(a, b, "|", int(result))

# ===== Random есеп генерация =====
def generate_question():
    operation = random.choice(["AND", "OR", "NOT"])

    if operation == "NOT":
        a = random.randint(0, 1)
        correct_answer = logic_not(bool(a))
        print(f"\nNOT {a}")
        return int(correct_answer)

    else:
        a = random.randint(0, 1)
        b = random.randint(0, 1)

        if operation == "AND":
            correct_answer = logic_and(bool(a), bool(b))
            print(f"\n{a} AND {b}")

        elif operation == "OR":
            correct_answer = logic_or(bool(a), bool(b))
            print(f"\n{a} OR {b}")

        return int(correct_answer)

# ===== Негізгі бағдарлама =====
def main():
    correct = 0
    wrong = 0

    while True:
        print("\n1 - Random есеп")
        print("2 - Truth Table")
        print("0 - Шығу")

        choice = input("Таңда: ")

        if choice == "0":
            break

        elif choice == "1":
            correct_answer = generate_question()
            user_answer = int(input("Жауабы (0/1): "))

            if user_answer == correct_answer:
                print("Дұрыс!")
                correct += 1
            else:
                print("Қате!")
                wrong += 1

        elif choice == "2":
            print_truth_table()

    print("\n===== СТАТИСТИКА =====")
    print("Дұрыс:", correct)
    print("Қате:", wrong)

# ===== Бағдарламаны іске қосу =====
if __name__ == "__main__":
    main()