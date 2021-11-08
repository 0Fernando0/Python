import time
roxo = '\033[33m'
fim = '\033[m'
for c in range(10,0,-1):
    print(c)
    time.sleep(1)
print('{}BOOM!!!{}'.format(roxo,fim))