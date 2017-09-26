def filter_numbers(listik):
	return [x for x in listik if type(x) == int]

def average_length(towns):
	towns_count = len(towns)
	char_sum = 0
	for town in towns:
		char_sum = char_sum + len(town)
	return char_sum / towns_count

def palindrome(name):
	name_len = len(name) #5

	for letter in name:
		if letter == name[name_len - 1]:
			name_len = name_len - 1
			continue
		else:
			return False
	return True

def overlapping(a, b):
	for num in a:
        if num in b:
            return True
	return False

def number_of_letters(pruzinka):
	slovnik = {}
	for letter in pruzinka:
		slovnik[letter] = pruzinka.count(letter)
	return slovnik


print(filter_numbers([1.2, "sdas", 4, 8, 3.4, "12", -3, True, 5, 8]))
print(average_length(["olomouc", "liberec", "ostrava", "praha", "brno"]))
print(palindrome("radar"))
print(palindrome("radek"))
print(overlapping([1,2,3], [4,5,6]))
print(overlapping([1,2,3], [3,4,5]))
print(number_of_letters("ababdacabbdabc"))
