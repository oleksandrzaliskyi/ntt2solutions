from sys import argv
from os import listdir
from os.path import isdir, isfile

debug = False

sybs = ['{','}','(',')','[',']','.',',',';','+','-','*','/',
        '&','|','<','>','=','~']

def gentag(tag,text):
    return "<{0}> {1} </{0}>".format(tag,text)

class JackTokenizer:
    def __init__(self, inputstream):
        for item in inputstream:
            pass
            # print("item: {0}".format(item))
        lines = inputstream
        self.tokentypes = ['KEYWORD','identifier','SYMBOL','INT_CONST','STRING_CONST']
        self.keywords = ['class','method','function','constructor','int',
            'boolean','char','void','var','static','field','let','do',
            'if','else','while','return','true','false','null','this']
        self.symbols = ['{','}','(',')','[',']','.',',',';','+','-','*','/',
        '&','|','<','>','=','~']
        # Here is a place to append xml code
        self.tokens = []
        self.tokens.append('<tokens>')
        for line in lines:
            llen = len(line)
            #print()
            #print("line =                      {0}".format(line))
            llist = line.split(' ')

            # string constant in double quotation marks to be grouped
            llist0 = []
            nquotes = llist.count("\"")
            #print('nquotes = {0}'.format(nquotes))
            indexes = []
            for i in range(len(llist)):
                if llist[i]=="\"":
                    indexes.append(i)
            # if " occured in llist
            if len(indexes)>0:
                #print("indexes = {0}".format(indexes))
                index1 = indexes[0]
                index2 = indexes[1]
                strslice = llist[index1+1:index2]
                strtext = ' '.join(strslice)
                #print("strtext = {0}".format(strtext))
                llist0 = llist[:index1]
                llist0.append(strtext)
                llist1 = llist0 + llist[index2+1:]
                llist = llist1

            llist = [element for element in llist if len(element)>0]
            #print("llist = {0}".format(llist))
            for item in llist:
                if item in self.keywords:
                    self.tokens.append(gentag('keyword',item))
                elif item in self.symbols:
                    if item == '<':
                        self.tokens.append(gentag('symbol','&lt;'))
                    elif item == '>':
                        self.tokens.append(gentag('symbol','&gt;'))
                    elif item == '&':
                        self.tokens.append(gentag('symbol','&amp;'))
                    else:
                        self.tokens.append(gentag('symbol', item))
                elif item not in self.symbols and item not in self.keywords and item.isalpha():
                    self.tokens.append(gentag('identifier',item))
                elif item.isdigit():
                    self.tokens.append(gentag('integerConstant',item))
                elif item[0].isalpha():
                    self.tokens.append(gentag('stringConstant',item))
                else:
                    self.tokens.append(gentag('------------------',item))
        self.tokens.append('</tokens>')

        self.tokenlines = self.tokens[1:-1]
        # for item in tokenlines: print(item)
        self.counter = 0
        self.tokenlist = []
        for i in range(len(self.tokenlines)):
            curtokendict = self.gettoken(i) # returns dict
            self.tokenlist.append(curtokendict) # appends dict
        self.counter = 0

    def gettoken(self, index):
        if not index < len(self.tokenlines):
            return None
        currenttag = self.tokenlines[index]
        t=currenttag.split(' ')[1]
        tt=currenttag.split(' ')[0][1:-1]

        return {'token':t,'type':tt}

    def currenttoken(self):
        return self.gettoken(self.counter)

    def hasmoretokens(self):
        return self.counter<len(self.tokenlines)

    def tokentype(self):
        currenttag = self.tokenlines[self.counter]
        ttype=currenttag.split(' ')[0][1:-1]
        return ttype

    def advance(self):
        self.counter = self.counter + 1
        if (self.counter < len(self.tokenlines)):
            return self.tokenlines[self.counter]
        else:
            return None

    def lookahead1(self):
        if self.counter + 1 < len(self.tokenlines):
            ind = self.counter + 1
            tkn = self.tokenlines[ind].split(' ')[1]
            tokentype = self.tokenlines[ind].split(' ')[0][1:-1]
            return {'type':tokentype, 'token':tkn}
        else:
            return None

    def lookahead2(self):
        if self.counter + 2 < len(self.tokenlines):
            ind = self.counter + 2
            tkn = self.tokenlines[ind].split(' ')[1]
            tokentype = self.tokenlines[ind].split(' ')[0][1:-1]
            return {'type':tokentype, 'token':tkn}
        else:
            return None

