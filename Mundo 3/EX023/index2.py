from time import sleep
def contador(i,f,p):
    if i < f and p == 0:
        while i != f:
            print(i,end=' ',flush=True)
            i += 1
            sleep(0.1)
        print('FIM')
    else:
        if i > f and p == 0:
            while i != f:
                print(i,end=' ',flush=True)
                i -= 1
                sleep(0.1)
            print('FIM')
        elif i < f:
            for c in range(i,f,p):
                print(c,end=' ',flush=True)
                sleep(0.1)
            print('FIM')   
        elif i > f:
            for c in range(i,f,-p):
                print(c,end=' ',flush=True)
                sleep(0.1)
            print('FIM')
#PROGRAMA PRINCIPAL
contador(10,1,2)