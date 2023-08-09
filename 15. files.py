f = open('data.txt', 'r')

for line in f:
	print(line)

# print(f.readline())
# print(f.readline())
# print(f.readline())

f.close()








with open('data_folder/data.txt') as f:
	# for line in f:
	# 	print(line)

	print(f.read(2))
	print(f.read(2))
	f.seek(0)
	print(f.read(2))










lines_data = ['shayan\n', 'biswas\n']
with open('data_folder/write_file.txt', 'a') as f:
	f.write('Riju\n')
	f.writelines(lines_data)