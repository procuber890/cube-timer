import random

def generate_scramble(moves=20):
    # Define possible moves
    faces = ['R', 'L', 'U', 'D', 'F', 'B']
    modifiers = ['', "'", '2']
    scramble = []

    for _ in range(moves):
        while True:
            move = random.choice(faces) + random.choice(modifiers)
            if len(scramble) == 0 or scramble[-1][0] != move[0]:
                scramble.append(move)
                break

    return ' '.join(scramble)

def practice_all_plls():
    pll_algorithms = {
        "Ua": "R2 U R U R' U' R' U' R' U R'",
        "Ub": "R U' R U R U R U' R' U' R2",
        "H": "M2 U M2 U2 M2 U M2",
        "Z": "M2 U M2 U M' U2 M2 U2 M' U2",
        "Aa": "x R' U R' D2 R U' R' D2 R2 x'",
        "Ab": "x' R U' R D2 R' U R D2 R2 x",
        "E": "x' R U' R D R' U R D' R' U R D R' U' R x",
        "T": "R U R' U' R' F R2 U' R' U' R U R' F'",
        "Y": "F R U' R' U' R U R' F' R U R' U' R' F R F'",
        "F": "R' U' F' R U R' U' R' F R2 U R' U' R U R' U R",
        "Ja": "x R2 F R F' R U2 r' U r U2 x'",
        "Jb": "R U R' F' R U R' U' R' F R2 U' R' U'",
        "Ra": "R U R' F' R U2 R' U2 R' F R U R U2 R'",
        "Rb": "R' U2 R U2 R' F R U R' U' R' F' R2 U'",
        "Na": "L U' R U2 L' U R' L U' R U2 L' U R'",
        "Nb": "R' U L' U2 R U' L R' U L' U2 R U' L",
        "V": "R' U R' U' y R' F' R2 U' R' U R' F R F",
        "Ga": "R2 U R' U R' U' R U' R2 D U' R' U R D'",
        "Gb": "R' U' R U D' R2 U R' U R U' R U' R2 D",
        "Gc": "R2 U' R U' R U R' U R2 D' U R U' R' D",
        "Gd": "R U R' U' D R2 U' R U' R' U R' U R2 D'",
    }

    pll_times = {}

    print("Practice all PLL cases:")
    print("Go through each case, enter your solve time, and track your progress.\n")

    for case, algorithm in pll_algorithms.items():
        print(f"PLL Case: {case}")
        print(f"Algorithm: {algorithm}")
        time = float(input(f"Enter your time for {case} (in seconds): "))
        pll_times[case] = time
        print("-" * 30)

    # Summarize results
    print("\nSummary of PLL practice:")
    for case, time in pll_times.items():
        print(f"{case}: {time:.2f} seconds")

    average_time = sum(pll_times.values()) / len(pll_times)
    print(f"\nAverage solve time for all PLLs: {average_time:.2f} seconds")
