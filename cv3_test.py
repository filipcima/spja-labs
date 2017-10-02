def add_line_numbers(filename):
	try:
		my_file = open(filename, 'rt')
		my_second_file = open("n_" + filename, 'wt')
		i = 0
		for line in my_file:
			str_i = str(i)
			my_second_file.write(str_i + ". " + line)
			i += 1
	except IOError as e:
		print ("chybicka: " + e)		
	finally:
		my_file.close()
		my_second_file.close()

def my_filtered_map(fun, lst, **kw):
	lst = [*map(fun, lst)]
	if 'max' and 'min'  in kw.keys():
		return [x for x in lst if x > kw['min'] and x < kw['max']]
		print("oba present")
	elif 'max' in kw.keys():
		return [x for x in lst if x < kw['max']]
		print("chybi min")
	elif 'min' in kw.keys():
		return [x for x in lst if x > kw['min']]
		print("chybi max")
	else:
		return lst

def bank_account(*filenames):
	arr = []
	acc_dict = {}
	try:
		for file in filenames:
			mf = open(file, 'rt')
			for line in mf:
				ln = line.split()
				acc_dict.update({ln[0]: 0})

		for file in filenames:
			mf = open(file, 'rt')
			for line in mf:
				ln = line.split()
				acc_no = ln[0]
				action = ln[1]
				amount = ln[2]
				if action == 'W':
					acc_dict[acc_no] -= int(amount)
				elif action == 'D':
					acc_dict[acc_no] += int(amount)
				else action == 'I':
					acc_dict[acc_no] /= int(amount)
	except IOError as e:
		print ("Chybicka: " + e)

#add_line_numbers("text.txt")
#print(my_filtered_map(lambda x: x*2, [-4.4, -2, 4], max = 0))
bank_account("cv2_files/bank_01.txt", "cv2_files/bank_02.txt")