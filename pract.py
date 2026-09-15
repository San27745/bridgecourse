def sum(*num):
    print(num)
sum(10,20,30,40,50)

n1=10
n2=20
n3=30
print(n1,n2,n3,sep=" ")#by default " " space

n1=10
n2=20
n3=30
print(n1)#by default \n
print(n2)
print(n3)


n1=10
n2=20
n3=30
print(n1,end=",")#end is by default \n but it will show ,
print(n2,end=",")
print(n3)

print(n1,n2,n3,sep="-",end="@")
print()


course="python"
duration="4 months"
trainer="gfghg"
print("course name is",course,"duration is",duration,"trainer is",trainer)# but because of coma it will show error if one miss so string formatting is used

#string formatting
#%d for int datatype
n1=20
n2=50
sum=n1+n2
print("the sum of %d and %d is %d"%(n1,n2,sum))

num=9
sq=num**2
print("square of %d is %d"%(num,sq))

#%f for float value
n1=20.90
n2=50.56
sum=n1+n2
print("the sum of %0.1f and %0.2f is %0.3f"%(n1,n2,sum))#here %0.2 is for the number after the decimal we want

coursen="java"
dura="6months"
trainee="bhumi"

#%s for string value
print("course name is %s duration is %s trainer is %s"%(coursen,dura,trainee))




#'ctr+?' for comment and '#' also ''' --------''' triple coat for write paragraphs/notes
#if you want to open vs code from file then write cmd and on command prompt "code ." is used