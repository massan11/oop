class Inputuser:
    def __init__(self):
        self.text = ""

    def input_txt(self):
        self.text = input()

    def uppercase_txt(self):
        print(self.text.upper())
    
txt = Inputuser()
txt.input_txt()
txt.uppercase_txt()


    