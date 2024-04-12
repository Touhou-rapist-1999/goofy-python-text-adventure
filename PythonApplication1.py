import time
import story_branch1
import story_branch2
import inventory
import stats
from make_choices import make_choice

def intro():
    print("Willkommen beim Text-Adventure!")
    time.sleep(1)
    print("Du befindest dich in einem mysteriösen Ort ...")
    time.sleep(1)
    print("Deine Entscheidungen ziehen Konsequenzen mit sich!")


def main():
    intro()
    print("\nDu stehst vor einer Entscheidung:")
    time.sleep(1)

    choices = ["Der Weg eines Helden", "Die dunklen Wälder"]
    choice = make_choice(choices)

    if choice == 1:
        story_branch1.main()
    else:
        story_branch2.main()

    print("Das spiel ist vorbei. Es wird Zeit dich zurück in die Hölle zu schicken. Abenteurer, grüße meinen Bruder von mir wenn du da bist!")

if __name__ == "__main__":
    main()