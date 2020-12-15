y = [2,9]
H = 50 

y_i = []

def set(y):                             
	for i in range(0, H):
		if(i == 0 or i == H):
			y_i.append(y[i])
		else:
			dy = y_i[i-1]+(y[1]-y[0])/H
			y_i.append(dy)
			print(dy)
	return y_i


def f(y):
	return 2*y-8



def summ_area(array):
	area = 0
	for i in range(len(array)-2):
		f_prev = f(array[i])        
		f_next = f(array[i+1])
		if(f_prev < f_next):
			area += (array[i+1] - array[i])*abs(f_prev)
		else:
			area += (array[i+1] - array[i])*abs(f_next) 
	print('Площадь:', area)
	return area

summ_area(set(y))

