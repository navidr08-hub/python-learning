# Chapter 24 - Text-to-Speech and Speech Recognition
# (Practice Program) - 99 Bottle of Water
# Windows 10 Only


import pyttsx3


def speak(speech: str):
    engine = pyttsx3.init()
    engine.say(speech)
    engine.runAndWait()
    engine.stop()


def bottles_99():
    bottles = 99
    
    while bottles > 1:
        speech = f"""
        {bottles} bottles of water on the wall,
        {bottles} bottles of water,
        Take one down, pass it around,
        {bottles - 1} bottles of water on the wall.
        """

        speak(speech)

        bottles -= 1

    speech = """
    1 bottle of water on the wall,
    1 bottles of water,
    Take one down, pass it around,
    0 bottles of water on the wall.
    """

    speak(speech)


def main():
    bottles_99()


if __name__ == "__main__":
    main()