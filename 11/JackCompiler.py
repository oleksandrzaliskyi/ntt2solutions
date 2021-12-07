from sys import argv
from os import listdir, remove, getcwd
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
        t=currenttag.split('>')[1]
        t = t.split('<')[0][1:-1]
        #print('t ={0}***'.format(t))
        tt=currenttag.split(' ')[0][1:-1]
        #print({'token':t,'type':tt})
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

    def lookahead3(self):
        if self.counter + 3 < len(self.tokenlines):
            ind = self.counter + 3
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
        #print('analyzing class')
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
            #print('do statement met')
            self.analyzedo();

        if self.curtoken()['token'] == 'if':
            #print('if statement met')
            self.analyzeif()
            #input()
        if self.curtoken()['token'] == 'while':
            #print('while statement met')
            self.analyzewhile()

        if self.curtoken()['token'] == 'let':
            self.analyzelet()

        if self.curtoken()['token'] == 'return':
            #print('return statement met')
            #input()
            self.analyzereturn()

    def analyzelet(self):
        self.markup.append('<letStatement>')
        # #print('let statement met')
        while not self.curtoken()['token'] == '=':
            ctok = self.curtoken()
            self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
            self.advance()
            if self.curtoken()['token'] == '[':
                #[
                ctok = self.curtoken()
                self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
                self.advance()

                self.analyzeexpression()

                # ]
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

        if self.curtoken()['token'] == 'else':
            # else
            ctok = self.curtoken()
            self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
            self.advance()


            # {
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

        if self.curtoken()['token'] in ['~','-']:
            # unaryop
            self.analyzeterm()

        while not self.curtoken()['token'] in [';',',',')',']']:
            ##print('loopmark')
            ##print(self.markup)
            ##print(self.curtoken())
            #input()



            if self.curtoken()['token'] == ';':
                break
            if self.curtoken()['token'] == '(':
                self.analyzeterm()
            if (self.curtoken()['type'] in ['integerConstant','stringConstant','keyword','identifier']):
                self.analyzeterm()
            if self.curtoken()['token'] in (ops+unaryops+['.']):
                ctok = self.curtoken()
                self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
                self.advance()

        self.markup.append('</expression>')

    def analyzeexpressionlist(self):
        self.markup.append('<expressionList>')

        if not self.curtoken()['token'] == ')':
            #print('entered line 365')
            #for item in self.markup: print("{0}".format(item))
            #input()
            while not self.curtoken()['token'] in [',',')']:
                self.analyzeexpression()
                #print(self.curtoken())
                #input()

                if self.curtoken()['token'] == ',':
                    ctok = self.curtoken()
                    self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
                    self.advance()

        self.markup.append('</expressionList>')

    def analyzeterm(self):
        self.markup.append('<term>')

        if self.curtoken()['token'] in ['~','-']:

            # unaryop
            ctok = self.curtoken()
            self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
            self.advance()
            self.analyzeterm()

        elif self.curtoken()['token'] == '(':
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

            if self.curtoken()['token'] == '.':

                # .
                ctok = self.curtoken()
                self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
                self.advance()

                # method name
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

            elif self.curtoken()['token'] == '[':
                # [
                ctok = self.curtoken()
                self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
                self.advance()

                self.analyzeexpression()

                # ]
                ctok = self.curtoken()
                self.markup.append("<{0}> {1} </{0}>".format(ctok['type'],ctok['token']))
                self.advance()

        self.markup.append('</term>')


# ./tools/TextComparer.sh projects/10/Square/Square.xml projects/10/Square/SquareTEST.xml

