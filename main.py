from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

questions = [
    {
        "q": "Capital of India?",
        "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"],
        "ans": "Delhi"
    },
    {
        "q": "2 + 2 = ?",
        "options": ["3", "4", "5", "6"],
        "ans": "4"
    }
]

class QuizApp(App):
    def build(self):
        self.score = 0
        self.q_index = 0

        self.layout = BoxLayout(orientation='vertical')
        self.question_label = Label(font_size=24)
        self.layout.add_widget(self.question_label)

        self.buttons = []
        for i in range(4):
            btn = Button(on_press=self.check_answer)
            self.buttons.append(btn)
            self.layout.add_widget(btn)

        self.load_question()
        return self.layout

    def load_question(self):
        q = questions[self.q_index]
        self.question_label.text = q["q"]
        for i in range(4):
            self.buttons[i].text = q["options"][i]

    def check_answer(self, instance):
        if instance.text == questions[self.q_index]["ans"]:
            self.score += 1

        self.q_index += 1
        if self.q_index < len(questions):
            self.load_question()
        else:
            self.question_label.text = f"Game Over!\nScore: {self.score}"
            for btn in self.buttons:
                btn.disabled = True

QuizApp().run()