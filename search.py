import cProfile
import random

def find_index(lst, value):
	for i in range(0,len(lst)):
		if value == lst[i]:
			return i

def search_binary(lst, value):
	lst.sort()
	top = len(lst)
	bottom = 0
	while top >= bottom:
		index = int((top - bottom)/2 + bottom)
		if value > lst[index]:
			bottom = index
		elif value < lst[index]:
			top = index
		else:
			return index
		

def test_binary_search():
	lst = []
	for i in range(0,10000):
		lst.append(i)
	random.shuffle(lst)
	value = 521
	index = search_binary(lst,value)


test_binary_search()


prof = cProfile.Profile()
prof2 = cProfile.Profile()


def benchmark_search(iteration_number):
	lst = []	
	for i in range(0,10000):
		lst.append(i)
	random.shuffle(lst)
	value = 521
	prof.enable()
	for i in range(0,iteration_number):
		find_index(lst,value)
	prof.disable()


def benchmark_search_bsp(iteration_number):
	lst = []	
	for i in range(0,10000):
		lst.append(i)
	random.shuffle(lst)
	value = 521
	prof2.enable()	
	for i in range(0,iteration_number):
		search_binary(lst,value)
	prof2.disable()




	



	
benchmark_search(100000)
benchmark_search_bsp(100000)
prof.print_stats()
prof2.print_stats()
