class TextBuffer:
    """
    Stores typed text for NeuroKeys.
    """

    def __init__(self):
        self.text = ""

    def add_character(self, char):
        self.text += char

    def backspace(self):
        self.text = self.text[:-1]

    def clear(self):
        self.text = ""

    def get_text(self):
        return self.text
    
    def last_character(self):

        if len(self.text) == 0:
            return ""

        return self.text[-1]