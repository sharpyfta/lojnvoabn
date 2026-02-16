import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QHBoxLayout, QVBoxLayout,
    QPushButton, QStackedWidget,
    QWidget, QLabel
)

from starfield import StarField
from cloudscript import CloudScriptEditor
from players import PlayerManager
from playstream import PlayStreamMonitor
from catalog import CatalogManager
from functions import FunctionManager

class NebulaStudio(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ultimate Nebula Studio | Made by Dash")
        self.setGeometry(100, 100, 1600, 900)

        self.background = StarField()
        self.setCentralWidget(self.background)

        layout = QHBoxLayout(self.background)

        self.sidebar = QVBoxLayout()
        layout.addLayout(self.sidebar)

        self.stack = QStackedWidget()
        layout.addWidget(self.stack)

        # Pages
        self.cloud = CloudScriptEditor()
        self.players = PlayerManager()
        self.playstream = PlayStreamMonitor()
        self.catalog = CatalogManager()
        self.functions = FunctionManager()

        self.stack.addWidget(self.cloud)
        self.stack.addWidget(self.players)
        self.stack.addWidget(self.playstream)
        self.stack.addWidget(self.catalog)
        self.stack.addWidget(self.functions)

        # Navigation
        self.sidebar.addWidget(self.nav("CloudScript", 0))
        self.sidebar.addWidget(self.nav("Players", 1))
        self.sidebar.addWidget(self.nav("PlayStream", 2))
        self.sidebar.addWidget(self.nav("Catalog", 3))
        self.sidebar.addWidget(self.nav("Functions", 4))

        self.sidebar.addWidget(QLabel("Made by Dash"))

        self.apply_styles()

    def nav(self, name, index):
        btn = QPushButton(name)
        btn.clicked.connect(lambda: self.stack.setCurrentIndex(index))
        return btn

    def apply_styles(self):
        self.setStyleSheet("""
            QPushButton {
                background-color: #1b1b3a;
                color: #8a2be2;
                padding: 12px;
                font-size: 15px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #2e2e6e;
                color: white;
            }
            QLabel {
                color: white;
                padding: 10px;
            }
        """)

app = QApplication(sys.argv)

window = NebulaStudio()
window.show()

sys.exit(app.exec())
