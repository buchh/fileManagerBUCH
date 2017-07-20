import maya.cmds as mc
import sys , os
if not 'D:\\bn\\python\\ygg' in sys.path :
    sys.path.append('D:\\bn\\python\\ygg')
        
import sublime.functionPlus04 as sf
reload(sf)

so = sf.functSO()
#==========================================
class guiBuch(object):
    def __init__(self):
        self.showfileList(so.default())
        self.selList = []
        self.sve = ''

    def cDefault(self,*args):
        self.selFile  = mc.textScrollList( 'showFileTextScroll',q=True,si = True)
        a = so.default()
        self.selList = self.showfileList(a)
        mc.text('pathText',l = '%s'%(so.textPath),e = True)
        mc.textScrollList('showFileTextScroll',e =True,ra = True, a = self.listScroll,dcc = self.cProject)
        
    def cProject(self,*args):
        self.selFile  = mc.textScrollList( 'showFileTextScroll',q=True,si = True)
        a = so.project(str(self.selFile[0]))
        self.pj = self.showfileList(a)
        mc.text('pathText',l = '%s'%(so.textPath),e = True)
        mc.textScrollList('showFileTextScroll',e =True,ra = True, a = self.listScroll,dcc = self.cProjectManage)
    def btPj(self,*args):
        self.listScroll = self.pj
        mc.textScrollList('showFileTextScroll',e =True,ra = True, a = self.listScroll ,dcc = self.cProjectManage)

    def cProjectManage(self,*args):
        self.selFile  = mc.textScrollList( 'showFileTextScroll',q=True,si = True)
        a = so.seq_asset(str(self.selFile[0]))
        self.pjm = self.showfileList(a)
        mc.text('pathText',l = '%s'%(so.textPath),e = True)
        mc.textScrollList('showFileTextScroll',e =True,ra = True, a = self.listScroll ,dcc = self.cSeqAss)
    def btPjM(self,*args):
        self.listScroll = self.pjm
        mc.textScrollList('showFileTextScroll',e =True,ra = True, a = self.listScroll ,dcc = self.cSeqAss)

    def cSeqAss(self,*args):
        self.selFile  = mc.textScrollList( 'showFileTextScroll',q=True,si = True)
        a = so.name_seq_asset(str(self.selFile[0]))
        self.sqAs = self.showfileList(a)
        mc.text('pathText',l = '%s'%(so.textPath),e = True)
        mc.text('nameText',l ='%s'%(so.showName()) ,e = True)
        mc.textScrollList('showFileTextScroll',e =True,ra = True, a = self.listScroll,dcc = self.cShNam)
    def btSqas(self,*args):
        self.listScroll = self.sqAs
        mc.textScrollList('showFileTextScroll',e =True,ra = True, a = self.listScroll ,dcc = self.cShNam)

    def cShNam(self,*args):
        self.selFile  = mc.textScrollList( 'showFileTextScroll',q=True,si = True)
        a = so.shots_name(str(self.selFile[0]))
        self.shNa = self.showfileList(a)
        mc.text('pathText',l = '%s'%(so.textPath),e = True)
        mc.text('nameText',l ='%s'%(so.showName()) ,e = True)
        mc.textScrollList('showFileTextScroll',e =True,ra = True, a = self.listScroll,dcc = self.cDept)
    def btDp(self,*args):
        self.listScroll = self.shNa
        mc.textScrollList('showFileTextScroll',e =True,ra = True, a = self.listScroll ,dcc = self.cDept)

    def cDept(self,*args):
        self.selFile  = mc.textScrollList( 'showFileTextScroll',q=True,si = True)
        a = so.dept(str(self.selFile[0]))
        self.dpt = self.showfileList(a)
        mc.text('pathText',l = '%s'%(so.textPath),e = True)
        mc.text('nameText',l ='%s'%(so.showName()) ,e = True)
        mc.textScrollList('showFileTextScroll',e =True,ra = True, a = self.listScroll,dcc = self.cScenes)
    def btS(self,*args):
        self.listScroll = self.dpt
        mc.textScrollList('showFileTextScroll',e =True,ra = True, a = self.listScroll ,dcc = self.cScenes)

    def cScenes(self,*args):
        self.selFile  = mc.textScrollList( 'showFileTextScroll',q=True,si = True)
        a = so.scene(str(self.selFile[0]))
        self.showfileList(a)
        mc.text('pathText',l = '%s'%(so.textPath),e = True)
        self.sve = mc.text('nameText',l ='%s'%(so.showName()) ,e = True)
        mc.textScrollList('showFileTextScroll',e =True,ra = True, a = self.listScroll,dcc = self.cFile)

    def cFile(self,*args):
        self.selFile  = mc.textScrollList( 'showFileTextScroll',q=True,si = True)
        self.refreshDisplay()
    
    def refreshDisplay(self,*args):
        mc.text('date',l = '%s'%(so.showDate(self.selFile[0])),e =True)
        mc.text('size',l = '%s'%(so.showSize(self.selFile[0])),e =True)
        
        
    def refreshNameTask(self,item):
        so.task(item)
        mc.text('nameText',l ='%s'%(so.showName()) ,e = True)
        
    def refreshVer(self,*args):
        dd = mc.optionMenu('taskOp',q = True,v = True)
        self.refreshNameTask(dd)
        
    def showfileList(self,item):
        self.listScroll = item
        return self.listScroll
        
    def currFile(self,*args):
        self.selN  = mc.textScrollList( 'showFileTextScroll',q=True,si = True)
        mc.text('nameText',l ='%s'%(self.selN[0]) ,e = True)
        self.opName = self.selN[0]
        self.refreshDisplay()
        
    def op(self,*args):
        print self.opName
        so.openFile(self.opName)
    def sv(self,*args):
        so.saveFile()
        path = mc.text('pathText',q = True,l = True)
        print path
        a = os.listdir(path)
        print a
        self.showfileList(a)
        mc.textScrollList('showFileTextScroll',e =True,ra = True, a = self.listScroll)
        
    def cls(self,*args):
        mc.deleteUI('guiBuch',wnd =True)
        

    #===========================================
    def GUI(self):
        if mc.window('guiBuch',exists = True):
            mc.deleteUI('guiBuch')
        mc.window( 'guiBuch', t = 'guiBUCH Open/Save' )
        listScroll = so.default()
        mc.columnLayout( 'mainLayout', adj = True)
    ################################
    #            PATH              #
    ################################    
        mc.rowLayout( 'pathRowLayout',p = 'mainLayout',numberOfColumns = 2,columnWidth2 =(100,700),height = 50,adj = True )
        mc.text('Path :',w = 100)
        mc.text('pathText',l = '%s'%(so.textPath),w=700,bgc = [1.0,0.2,0.6])

    ################################
    #            PROJECT           #
    ################################
        mc.rowLayout( 'folderRowLayout',p = 'mainLayout',numberOfColumns = 2,columnWidth2 =(200,600),height = 350 ,rat = (1,'top',0),adj = 2)
        mc.columnLayout('pjColLayout',p = 'folderRowLayout',columnWidth = 200,h = 350)
        mc.button('pj' ,l = 'project',p = 'pjColLayout',w = 200,h = 40 ,bgc = [1.0,0.2,0.6],c = self.cDefault )
        mc.button('pjm' ,l = 'project manage',p = 'pjColLayout',w = 200,h = 40,bgc = [1.0,0.2,0.6],c = self.btPj)
        mc.button('sqas' ,l = 'sequences/assets',p = 'pjColLayout',w = 200,h = 40,bgc = [1.0,0.2,0.6] ,c = self.btPjM)
        mc.button('shn' ,l = 'shot/name',p = 'pjColLayout',w = 200,h = 40,bgc = [1.0,0.2,0.6],c = self.btSqas)
        mc.button('dp' ,l = 'dept',p = 'pjColLayout',w = 200,h = 40,bgc = [1.0,0.2,0.6],c = self.btDp)
        mc.button('sc' ,l = 'scenes',p = 'pjColLayout',w = 200,h = 40,bgc = [1.0,0.2,0.6],c = self.btS)

    ################################
    #           DATE SIZE          #
    ################################ 
        mc.rowLayout( 'dateRowLayout',p = 'pjColLayout',numberOfColumns = 2,columnWidth2 =(50,150),h = 80,rat = [(1,'bottom',0),(2,'bottom',0)],cat = [(1,'both',2),(2,'both',2)])
        mc.text(l = 'Date :')
        mc.text('date',l = 'Y/M/D',bgc = [1.0,0.2,0.6])
        mc.rowLayout( 'sizeRowLayout',p = 'pjColLayout',numberOfColumns = 2,columnWidth2 =(50,150),h = 30,rat = [(1,'bottom',2),(2,'bottom',2)],cat = [(1,'both',2),(2,'both',2)])
        mc.text(l = 'Size :')
        mc.text('size',l = 'KB',bgc = [1.0,0.2,0.6])

    ################################
    #         FOLDER SCROLL        #
    ################################
        mc.columnLayout('showFileLayout',p = 'folderRowLayout',columnWidth = 600,h = 350)
        mc.textScrollList('showFileTextScroll',p = 'showFileLayout',w = 600,h = 345,numberOfRows=10,a = self.listScroll,dcc = self.cProject)

        
    ################################
    #           NAME /TASK         #
    ################################    
        mc.rowLayout( 'ntsRowLayout',p = 'mainLayout',numberOfColumns = 3,columnWidth3 = (100,600,100),height = 110,adj = 2)
        mc.columnLayout('ntColLayout',p = 'ntsRowLayout',columnWidth = 100, co = ['both',30],rs = 30)
        mc.text('Name :')
        mc.text('Task :')

    ################################
    #      SAVENAME /SET TASK      #
    ################################   
        mc.columnLayout('ntMidColLayout',p = 'ntsRowLayout',columnWidth = 100)
        mc.text('nameText',l= '%s'%(so.showName()),p = 'ntMidColLayout',w = 550,bgc = [1.0,0.2,0.6])
        mc.rowLayout('tvRowLayout',numberOfColumns = 2,columnWidth2 =(300,300),height = 50,rat =[(1, 'bottom', 4), (2, 'bottom', 7)],cat = [2,'both',30])
        mc.optionMenu('taskOp',p = 'tvRowLayout' ,w = 300,bgc = [1.0,0.2,0.6] ,cc = self.refreshNameTask)
        mc.menuItem( label='none' )
        mc.menuItem( label='master')
        mc.menuItem( label='block')
        mc.menuItem( label ='polish')

    ################################
    #        VERSION CHECK         #
    ################################
        mc.checkBox(l = 'version update',v = True,ofc = self.currFile,onc = self.refreshVer)
        
    ################################
    #        BUTTON OP SAV         #
    ################################    
        mc.columnLayout('oscColLayout',p = 'ntsRowLayout',columnWidth = 100 ,rs = 10,co = ('both',3))
        mc.button(l = 'open',p = 'oscColLayout',w = 90,h = 30,bgc = [1.0,0.2,0.6],c = self.op)
        mc.button(l = 'save',p = 'oscColLayout',w = 90,h = 30,bgc = [1.0,0.2,0.6],c = self.sv)
        mc.button(l = 'close',p = 'oscColLayout',w = 90,h = 20,bgc = [1.0,0.2,0.6],c = self.cls)

        mc.showWindow( 'guiBuch' )
        mc.window( 'guiBuch', e = True, w = 800, h = 500 )

        
g = guiBuch()
g.GUI()

