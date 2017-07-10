import maya.cmds as mc
'''import sys 
if not 'D:\\bn\\python\\ygg' in sys.path :
    sys.path.append('D:\\bn\\python\\ygg')
    
import sublime.function05 as sf
reload(sf)

so = sf.functSO()'''
#===========================================
def GUI():
    if mc.window('guiBuch',exists = True):
        mc.deleteUI('guiBuch')
    mc.window( 'guiBuch', t = 'guiBUCH Open/Save' )
    
    mc.columnLayout( 'mainLayout', adj = True )
    
    mc.rowLayout( 'pathRowLayout',p = 'mainLayout',numberOfColumns = 2,columnWidth2 =(100,700),height = 50 )
    mc.text('Path :',w = 100)
    #mc.button(p = 'pathRowLayout',w = 100,h = 50)
    mc.text('C:\\user\\user\\',w=700)
    #mc.button(p = 'pathRowLayout',w = 700,h = 50)
    
    mc.rowLayout( 'folderRowLayout',p = 'mainLayout',numberOfColumns = 2,columnWidth2 =(200,600),height = 350 ,rat = (1,'top',0))
    mc.columnLayout('pjColLayout',p = 'folderRowLayout',columnWidth = 200,h = 350)
    mc.button(l = 'project',p = 'pjColLayout',w = 200,h = 40)
    mc.button(l = 'project manage',p = 'pjColLayout',w = 200,h = 40)
    mc.button(l = 'sequences/assets',p = 'pjColLayout',w = 200,h = 40)
    mc.button(l = 'shot/name',p = 'pjColLayout',w = 200,h = 40)
    mc.button(l = 'scenes',p = 'pjColLayout',w = 200,h = 40)
    mc.text(' ',w = 200 , h = 50)
    mc.text('Date :',w = 200,h = 50)
    mc.text('Size:',w = 200 ,h = 50)
    #mc.button(p = 'folderRowLayout',w = 200,h = 350)
    #mc.columnLayout('dsColLayout',p = 'folderRowLayout',columnWidth = 200)
    #mc.text('Date :')
    #mc.text('Size:')
    mc.button(p = 'folderRowLayout',w = 600,h = 350)
    
    
    mc.rowLayout( 'ntsRowLayout',p = 'mainLayout',numberOfColumns = 3,columnWidth3 = (100,600,100),height = 100 )
    mc.columnLayout('ntColLayout',p = 'ntsRowLayout',columnWidth = 100, co = ['both',30],rs = 30)
    mc.text('Name :')
    #mc.text(' ',h = 30)
    #mc.button(l = 'name',p = 'ntColLayout',w = 100,h = 50)
    mc.text('Task :')
    #mc.button(l = 'task',p = 'ntColLayout',w = 100,h = 50)
    
    mc.columnLayout('ntMidColLayout',p = 'ntsRowLayout',columnWidth = 100)
    mc.button(p = 'ntMidColLayout',w = 600,h = 50)
    #mc.button(p = 'ntMidColLayout',w = 600,h = 50)
    mc.rowLayout('tvRowLayout',numberOfColumns = 2,columnWidth2 =(300,300),height = 50)
    mc.button(p = 'tvRowLayout',w = 300,h = 50)
    mc.button(p = 'tvRowLayout',w = 300,h = 50)
    
    mc.columnLayout('oscColLayout',p = 'ntsRowLayout',columnWidth = 100 ,rs = 5,co = ('both',3))
    mc.button(l = 'open',p = 'oscColLayout',w = 90,h = 30)
    mc.button(l = 'save',p = 'oscColLayout',w = 90,h = 30)
    mc.button(l = 'cancel',p = 'oscColLayout',w = 90,h = 20)
    
    
    #mc.button(p = 'ntRowLayout',w = 600,h = 100)
    #mc.button(p = 'ntRowLayout',w = 100,h = 100)
    
    ''' mc.rowLayout( 'taskRowLayout',p = 'mainLayout',numberOfColumns = 3,columnWidth3 =(100,600,100),height = 50 )
    mc.button(p = 'taskRowLayout',w = 100,h = 50)
    mc.rowLayout('versionRowLayout',numberOfColumns = 2,columnWidth2 =(300,300),height = 50)
    mc.button(p = 'versionRowLayout',w = 300,h = 50)
    mc.button(p = 'versionRowLayout',w = 300,h = 50)
    mc.button(p = 'taskRowLayout',w = 100,h = 50)'''
    
    #mc.button()
    mc.showWindow( 'guiBuch' )
    mc.window( 'guiBuch', e = True, w = 800, h = 500 )
GUI()
