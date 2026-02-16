import threading
import json
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton
from api import call

class PlayStreamMonitor(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.log = QTextEdit()
        self.refresh_btn = QPushButton("Refresh Events")

        self.refresh_btn.clicked.connect(self.load_events)

        layout.addWidget(self.log)
        layout.addWidget(self.refresh_btn)

        self.setLayout(layout)

        self.load_events()

    def load_events(self):
        data = call("Admin/GetPlayStreamEvents", {
            "MaxResults": 20
        })

        if "data" in data:
            events = data["data"].get("Events", [])
            formatted = ""

            for e in events:
                formatted += f"{e.get('EventName')} | {e.get('Timestamp')}\n"

            self.log.setText(formatted)
