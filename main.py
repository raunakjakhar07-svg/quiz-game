from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class QuizApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        question = Label(text="What is 2 + 2?", font_size=24)
        result = Label(text="", font_size=20)

        def check_answer(ans):
            result.text = "Correct ✅" if ans == 4 else "Wrong ❌"

        btn1 = Button(text="3")
        btn1.bind(on_press=lambda x: check_answer(3))

        btn2 = Button(text="4")
        btn2.bind(on_press=lambda x: check_answer(4))

        layout.add_widget(question)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(result)

        return layout

if __name__ == "__main__":
    QuizApp().run()
