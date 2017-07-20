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
		self.txtTtn = QtGui.QLabel("PAO YING SHUB")
		self.txtTtn.setAlignment(100)

		#self.btnBldH = QtGui.QPushButton("HP Hero")
		self.proHeroHP = QtGui.QProgressBar()
		self.proHeroHP.setValue(80)
		self.proHeroHP.setTextVisible (False)

		self.txtRd = QtGui.QLabel("%s"%(self.setRound()))

		self.proMonsHP = QtGui.QProgressBar()
		self.proMonsHP.setValue(80)
		self.proMonsHP.setInvertedAppearance(True)
		self.proMonsHP.setTextVisible (False)
		#self.btnBldM = QtGui.QPushButton("HP monster")

		#self.btnPH = QtGui.QPushButton()
		#self.btnPH.setIcon(QtGui.QIcon('D:\\bn\\python\\ygg\\Pyside\\charHero_b.png'))
		#self.btnPH.setIconSize(QtCore.QSize(100,100))

		self.labPH = QtGui.QLabel()
		self.labPH.setPixmap('D:\\bn\\python\\ygg\\Pyside\\charHero_b.png')

		shubH = 'D:\\bn\\python\\ygg\\Pyside\\fist2.png'
		
		self.imgShH = QtGui.QPixmap(shubH)
		self.imgShH = self.imgShH.scaled(80,80,mode = QtCore.Qt.SmoothTransformation)

		self.labShH = QtGui.QLabel()
		self.labShH.setPixmap(self.imgShH)
		#self.labShH.setPixmap('D:\\bn\\python\\ygg\\Pyside\\fist2.png')
		#self.labShH.setFixedSize(100,100)
		#self.labShH.setPixmap(QtGui.QPixmap(80,80))

		self.txtVS = QtGui.QLabel("VS")

		self.labPM = QtGui.QLabel()
		self.labPM.setPixmap('D:\\bn\\python\\ygg\\Pyside\\charMons_b.png')

		self.imgShM = QtGui.QPixmap(shubH)
		self.imgShM = self.imgShH.scaled(80,80,mode = QtCore.Qt.SmoothTransformation)

		self.labShM = QtGui.QLabel()
		self.labShM.setPixmap(self.imgShH)
		#self.labShM = QtGui.QLabel()
		#self.labShM.setPixmap('D:\\bn\\python\\ygg\\Pyside\\two.png')

		
		self.txtHero = QtGui.QLabel("Hero")
		self.txtHero.setAlignment(100)
		self.txtMons = QtGui.QLabel("Monster")
		self.txtMons.setAlignment(100)
		
		self.btn1 = QtGui.QPushButton()
		self.btn1.setIcon(QtGui.QIcon('D:\\bn\\python\\ygg\\Pyside\\two.png'))
		self.btn1.setIconSize(QtCore.QSize(80,80))
		#self.btn1.setIconSize()
		self.btn2 = QtGui.QPushButton()
		self.btn2.setIcon(QtGui.QIcon('D:\\bn\\python\\ygg\\Pyside\\fist2.png'))
		self.btn2.setIconSize(QtCore.QSize(80,80))
		self.btn3 = QtGui.QPushButton()
		self.btn3.setIcon(QtGui.QIcon('D:\\bn\\python\\ygg\\Pyside\\five.png'))
		self.btn3.setIconSize(QtCore.QSize(80,80))
	
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

		layoutBlood.addWidget(self.proHeroHP)
		layoutBlood.addWidget(self.txtRd)
		layoutBlood.addWidget(self.proMonsHP)

		layoutCard.addWidget(self.labPH)
		layoutCard.addWidget(self.labShH)
		layoutCard.addWidget(self.txtVS)
		layoutCard.addWidget(self.labShM)
		layoutCard.addWidget(self.labPM)

		layoutName.addWidget(self.txtHero)
		layoutName.addWidget(self.txtMons)

		layoutChoose.addWidget(self.btn1)
		layoutChoose.addWidget(self.btn2)
		layoutChoose.addWidget(self.btn3)

		self.setLayout(mainLayout)

	def connect(self):
		print 'a'	

	def setRound(self):
		r = 0
		if r < 10:
			rr = 0
		else :
			rr + 1
			r = 0
		return str(rr) + str(r)

		
app = QtGui.QApplication(sys.argv)
window = mainWindow()
window.show()
app.exec_()