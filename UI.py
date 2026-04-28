from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Button


class ButtonApp(App):
    CSS = """
    Screen {
        align: center middle;
    }

    Vertical {
        width: auto;
        height: auto;
    }

    Button {
        border: double white;
        width: 40;
        height: 3;
        content-align: center middle;
        margin: 1 2;
    }

    Button:hover {
    background: white;
    color: black;
    text-style: bold;
    border: double black;
    }
    """

    def compose(self) -> ComposeResult:
        yield Vertical(
            Button("Click Me!"),
            Button("Another Button"),
            Button("Third Button"),
        )

    def on_button_press(self, event: Button.Pressed) -> None:
        if event.button.id == "btn1":
            self.do_first_function()
        elif event.button.id == "btn2":
            self.do_second_function()
        elif event.button.id == "btn3":
            self.do_third_function()

    def do_first_function(self):
        print("Hii!!!!")

    def do_second_function(self):
        print("676767")

    def do_third_function(self):
        while True:
            print("676767")
            break

if __name__ == "__main__":
    app = ButtonApp()
    app.run()




