import random
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QPainter, QColor

class Star:
    def __init__(self, w, h):
        self.x = random.randint(0, w)
        self.y = random.randint(0, h)
        self.speed = random.uniform(0.3, 1.2)
        self.size = random.randint(1, 3)

class StarField(QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)

        self.stars = [Star(1400,900) for _ in range(300)]
        self.mouse_x = 0
        self.mouse_y = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stars)
        self.timer.start(16)

    def mouseMoveEvent(self, event):
        self.mouse_x = event.position().x()
        self.mouse_y = event.position().y()

    def update_stars(self):
        for s in self.stars:
            s.y += s.speed
            if s.y > self.height():
                s.y = 0
                s.x = random.randint(0,self.width())

            dx = s.x - self.mouse_x
            dy = s.y - self.mouse_y
            dist = max((dx*dx+dy*dy)**0.5,1)

            if dist < 120:
                s.x += dx/dist*2
                s.y += dy/dist*2

        self.update()

    def paintEvent(self, e):
        p = QPainter(self)
        p.fillRect(self.rect(), QColor(5,5,20))
        p.setPen(Qt.GlobalColor.white)
        for s in self.stars:
            p.drawPoint(int(s.x), int(s.y))
