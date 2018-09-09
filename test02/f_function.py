
import sys
def firt_function(mytxt):
    for i in range(0,5):
        print(mytxt)

#s=input("please Enter your favorit string: ")
s=sys.argv[0]
j=len(sys.argv)
firt_function(s)
print(j)
