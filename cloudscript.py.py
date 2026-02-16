from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QComboBox
from PyQt6.Qsci import QsciScintilla, QsciLexerJavaScript
from api import call

class CloudScriptEditor(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.revisions = QComboBox()
        self.load_revisions()

        self.editor = QsciScintilla()
        lexer = QsciLexerJavaScript()
        self.editor.setLexer(lexer)
        self.editor.setMarginWidth(0,"00000")

        self.load_btn = QPushButton("Load Revision")
        self.save_btn = QPushButton("Save Revision")

        self.load_btn.clicked.connect(self.load_revision)
        self.save_btn.clicked.connect(self.save_revision)

        layout.addWidget(self.revisions)
        layout.addWidget(self.editor)
        layout.addWidget(self.load_btn)
        layout.addWidget(self.save_btn)

        self.setLayout(layout)

    def load_revisions(self):
        data = call("Admin/GetCloudScriptRevision")
        if "data" in data:
            rev = data["data"].get("Revision",-1)
            self.revisions.addItem(str(rev))

    def load_revision(self):
        data = call("Admin/GetCloudScriptRevision")
        if "data" in data:
            self.editor.setText(data["data"].get("Script",""))

    def save_revision(self):
        script = self.editor.text()
        call("Admin/UpdateCloudScript",{
            "Script":script,
            "Revision":-1
        })