class JackCodeCleaner:
    def __init__(self, pathtofile):
        f = open(pathtofile,'r')
        flines = f.readlines();
        f.close()
        flines1 = [line.split("//")[0] for line in flines]
        # // delete inline comments
        flines2 = [line for line in flines1 if not line.startswith("//")]
        flines2 = [line.rstrip().lstrip() for line in flines2]
        # /*delete long comments*/
        flines3 = [line for line in flines2 if (not (line.startswith("/*") or (line.startswith("*") or line.endswith("*/"))))]
        flines4 = [line.rstrip().lstrip() for line in flines3]
        flines5 = [line for line in flines4 if len(line)>0]
        for i in range(len(flines5)):
            currentfline = flines5[i]
            newfline = ''
            for char in currentfline:
                if char in sybs or char =="\"":
                    newfline += ' '
                    newfline+=char
                    newfline += ' '
                else:
                    newfline += char
            flines5[i] = newfline

        self.codelines = flines5



class JackAnalyzer:
    def __init__(self,tokenizer):
        self.t = tokenizer
        self.markup = []
        self.tokens = self.t.tokenlist

    def lookahead1(self):
        return self.t.lookahead1()

    def advance(self):
        self.t.advance()
    def curtoken(self):
        return self.t.currenttoken()

    def hasmoretokens():
        return self.t.hasmoretokens()

    def analyze(self):
        if self.curtoken()['token'] == 'class':
            self.analyzeclass()

    def analyzeclass(self):
        self.markup.append('<class>')
        print('analyzing class')
        while not self.curtoken()['token'] == '{':
             ctok = self.curtoken()
             self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
             self.advance()

        ctok = self.curtoken()
        self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
        self.advance()

        while self.curtoken()['token'] in ['static','field']:
            self.analyzeclassvardec()


        while self.curtoken()['token'] in [';','method','function','constructor']:
            self.analyzesubroutine()

        # }
        ctok = self.curtoken()
        self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
        self.advance()

        self.markup.append('</class>')

    def analyzeclassvardec(self):
        self.markup.append('<classVarDec>')
        while not self.curtoken()['token'] in [';','method','function','constructor']:
            ctok = self.curtoken()
            self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
            self.advance()

        ctok = self.curtoken()
        self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
        self.advance()


        self.markup.append('</classVarDec>')


    def analyzesubroutine(self):
        self.markup.append('<subroutineDec>')
        while not self.curtoken()['token'] == '(':
            ctok = self.curtoken()
            self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
            self.advance()
        # (
        ctok = self.curtoken()
        self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
        self.advance()


        self.analyzeparameterlist()

        # )
        ctok = self.curtoken()
        self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
        self.advance()

        self.analyzesubroutinebody()

        self.markup.append('</subroutineDec>')

    def analyzeparameterlist(self):
        self.markup.append('<parameterList>')
        while not self.curtoken()['token'] == ')':
            ctok = self.curtoken()
            self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
            self.advance()
        self.markup.append('</parameterList>')

    def analyzesubroutinebody(self):
        self.markup.append("<subroutineBody>")

        # {
        ctok = self.curtoken()
        self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
        self.advance()

        # variable declarations
        while self.curtoken()['token'] == "var":
            self.analyzevardec()
        # method body
        self.analyzestatements()

        # }
        ctok = self.curtoken()
        self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
        self.advance()


        self.markup.append("</subroutineBody>")


    def analyzevardec(self):
        self.markup.append('<varDec>')
        while not self.curtoken()['token'] == ';':
            ctok = self.curtoken()
            self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
            self.advance()
        # ;
        ctok = self.curtoken()
        self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
        self.advance()

        self.markup.append('</varDec>')

    def analyzestatements(self):
        self.markup.append('<statements>')
        while self.curtoken()['token'] in ['let','do','if','while','return']:
            self.analyzestatement();

        self.markup.append('</statements>')

    def analyzestatement(self):
        if self.curtoken()['token'] == 'do':
            print('do statement met')
            self.analyzedo();

        if self.curtoken()['token'] == 'if':
            print('if statement met')
            self.analyzeif()
            #input()
        if self.curtoken()['token'] == 'while':
            print('while statement met')
            self.analyzewhile()

        if self.curtoken()['token'] == 'let':
            self.analyzelet()

        if self.curtoken()['token'] == 'return':
            print('return statement met')
            #input()
            self.analyzereturn()

    def analyzelet(self):
        self.markup.append('<letStatement>')
        # print('let statement met')
        # input()
        while not self.curtoken()['token'] == '=':
            ctok = self.curtoken()
            self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
            self.advance()

        # =
        ctok = self.curtoken()
        self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
        self.advance()

        # права частина рівняння
        self.analyzeexpression()

        # ;
        ctok = self.curtoken()
        self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
        self.advance()

        self.markup.append('</letStatement>')

    def analyzedo(self):
        self.markup.append('<doStatement>')
        while not self.curtoken()['token'] == '(':
            ctok = self.curtoken()
            self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
            self.advance()

        # (
        ctok = self.curtoken()
        self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
        self.advance()

        self.analyzeexpressionlist()

        # )
        ctok = self.curtoken()
        self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
        self.advance()

        # ;
        ctok = self.curtoken()
        self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
        self.advance()

        self.markup.append('</doStatement>')

    def analyzereturn(self):
        self.markup.append("<returnStatement>")

        # return
        ctok = self.curtoken()
        self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
        self.advance()

        if not self.curtoken()['token'] == ';':
            self.analyzeexpression()

        # ;
        ctok = self.curtoken()
        self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
        self.advance()

        self.markup.append("</returnStatement>")

    def analyzeif(self):
        self.markup.append('<ifStatement>')

        # if
        ctok = self.curtoken()
        self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
        self.advance()

        if self.curtoken()['token'] == '(':
            # (
            ctok = self.curtoken()
            self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
            self.advance()

        if not self.curtoken()['token'] == ')':
            self.analyzeexpression()

        if self.curtoken()['token'] == ')':
            # )
            ctok = self.curtoken()
            self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
            self.advance()

        if self.curtoken()['token'] == "{":
            ctok = self.curtoken()
            self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
            self.advance()

        self.analyzestatements()

        # }
        ctok = self.curtoken()
        self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
        self.advance()
        self.markup.append('</ifStatement>')

    def analyzewhile(self):
        self.markup.append('<whileStatement>')

        # while
        ctok = self.curtoken()
        self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
        self.advance()

        if self.curtoken()['token'] == '(':
            # (
            ctok = self.curtoken()
            self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
            self.advance()

        if not self.curtoken()['token'] == ')':
            self.analyzeexpression()

        if self.curtoken()['token'] == ')':
            # )
            ctok = self.curtoken()
            self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
            self.advance()

        if self.curtoken()['token'] == "{":
            ctok = self.curtoken()
            self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
            self.advance()

        self.analyzestatements()

        if self.curtoken()['token'] == "}":
            ctok = self.curtoken()
            self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
            self.advance()

        self.markup.append('</whileStatement>')

    def analyzeexpression(self):
        ops = ['+','-','*','/','&amp;','|','&lt;','&gt;','=']
        unaryops = ['~','-']
        self.markup.append('<expression>')
        self.analyzeterm()
        while not self.curtoken()['token'] in [';',',',')']:
            self.advance()
        self.markup.append('</expression>')

    def analyzeexpressionlist(self):
        self.markup.append('<expressionList>')

        if not self.curtoken()['token'] == ')':
            print('entered line 365')
            for item in self.markup: print("{0}".format(item))
            #input()
            while not self.curtoken()['token'] in [',',')']:
                self.analyzeexpression()
                print(self.curtoken())
                #input()
                if self.curtoken()['token'] == ',':
                    ctok = self.curtoken()
                    self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
                    self.advance()

        self.markup.append('</expressionList>')

    def analyzeterm(self):
        self.markup.append('<term>')
        if self.curtoken()['token'] == '(':
            # (
            ctok = self.curtoken()
            self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
            self.advance()

            self.analyzeexpression()

            # )
            ctok = self.curtoken()
            self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
            self.advance()
        else:
            ctok = self.curtoken()
            self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
            self.advance()

        self.markup.append('</term>')


