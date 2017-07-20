import sys
from PySide import QtGui,QtCore

class mainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setWindowTitle('HELLO BUBBLE')
        #self.setGeometry(300,300,400,400)
        self.tabMenu()
        center = Main()
        self.setCentralWidget(center)
        
    def tabMenu(self):
    	restartAct = QtGui.QAction('Restart', self)
        exitAct = QtGui.QAction('Exit', self)

        manageMenu = QtGui.QMenu('Manage')
        manageMenu.addAction(restartAct)
        manageMenu.addAction(exitAct)

        restartAct.triggered.connect(self.restart)
        exitAct.triggered.connect(self.close)

        menuBar = QtGui.QMenuBar()
        menuBar.addMenu(manageMenu)


        self.setMenuBar(menuBar)

    def restart(self):
    	self.close()
    	self.show()
    	#print 'restart'

class Main(QtGui.QDialog):
	def __init__(self):
		super(Main,self).__init__()
		self.widget()
		self.Layout()
		self.connect()

	def widget(self):
		self.txtTtn = QtGui.QLabel("Pao Ying Shub")

		self.btnBldH = QtGui.QPushButton("HP Hero")
		self.txtRd = QtGui.QLabel("00")
		self.btnBldM = QtGui.QPushButton("HP monster")

		self.btnPH = QtGui.QPushButton("pic Hero")
		self.btnShH = QtGui.QPushButton("shub H")
		self.txtVS = QtGui.QLabel("VS")
		self.btnPM = QtGui.QPushButton("Pic monster")
		self.btnShM = QtGui.QPushButton("shub M")
		
		self.txtHero = QtGui.QLabel("Hero")
		self.txtMons = QtGui.QLabel("Monster")
		
		self.btn1 = QtGui.QPushButton("1")
		self.btn2 = QtGui.QPushButton("2")
		self.btn3 = QtGui.QPushButton("3")
	
	def Layout(self):
		mainLayout = QtGui.QVBoxLayout()
		layoutTitle = QtGui.QVBoxLayout()
		layoutBlood = QtGui.QHBoxLayout()

		layoutCard = QtGui.QHBoxLayout()
		layoutName = QtGui.QHBoxLayout()

		layoutChoose = QtGui.QHBoxLayout()

		mainLayout.addLayout(layoutTitle)
		mainLayout.addLayout(layoutBlood)
		mainLayout.addLayout(layoutCard)
		mainLayout.addLayout(layoutName)
		mainLayout.addLayout(layoutChoose)

		layoutTitle.addWidget(self.txtTtn)

		layoutBlood.addWidget(self.btnBldH)
		layoutBlood.addWidget(self.txtRd)
		layoutBlood.addWidget(self.btnBldM)

		layoutCard.addWidget(self.btnPH)
		layoutCard.addWidget(self.btnShH)
		layoutCard.addWidget(self.txtVS)
		layoutCard.addWidget(self.btnShM)
		layoutCard.addWidget(self.btnPM)

		layoutName.addWidget(self.txtHero)
		layoutName.addWidget(self.txtMons)

		layoutChoose.addWidget(self.btn1)
		layoutChoose.addWidget(self.btn2)
		layoutChoose.addWidget(self.btn3)

		self.setLayout(mainLayout)

	def connect(self):
		print 'a'	

	def pressBtn(self):
		print 'push'

		
app = QtGui.QApplication(sys.argv)
window = mainWindow()
window.show()
app.exec_()