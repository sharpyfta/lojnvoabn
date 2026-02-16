from PyQt6.QtWidgets import QWidget,QVBoxLayout,QLineEdit,QPushButton,QTextEdit
from api import call
import json

class PlayerManager(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.search = QLineEdit()
        self.search.setPlaceholderText("PlayFabId")

        self.load = QPushButton("Load Profile")
        self.ban = QPushButton("Ban 24h")
        self.currency = QPushButton("Add 100 GC")

        self.output = QTextEdit()

        self.load.clicked.connect(self.load_player)
        self.ban.clicked.connect(self.ban_player)
        self.currency.clicked.connect(self.add_currency)

        layout.addWidget(self.search)
        layout.addWidget(self.load)
        layout.addWidget(self.ban)
        layout.addWidget(self.currency)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def load_player(self):
        pid = self.search.text()
        data = call("Admin/GetUserAccountInfo",{
            "PlayFabId":pid
        })
        self.output.setText(json.dumps(data,indent=2))

    def ban_player(self):
        pid = self.search.text()
        call("Admin/BanUsers",{
            "Bans":[{
                "PlayFabId":pid,
                "Reason":"Dash Studio Ban",
                "DurationInHours":24
            }]
        })

    def add_currency(self):
        pid = self.search.text()
        call("Admin/AddUserVirtualCurrency",{
            "PlayFabId":pid,
            "VirtualCurrency":"GC",
            "Amount":100
        })
