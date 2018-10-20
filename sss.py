import sys
import numpy as np
#from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5 import QtCore, QtWidgets
from googletrans import Translator
translator = Translator()
class myTranslator():
# file-input.py
#def open_text(txt_name):
#	f = open(txt_name,'r')
#	message = f.read()
#	print(message)
#	f.close()
   

#if clicked, clicked item becomes variable Query, string

#print slice_translation(str(translator.translate(message))) # test line


# Give slice of translated portion for only the translation
    def find_third_equals(self, s):     #give index of third = sign
        letter_count = 0
        for i in range(len(s)):
            if s[i] == "=":
                letter_count += 1
            if letter_count == 3:
                return i + 1
                
    def find_pronunciation(self, s):    #give index of pronunciation
        return int(s.find(" pronunciation"))
    
    def slice_translation(self, s):    #give slice of string for substring of only translated word
        return s[self.find_third_equals(s):self.find_pronunciation(s)-1]  
# print slice_translation("<Translated src=ko dest=ja text=hello there pronunciation=Kon'nichiwa.>")
# Slice functions above

    #print (slice_translation(str(translator.translate(message))))

class MyLabel(QtWidgets.QLabel):
    
    def __init__(self,*args,**kwargs):
        super(MyLabel,self).__init__(*args,**kwargs)
        
    #here we reimplement the function to respond user event    
    def mousePressEvent(self,e):
        if e.buttons() == QtCore.Qt.LeftButton:
            
            QtWidgets.QMessageBox.about(self, "Title", myTranslator().slice_translation(str(translator.translate(self.text()))))
    
           
        if e.buttons() == QtCore.Qt.RightButton:
            print(self.text()+'  which is translated')
        

     

class MainWin(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.count = 0
        self.initParam()
        self.fReading()
        self.initUI()
       
        
    def initParam(self):
        self.lenSentence = 5
        self.fPath = "E:\Codes\PythonProjects\Learning\hackthon\something_to_read.txt"
        
    def fReading(self):
        self.data = []
        with open(self.fPath,'r') as f:
            for line in f:
                cells = line.strip().split(" ")
                self.data.append(cells)
                
                
        data = []
        for row in self.data:
            for c in row:
                data.append(c)
        self.data = data
        
    def rearranging(self):
        print(self.data)
        for y in range(6):
            for x in range(self.lenSentence):
                idx = self.lenSentence*y + x
                lbl = MyLabel(self.data[idx],self)
                lbl.move(100*x + 10,50*y + 10)
        
    def initUI(self):
#        print(self.data)
        self.rearranging()
        
#        lbl1 = MyLabel('how', self)
#        lbl1.move(15, 10)
        self.setGeometry(300, 300, 1550, 850)
        self.setWindowTitle('Window')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWin()
    sys.exit(app.exec_())