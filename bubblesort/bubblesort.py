# Bubble Sort using Python (jasonbrianhall@gmail.com); don't use this code as it is EXTREMELY INEFFICIENT

# Swaps characters
def swap_chars(string, idx1, idx2):
	  chars = list(string)
	  chars[idx1], chars[idx2] = chars[idx2], chars[idx1]
	  return ''.join(chars)

# Bubble sort data
def sort(data):
	for x in range(len(data)):
		for y in range(len(data)):
			if data[x]<data[y]:
				data=swap_chars(data, x, y)
	return data
			
		

data="986765FrEaK431388998432148328Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadfafa1212432123afa!@#$BCDJASON0"
print("Length1: ", len(data))
sorteddata=sort(data)
print("Length2: ", len(sorteddata))
print(data)
print(sorteddata)
#data[1]="a"

