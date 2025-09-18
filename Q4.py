#print all alphebets from a to z

def all_alphebet_atoz_for():
    for x in range(ord('a'),ord('z')+1):
        print(chr(x))

def all_alphebet_AtoZ_for():
    for y in range(ord('A'),ord('Z')+1):
        print(chr(y))

def all_alphebet_atoz_while():
    i=ord('a')
    while i<=ord('z'):
        print(chr(i))
        i+=1

def all_alphebet_AtoZ_while():
    j=ord('A')
    while j<=ord('Z'):
        print(chr(j))
        j+=1

all_alphebet_atoz_for()
all_alphebet_AtoZ_for()
all_alphebet_atoz_while()
all_alphebet_AtoZ_while()