#a,b = 6,5
#if(a>b):
#    print ('a({})is bigger than b({})'.format(a,b))
#else:
#    print('a({})is smaller than b({})'.format(a,b))
#    
#print ('foo' if a > b else 'moo')
#
#a,b = 0,1
#while b < 50:
#    print (b)
#    a,b = b, b + a
#    
#fh = open('test.txt')
#
#print (fh)
#for line in fh.readlines():
#    print(line,end='')
    
#def isPrime(n):
#    if n == 1:
#        print('1 is special')
#        return False
#    for x in range(2,n):
#        if n%x == 0 :
#            print('{} is equal to {} x {}'.format(n,x,n/x))
#            return False
#    else:
#        print(n, 'is prime')
#        return True
#    
#for n in range(1,20):
#    isPrime(n)
    
def main(): print('hello world')

if __name__ == "__main__": main()
    

def func(a=7):
    for x in range(a,10):
        print(x)
        
func()

class Egg:
    def __init__(self,kind = 'fried'):
        self.kind = kind
    
    def whatKind(self):
        return self.kind
    
friend = Egg()
print (friend.kind)

s = 'this is a \n string'
print(s)

x = {'one':1,'two':2,'three':3}
for i in sorted(x.keys()):
    print(i)

choices = dict(
            one = 'first',
            two = 'second',
            three = 'third'
        )
v = 'forth'
print(choices.get(v,'other'))











    
    