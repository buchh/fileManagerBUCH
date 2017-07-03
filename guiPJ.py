import maya.cmds as mc

class functSO():
    
    self.oriPath = 'C:\\Users\\User\\Documents\\yggintern'
    self.textPath = self.oriPath

    def pathBox(conPth):
        x = str(conPth)
        self.textPath += '\\' + str(conPth)
        #show path in text path|___\___\___\__|
        #if conPth == shot : #use regular exp pattern
        #saveName =+ str(conPth) + '_'
        #if conPth == file : #use regular exp pattern
        #saveName =+ str(conPth)
        self.saveName = ''
        searchShots = re.search('[a-zA-Z][0-9]+[_][0-9]+',x)
        searchShots = re.search(str(shots),x)
        searchDept = re.search(str(dept),x)
        searchtask = re.search('[a-zA-Z][0-9]+[_][0-9]+',x)
        if x in shots or x in dept :
            saveName =+ str(conPth) + '_'
        elif x in  
        else :
            saveName =+ str(conPth)
        #aText = searchText.group()
    def saveFile(textMPB):
        #oriPath = 'C:\\Users\\User\\Documents\\yggintern'
        #textbox write master ,polish ,block
        #mc.file( save = True )
        mc.file( rename = ) # M P B
        mc.file( type = 'mayaAscii', save = True )

    def openFile():
        #oriPath = 'C:\\Users\\User\\Documents\\yggintern'
        mc.file( self.textPath , open = True )

    '''def scene(pj,seq,shots,dept):
        pjPath = oriPath + '\\' + pj
        seqPath = pjPath + '\\' + seq
        shPath = seqPath + '\\' + shots
        dePath = shPath + '\\' + dept
        #nameFile = shots + '_' + dept + '_' + '''
    
    def default(pth):
        self.listPj = os.listdir(pth)
        #open gui > meet project page by oriPath 
        #auto in project page for select
        #project(pj)_click project page
    def project(pth,nFile):
        pathBox(nFile)
        dir = os.listdir(pth)
        self.listSq = []
        self.listAs = []
        for x in dir :
            searchSeq = re.search('sequences',x)
            searchAs = re.search('asset',x)
            if searchSeq :
                self.listSq.append(x) # listSeq append x 
            if searchAs :
                self.listAs.append(x)
        #show file in project
        #seq(pathBox,sq)_click seq page
    def seq_asset(nFile):
        pathBox(nFile)
        #show file in seq
        #shots(pathBox,sh)_click shots page
    def shots(nFile):
        pathBox(nFile)
        #show file in shots
        #dept(pathBox,dp)_click dept page
    def dept(nFile):
        pathBox(nFile)
        #show file in dept
        #scene(pathBox,sc)_click scene page
    def scene(nFile):
        pathBox(nFile)
        #show file in scene
        #fl = textbox for write file's name
        #saveFile(pathBox,fl)_click save

    