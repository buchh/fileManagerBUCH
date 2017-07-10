import maya.cmds as mc
import re
import os
import time
import math

class functSO(object):
    def __init__(self):
        self.oriPath = 'C:\\Users\\User\\Documents\\yggintern'
        self.textPath = self.oriPath
        self.pthSl = ''
        self.dateMod = ''
        self.shDep = ''
        self.version = ''
        self.nFile = ''
        
    def pathBox(self):
        return self.textPath

    def checkVersion(self):
        self.dirr = os.listdir(self.textPath)

        def master(self):
            for x in self.dirr :
                searchObj = re.search('master', x)
                if searchObj :
                    ver = x[-6:-3]
                    newVer = "%03d"%(int(ver)+1)
                    self.version = 'v' + newVer + '.ma'
                else :
                    self.version = 'v001.ma'

        def polish(self):
            for x in self.dirr :
                searchObj = re.search('polish', x)
                if searchObj :
                    ver = x[-6:-3]
                    newVer = "%03d"%(int(ver)+1)
                    self.version = 'v' + newVer + '.ma'
                else :
                    self.version = 'v001.ma'
        def block(self):
            for x in self.dirr :
                searchObj = re.search('block', x)
                if searchObj :
                    ver = x[-6:-3]
                    newVer = "%03d"%(int(ver)+1)
                    self.version = 'v' + newVer + '.ma'
                else :
                    self.version = 'v001.ma'

        def none(self):
            for x in self.dirr :
                searchObj = re.search('[a-z][0-9]{3}', x)
                if searchObj :
                    ver = x[-6:-3]
                    newVer = "%03d"%(int(ver)+1)
                    self.version = 'v' + newVer + '.ma'
                else :
                    self.version = 'v001.ma'
        
        if self.taskN == 'master':
            master(self)
        elif self.taskN == 'polish':
            polish(self)
        elif self.taskN == 'block':
            block(self)
        elif self.taskN == 'none':
            none(self)
        
    def saveFile(self):#task is master ,polish , block 
        mc.file( rename = self.saveName ) # M P B
        mc.file( type = 'mayaAscii', save = True )

#############################################
#                                           #
#                 SEQUENCES                 #
#                                           #
#############################################
    
    def task(self):
        taskN = ['master','polish','block','none']
        self.taskN = taskN[3]

    def saveSeq(self):
        self.task()
        self.checkVersion()
        self.firstName = self.textPath + '\\' + self.shDep + '_' + self.taskN + '.' 
        if not os.path.exists(self.firstName) :
            self.saveName = self.firstName + self.version
        print self.saveName
        

#############################################
#                                           #
#                 ASSETS                    #
#                                           #
#############################################

    def saveAss(self):
        self.task()
        self.checkVersion()
        self.saveName =  self.textPath + '\\' + self.shDep + '.' + self.version       

#############################################
#                                           #
#              SEQUENCES/ASSETS             #
#                                           #
#############################################
    
    def openFile(self,nFile):
        self.openName = self.textPath + '\\' + nFile
        mc.file( self.textPath , open = True )        
        
    def default(self):
        self.pathBox()
        self.listPj = os.listdir(self.oriPath)
        return self.listPj
    
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
        
    
    def scene(self,item):
        self.textPath += '\\' + item
        self.pathBox()
        self.listFile = os.listdir(self.textPath)

#############################################
#                                           #
#                 DISPLAY                   #
#                                           #
#############################################

    def fileDisplay(self):
        def showName(self):
            if self.waySA == 0 :
                self.saveSeq()
            elif self.waySA == 1 :
                self.saveAss()
        def showDate(self,nFile):
            self.pthSl = self.textPath + '\\' + nFile
            codeDate = os.path.getmtime(self.pthSl)
            fullDate = time.ctime(codeDate)
            listDate = fullDate.split(" ")
            self.dateMod = listDate[4] + listDate[1] + listDate[2] + ' ' + listDate[3]
            return self.dateMod

        def showSize(self,nFile):
            self.pthSl = self.textPath + '\\' + nFile
            self.fileSize =  os.path.getsize(self.pthSl)
            return convert_size(self,self.fileSize)

        def convert_size(self,size_bytes):
            if size_bytes == 0:
                return "0B"
            self.size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
            self.i = int(math.floor(math.log(size_bytes, 1024)))
            self.p = math.pow(1024, self.i)
            self.s = round(size_bytes / self.p, 2)
            return "%s %s" % (self.s, self.size_name[self.i])
        showName(self)
        showDate(self,self.nFile)
        showSize(self,self.nFile)