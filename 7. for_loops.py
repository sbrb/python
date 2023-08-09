#for loop
for x in range(10):
    print(2*x, end=",")


# new line
print('\n')


# list with for loop
a=['a','c','d']
for n in a:
    print(n*2)



# while loop
n=70
while n>=60:
    print(n)
    n-=1



#break 
for i in range(10):
    if i>6:
        break
    print(i)

# continue
for i in range(10):
	if i == 7:
		continue
	print(i)