class CompilationEngine:
    def __init__(self, analyzer):
        self.analyzer = analyzer
        self.tokenizer = self.analyzer.t
        self.tokens = self.analyzer.t.tokens[1:-1]
        self.counter = 0
        self.classst = SymbolTable()
        self.subst = SymbolTable()
        self.vmcode = []
        self.labels = []
        self.classsymboltable = SymbolTable()

        #for item in self.tokens:
        #    print(item)
        from classes import cls
        self.classnames = cls

        #for i in range(len(self.tokens)):
            #print(self.gettoken(i))
            #print(self.curtoken())
            #self.advance()
        self.counter = 0
        #print('end of tokenizer markup')
        #print('end of constructor')
        #input()

    def gettoken(self, ind):
        if ind < len(self.tokens):
            curxmltoken = self.tokens[ind].rstrip().lstrip()
            ttype = curxmltoken.split()[0][1:-1]
            #tkn = curxmltoken.split()[1]
            tkn = curxmltoken.split('>')[1].split('<')[0][1:-1]
            return {'token':tkn, 'type':ttype}
        else:
            return None

    def curtoken(self):
        return self.gettoken(self.counter)

    def lookahead1(self):
        return self.gettoken(self.counter + 1)

    def lookahead2(self):
        return self.gettoken(self.counter + 2)

    def lookahead3(self):
        return self.gettoken(self.counter + 3)

    def advance(self):
        self.counter += 1

    def hasmoretokens(self):
        return self.counter < len(self.tokens) - 1

    def whereami(self, keypress = False, msg = ''):
        strmsg = '' if msg == '' else ' {0} '.format(msg)
        #print(strmsg + 'at line {0}, current token: {1}'.format(
        #    self.counter + 2, self.curtoken()))
        if keypress:
            pass
            #input()

    def cmclass(self):
        self.whereami(msg='compileclass')
        self.advance()
        self.whereami(msg='compileclass')
        self.classname = self.curtoken()['token']
        print('classname = {0}'.format(self.classname))
        self.advance() # now on {
        self.advance() # now on classVarDec or subroutineDec
        self.classsymboltable = SymbolTable()
        self.classvartypes = ['field', 'static']
        #print('must be classVarDec')
        self.whereami()
        while self.curtoken()['token'] in self.classvartypes:
            self.cm_classvardec()

        self.subroutinetypes = ['constructor','function','method']



        while self.curtoken()['token'] in self.subroutinetypes:
            self.cm_subroutine()
            # print('compiled subroutine, now at')
            self.whereami()
            # print(self.classname)
            #input()

        # print('***************************************')
        # print('virtual machine code has been generated')
        # print('{} lines of vm code'.format(len(self.vmcode)))
        # print('***************************************')
        # print('class symbol table for {0}'.format(self.classname))
        # print(self.classsymboltable)

    def cm_classvardec(self):
        # print('compiling classVarDec')
        varkind = self.curtoken()['token']
        #input()
        segment = None
        if varkind == 'static':
            segment = 'static'
        elif varkind == 'field':
            segment = 'this'
        else:
            # print('Unknown segment name while cm_classvardec')
            self.whereami()
            #input()
        self.advance() # go to variable type
        vartype = self.curtoken()['token']
        self.advance()
        varname = self.curtoken()['token']
        self.classsymboltable.define(varname, vartype, segment)
        self.advance() # pass first varname
        while self.curtoken()['token'] == ',':
            self.advance()
            varname = self.curtoken()['token']
            self.classsymboltable.define(varname, vartype, segment)
            self.advance()
        self.advance() # pass ;
        # print('finished compiling classVarDec')
        self.whereami()


    def cm_subroutine(self):
        # print('compile subroutine')
        # input()

        self.srsymboltable = SymbolTable()
        # print('symbol table created')

        # now on subroutine type
        srtype = self.curtoken()['token']
        self.srtype = srtype

        self.advance() # to function type
        srrettype = self.curtoken()['token']


        if srtype in ['method',]:    # ['constructor','method']:
            self.srsymboltable.define('this', self.classname, 'argument')
        self.advance() # to subroutine name
        srname = self.curtoken()['token']

        self.advance() # to (
        self.advance() # to ) or first arg


        # if met - type varName
        if not self.curtoken()['token'] == ')': # if args met
            # first arg
            argtype = self.curtoken()['token']
            self.advance() # now on first argname
            argname = self.curtoken()['token']

            self.srsymboltable.define(argname, argtype,'argument')

            self.advance() # to ) or ,
            # (','type varName)*
            while self.curtoken()['token'] == ',':
                self.advance() # pass ,
                argtype = self.curtoken()['token']
                self.advance() # pass argument type
                argname = self.curtoken()['token']
                self.srsymboltable.define(argname, argtype,'argument')
                self.advance() # pass argument name
        # we are now on )
        self.advance()


        # print('self.vmcode = {0}'.format(self.vmcode))
        # input()

        # we are now on {

        self.advance()

        # print('compile local variables')
        # print(self.curtoken())
        # print(self.counter+2)
        # input()

        # compile local variables
        # var int a,b,c;
        while self.curtoken()['token'] == 'var':
            self.advance()
            vartype = self.curtoken()['token']
            self.advance()
            varname = self.curtoken()['token']
            self.srsymboltable.define(varname,vartype,'local')
            self.advance(); # to , or ;
            # , varname
            while self.curtoken()['token'] == ',':
                self.advance() # to varname
                varname = self.curtoken()['token']
                self.srsymboltable.define(varname,vartype,'local')
                self.advance() # to , or )
            self.advance() # pass ';'
        # print(self.srsymboltable)

        nlocals = self.srsymboltable.varcount('local')
        self.vmcode.append('')
        self.vmcode.append('function {0}.{1} {2}'.format(self.classname,
            srname, nlocals))

        if srtype == 'method':                  # Anchor the address
            self.vmcode.append('push argument 0')
            self.vmcode.append('pop pointer 0')


        if srtype == 'constructor':
            thiscount = self.classsymboltable.varcount('this')
            self.vmcode.append('push constant {}'.format(thiscount))
            self.vmcode.append('call Memory.alloc 1')
            self.vmcode.append('pop pointer 0')



        # all the names of void methods go to voidmethods.txt
        if srrettype == 'void':
            with open('voidmethods.txt','a') as f:
                f.write('{}.{}'.format(self.classname, srname))
                f.write(' ')


        # statements compilation
        self.whereami(msg = 'should be now beginning of statement')
        self.cm_statements()


        self.advance() # pass } in the end of subroutine
        # print('end of subroutine compilation, curtoken = {}'.format(self.curtoken()))
        # print('Symbol table of {}.{}'.format(self.classname,srname))
        # print(self.srsymboltable)

    def cm_statements(self):
        # print('compiling statements')
        self.whereami()
        self.statementtypes = ['while','if','do','return','let']
        while self.curtoken()['token'] in self.statementtypes:
            ctok = self.curtoken()['token']
            if ctok == 'do':
                # print('do statement met')
                self.whereami()
                #input()
                self.cm_do()
            elif ctok == 'while':
                #for item in self.vmcode: # print(item)
                # print('while statement met')
                self.whereami()
                #input()

                self.cm_while()

            elif ctok == 'let':
                # print('let statement met')
                self.whereami()
                #input()
                self.cm_let()
            elif ctok == 'return':
                # print('return statement met')
                self.whereami()
                #input()
                self.cm_return()
            elif ctok == 'if':
                # print('if statement met')
                self.whereami()
                #input()
                self.cm_if()
            else:
                self.whereami(keypress = True, msg = 'unknown statement type')
        # print('end compiling statements')
        self.whereami()

    def cm_let(self):
        """ 'let' varName('[' expression ']')? '=' expression ';' """
        # print('compile let')
        self.whereami(msg="compile let ")
        self.advance() # pass the let
        varname = self.curtoken()['token']
        # print('varname = {}'.format(varname))
        self.advance() # pass the varName, now on = or [
        if self.curtoken()['token'] == '[':
            # print('array assignment met in let statement (left)')
            self.whereami()
            #input()
            varobj = self.srsymboltable.lookup(varname)
            if varobj is None: varobj = self.classsymboltable.lookup(varname)
            if varobj is None:
                print('ERROR - cannot find array in the symbol table')

            # push array start address on the top of the stack
            self.vmcode.append('push {0} {1}'.format(varobj['segment'],
                varobj['num']))
            self.advance() # pass [
            self.cm_expression()
            self.vmcode.append('add') # a[i]: a+i on top of the stack
            self.advance() # pass ]
            self.advance() # pass =
            self.cm_expression() # expression value is on top of the stack

            # save the expression value to temp 4
            self.vmcode.append('pop temp 4') # save right part
            self.vmcode.append('pop pointer 1') # set address
            self.vmcode.append('push temp 4') # push right part
            self.vmcode.append('pop that 0') # assignment done


        elif self.curtoken()['token'] == '=':
            # print('no array option')
            self.advance() # pass the '=' token
            self.cm_expression()
            # now the expression value is on the top of the stack
            # need to pop it
            curvarobj = self.srsymboltable.lookup(varname)
            if curvarobj is None:
                curvarobj = self.classsymboltable.lookup(varname)
            # print('curvarobj = {}'.format(curvarobj))
            self.vmcode.append('pop {} {}'.format(
                curvarobj['segment'], curvarobj['num']))
        self.advance() #  pass ';' token
        # print('end compile let statement, curtoken = {}'.format(self.curtoken()))

    def writelabel(self,label):
        self.vmcode.append('label {}'.format(label))

    def cm_if(self):
        # print('IF')
        # print('compiling IF')
        self.advance() # pass the 'if' token
        self.advance() # pass ( token
        self.cm_expression()
        # print('if:         conditional  expression compiled')
        # print()
        self.whereami()
        self.advance() # pass ) token
        self.vmcode.append('not') # negate the expression

        # let's generate labels
        ifpaircount = int(len([x for x in self.labels if 'if' in x])/2)
        iflabel1 = 'if{}label1'.format(ifpaircount)
        iflabel2 = 'if{}label2'.format(ifpaircount)
        self.labels.append(iflabel1)
        self.labels.append(iflabel2)

        self.vmcode.append('if-goto {}'.format(iflabel1))

        self.advance() # pass the opening brackets of true option
        self.cm_statements()
        self.advance() # pass the closing brackets of true option




        self.vmcode.append('goto {}'.format(iflabel2))

        self.writelabel(iflabel1)


        # if else clause has been met
        if self.curtoken()['token'] == 'else':
            # print('else clause met ')
            self.advance() # pass else
            self.advance() # pass {
            self.cm_statements()
            self.advance() # pass }

        self.writelabel(iflabel2)
        # print('if statement has been compiled, ctok={}'.format(self.curtoken()))
        self.whereami()


    def cm_while(self):
        self.whereami(msg = 'compile while statement')

        # let's generate labels
        whilepaircount = len([x for x in self.labels if 'while' in x])
        # print('whilepaircount = {}'.format(whilepaircount))
        whilelabel1 = 'while{}label1'.format(whilepaircount)
        whilelabel2 = 'while{}label2'.format(whilepaircount)
        self.labels.append(whilelabel1)
        self.labels.append(whilelabel2)


        self.writelabel(whilelabel1)
        self.advance() # pass the 'while' token
        self.advance() # pass ( token
        self.cm_expression()
        self.advance() # pass ) token
        self.vmcode.append('not') # negate the expression
        # print('inside while after neg - {}'.format(self.curtoken()))


        self.vmcode.append('if-goto {}'.format(whilelabel2))

        self.advance() # pass the opening brackets of statements
        # print('before statements')
        # print(self.curtoken())
        self.cm_statements()
        self.advance() # pass the closing brackets of statements

        self.vmcode.append('goto {}'.format(whilelabel1))
        self.vmcode.append('label {}'.format(whilelabel2))
        # print('while statement has been compiled, ctok={}'.format(self.curtoken()))
        self.whereami()


    def cm_do(self):
        self.advance() # to classname

        ctok = self.curtoken()['token']
        # static methods or constructors
        if ctok in self.classnames:
            functocall = ''
            while not self.curtoken()['token'] == '(':
                functocall += self.curtoken()['token']
                self.advance()
            # now we are on ( token
            self.advance() # now on ) or expressionList
            # if there is at least one expression
            nargs = 0
            if not self.curtoken()['token'] == ')':
                nargs = self.cm_expressionlist()
            self.vmcode.append('call {} {}'.format(functocall, nargs))
            self.advance() # pass )
            self.advance() # pass ;
            # print('do statement compiled, curtoken = {}'.format(self.curtoken()))
            self.whereami()

        # call on instance OR one-word function name
        else:
            #if this is not one-word function name like do draw()
            if not self.lookahead1()['token'] == '(':
                varobj = self.srsymboltable.lookup(ctok)
                if varobj is None:
                    varobj = self.classsymboltable.lookup(ctok)
                if varobj is not None: # if var has been found in symboltables
                    self.cm_insrcall()
                    self.advance() # pass ;
                else:
                    # print('ERROR - could not find variable in symboltables')
                    self.whereami()
                    #input()
            #if that's one word function name
            elif self.lookahead1()['token'] == '(':
                funcname = self.classname + '.' + ctok
                self.advance() # to (
                self.vmcode.append('push pointer 0')

                self.advance() # pass (
                nargs = 1
                if not self.curtoken()['token'] == ')':
                    nargs += self.cm_expressionlist()
                # now we are on )
                self.advance()             # pass )
                self.advance()             # pass ;
                self.vmcode.append('call {} {}'.format(funcname, nargs))

    def cm_return(self):
        self.advance() # pass the return word
        # void subroutine pushes 0 onto the stack
        if self.curtoken()['token'] == ';':
            self.vmcode.append('push constant 0')
            self.vmcode.append('return')
        else:
            if self.srtype == 'constructor':
                self.vmcode.append('push pointer 0')
                self.vmcode.append('return')
                self.advance(); # pass 'this'
            else:
                self.cm_expression()
                self.vmcode.append('return')
        self.advance()      # pass ;



    def cm_expressionlist(self):
        """  (expression (',' expression)* )?  """
        # print('compile expressionList')
        self.cm_expression()
        quanexp = 1
        while self.curtoken()['token'] == ',':
            self.advance() # pass comma, go to next expression
            self.cm_expression()
            quanexp += 1
        return quanexp

    def cm_expression(self):
        """ term (op term)* """
        # print('compiling expression')
        self.opsymbols = ['+', '-', '*', '/', '&amp;', '|', '&lt;', '&gt;','=']
        self.unaryops = ['-','~']
        # print('term to compile: {}'.format(self.curtoken()))
        self.cm_term()
        # print('first term compiled: now at {0}'.format(self.curtoken()))
        self.whereami()
        while self.curtoken()['token'] in self.opsymbols:
            opsymbol = self.curtoken()['token']
            # print('{0} opsymbol met while compile expression'.format(opsymbol))
            # input()
            self.advance()
            self.whereami(msg = 'in while cycle of expression compilation')
            # print('term to compile: {}'.format(self.curtoken()))
            self.cm_term()
            self.writeop(opsymbol)
        # print('expression compiled')
        self.whereami()


    def cm_term(self):
        """integerConstant | stringConstant | keywordConstant | varName |
        | varName'[' expression ']' | subroutineCall | '(' expression ')'|
        unaryOp term """
        # print('compiling term')
        self.whereami()
        if self.term_isintegerconstant():
            # print('term integerConstant')
            num = int(self.curtoken()['token'])
            self.vmcode.append('push constant {0}'.format(num))
            self.advance()

        elif self.term_iskeywordconstant():
            # print('term keywordConstant')
            if self.curtoken()['token'] == 'this':
                self.vmcode.append('push argument 0')

            if self.curtoken()['token'] == 'true':
                self.vmcode.append('push constant 1')
                self.vmcode.append('neg')
            if self.curtoken()['token'] == 'false':
                self.vmcode.append('push constant 0')
            self.advance()

        elif self.term_isvarname():
            # print('term varname, varname = {}'.format(self.curtoken()))
            varname = self.curtoken()['token']
            self.advance()
            lu = self.srsymboltable.lookup(varname)
            segment, num = '',''
            if lu is None:
                lu = self.classsymboltable.lookup(varname)
            if lu is not None:
                self.vmcode.append('push {0} {1}'.format(
                    lu['segment'], lu['num']))
            else:
                # print('ERROR - should be not None, varname = {}'.format(varname))
                self.whereami(msg='term varname ERROR')

        elif self.term_isarrayname():
            #print('term term_isarrayname')
            #print('arrayname met')
            varname = self.curtoken()['token']

            varobj = self.srsymboltable.lookup(varname)
            if not varobj : self.classsymboltable.lookup(varname)

            self.vmcode.append('push {} {}'.format(varobj['segment'],
                varobj['num'])) # push base address
            self.advance() # pass arrayname
            self.advance() # pass [
            self.cm_expression() # increment is on the stack
            self.advance() # pass ]
            self.vmcode.append('add')
            self.vmcode.append('pop pointer 1')
            self.vmcode.append('push that 0') # the a[i] is on the stack now


        elif self.term_issubroutinecall():
            #print('term issubroutinecall')
            #print('subroutinecall met')
            self.whereami()
            ctok = self.curtoken()['token']

            # static function or constructor Classname.methodname()
            if ctok in self.classnames:
                nargs = 0
                funcname = ''
                while not self.curtoken()['token'] == '(':
                    funcname += self.curtoken()['token']
                    self.advance()
                self.advance() # pass (
                if not self.curtoken()['token'] == ')':
                    nargs = self.cm_expressionlist()
                self.advance() # pass )
                self.vmcode.append("call {} {}".format(funcname, nargs))
                #print('subroutinecall has been compiled (Classname.Methodname)')
                self.whereami()
            # method call on instance
            # check if instance is present in symbol tables
            # and then push it onto the stack
            elif self.srsymboltable.lookup(ctok) or self.classsymboltable.lookup(ctok) and self.lookahead1()['token'] == '.':
                #print('instance method call')
                self.whereami()
                self.cm_insrcall()

            # error?
            else:
                #print('ERROR - unknown subroutine call')
                self.whereami()
                #input()


        elif self.term_isexpinparentheses():
            #print('term expression in parentheses')
            self.advance() # pass (
            self.cm_expression()
            self.advance() # pass )

        elif self.term_isunaryopterm():
            #print('term unaryop term')
            unaryop = self.curtoken()['token']
            self.advance()
            self.cm_term()
            if unaryop == '-':
                self.vmcode.append('push constant 1')
                self.vmcode.append('neg')
                self.vmcode.append('call Math.multiply 2')
            elif unaryop == '~':
                self.vmcode.append('not')
        elif self.term_isstringconstant():
            # # print('string constant met')
            ctok = self.curtoken()['token']
            st = ctok
            self.advance() # pass the string constant
            strlen = len(st)

            # push length onto the stack
            self.vmcode.append('push constant {0}'.format(strlen))
            self.vmcode.append('call String.new 1')
            # now stringAdress on top of stack

            #let's save it into temp2
            self.vmcode.append('pop temp 2')
            self.vmcode.append('push temp 2')
            # now the address is on the stack but it's also in temp 2

            # for every symbol in the string, setCharAt called
            for ind in range(len(st)):
                # push char
                charint = ord(st[ind])
                self.vmcode.append('push constant {0}'.format(charint))
                # Method void setCharAt(int j, char c)
                self.vmcode.append('call String.appendChar 2')

            # now, the string address is on the top of the stack
            # strin constant compilation finished
            # memory leak
        #print('end compiling term')
        self.whereami()

    def cm_insrcall(self):
        #print('begin compile cm_insrcall')
        self.whereami()
        varname = self.curtoken()['token']
        instobj = self.srsymboltable.lookup(varname)
        if instobj is None:
            instobj = self.classsymboltable.lookup(varname)
        #should be not None now
        if instobj == None:
            #print('ERROR - varname {0} not found in symbol tables'.format(varname))
            self.whereami()
            #input()
        else:
            # process method call on instobj
            self.vmcode.append('push {0} {1}'.format(instobj['segment'],
                instobj['num']))
            instclass = instobj['type']
            self.advance() # pass instname
            self.advance() # pass '.' , now on methodname
            methodname = self.curtoken()['token']
            fname = instclass + '.' + methodname
            self.advance() # pass methodname
            self.advance() # pass (
            # number of arguments for function call, where 1 is for arg0
            # instance
            nargs = 1
            #self.whereami()
            #input()
            if not self.curtoken()['token'] == ')':
                nargs += self.cm_expressionlist()
            self.advance() # pass )
            #self.advance() # pass ;
            self.vmcode.append('call {0} {1}'.format(fname, nargs))
        #print('end compile cm_insrcall')
        self.whereami()

    def writeop(self, opsymbol):
        if opsymbol == '+':
            self.vmcode.append('add')
        elif opsymbol == '-':
            self.vmcode.append('sub')
        elif opsymbol == '*':
            self.vmcode.append('call Math.multiply 2')
        elif opsymbol == '/':
            self.vmcode.append('call Math.divide 2')
        elif opsymbol == '&amp;':
            self.vmcode.append('and')
        elif opsymbol == '|':
            self.vmcode.append('or')
        elif opsymbol == '&gt;':
            self.vmcode.append('gt')
        elif opsymbol == '&lt;':
            self.vmcode.append('lt')
        elif opsymbol == '=':
            self.vmcode.append('eq')
        else:
            print('ERROR: opsymbol = {0} \n need '
                     'to debug def writeop'.format(opsymbol))


    def term_isintegerconstant(self):
        if self.curtoken()['type'] == 'integerConstant':
            #print('term is integerConstant')
            return True
        return False

    def term_isstringconstant(self):
        if self.curtoken()['type'] == 'stringConstant':
            #print('term is stringConstant')
            return True
        return False

    def term_iskeywordconstant(self):
        if self.curtoken()['token'] in ['true','false','null','this']:
            #print('term is keywordConstant')
            return True
        return False

    def term_isvarname(self):
        """checks if the current term is a variable name"""
        ctok = self.curtoken()['token']
        # look up our var in the subroutine level symbol table
        srlookup = self.srsymboltable.lookup(ctok)
        if (srlookup is not None) and not self.lookahead1()['token'] == '[':
            if not self.lookahead1()['token'] == '.': # not srcall on instance
                #print('term is varName')
                return True

        # look up our var in the subroutine level symbol table
        cllookup = self.classsymboltable.lookup(ctok)
        if (cllookup is not None) and not self.lookahead1()['token'] == '[':
            if not self.lookahead1()['token'] == '.': # not srcall on instance
                #print('term is varName')
                return True

        return False

    def term_isarrayname(self):
        """ if it is array """
        ctok = self.curtoken()['token']
        if (self.lookahead1()['token'] == '[' and
                (self.srsymboltable.lookup(ctok)
                or self.classsymboltable.lookup(ctok)) ):
            #print('term is arrayName')
            return True
        return False

    def term_issubroutinecall(self):
        """ ( (className|varname)'.' subroutineName'('expressionList')' """
        if (self.curtoken()['type'] == 'identifier' and
               self.lookahead1()['token'] == '.' and
               self.lookahead2()['type'] == 'identifier' and
               self.lookahead3()['token'] == '(' ):
           #print('term is subroutineCall')
           return True
        return False


    def term_isexpinparentheses(self):
        if self.curtoken()['token'] == '(' and not self.lookahead1()['token']==')':
            #print('term is exp in parentheses')
            return True
        return False

    def term_isunaryopterm(self):
        if self.curtoken()['token'] in self.unaryops:
            #print('term is unaryop term')
            return True
        return False

