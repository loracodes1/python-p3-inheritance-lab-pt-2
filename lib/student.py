class Student:
    def hello(self):
        """
        Prints a welcome message indicating excitement for learning.
        """
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        """
        Prints a phrase indicating the student wants to participate.
        """
        print("Pick me!")


class ChattyStudent(Student):
    def hello(self):
        """
        Prints the inherited welcome message and augments it with additional chatty phrases.
        """
        super().hello()
        print(
            "How are you doing today? I'm okay, but I'm kind of tired. "
            "Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! "
            "What, you don't want any spoilers? Okay well let me just tell you who died..."
        )

    def raise_hand(self):
        """
        Prints "Pick me!" ten times using super() multiple times.
        """
        for _ in range(10):
            super().raise_hand()

