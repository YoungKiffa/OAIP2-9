class Button:
    def __init__(self, text, color="default", size="medium"):
        self.text = text
        self.color = color
        self.size = size
        self.is_clicked = False

    def click(self):
        self.is_clicked = True
        print(f"Кнопка '{self.text}' нажата")

    def display(self):
        print(f"Кнопка '{self.text}' цветом '{self.color}' и размером '{self.size}'")


button1 = Button("Submit", "green", "large")
button2 = Button("Cancel", "red", "large")

button1.display()
button2.display()

button1.click()
print(f"Кнопка '1' нажата: {button1.is_clicked}")