class SymbolTable:
    def __init__(self):
        self.table = []
    def __str__(self):
        r = 'Symbol Table Output\n'
        r+= 'segment num  name  type\n'
        for item in self.table:
            itemstring = '{0} {1}     {2}     {3}'.format(item['segment'],
                                   item['num'],
                                   item['name'],
                                   item['type'])

            r = r + itemstring + '\n'
        return r


    def varcount(self, segment):
        return len([x for x in self.table if x['segment'] == segment])

    # lookup function
    def lookup(self, varname):
        for item in self.table:
            if item['name'] == varname:
                return item
        return None

    def kindof(self, name):
        for item in self.table:
            if item['name'] == name:
                return item
        return None

    def define(self, name, type, segment):
        nseg = len([x for x in self.table if x['segment'] == segment])
        newelement = {'segment':segment, 'name':name, 'type':type, 'num':nseg}
        self.table.append(newelement)
    def output(self):
        for item in self.table: pass
            #print("{0}  {1}  {2}  {3}".format(item['segment'], item['num'],item['name']))


def analyzejackfile(jackpath):
    # #print('the path leads to a file')
    jkfilename = jackpath
    jkcodecleaned = JackCodeCleaner(jkfilename)
    tokenizer = JackTokenizer(jkcodecleaned.codelines)
    xmlfilename = jkfilename[:-5]+'T'+'.xml'
    with open(xmlfilename,'w') as f:
        for line in tokenizer.tokens:
            f.write(line)
            f.write("\n")
    anz = JackAnalyzer(tokenizer)
    xmlname = jkfilename[:-5]+'.xml'
    try:
        anz.analyze()
        # reformat markup
    except Exception as e:
        with open(xmlname,'w') as f:
            for line in anz.markup:
                f.write(line)
                f.write('\n')

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

    #it's time to generate code

    ce = CompilationEngine(anz)
    #print(ce.markup)
    ce.cmclass()

    vmfilename = xmlname[:-4] + '.vm'
    with open(vmfilename,'w') as f:
        for line in ce.vmcode:
            f.write('{}\n'.format(line))


