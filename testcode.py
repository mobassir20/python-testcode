pattern=input("Enter Pattern:")
tstring=input("Enter Text String:")
store= pattern in tstring #store true or false
if(store== False):
    tstring= tstring [::-1] #reverse the string
    print(pattern in tstring) #print true or false after reversed

else :
    print(store) #will print true if pattern re cognised diretly in tstring