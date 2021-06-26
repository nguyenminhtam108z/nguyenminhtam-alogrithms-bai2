def bai2(x,y):
    step = 0
    while(True):
        if x>y:
            x = x-1
            print('x = x - 1 = ', x)
        elif x*2<=y:
            x=x*2
            print('x = x*2 = ', x)
        elif x*2>y and y%2==1:
            print('x = x*2 = ', x)
            logs=logs+'*'
        elif x*2>y and y%2==0:
            x=x-1
            print('x = x - 1 = ', x)
        step = step + 1

        if x==y:
            return step

print('số bước ít nhất:',bai2(2,20))