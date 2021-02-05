vowel = "a,e,i,o,u"
consonant = "b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z"

alphabet = input("Input an alphabet: ")
if alphabet in vowel:
    print("Input letter is Vowel")
elif alphabet in consonant:
    print("Input letter is consonant")