import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from converter import Ui_MainWindow
from currency_converter import CurrencyConverter


class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__() 
        self.converter = Ui_MainWindow()
        self.converter.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('КОНВЕРТАЦИЯ ВАЛЮТ')
        self.setWindowIcon(QIcon('Arrows.svg'))

        self.converter.input_currency.setPlaceholderText('Из валюты: ')
        self.converter.input_amount.setPlaceholderText('У меня есть: ')
        self.converter.output_currency.setPlaceholderText('В валюту: ')
        self.converter.output_amount.setPlaceholderText('Я получу: ')

        self.converter.pushButton.clicked.connect(self.converting)

    def converting(self):
        c = CurrencyConverter()
        input_currency = self.converter.input_currency.text()
        output_currency = self.converter.output_currency.text()
        input_amount = int(self.converter.input_amount.text())

        output_amount = round(c.convert(input_amount, '%s' % input_currency, '%s' % output_currency), 2)

        self.converter.output_amount.setText(str(output_amount))


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())
