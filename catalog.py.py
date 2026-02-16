import json
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit
from api import call

class CatalogManager(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.output = QTextEdit()
        self.load_btn = QPushButton("Load Catalog")

        self.load_btn.clicked.connect(self.load_catalog)

        layout.addWidget(self.output)
        layout.addWidget(self.load_btn)

        self.setLayout(layout)

    def load_catalog(self):
        data = call("Admin/GetCatalogItems")

        self.output.setText(json.dumps(data, indent=2))
