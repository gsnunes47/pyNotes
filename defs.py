def findFile(txt):
    try:
        f = open(txt, 'rt')
        f.close()
    except FileNotFoundError:
        return False
    else: 
        return True

def createFile(txt):
    a = open(txt, 'wt+')
    a.close()
    

def writeFile(file, log, passw):
    a = open(file, 'at')
    a.write(f'{log} ; {passw}\n')
    a.close()

def findUser(file, user):
     with open(file, 'rt+') as arq:
            try:
                for l in arq:
                    if user in l:
                        return True
            except:
                return False

def menu(*txt):
    print('-' * 30)
    print(f'{"MENU":^30}')
    print('-' * 30)
    cont = 0
    for t in txt:
        cont += 1
        print(f'[{cont}] - {t}.')
    print
