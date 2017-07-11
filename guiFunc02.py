import maya.cmds as mc
import sys 
if not 'D:\\bn\\python\\ygg' in sys.path :
    sys.path.append('D:\\bn\\python\\ygg')
        
import sublime.functionPlus01 as sf
reload(sf)

so = sf.functSO()
#==========================================
class guiBuch(object):
    def __init__(self):
        self.showfileList(so.default())

    '''def project(self,item):
        pth = 'C:\\Users\\User\\Documents\\yggintern'
        pth += '\\' + item
        print pth
        return pth'''
            
    def test(self,*args):
        self.testT  = mc.textScrollList( 'showFileTextScroll',q=True,si = True)
        a = so.project(str(self.testT[0]))
        self.showfileList(a)
       # mc.textScrollList('showFileTextScroll',e =True,ra = True)
        mc.textScrollList('showFileTextScroll',e =True,ra = True, a = self.listScroll)
        
    def showfileList(self,item):
        #print item
        self.listScroll = item
        print self.listScroll
        
    def selFolder(self):
        selFile = mc.textScrollList( 'showFileTextScroll',q=True,si = True)
        print selFile[0]
        return selFile[0]
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
        mc.button('pj' ,l = 'project',p = 'pjColLayout',w = 200,h = 40 ,bgc = [1.0,0.2,0.6])
        mc.button('pjm' ,l = 'project manage',p = 'pjColLayout',w = 200,h = 40,bgc = [1.0,0.2,0.6])
        mc.button('sqas' ,l = 'sequences/assets',p = 'pjColLayout',w = 200,h = 40,bgc = [1.0,0.2,0.6])
        mc.button('shn' ,l = 'shot/name',p = 'pjColLayout',w = 200,h = 40,bgc = [1.0,0.2,0.6])
        mc.button('sc' ,l = 'scenes',p = 'pjColLayout',w = 200,h = 40,bgc = [1.0,0.2,0.6])

    ################################
    #           DATE SIZE          #
    ################################ 
        mc.rowLayout( 'dateRowLayout',p = 'pjColLayout',numberOfColumns = 2,columnWidth2 =(50,150),h = 120,rat = [(1,'bottom',0),(2,'bottom',0)],cat = [(1,'both',2),(2,'both',2)])
        mc.text(l = 'Date :')
        mc.text(l = '2017 10 JULY 15:58',bgc = [1.0,0.2,0.6])
        mc.rowLayout( 'sizeRowLayout',p = 'pjColLayout',numberOfColumns = 2,columnWidth2 =(50,150),h = 30,rat = [(1,'bottom',2),(2,'bottom',2)],cat = [(1,'both',2),(2,'both',2)])
        mc.text(l = 'Size :')
        mc.text(l = '3 MB',bgc = [1.0,0.2,0.6])

    ################################
    #         FOLDER SCROLL        #
    ################################
        mc.columnLayout('showFileLayout',p = 'folderRowLayout',columnWidth = 600,h = 350)
        mc.textScrollList('showFileTextScroll',p = 'showFileLayout',w = 600,h = 345,numberOfRows=10,a = self.listScroll,dcc = self.test)
        
    ################################
    #           NAME /TASK         #
    ################################    
        mc.rowLayout( 'ntsRowLayout',p = 'mainLayout',numberOfColumns = 3,columnWidth3 = (100,600,100),height = 100,adj = 2)
        mc.columnLayout('ntColLayout',p = 'ntsRowLayout',columnWidth = 100, co = ['both',30],rs = 30)
        mc.text('Name :')
        mc.text('Task :')

    ################################
    #      SAVENAME /SET TASK      #
    ################################   
        mc.columnLayout('ntMidColLayout',p = 'ntsRowLayout',columnWidth = 100)
        mc.textField(p = 'ntMidColLayout',w = 550,bgc = [1.0,0.2,0.6])
        mc.rowLayout('tvRowLayout',numberOfColumns = 2,columnWidth2 =(300,300),height = 50,rat =[(1, 'bottom', 4), (2, 'bottom', 7)],cat = [2,'both',30])
        mc.optionMenu(p = 'tvRowLayout' ,w = 300,bgc = [1.0,0.2,0.6])
        mc.menuItem( label='master' )
        mc.menuItem( label='polish' )
        mc.menuItem( label='block' )
        mc.menuItem( l ='none')

    ################################
    #        VERSION CHECK         #
    ################################
        mc.checkBox(l = 'version update')
        
    ################################
    #        BUTTON OP SAV         #
    ################################    
        mc.columnLayout('oscColLayout',p = 'ntsRowLayout',columnWidth = 100 ,rs = 5,co = ('both',3))
        mc.button(l = 'open',p = 'oscColLayout',w = 90,h = 30,bgc = [1.0,0.2,0.6])
        mc.button(l = 'save',p = 'oscColLayout',w = 90,h = 30,bgc = [1.0,0.2,0.6])
        mc.button(l = 'cancel',p = 'oscColLayout',w = 90,h = 20,bgc = [1.0,0.2,0.6])


        #mc.textScrollList('showFileTextScroll' ,dcc = self.project('YIT'))
        #mc.textScrollList('showFileTextScroll' ,dcc = self.showfileList(self.selFolder))
        mc.showWindow( 'guiBuch' )
        mc.window( 'guiBuch', e = True, w = 800, h = 500 )
        
g = guiBuch()
g.GUI()

