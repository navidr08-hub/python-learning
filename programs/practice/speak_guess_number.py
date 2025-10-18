# Chapter 24 - Text-to-Speech and Speech Recognition
# (Practice Program) - Adding Voice to Guess the Number
# Windows 10 ONLY


# This is a guess the number game.
import random
import pyttsx3


def speak(speech: str):
    engine = pyttsx3.init()
    engine.say(speech)
    engine.runAndWait()
    engine.stop()


def guess_number():
    secret_number = random.randint(1, 20)
    speak('I am thinking of a number between 1 and 20.')

    # Ask the player to guess 6 times.
    for guesses_taken in range(1, 7):
        speak('Take a guess.')
        guess = int(input('>'))

        if guess < secret_number:
            speak('Your guess is too low.')
        elif guess > secret_number:
            speak('Your guess is too high.')
        else:
            break  # This condition is the correct guess!

    if guess == secret_number:
        if guesses_taken == 1:
            speak('Good job! You got it in 1 guess!')
        else:    
            speak('Good job! You got it in ' + str(guesses_taken) + ' guesses!')
    else:
        speak('Nope. The number was ' + str(secret_number))


def main():
    guess_number()


if __name__ == "__main__":
    main()