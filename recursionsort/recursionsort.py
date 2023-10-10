# Recursion Sort Using Queues (jasonbrianhall@gmail.com)

def sort2(queue1):
	queue2=[]
	while len(queue1)>1:
		d1=queue1.pop()
		d2=queue1.pop()
		counter=0
		counter2=0
		data=""
		exittheloop=False
		while exittheloop==False:
			if counter>=len(d1):
				data+=str(d2[counter2])
				counter2+=1
			elif counter2>=len(d2):
				data+=str(d1[counter])
				counter+=1
			else:
				if d1[counter]<=d2[counter2]:
					data+=str(d1[counter])
					counter+=1
				else:
					data+=str(d2[counter2])
					counter2+=1
			if counter>=len(d1) and counter2>=len(d2):
				exittheloop=True
		queue2.append(data)

	if len(queue1)>=1:
		queue2.append(queue1.pop())

	queue1=queue2
	queue2=[]

	if len(queue1)>1:
		data=sort2(queue1)
	else:
		return queue1.pop()

	return data

def sort(data):
	queue1=[]
	queue2=[]

	for number in data:
		queue1.append(number)

	while len(queue1)>1:
		d1=queue1.pop()
		d2=queue1.pop()
		counter=0
		counter2=0
		data=""
		exittheloop=False
		while exittheloop==False:
			if counter>=len(d1):
				data+=str(d2[counter2])
				counter2+=1
			elif counter2>=len(d2):
				data+=str(d1[counter])
				counter+=1
			else:
				if d1[counter]<=d2[counter2]:
					data+=str(d1[counter])
					counter+=1
				else:
					data+=str(d2[counter2])
					counter2+=1
			if counter>=len(d1) and counter2>=len(d2):
				exittheloop=True
		queue2.append(data)

	if len(queue1)>=1:
		queue2.append(queue1.pop())

	queue1=queue2
	queue2=[]

	return sort2(queue1)

data="986765FrEaK431388998432148328Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadfafa1212432123afa!@#$BCDJASON0"
print("Length1: ", len(data))
sorteddata=sort(data)
print("Length2: ", len(sorteddata))
print(data)
print(sorteddata)

