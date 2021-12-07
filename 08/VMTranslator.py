from sys import argv
from os import listdir
from os.path import isdir, isfile


def translate_command_set(path_to_batch):
    c = []
    labels = []
    vmalias = ''
    finalfilename=''
    if isdir(argv[1]):
        filelist = listdir(argv[1])
        print(filelist)
        lst = argv[1].split('/')
        lst = [x for x in lst if len(x)>0]
        print('lst = {0}'.format(lst))
        vmalias = lst[-1]
        print('vmalias = {0}'.format(vmalias))
        finalfilename = argv[1]+vmalias+'.asm'
        print('finalfilename = {0}'.format(finalfilename))
        vmfilelist = [f for f in filelist if '.vm' in f]
        if 'Sys.vm' in vmfilelist:
            vmfilelist.remove('Sys.vm')
            vmfilelist = ['Sys.vm'] + vmfilelist
        print('vmfilelist = {0}'.format(vmfilelist))
        pathtofiles = argv[1]

        commands = []
        print('*****************')
        for item in vmfilelist:
            print('{0}{1}'.format(pathtofiles,item))

            st = open('{0}{1}'.format(pathtofiles,item),'r').readlines()
            lines = [line  for line in list(st) if line[0].isalpha()]
            # lines - список команд у вигляді рядків, їх ще розділяти треба
            # і повидаляти все лишнє
            lines = [line.split('/')[0] for line in lines]
            lns = []
            for item in lines:
                newln = item.replace('\t','')
                lns.append(newln)
            lines = lns

            kommands = [line.rstrip('\n').split(' ') for line in lines]
            comds = []
            for item in kommands:
                newitem = [subitem for subitem in item if (len(subitem)>1) or subitem.isalnum()]
                comds.append(newitem)
            kommands = comds
            commands += kommands
        print('*****************')

        # Bootstrap code
        c.append('@256')
        c.append('D=A')
        c.append('@SP')
        c.append('M=D')
        #c.append('@Sys.init')
        #c.append('0;JMP')
        commands= [['call','Sys.init','0']]+ commands
        print(commands)
        # End of bootstrap code

    if isfile(argv[1]):
        vmalias = argv[1].split('/')[-1].split('.')[0]
        finalfilename = argv[1].split('.')[0]+'.asm'
        print('vmalias = {0}'.format(vmalias))
        st = open(argv[1]).readlines()
        lines = [line  for line in list(st) if line[0].isalpha()]
        # lines - список команд у вигляді рядків, їх ще розділяти треба
        # і повидаляти все лишнє
        lines = [line.split('/')[0] for line in lines]
        lns = []
        for item in lines:
            newln = item.replace('\t','')
            lns.append(newln)
        lines = lns

        commands = [line.rstrip('\n').split(' ') for line in lines]
        comds = []
        for item in commands:
            newitem = [subitem for subitem in item if (len(subitem)>1) or subitem.isalnum()]
            comds.append(newitem)
        commands = comds

    # на цьому етапі вже повинен бути список списків commands
    # компіляція - початок
    for item in commands:
        print(item)
        c.append('// {0}'.format(' '.join(item)))
        n_instructions = len([x for x in c if '//' not in x and len(x)>1])
        c.append('//інструкція {0}'.format(n_instructions))
        cname = item[0]
        if len(item) == 1:
            if cname == 'add':
                # зберігаємо в регістр D Значення верхнє з двох
                c.append('@SP')
                c.append('M=M-1') # понижаємо стек на одиницю
                c.append('A=M')
                c.append('D=M') # і беремо звідти значення

                c.append('@SP')
                c.append('M=M-1') # понижаємо стек ще на одиницю
                c.append('A=M') # переходимо до верхнього значення
                c.append('M=M+D')

                c.append('@SP')
                c.append('M=M+1') # наростили стек
            if cname == 'sub':
                # зберігаємо в регістр D Значення верхнє з двох
                c.append('@SP')
                c.append('M=M-1') # понижаємо стек на одиницю
                c.append('A=M')
                c.append('D=M') # і беремо звідти значення

                c.append('@SP')
                c.append('M=M-1') # понижаємо стек ще на одиницю
                c.append('A=M') # переходимо до верхнього значення
                c.append('M=M-D')

                c.append('@SP')
                c.append('M=M+1') # наростили стек

            if cname == 'neg':
                c.append('@SP')
                c.append('A=M-1')
                c.append('M=-M')

            if cname == 'not':
                c.append('@SP')
                c.append('A=M-1')
                c.append('M=!M')

            if cname in ['and','or']:
                c.append('@SP')
                c.append('M=M-1')
                c.append('A=M')
                c.append('D=M')

                c.append('@SP')
                c.append('M=M-1')
                c.append('A=M')

                if cname == 'and':
                    c.append('M=M&D')
                if cname == 'or':
                    c.append('M=M|D')

                c.append('@SP')
                c.append('M=M+1') # наростили стек


            if cname in ['gt','lt','eq']:
                # зберігаємо в регістр D Значення верхнє з двох
                c.append('@SP')
                c.append('M=M-1') # понижаємо стек на одиницю
                c.append('A=M')
                c.append('D=M') # і беремо звідти значення

                c.append('@SP')
                c.append('M=M-1') # понижаємо стек ще на одиницю
                c.append('A=M') # переходимо до верхнього значення

                c.append('D=M-D') # в D знаходиться різниця аргументів

                count_of_settrues= len([x for x in labels if "SETTRUE" in x])
                count_of_setfalses= len([x for x in labels if "SETFALSE" in x])
                count_of_endbranches= len([x for x in labels if "ENDBRANCH" in x])
                labels.append('SETTRUE.{0}'.format(count_of_settrues))
                labels.append('SETFALSE.{0}'.format(count_of_setfalses))
                labels.append('ENDBRANCH.{0}'.format(count_of_endbranches))

                c.append('@SETTRUE.{0}'.format(count_of_settrues))
                if cname =='gt':
                    c.append('D;JGT')
                if cname == 'eq':
                    c.append('D;JEQ')
                if cname == 'lt':
                    c.append('D;JLT')

                c.append("(SETFALSE.{0})".format(count_of_setfalses))
                c.append('@SP')
                c.append('A=M')
                c.append('M=0')
                c.append('@ENDBRANCH.{0}'.format(count_of_endbranches))
                c.append('0;JMP')

                c.append("(SETTRUE.{0})".format(count_of_settrues))
                c.append('@SP')
                c.append('A=M')
                c.append('M=-1')
                c.append('@ENDBRANCH.{0}'.format(count_of_endbranches))
                c.append('0;JMP')

                c.append('(ENDBRANCH.{0})'.format(count_of_endbranches))

                c.append('@SP')
                c.append('M=M+1') # наростили стек
            if cname == 'return':

                # @FRAME = LCL
                c.append('@LCL')
                c.append('A=M')
                c.append('D=A')
                c.append('@FRAME')
                c.append('M=D')

                #RET = *(FRAME-5)
                c.append('@FRAME')
                c.append('A=M')
                c.append('A=A-1')
                c.append('A=A-1')
                c.append('A=A-1')
                c.append('A=A-1')
                c.append('A=A-1')
                c.append('D=M') # return label now in D
                c.append('@RET')
                c.append('M=D')

                # *ARG = pop()     результат функції помістити в ARG
                c.append('@SP')
                c.append('A=M')
                c.append('A=A-1')
                c.append('D=M')

                c.append('@ARG')
                c.append('A=M')
                c.append('M=D') # результат знаходиться в ARG

                # SP = ARG+1
                c.append('@ARG')
                c.append('D=M')
                c.append('@SP')
                c.append('M=D+1')

                # THAT = *(FRAME-1)
                c.append('@FRAME')
                c.append('A=M')
                c.append('A=A-1')
                c.append('D=M')
                c.append('@THAT')
                c.append('M=D')

                # THIS = *(FRAME-2)
                c.append('@FRAME')
                c.append('A=M')
                c.append('A=A-1')
                c.append('A=A-1')
                c.append('D=M')
                c.append('@THIS')
                c.append('M=D')

                # ARG = *(FRAME-3)
                c.append('@FRAME')
                c.append('A=M')

                c.append('A=A-1')
                c.append('A=A-1')
                c.append('A=A-1')

                c.append('D=M')
                c.append('@ARG')
                c.append('M=D')


                # LOCAL = *(FRAME-4)
                c.append('@FRAME')
                c.append('A=M')

                c.append('A=A-1')
                c.append('A=A-1')
                c.append('A=A-1')
                c.append('A=A-1')

                c.append('D=M')
                c.append('@LCL')
                c.append('M=D')

                # goto RET
                c.append('@RET')
                c.append('A=M')
                c.append('0; JMP')


        if len(item) == 2:
            if cname == 'goto':
                labelname = item[1]
                c.append('@{0}'.format(labelname))
                c.append('0;JMP')

            if cname == 'if-goto':
                labelname = item[1]
                c.append('@SP')
                c.append('M=M-1') # пониження стека
                c.append('A=M')
                c.append('D=M') # в регістр D взяли умову
                c.append('@{0}'.format(labelname))
                c.append('D;JNE')
            if cname == 'label':
                labelname = item[1]
                labels.append(labelname)
                c.append('({0})'.format(labelname))

        if len(item) == 3:
            segment = item[1]
            num = item[2]
            if segment in ['local','argument','this','that']:
                shortcut = {'local':'LCL',
                            'argument':'ARG',
                            'this':'THIS',
                            'that':'THAT'}[segment]

            if cname == 'push':
                if segment == 'constant':
                    c.append('@{0}'.format(num))
                    c.append('D=A') # в регістр D взяли значення

                if segment in ['local','argument','this','that']:
                    c.append('@{0}'.format(num))
                    c.append('D=A')
                    c.append('@{0}'.format(shortcut))
                    c.append('A=M+D')
                    c.append('D=M') # в регістр D взяли значення

                if segment == 'temp':
                    tempaddr = 5 + int(num)
                    c.append('@{0}'.format(tempaddr))
                    c.append('D=M') # в регістр D взяли значення
                if segment == 'pointer':
                    poaddr = 3 + int(num)
                    c.append('@{0}'.format(poaddr))
                    c.append('D=M')
                if segment == 'static':
                    saddr = 16 + int(num)
                    c.append('@{0}'.format(saddr))
                    c.append('D=M')

                # загальний шматок коду для всих команд PUSH
                c.append('@SP')
                c.append('A=M')
                c.append('M=D')
                c.append('@SP') # інкремент стека
                c.append('M=M+1')

            if cname == 'pop':
                c.append('@SP')
                c.append('M=M-1')
                c.append('@SP')
                c.append('A=M')
                c.append('D=M') # взяли в регістр D значення, стек вже понижений
                c.append('@R15')
                c.append('M=D') # значення в R15 залишене

                if segment in ['local','argument','this','that']:
                    c.append('@{0}'.format(num))
                    c.append('D=A')
                    c.append('@{0}'.format(shortcut))
                    c.append('D=M+D')
                    c.append('@R14')
                    c.append('M=D') # адресу куди зберігати збережено в R14
                if segment == 'temp':
                    tempaddr = 5 + int(num)
                    c.append('@{0}'.format(tempaddr))
                    c.append('D=A')
                    c.append('@R14')
                    c.append('M=D')

                if segment == 'pointer':
                    poaddr = 3 + int(num)
                    c.append('@{0}'.format(poaddr))
                    c.append('D=A')
                    c.append('@R14')
                    c.append('M=D')

                if segment == 'static':
                    saddr = 16 + int(num)
                    c.append('@{0}'.format(saddr))
                    c.append('D=A')
                    c.append('@R14')
                    c.append('M=D')

                # В 14 Знаходиться адреса, в 15 значення
                c.append('@R15')
                c.append('D=M')
                c.append('@R14')
                c.append('A=M')
                c.append('M=D')
            if cname == 'function':
                funcname = item[1]
                nlocal = int(item[2])
                labels.append(funcname)
                c.append('({0})'.format(funcname))
                for i in range(nlocal):
                    c.append('@SP')
                    c.append('A=M')
                    c.append('M=0')
                    c.append('@SP')
                    c.append('M=M+1')

            if cname == 'call':
                funcname = item[1]
                nargs = item[2]
                n_of_returns = len([lbl for lbl in labels if '{0}.ret'.format(funcname) in lbl])
                returnlabelname = '{0}.{1}'.format(funcname,n_of_returns)
                c.append('@{0}'.format(returnlabelname))
                c.append('D=A') # беремо мітку в регістр D

                c.append('@SP')
                c.append('A=M')
                c.append('M=D') # мітку повернення поставили в стек

                c.append('@SP')
                c.append('M=M+1') # наростили стек

                for seg in ['LCL','ARG','THIS','THAT']:
                    # запам'ятовуємо Локал і інші в стек
                    c.append("@{0}".format(seg))
                    c.append('D=M')

                    c.append('@SP')
                    c.append('A=M')
                    c.append('M=D') # зберегли в стек значення

                    c.append('@SP')
                    c.append('M=M+1') # наростили стек

                funclabel = funcname
                c.append('@{0}'.format(funcname))
                c.append('0; JMP')
                c.append('({0})'.format(returnlabelname))

        c.append('')

    # компіляція - кінець
    # commands_translated можна вже записувати у файл


    finalfile = open(finalfilename, 'w')
    for item in c:
        finalfile.write('{0}\n'.format(item))
    finalfile.close()


if __name__ == '__main__':
    print('Програма почалася!!')
    print('argv: '.format(argv))
    print(argv)
    if not len(argv) == 2:
        print('Довжина аргумент-вектора має дорівнювати 2!')
        print('вихід з програми')
        exit()
    path_to_batch = argv[1]

    commands = translate_command_set(path_to_batch)
