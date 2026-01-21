from TRIES import tree

with open("romeo_juliet.txt","r") as file:
    words=[word.lower().replace('.','') +"$" for word in file.read().split()]

ter=tree(words)

n=input("ENTER THE WORD TO FIND MATCH  ")
an=ter.pred(n)
print(an[:-1])