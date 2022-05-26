#! /env/bin/ python
#We can also calculate the probability of regression where x is current progression and y the regression or stabilised tumors. We are looking at the probability of tumor types progressing or regressing based on current data x and y per tumor type:

#lists of values
x = [1.98, 1.21, 1.34]     #progressive
y = [0.00, -0.03, -1.09]   #regressive

def pdf(x, y):
	for l in pdf(x, y):
		for i in range(len(y)):
			for j in range(len(x)):
				l / (i + y)

a = pdf(x, y)

print(a)