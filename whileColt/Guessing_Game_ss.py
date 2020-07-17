import random

def try_again():
    print("Try again >> ", end="")
    
def main():
    RAND_NUM = random.randint(1,31)

    while True:
        try:
            guessed = int(input("Guess the number I guessed: "))
        except:
            print("This has to be number not anything else!")
            try_again()
            continue
        if guessed>RAND_NUM:
            print("Too high!")
            try_again()
        elif guessed<RAND_NUM:
            print("Too low")
            try_again()
        else:
            print("You won!")
            break

if __name__ == "__main__":
    main()