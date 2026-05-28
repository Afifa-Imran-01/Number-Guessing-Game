import random

def guess_game():
    while True:  # Sabse bahar wala loop: Ye poore game ko repeat karega
        secret_number = random.randint(1, 100)
        attempts = 0
        
        print("\n--- Naya Game Shuru! ---")
        print("Maine 1 se 100 ke beech ek number socha hai.")

        while True:  # Andar wala loop: Ye sirf tab tak chalega jab tak aap sahi guess nahi karte
            try:
                user_guess = int(input("Guess karein: "))
                attempts += 1

                if user_guess < secret_number:
                    print("Thoda aur upar!")
                elif user_guess > secret_number:
                    print("Thoda niche!")
                else:
                    print(f"BINGO! {attempts} koshishon mein sahi jawab!")
                    break  # Ye break sirf ANDAR wale loop ko rokega
            except ValueError:
                print("Error: Please sirf number likhein.")

        # Game khatam hone ke baad 'Play Again' poochna
        choice = input("\nKya aap phir se khelna chahte hain? (yes/no): ").lower()
        if choice != 'yes':
            print("Khelne ke liye shukriya! Bye-bye.")
            break  # Ye break BAHAR wale loop ko rokega aur program band ho jayega

guess_game()