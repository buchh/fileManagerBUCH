import maya.cmds as mc
import re
import os

class functSO(object):
    def __init__(self):
        self.oriPath = 'C:\\Users\\User\\Documents\\yggintern'
        self.textPath = self.oriPath
        self.shDep= ''
        self.task = 'polish'
        #self.task = ''
        self.version = 'V002.ma'
        
    def pathBox(self):
        print self.textPath
        
    def saveFile(self):#task is master ,polish , block 
        #textbox write master ,polish ,block
        #mc.file( save = True )
        #self.saveName = 
        mc.file( rename = self.saveName ) # M P B
        mc.file( type = 'mayaAscii', save = True )

#############################################
#                                           #
#                 SEQUENCES                 #
#                                           #
#############################################

    def saveSeq(self):
        pth = 'C:\\Users\\User\\Documents\\yggintern\\YIT\\sequences\\Y01\\Y01_0010\\Animation\\scenes'
        self.saveName =  pth + '\\' + self.shDep + '_' + self.task + '.' + self.version
        print self.saveName
        

#############################################
#                                           #
#                 ASSETS                    #
#                                           #
#############################################

    def saveAss(self):
        pth = 'C:\\Users\\User\\Documents\\yggintern\\YIT\\assets\\Characters\\norman\\Models\\scenes'
        self.saveName =  pth + '\\' + self.shDep + '.' + self.version
        print self.saveName        

#############################################
#                                           #
#              SEQUENCES/ASSETS             #
#                                           #
#############################################
    
    def openFile(self):
        mc.file( self.textPath , open = True )        
        
    def default(self):
        self.pathBox()
        self.listPj = os.listdir(self.oriPath)
        print self.listPj
    
    def project(self,item):
        self.textPath += '\\' + item
        self.pathBox()
        dir = os.listdir(self.textPath)
        self.listSq = []
        self.listAs = []
        for x in dir :
            searchSeq = re.search('sequences',x)
            searchAs = re.search('assets',x)
            if searchSeq :
                self.listSq.append(x) # listSeq append x 
            elif searchAs :
                self.listAs.append(x)
        print self.listSq , self.listAs  
          
    def seq_asset(self,item):
        self.textPath += '\\' + item
        self.pathBox()
        dir = os.listdir(self.textPath)
        self.listNsq = []
        self.listNas = []
        for x in dir :
            searchNsq = re.match('[a-zA-Z]+[0-9]+',x)
            searchNas = re.match('[a-zA-Z]+',x)
            if searchNsq :
                self.listNsq.append(x) # listSeq append x
                self.waySA = 0 
            elif searchNas :
                self.listNas.append(x)
                self.waySA = 1
        print self.listNsq , self.listNas
    
    def name_seq_asset(self,item):
        self.textPath += '\\' + item
        if self.waySA == 1 :
            self.shDep += item[0:4] + '_'
        self.pathBox()
        dir = os.listdir(self.textPath)
        self.listSh = []
        self.listNa = []
        for x in dir :
            searchSh = re.search('[a-zA-Z][0-9]+[_][0-9]+',x)
            searchNa = re.search('[a-zA-Z]+',x)
            if searchSh :
                self.listSh.append(x) # listSeq append x 
            elif searchNa :
                self.listNa.append(x)
        print self.listSh , self.listNa
             
        
    def shots_name(self,item):
        self.textPath += '\\' + item
        self.shDep += item
        self.pathBox()
        self.listDep = os.listdir(self.textPath)
        print self.listDep

    def dept(self,item):
        self.textPath += '\\' + item
        self.shDep += '_' + item
        self.pathBox()
        self.listScene = os.listdir(self.textPath)
        print self.listScene
        
    
    def scene(self,item):
        self.textPath += '\\' + item
        self.pathBox()
        self.listFile = os.listdir(self.textPath)
        print self.listFile

#############################################
#                                           #
#                 DISPLAY                   #
#                                           #
#############################################

    def fileDisplay(self):
        def showName(self):
            if self.waySA == 0 :
                self.saveSeq()
            if self.waySA == 1 :
                self.saveAss()
        def showDate(self):
            v
        def showSize(self):
            print self.textPath
            print os.path.getsize(self.textPath)
        showName(self)
        showSize(self)

f = functSO()
f.default()
f.project('YIT')
f.seq_asset('sequences')
f.name_seq_asset('Y01')
f.shots_name('Y01_0010')
f.dept('Animation')
f.scene('Scenes')
f.fileDisplay()

f = functSO()
f.default()
f.project('YIT')
f.seq_asset('assets')
f.name_seq_asset('Characters')
f.shots_name('norman')
f.dept('Models')
f.scene('Scenes')
f.fileDisplay()
#f.saveFile()
#f.fileDisplay()
#f.showSize()
#print f.f()