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
        self.sh = ''
        self.dep = ''
        self.version = ''
        self.nFile = ''
        self.taskN = ''
        self.waySA = 0
        self.firstName = ''

    def pathBox(self):
        return self.textPath

    def checkVersion(self):
        self.dirr = os.listdir(self.textPath)
        print self.textPath

        def master(self):
            check = False
            for x in self.dirr :
                searchObj = re.search('master', x)
                if searchObj :
                    print 'have master'
                    ver = x[-6:-3]
                    print ver
                    newVer = "%03d"%(int(ver)+1)
                    print newVer
                    check = True
            if check == False :
                newVer = '001'
            self.version = 'v' + newVer + '.ma'
            print self.version

        def polish(self):
            check = False
            for x in self.dirr :
                searchObj = re.search('polish', x)
                if searchObj :
                    ver = x[-6:-3]
                    newVer = "%03d"%(int(ver)+1)
                    check = True
            if check == False :
                newVer = '001'
            self.version = 'v' + newVer + '.ma'

        def block(self):
            check = False
            for x in self.dirr :
                if 'block' in x :
                    print 'have block'
                    ver = x[-6:-3]
                    print ver
                    newVer = "%03d"%(int(ver)+1)
                    print newVer
                    check = True
            if check == False :
                newVer = '001'
            print 'newVer='+newVer
            self.version = 'v' + newVer + '.ma'

        def none(self):
            check = False
            for x in self.dirr :
                searchObj = re.search('[v][0-9]{3}', x)
                if searchObj :
                    ver = x[-6:-3]
                    newVer = "%03d"%(int(ver)+1)
                    check = True
            if check == False :
                newVer = '001'
            self.version = 'v' + newVer + '.ma'
            #return self.version
        
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
        print item
        self.taskN = item
        self.firstName = ''
        self.showName()

    def saveSeq(self):
        self.firstName = ''
        self.checkVersion()
        print self.version
        self.firstName = self.textPath + '\\' + self.sh + '_' + self.dep + '_' + self.taskN + '.' 
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
        self.checkVersion()
        self.saveName =  self.textPath + '\\' + self.sN + '_' + self.sh + '_' + self.dep + '.' + self.version
        a = os.path.basename(self.saveName)
        return a      

#############################################
#                                           #
#              SEQUENCES/ASSETS             #
#                                           #
#############################################
    def saveFile(self):
        print self.saveName
        mc.file( rename = self.saveName ) 
        mc.file( type = 'mayaAscii', save = True,f = True )
    
    def openFile(self,nFile):
        self.openName = self.textPath + '\\' + nFile 
        print self.openName
        mc.file( self.openName , open = True ,f =True)        
        
    def default(self,*args):
        self.pathBox()
        self.listPj = os.listdir(self.oriPath)
        return self.listPj
    
    def project(self,item):
        a = 'C:\Users\User\Documents\yggintern'
        self.pjPth = a + '\\' + item
        self.textPath = self.pjPth
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
            elif searchNas :
                self.listNas.append(x)
                self.waySA = 1
        if self.waySA == 0 :
            return self.listNsq
        elif self.waySA == 1 :
            return self.listNas
    
    def name_seq_asset(self,item):
        print item
        self.sN = ''
        a = self.saPth
        print item
        self.nsaPth = a + '\\' + item
        self.textPath = self.nsaPth
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
        if self.waySA == 0 :
            return self.listSh
        elif self.waySA == 1 :
            self.sN += item[0:4]
            print self.sN
            return self.listNa
             
        
    def shots_name(self,item):
        self.sh = ''
        a = self.nsaPth
        self.shPth = a + '\\' + item
        self.textPath = self.shPth
        self.sh += item
        print self.sh
        self.pathBox()
        self.listDep = os.listdir(self.textPath)
        return self.listDep

    def dept(self,item):
        self.dep = ''
        a = self.shPth
        self.dPth = a + '\\' + item
        self.textPath = self.dPth
        self.dep += item
        self.pathBox()
        self.listScene = os.listdir(self.textPath)
        return self.listScene
        
    
    def scene(self,item):
        a = self.dPth
        self.sth = a + '\\' + item
        self.textPath = self.sth
        self.pathBox()
        self.listFile = os.listdir(self.textPath)
        return self.listFile

#############################################
#                                           #
#                 DISPLAY                   #
#                                           #
#############################################

    def showName(self):
        if self.waySA == 0 :
            return self.saveSeq()
        elif self.waySA == 1 :
            return self.saveAss()
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
        a = self.convert_size(self.fileSize)
        return a

    def convert_size(self,size_bytes):
        if size_bytes == 0:
            return "0B"
        self.size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        self.i = int(math.floor(math.log(size_bytes, 1024)))
        self.p = math.pow(1024, self.i)
        self.s = round(size_bytes / self.p, 2)
        return "%s %s" % (self.s, self.size_name[self.i])