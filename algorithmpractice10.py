def find_routes(rows,columns):
	dictionary = {}
	for i in range (0,rows+1):
		for j in range (0,columns+1):
			current_point = (i,j)
			if j == 0 or i == 0:
				dictionary[current_point] = 1
			else:
				val1 = i-1
				val2 = j-1
				current_val = dictionary[(val1,j)] + dictionary[(i,val2)]
				dictionary[current_point] = current_val
	print dictionary[rows,columns]

find_routes(20,20)