def catchvoids(pathto):
    voidslist = open('voidmethods.txt','r').readlines()[0].split()
    osfiles = ['Sys.vm','Array.vm','Keyboard.vm','Math.vm','Memory.vm','Output.vm','Screen.vm','String.vm']
    vmlist = [x for x in listdir(pathto) if '.vm' in x]
    print('vmlist while catching voids: {}'.format(vmlist))
    vmlist = [x for x in vmlist if x not in osfiles]
    print('filtered vmlist while catching voids: {}'.format(vmlist))
    vmlist = [pathto+'/'+ item for item in vmlist]

    # List of files with full address
    for vmitem in vmlist:
        lines = open(vmitem).readlines()
        #print(len(lines))
        #print("{} has {} lines".format(vmitem, len(lines)))
        lines1 = []
        for vmline in lines:
            lines1.append(vmline)
            if (len(vmline)>1 and
                    vmline.split()[0] == 'call' and
                    vmline.split()[1] in voidslist):
                lines1.append('pop temp 0\n')

        # delete the file
        remove(vmitem)
        # recreate the file
        with open(vmitem,'a') as f:
            for vmline in lines1:
                f.write(vmline)
            f.write('// voids processed')
    print('void methods are: {}'.format(voidslist))
    print('PWD')
    print(getcwd())
    print('listdir')
    ls = listdir()
    print(ls)
    if 'Average' in ls:
        print('listfiles in Average: {}'.format(listdir('Average')))
        #with open('Average/Main.vm')



