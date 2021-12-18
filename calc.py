import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
from PyQt5.QtGui import QImage, QPalette, QBrush

class MainWindow(qtw.QWidget):

    a = int()
    b = int()
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setFixedSize(360,590)
        
        bImage = QImage("FT2bg.png")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(bImage))                        
        self.setPalette(palette)

        #digit display
        self.digit_display = qtw.QLabel('0', self)
        self.digit_display.setAlignment(qtc.Qt.AlignRight)
        self.digit_display.setFont(qtg.QFont('Helvetica Neue', 72))
        self.digit_display.setGeometry(5,15,350,90)

        #creating buttons
        #row 1
        self.clear_button = qtw.QPushButton("C",self, clicked=lambda: self.pressed_fn("C")) 
        self.clear_button.setGeometry(0,110,90,90)  
        self.mod_button = qtw.QPushButton("%",self, clicked=lambda: self.pressed_fn("%")) 
        self.mod_button.setGeometry(90,110,90,90)
        self.divide_button = qtw.QPushButton("/",self, clicked=lambda: self.pressed_fn("/")) 
        self.divide_button.setGeometry(180,110,90,90)
        self.square_button = qtw.QPushButton("<<",self, clicked=lambda: self.bkspce_fn()) 
        self.square_button.setGeometry(270,110,90,90) 

        #row 2
        self.seven_button = qtw.QPushButton("7",self, clicked=lambda: self.pressed_fn("7")) 
        self.seven_button.setGeometry(0,205,90,90)  
        self.eight_button = qtw.QPushButton("8",self, clicked=lambda: self.pressed_fn("8")) 
        self.eight_button.setGeometry(90,205,90,90)
        self.nine_button = qtw.QPushButton("9",self, clicked=lambda: self.pressed_fn("9")) 
        self.nine_button.setGeometry(180,205,90,90)
        self.mult_button = qtw.QPushButton("X",self, clicked=lambda: self.pressed_fn("*")) 
        self.mult_button.setGeometry(270,205,90,90) 

        #row 3
        self.four_button = qtw.QPushButton("4",self, clicked=lambda: self.pressed_fn("4")) 
        self.four_button.setGeometry(0,300,90,90)  
        self.five_button = qtw.QPushButton("5",self, clicked=lambda: self.pressed_fn("5")) 
        self.five_button.setGeometry(90,300,90,90)
        self.six_button = qtw.QPushButton("6",self, clicked=lambda: self.pressed_fn("6")) 
        self.six_button.setGeometry(180,300,90,90)
        self.sub_button = qtw.QPushButton("-",self, clicked=lambda: self.pressed_fn("-")) 
        self.sub_button.setGeometry(270,300,90,90)

        #row 4
        self.one_button = qtw.QPushButton("1",self, clicked=lambda: self.pressed_fn("1")) 
        self.one_button.setGeometry(0,395,90,90)  
        self.two_button = qtw.QPushButton("2",self, clicked=lambda: self.pressed_fn("2")) 
        self.two_button.setGeometry(90,395,90,90)
        self.three_button = qtw.QPushButton("3",self, clicked=lambda: self.pressed_fn("3")) 
        self.three_button.setGeometry(180,395,90,90)
        self.add_button = qtw.QPushButton("+",self, clicked=lambda: self.pressed_fn("+")) 
        self.add_button.setGeometry(270,395,90,90)  

        #row 5
        self.sign_button = qtw.QPushButton("x^2",self, clicked=lambda: self.sqr_fn()) 
        self.sign_button.setGeometry(0,490,90,90)  
        self.zero_button = qtw.QPushButton("0",self, clicked=lambda: self.pressed_fn("0")) 
        self.zero_button.setGeometry(90,490,90,90)
        self.decimal_button = qtw.QPushButton(".",self, clicked=lambda: self.decimal_fn()) 
        self.decimal_button.setGeometry(180,490,90,90)
        self.equal_button = qtw.QPushButton("=",self, clicked=lambda: self.equal_fn()) 
        self.equal_button.setGeometry(270,490,90,90)       

        
        self.show() #show the app

        
    #defining events
    
    def bkspce_fn(self):
        screen = self.digit_display.text()
        screen = screen[:-1] #remove last item from string
        self.digit_display.setText(f'{screen}')

    def sqr_fn(self):
        screen = self.digit_display.text()
        self.digit_display.setText(f'({screen})**2')


    def equal_fn(self):
        print(self.digit_display.text())
        screen = self.digit_display.text()
        answer = eval(screen)
        self.digit_display.setText(str(answer))

    
    def decimal_fn(self):#add a decimal
        screen = self.digit_display.text()
        symbols = {"+", "-", "x", "/"}
        if any(char in screen for char in symbols):
            if screen[-1] == ".":
                pass
            else:
                self.digit_display.setText(f'{screen}.')
        else:
            if "." not in screen:
                self.digit_display.setText(f'{screen}.')
            else:
                pass

    
    def pressed_fn(self, pressed):
        if pressed == "C":
            self.digit_display.setText("0")
        else:    
            if self.digit_display.text()!="0": #check to see if starts with 0 otherwise concat
                self.digit_display.setText(f'{self.digit_display.text()}{pressed}')
            else:
                self.digit_display.setText(pressed)

                
if __name__ == "__main__":
    import sys
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
