
'''
map(func,iterl)
first make  a function then list
'''
#program for sqr root
def sqr(a) :
    return a*a
num=[1,3,4,5,6]
result=list(map(sqr,num))
print(result)
print("..............................")
# filter
num=[1,3,4,5,6]
result= list(filter(lambda a : a%2==0,num))
print (result)

print (".........list comprehensions..........")
# for square program
num=[1,3,4,5,6]
result=[a*a for a in num]
print(result)

# for filter program
result= [c for c in num if c%2==0]
print (result)


