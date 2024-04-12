def main():
    return

def make_choice(choices):
    print("\nWähle eine Option:")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice = int(input("Deine Wahl: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Ungültige Eingabe. Bitte wähle eine gültige Option.")
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine Zahl ein.")