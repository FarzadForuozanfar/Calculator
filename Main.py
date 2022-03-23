from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader
from functools import partial
from math import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.loader = QUiLoader()
        self.ui = self.loader.load("Calculator.ui")
        self.ui.show()
        self.temp_num = 0
        self.result = 0
        self.current_op = ''  #آخرین عملگر ریاضی را در خود ذخیره می کند تا در زمان استفاده از مساوی بداند باید چه عملی انجام دهد
        ##################### Operations ########################
        self.ui.btn_sum.clicked.connect(partial(self.The_four_basic_mathematical_operations,'+'))
        self.ui.btn_mines.clicked.connect(partial(self.The_four_basic_mathematical_operations,'-'))
        self.ui.btn_div.clicked.connect(partial(self.The_four_basic_mathematical_operations,'/'))
        self.ui.btn_multi.clicked.connect(partial(self.The_four_basic_mathematical_operations,'*'))
        self.ui.btn_q.clicked.connect(partial(self.Symmetry,'q'))
        self.ui.btn_sin.clicked.connect(partial(self.Trigonometric_calculations,'sin'))
        self.ui.btn_cos.clicked.connect(partial(self.Trigonometric_calculations,'cos'))
        self.ui.btn_tan.clicked.connect(partial(self.Trigonometric_calculations,'tan'))
        self.ui.btn_cot.clicked.connect(partial(self.Trigonometric_calculations,'cot'))
        self.ui.btn_eqaul.clicked.connect(self.Eqaul)
        self.ui.btn_log.clicked.connect(self.Logarithm)
        self.ui.btn_sqrt.clicked.connect(self.Sqrt)
        self.ui.btn_percent.clicked.connect(self.Percent)
        self.ui.btn_clear.clicked.connect(self.Clear_text_box)
        ##################### Number btn #########################
        self.ui.btn_0.clicked.connect(partial(self.Write_number_in_text_box,0))
        self.ui.btn_1.clicked.connect(partial(self.Write_number_in_text_box,1))
        self.ui.btn_2.clicked.connect(partial(self.Write_number_in_text_box,2))
        self.ui.btn_3.clicked.connect(partial(self.Write_number_in_text_box,3))
        self.ui.btn_4.clicked.connect(partial(self.Write_number_in_text_box,4))
        self.ui.btn_5.clicked.connect(partial(self.Write_number_in_text_box,5))
        self.ui.btn_6.clicked.connect(partial(self.Write_number_in_text_box,6))
        self.ui.btn_7.clicked.connect(partial(self.Write_number_in_text_box,7))
        self.ui.btn_8.clicked.connect(partial(self.Write_number_in_text_box,8))
        self.ui.btn_9.clicked.connect(partial(self.Write_number_in_text_box,9))
        self.ui.btn_decimal.clicked.connect(partial(self.Write_number_in_text_box,'.'))
        #####################################################################
    def Write_number_in_text_box(self,number):
        if self.ui.lineEdit.text() != str(0):
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + str(number))
        
        else:
            self.ui.lineEdit.setText(str(number))
        
    def The_four_basic_mathematical_operations(self,operation):
        try:
                if operation == '+':
                    self.current_op = '+'
                    self.result = float(self.ui.lineEdit.text())

                elif operation == '-':
                    self.current_op = '-'
                    self.result = float(self.ui.lineEdit.text())
                    

                elif operation == '*':
                    self.result = float(self.ui.lineEdit.text())
                    self.current_op = '*'

                elif operation == '/':
                    self.result = float(self.ui.lineEdit.text())
                    self.current_op = '/'
       
                self.ui.lineEdit.setText("")
        except:
            self.ui.lineEdit.setText("!! خطا !!")
            self.result = 0
        
    def Trigonometric_calculations(self,operation):
        try:
            if operation == 'sin':
                self.result = float(self.ui.lineEdit.text())
                self.ui.lineEdit.setText(str(sin(radians(self.result))))
                self.box_is_empty = False
            elif operation == 'cos':
                self.result = float(self.ui.lineEdit.text())
                self.ui.lineEdit.setText(str(cos(radians(self.result))))
            elif operation == 'tan':
                self.result = float(self.ui.lineEdit.text())
                self.ui.lineEdit.setText(str(tan(radians(self.result))))
            elif operation == 'cot':
                self.result = float(self.ui.lineEdit.text())
                self.result = 1 / tan(radians(self.result))
                self.ui.lineEdit.setText(str(self.result))
        except:
            self.ui.lineEdit.setText("!! خطا !!")
            self.result = 0
            
    def Logarithm(self):
        self.ui.lineEdit.setText(str(log10(float(self.ui.lineEdit.text()))))

    def Percent(self):
        self.result = float(self.ui.lineEdit.text())
        self.result /= 100
        self.ui.lineEdit.setText(str(self.result))

    def Sqrt(self):
        self.ui.lineEdit.setText(str(sqrt(float(self.ui.lineEdit.text()))))

    def Clear_text_box(self):
        self.result = 0
        self.current_op = None
        self.temp_num = None
        self.ui.lineEdit.setText("")
    def Symmetry(self,operation):
        self.result = float(self.ui.lineEdit.text())
        self.result = self.result * -1
        self.ui.lineEdit.setText("")
        self.ui.lineEdit.setText(str(self.result))
    def Eqaul(self):    
        self.temp_num = float(self.ui.lineEdit.text())
        if self.current_op == '+':
            self.ui.lineEdit.setText(str(self.result + self.temp_num))
        elif self.current_op == "-":
            self.ui.lineEdit.setText(str(self.result - self.temp_num))
            
        elif self.current_op == "*":
            self.ui.lineEdit.setText(str(self.result * self.temp_num))
        elif self.current_op == "/":
            self.ui.lineEdit.setText(str(self.result / self.temp_num))
        self.result = 0
        self.current_op = ""
        self.temp_num = 0
app = QApplication()
main_window = MainWindow()
app.exec()
