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
        self.taskN = ''
        self.waySA = 0
        self.firstName = ''

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
    
    def task(self,item):
        #taskN = ['master','polish','block','none']
        print item
        self.taskN = item
        #return self.taskN
        self.firstName = ''
        self.showName()

    def saveSeq(self):
        #self.task()
        #self.firstName = ''
        #self.saveName = ''
        #print self.saveName
        self.checkVersion()
        #print self.taskN
        self.firstName = self.textPath + '\\' + self.shDep + '_' + self.taskN + '.' 
        if not os.path.exists(self.firstName) :
            self.saveName = self.firstName + self.version
        a = os.path.basename(self.saveName)
        return a
        

#############################################
#                                           #
#                 ASSETS                    #
#                                           #
#############################################

    def saveAss(self):
        #self.task()
        #self.firstName = ''
        #self.saveName = ''
        self.checkVersion()
        self.saveName =  self.textPath + '\\' + self.shDep + '.' + self.version 
        a = os.path.basename(self.saveName)
        return a      

#############################################
#                                           #
#              SEQUENCES/ASSETS             #
#                                           #
#############################################
    
    def openFile(self,nFile):
        self.openName = self.textPath + '\\' + nFile
        mc.file( self.textPath , open = True )        
        
    def default(self,*args):
        self.pathBox()
        self.listPj = os.listdir(self.oriPath)
        #self.listPj = ['one','two']
        #print self.listPj
        return self.listPj
    
    def project(self,item):
        a = 'C:\Users\User\Documents\yggintern'
        self.pjPth = a + '\\' + item
        self.textPath = self.pjPth
        #self.textPath += '\\' + item
        #print self.textPath
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
        return self.listSq + self.listAs    

          
    def seq_asset(self,item):
        a = self.pjPth
        self.saPth = a + '\\' + item
        self.textPath = self.saPth
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
                #return self.listNsq
            elif searchNas :
                self.listNas.append(x)
                self.waySA = 1
                #return self.listNas
        if self.waySA == 0 :
            return self.listNsq
        elif self.waySA == 1 :
            return self.listNas
    
    def name_seq_asset(self,item):
        a = self.saPth
        self.nsaPth = a + '\\' + item
        self.textPath = self.nsaPth
        #self.textPath += '\\' + item
        if self.waySA == 1 :
            self.shDep += item[0:4] + '_'
        self.pathBox()
        #print self.textPath
        dir = os.listdir(self.textPath)
        self.listSh = []
        self.listNa = []
        for x in dir :
            searchSh = re.search('[a-zA-Z][0-9]+[_][0-9]+',x)
            searchNa = re.search('[a-zA-Z]+',x)
            if searchSh :
                self.listSh.append(x) # listSeq append x 
                #return self.listSh 
            elif searchNa :
                self.listNa.append(x)
                #return self.listNa
        if self.waySA == 0 :
            return self.listSh
        elif self.waySA == 1 :
            return self.listNa
             
        
    def shots_name(self,item):
        self.shDep = ''
        a = self.nsaPth
        self.shPth = a + '\\' + item
        self.textPath = self.shPth
        #self.textPath += '\\' + item
        self.shDep += item
        self.pathBox()
        self.listDep = os.listdir(self.textPath)
        return self.listDep

    def dept(self,item):
        a = self.shPth
        self.dPth = a + '\\' + item
        self.textPath = self.dPth
        #self.textPath += '\\' + item
        self.shDep += '_' + item
        self.pathBox()
        self.listScene = os.listdir(self.textPath)
        return self.listScene
        
    
    def scene(self,item):
        a = self.dPth
        self.sth = a + '\\' + item
        self.textPath = self.sth
        #self.textPath += '\\' + item
        self.pathBox()
        self.listFile = os.listdir(self.textPath)
        return self.listFile

#############################################
#                                           #
#                 DISPLAY                   #
#                                           #
#############################################

    def showName(self):
        #print 'a'
        if self.waySA == 0 :
            return self.saveSeq()
        elif self.waySA == 1 :
            return self.saveAss()
        #print self.saveSeq()
        #print self.saveAss()
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