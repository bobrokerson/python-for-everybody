# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. 
# If the score is between 0.0 and 1.0, print a grade using the following table: Score Grade >= 0.9 A >= 0.8 B >= 0.7 C >= 0.6 D < 0.6 F 
# If the user enters a value out of range, print a suitable error message and exit

score = input("Enter Score: ")
s =  float(score)
x = 'Error'
if s >= 0.9:
	x = 'A'
elif s >=0.8:
	x='B'
elif s >=0.7:
	x='C'
elif s >= 0.6:
	x='D'
elif s < .6:
	x ='F'
else:
	x ="Out of Range"
  
print(x)