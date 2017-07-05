import maya.cmds as mc
import re
import os

class functSO(object):
    def __init__(self):
        self.oriPath = 'C:\\Users\\User\\Documents\\yggintern'
        self.textPath = self.oriPath
        
    def pathBox(self):
        print self.textPath
        
    def saveFile(self,saveName,task):#task is master ,polish , block 
        #textbox write master ,polish ,block
        #mc.file( save = True )
        self.saveName = 
        mc.file( rename =  ) # M P B
        mc.file( type = 'mayaAscii', save = True )
    
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
            if searchAs :
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
            elif searchNas :
                self.listNas.append(x)
        print self.listNsq , self.listNas
    
    def name_seq_asset(self,item):
        self.textPath += '\\' + item
        self.pathBox()
        dir = os.listdir(self.textPath)
        self.listSh = []
        self.listTy = []
        for x in dir :
            searchSh = re.search('[a-zA-Z][0-9]+[_][0-9]+',x)
            searchTy = re.search('[a-zA-Z]+',x)
            if searchSh :
                self.listSh.append(x) # listSeq append x 
            elif searchTy :
                self.listTy.append(x)
        print self.listSh , self.listTy
             
        
    def shots_type(self,item):
        self.textPath += '\\' + item
        self.pathBox()
        self.listDep = os.listdir(self.textPath)
        print self.listDep

    def dept(self,item):
        self.textPath += '\\' + item
        self.pathBox()
        self.listScene = os.listdir(self.textPath)
        print self.listScene
    
    def scene(self,item):
        self.textPath += '\\' + item
        self.pathBox()
        self.listFile = os.listdir(self.textPath)
        print self.listFile

f = functSO()
f.default()
f.project('YIT')
f.seq_asset('sequences')
f.name_seq_asset('Y01')
f.shots_type('Y01_0010')
f.dept('Animation')
f.scene('Scenes')
#print f.f()