# ./tools/TextComparer.sh projects/10/Square/Square.xml projects/10/Square/SquareTEST.xml

if __name__=="__main__":
    if not len(argv) == 2:
        print('Довжина аргумент-вектора має дорівнювати 2')
        print('вихід з програми')
        exit()
    path_to_batch = argv[1]
    if isdir(path_to_batch):
        pass
    if isfile(path_to_batch):
        # print('the path leads to a file')
        jkfilename = path_to_batch
        jkcodecleaned = JackCodeCleaner(jkfilename)
        tokenizer = JackTokenizer(jkcodecleaned.codelines)
        xmlfilename = jkfilename[:-5]+'TGEN'+'.xml'
        with open(xmlfilename,'w') as f:
            for line in tokenizer.tokens:
                f.write(line)
                f.write("\n")
        anz = JackAnalyzer(tokenizer)
        xmlname = jkfilename[:-5]+'TEST'+'.xml'

        anz.analyze()
        # reformat markup

        stk = 0 # markup stack

        # make left gap bigger
        for i in range(len(anz.markup)):
            anz.markup[i] = anz.markup[i].lstrip().rstrip()
            line = anz.markup[i].split(" ")

            if len(line) == 1:
                # closing tag

                if "/" in line[0]:
                    stk = stk - 1
            anz.markup[i] = " "*stk*2 + anz.markup[i]
            if len(line) == 1:
                if "/" not in line[0]:
                    stk = stk + 1



        with open(xmlname,'w') as f:
            for line in anz.markup:
                f.write(line)
                f.write('\n')
