f = ['Banana', 'Apple', 'Kiwi', 'Kiwi']
f[0] = 'Mango'
print(f[0])
print(f[-1])


# del f
del f[2]
print(f)








# list comprehension
# new_list=["expression"   "for item in list"   "if condition"]
a=[x for x in range(11)]
print(a)

b=[x for x in range(11) if x%2==0]
print(b)

c = [3**i for i in range(10)]
print(c)









a=[1,2,3,4]

a.pop()
print(a)

a.append(5)
print(a)

a.insert(1,56)
print(a)

a.reverse()
print(a)

s=['z','c','b','a']

s.sort()
print(s)

print(s.index('z'))
print(s.count('b'))

s.clear()
print(s)










n = [6, 2, 3, 9, 1, 6, 4, 5]
print(len(n))
print(max(n))
print(min(n))
print(sum(n))






name = "Shayan"
print(list(name))







m = [6, 2, 3, 9, 1, 6, 4, 5]
for element in m:
	print(element * 2, end = " ")