if __name__=="__main__":
    if 'voidmethods.txt' in listdir():
        remove('voidmethods.txt')
    if 'voidmethods.txt' not in listdir():
        with open('voidmethods.txt','w') as f:
            f.write('')



    if not len(argv) == 2:
        #print('Довжина аргумент-вектора має дорівнювати 2')
        #print('вихід з програми')
        exit()
    path_to_batch = argv[1]
    if isdir(path_to_batch):
        lst = listdir(path_to_batch)
        #print("список файлів за адресою {0}".format(path_to_batch))
        #print(lst)
        #print("З них файли jack :")
        jackfiles = [x for x in lst if x[-5:] == '.jack']

        # let's list classes in special file
        classes = [x[:-5] for x in jackfiles]
        classes +=  ['Array','Keyboard',
            'Math','Memory','Output','Screen','String','Sys']
        with open('classes.py','w') as f:
            f.write('cls = {}'.format(str(classes)))

        #for item in jackfiles: print(item)
        jackfiles = [path_to_batch +'/'+ x for x in jackfiles]
        #print('*******************')
        #print('                    ')
        #print('*******************')
        #print("ось шляхи до кожного файла:")
        #for file in jackfiles: print(file)
        for file in jackfiles:
            #print("зараз буде аналізуватися {0}".format(file))
            analyzejackfile(file)
            #print("{0} проаналізовано".format(file))

        catchvoids(path_to_batch)

    if isfile(path_to_batch):
        analyzejackfile(path_to_batch)
        pathforcatch = '/'.join(path_to_batch.split('/')[:-1])+'/'
        #print('pathforcatch = {}'.format(pathforcatch))
        catchvoids(pathforcatch)
