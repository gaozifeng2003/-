# -*- coding: utf-8 -*-
import sys
import os
import cffi
from ui_testmake import * 
from PyQt5 import QtWidgets
from persistent import Persistent
from ZODB import FileStorage, DB
import transaction
import shutil 
def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop')
class Question(Persistent):
  def __init__(self, question, answer,analysis):
    self.question = question
    self.answer = answer
    self.analysis=analysis
    self.wrong_num =""
    self.isdo=0

class MyZODB(object):

  def __init__(self, path):

      self.storage = FileStorage.FileStorage(path)

      self.db = DB(self.storage)

      self.connection = self.db.open()

      self.dbroot = self.connection.root()

  def close(self):

      self.connection.close()

      self.db.close()

      self.storage.close()
    
class MyWindow(QtWidgets.QMainWindow,Ui_Form):
    
  def __init__(self):

      super(MyWindow,self).__init__()

      self.db = MyZODB('./Data.fs')
      self.dbroot = self.db.dbroot
           
      self.numb=len(self.dbroot.keys())
      self.question=""
      self.answer=""
      self.analysis=""
      print(self.numb)

      self.setupUi(self)
  def slot_testsave(self):
      if self.textEdit.toHtml()=="" or self.question==self.textEdit. toHtml() :
        pass
      else:
          self.question=self.textEdit.toHtml()
          self.answer=self.textEdit_2.toHtml()
          self.analysis=self.textEdit_3.toHtml()
          
          self.numb+=1
          self.name="test"+str(self.numb)
          self.dbroot[self.name]=Question(self.question,self.answer,self.analysis)
          transaction.commit()
          #print(self.numb)
  def slot_testclear(self):
      transaction.commit()
      
      self.db.close()
          
      os.remove('./Data.fs')
      os.remove('./Data.fs.index')
      os.remove('./Data.fs.lock')
      os.remove('./Data.fs.tmp')
      sys.exit()
      
  def slot_testderive(self):
      path=GetDesktopPath()+"./Data.fs"
      shutil.copyfile('./Data.fs',path)
                      
  def slot_testexit(self):
      transaction.commit()
      self.db.close()
      sys.exit()
  def slot_testnext(self):

      self.textEdit.setHtml("")
      self.textEdit_2.setHtml("")
      self.textEdit_3.setHtml("")    
        
    
if __name__=="__main__":
  app=QtWidgets.QApplication(sys.argv)
  myshow=MyWindow()
  myshow.show()
  sys.exit(app.exec_())
