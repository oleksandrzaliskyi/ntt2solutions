from sys import argv
from os.path import isdir, isfile


def translate_command_set(path_to_batch):
    c = []
    labels = []
    if isdir(argv[1]):
        print('Каталог! вихід з програми!')
        exit()
    if isfile(argv[1]):
        st = open(argv[1]).readlines()
        lines = [line  for line in list(st) if line[0].isalpha()]
        for item in lines:
            print(item)
        # lines - список команд у вигляді рядків, їх ще розділяти треба
        # і повидаляти все лишнє
        commands = [line.rstrip('\n').split(' ') for line in lines]
        print('commands')
    # на цьому етапі вже повинен бути список списків commands
    # компіляція - початок
    for item in commands:
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


        if len(item) == 2:
            pass
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

        c.append('')

    # компіляція - кінець
    # commands_translated можна вже записувати у файл

    finalfilename = argv[1].split('.')[0]+'.asm'
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
