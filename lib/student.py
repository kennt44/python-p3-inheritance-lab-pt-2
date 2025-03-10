class Student:
    def hello(self):
        """Prints a greeting message."""
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        """Prints a message indicating the student is raising their hand."""
        print("Pick me!")

from lib.student import Student

class ChattyStudent(Student):
    def hello(self):
        """Inherits hello() from Student and adds more chatty content."""
        super().hello()  # Calls the hello method from Student
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")

    def raise_hand(self):
        """Inherits raise_hand() from Student and repeats it 10 times."""
        for _ in range(10):
            super().raise_hand()  # Calls the raise_hand method from Student 10 times

