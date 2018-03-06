def bubble(list):
	for i in range(len(list)):
		for j in range(len(list)-1):
			if list[j]<=list[j+1]:
				temp=list[j]
				list[j]=list[j+1]
				list[j+1]=temp


def insertion(list):
	for i in range(len(list)):
		for j in range(i):
			if list[j]<=list[j+1]:
				temp=list[j]
				list[j]=list[j+1]
				list[j+1]=temp


def selection(list):
	large=0
	l=0
	for i in range(len(list)):
		for j in range(len(list)-1):
			if list[i]>list[j]:
				temp=list[i]
				list[i]=list[j]
				list[j]=temp

list=[5,3,7,6,4,1]
bubble(list)
print(list)
list=[5,3,7,6,4,1]
insertion(list)
print(list)
list=[5,3,7,6,4,1]
selection(list)
print(list)
