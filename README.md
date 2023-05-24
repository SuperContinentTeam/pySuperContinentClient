# pySuperContinentClient


```python

self.timer = QTimer(self)
self.tick = 1

self.timer.timeout.connect(self.receiver_from_server)
self.timer.start(1000)

def receiver_from_server(self):
    print("Hello world", self.tick)
    self.tick += 1


# 绘制图片
img = QImage("xxx.png")
rect = QRect(x, y, img.width()/2, img.height()/2)
painter.drawImage(rect, img)

```