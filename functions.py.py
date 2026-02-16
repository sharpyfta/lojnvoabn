import json
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit
from api import call

class FunctionManager(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.output = QTextEdit()
        self.load_btn = QPushButton("Load Functions")

        self.load_btn.clicked.connect(self.load_functions)

        layout.addWidget(self.output)
        layout.addWidget(self.load_btn)

        self.setLayout(layout)

    def load_functions(self):
        data = call("Admin/GetCloudScriptRevision")

        self.output.setText(json.dumps(data, indent=2))