def practice_all_olls():
    oll_algorithms = {
    "OLL 1": "R U2 R2 F R F' U2 R' F R F'",
    "OLL 2": "r U r' U2 r U2 R' U2 R U' r'",
    "OLL 3": "R U R' U R U' B U' B' R'",
    "OLL 4": "R' U' R' F R F' U R",
    "OLL 5": "r U R' U R U2 r'",
    "OLL 6": "r' U' R U' R' U2 r",
    "OLL 7": "R U R' U' R' F R2 U R' U' F'",
    "OLL 8": "R' U' R U' R' U2 R",
    "OLL 9": "L F' L' U' L U F U' L'",
    "OLL 10": "R' F R U R' U' F' U R",
    "OLL 11": "r U R' U R U2 r2 U' R U' R' U2 r",
    "OLL 12": "M' R' U' R U' R' U2 R U' R r'",
    "OLL 13": "F U R U' R2 F' R U R U' R'",
    "OLL 14": "R' F R U R' U' F' U R",
    "OLL 15": "l' U2 L U L' U l",
    "OLL 16": "r U2 R' U' R U' r'",
    "OLL 17": "R2 D R' U2 R D' R' U2 R'",
    "OLL 18": "R U R' U R U' R' U R U2 R'",
    "OLL 19": "R U2 R2 U' R2 U' R2 U2 R",
    "OLL 20": "R2 U2 R' U2 R2",
    "OLL 21": "R U R' U' R U' R' F' U' F R U R'",
    "OLL 22": "r U' r' U2 r U2 R' U' R U r",
    "OLL 23": "r' U r U2 r' U2 R' U2 R U r",
    "OLL 24": "r U' r' U2 r U2 R U' R' U r",
    "OLL 25": "R' U2 R U R' U' R' U2 R",
    "OLL 26": "r U2 R' U' R U' r'",
    "OLL 27": "r' U' R U' R' U2 r",
    "OLL 28": "R2 D2 R' U R D2 R' U2 R'",
    "OLL 29": "R U R' U R' U' R U R' U2 R U R'",
    "OLL 30": "R' U2 R U2 R' F R U R' U' R' F' R2 U'",
    "OLL 31": "R U R' U' R U' R' F' U' F R U R'",
    "OLL 32": "R U2 R' U' R U2 R' U' R U' R' U2 R",
    "OLL 33": "R2 D R' U R U' R D' R' U2 R'",
    "OLL 34": "R U' R' U' R U' R' F R U R U' R' F' R",
    "OLL 35": "R U R' F' R U R' U' R U' R' F R",
    "OLL 36": "R' U R U2 R' U2 R U' R' U R' U2 R",
    "OLL 37": "R U' R' U2 R' U R U2 R' U' R",
    "OLL 38": "R U2 R' U' R U2 R' U' R' U2 R",
    "OLL 39": "R U R' U R' U' R' U' R U R",
    "OLL 40": "R' U' R U2 R U' R' U R U' R'",
    "OLL 41": "R U' R' F' R U R' U' R U R' F R",
    "OLL 42": "R U R' U R' F R2 U' R' U' F' R",
    "OLL 43": "R U R' U2 R U R' U2 R U' R' U2 R",
    "OLL 44": "R' U2 R U2 R' F R U R' U' R' F' R2",
    "OLL 45": "R2 U2 R U' R U' R' U2 R U' R' U2 R",
    "OLL 46": "R' F R U R' U' F' U R",
    "OLL 47": "R2 U2 R' U R U' R U' R' U2 R",
    "OLL 48": "r U r' U' r U2 R U R' U2 r'",
    "OLL 49": "r' U' r U r' U2 R' U2 R U r",
    "OLL 50": "r U2 R' U' R U' r'",
    "OLL 51": "r' U r U r' U2 R' U R U2 r",
    "OLL 52": "R2 D' R' U R D R' U2 R'",
    "OLL 53": "R' U2 R U' R' U2 R U' R' U' R",
    "OLL 54": "R' U R U2 R' U' R U2 R' U R' U' R",
    "OLL 55": "R U R' U' R' F R2 U' R' U' R' F R",
    "OLL 56": "R U' R' F' R U R' U' R U R' F R",
    "OLL 57": "R' F R U R' U' F' U R",
    }

    oll_times = {}

    print("Practice all OLL cases:")
    print("Go through each case, enter your solve time, and track your progress.\n")

    for case, algorithm1 in oll_algorithms.items():
        print(f"OLL Case: {case}")
        print(f"Algorithm: {algorithm1}")
        time = float(input(f"Enter your time for {case} (in seconds): "))
        oll_times[case] = time
        print("-" * 30)

    # Summarize results
    print("\nSummary of OLL practice:")
    for case, time in oll_times.items():
        print(f"{case}: {time:.2f} seconds")

    average_time = sum(oll_times.values()) / len(oll_times)
    print(f"\nAverage solve time for all PLLs: {average_time:.2f} seconds")



def main():
    avg = float(input("What do you average (in seconds)? "))
    Rrange = 1200

    if avg <= Rrange:
        print("You can continue cubing")
    else:
        print("Learn how to solve the Rubik's Cube faster")
        exit()

    while True:
        option = input("\nWhat do you want to do?\n1. Race the Rubik's robot\n2. Just practice\n3. Practice PLL\n4. Practice OLL\n5. Exit\nEnter your choice: ")

        if option == "1":
            # Race the Rubik's robot
            rounds = 5
            for i in range(1, rounds + 1):
                scramble = generate_scramble()
                print(f"Scramble {i}: {scramble}")
                Rubiks_Robot = random.uniform(avg - 5, avg + 5)
                print(f"Rubik's Robot Time: {Rubiks_Robot:.2f} seconds")
                s = float(input(f"Your time for scramble {i}: "))
                if s < Rubiks_Robot:
                    print("You win!")
                elif s == Rubiks_Robot:
                    print("You tied!")
                else:
                    print("You lost!")

        elif option == "2":
             solves=0
             mean=0
             totaltime=0
             print("Happy practicing! Here's scrambles:")
             navg=int(input("How many solves do you want to do "))
             while solves<navg:
              solves=solves+1
              print(generate_scramble())
              asktime=float(input("What is your time: "))
              totaltime=totaltime+asktime
              mean=totaltime/navg
             print(mean)

        elif option == "3":
            practice_all_plls()

        elif option == "4":
            practice_all_olls()


        elif option == "5":
            print("Goodbye! Happy cubing!")
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
