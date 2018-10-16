from random import randint
from getpass import getpass

def main():
    die_again = True

    print("[===-==-=-==-===-=-==-===-==-=-==-===-==-=-==-===]")
    print("[ ***                                        *** ]")
    print("[   ***      ROCK - PAPER - SCISSORS        ***  ]")
    print("[    ***                                   ***   ]")
    print("[   ***            MORTAL COMBAT            ***  ]")
    print("[ ***                                        *** ]")
    print("[===-==-=-==-===-=-==-===-==-=-==-===-==-=-==-===]\n")

    name_p1 = input(" PLAYER 1 enter you name: ")
    name_p2 = input(" PLAYER 2 enter you name: ")
    print("")

    while die_again:
        weapon_p1 = ""
        weapon_p2 = ""

        select_weapon(name_p1)
        while True:
            weapon_p1 = getpass("")
            try:
                weapon_p1 = int(weapon_p1)
            except ValueError:
                print(" [INPUT ERROR] Weapon not available\n")
                select_weapon(name_p1)
                continue
            if weapon_p1 not in [1, 2, 3]:
                print(" [INPUT ERROR] Weapon not available\n")
                select_weapon(name_p1)
            else:
                break

        select_weapon(name_p2)
        while True:
            weapon_p2 = getpass("")
            try:
                weapon_p2 = int(weapon_p2)
                break
            except ValueError:
                print(" [INPUT ERROR] Weapon not available\n")
                select_weapon(name_p2)
            if weapon_p2 not in [1, 2, 3]:
                print(" [INPUT ERROR] Weapon not available\n")
                select_weapon(name_p2)
            else:
                break

        print("+------------------------------------------------+")
        if weapon_p1 == weapon_p2:
            print(" When the dust settles two man lie dead on the\n ground covered in blood...")
            print("\n +2 for the grim reaper.")
        else:
            if weapon_p1 < weapon_p2:
                if weapon_p1 - weapon_p2 == -1:
                    surviver = name_p2
                    surviver_weapon = weapon_p2
                    victim = name_p1
                else:
                    surviver = name_p1
                    surviver_weapon = weapon_p1
                    victim = name_p2
            else:
                if weapon_p2 - weapon_p1 == -1:
                    surviver = name_p1
                    surviver_weapon = weapon_p1
                    victim = name_p2
                else:
                    surviver = name_p2
                    surviver_weapon = weapon_p2
                    victim = name_p1

            if surviver_weapon == 1:
                print(" %s picks up a rock and smashes %s head\n with such brutal force that the head gets\n split off from the rest of the body,\n which hits the ground in the shape of a scissor." % (surviver, victim))
            elif surviver_weapon == 2:
                print(" %s cuts %s`s body into pieces.\n And this poor guy thought he was hard as a rock." % (surviver, victim))
            else:
                print(" %s stabs %s %d times with a scissor like\n he was paper!" % (surviver, victim, randint(2,42)))
        print("+------------------------------------------------+\n")

        die_again = input(" Die again? [y/n] ")
        if die_again == "y":
            die_again = True
        else:
            die_again = False

def choice_to_text(choice):
    if choice == 1:
        return "Rock"
    elif choice == 2:
        return "Paper"
    else:
        return "Scissors"

def select_weapon(player_name):
    print(" Choose your weapon %s:" % player_name)
    print("  Rock     - 1")
    print("  Paper    - 2")
    print("  Scissors - 3")

if __name__ == "__main__":
    main()
