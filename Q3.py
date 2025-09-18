#print all alphebets from a to z

def all_alphebet_atoz_for():
    for x in range(ord('a'),ord('z')+1):
        print(chr(x))

def all_alphebet_atoz_while():
    i=ord('a')
    while i<=ord('z'):
        print(chr(i))
        i+=1

all_alphebet_atoz_for()
all_alphebet_atoz_while()