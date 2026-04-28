from textual.app import App, ComposeResult
from textual.widgets import Button
from textual.containers import Center, Middle

class DirectionApp(App):
    # This CSS handles the sizing and colors
    CSS = """
    Screen {
        align: center middle;
    }

    .big {
        width: 30;
        height: 5;
        border: double red;
    }

    .small {
        width: 15;
        height: 3;
        border: solid green;
    }

    #up { margin-bottom: 1; }
    #down { margin-top: 1; }
    #left { margin-right: 2; }
    #right { margin-left: 2; }

    Button:hover {
        background: $accent;
        color: white;
    }
    """

    def compose(self) -> ComposeResult:
        # 1. Top Button
        yield Center(Button("UP (Big)", id="up", classes="big"))
        
        # 2. Middle Row (Left and Right)
        with Center():
            yield Button("LEFT", id="left", classes="small")
            yield Button("RIGHT", id="right", classes="small")
        
        # 3. Bottom Button
        yield Center(Button("DOWN (Big)", id="down", classes="big"))



if __name__ == "__main__":
    app = DirectionApp()
    app.run()