import sys

import requests
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow

COORDS = ["11.547906", "48.161996"]
delta = 0.2
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
map_api_server = "http://static-maps.yandex.ru/1.x/"


def get_map_pic():
    map_params = {
        "ll": ",".join(COORDS),
        "spn": ",".join([str(delta), str(delta)]),
        "l": "map"}

    response = requests.get(map_api_server, params=map_params)

    if not response:
        print("Произошла ошибка во время запроса.")

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('map_app.ui', self)
        # self.pushButton.clicked.connect(self.run)
        self.radioButton_3.setChecked(True)
        self.run()

    def run(self):
        map_file = get_map_pic()
        pixmap = QPixmap(map_file)
        self.label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
