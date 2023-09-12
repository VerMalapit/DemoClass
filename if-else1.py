number = int(input("Enter number: "))
if number > 0:
	print("The number is positive")
elif number == 0:
	print("The number is zero")
else:
	print("The number is negative")
	
score = int(input("Enter score: "))
if score > 10:
	print("Score is out of range")
elif score == 10:
	print("You got a perfect score")
elif score >= 7.5:
	print("You passed the quiz")
else:
	print("Oops, try to do better next time")
	
score = int(input("Enter score: "))
if score >= 7.5:
	print("You passed the quiz")
elif score > 10:
	print("Score is out of range")
elif score == 10:
	print("You got a perfect score")
else:
	print("Oops, try to do better next time")
	
for variable in range(parameters):
	statements
	
multiples = [5, 10, 15, 20, 25]
for number in multiples:
	print(number)
else:
	print("No more numbers left")

#Program 1	
for letter in "Hogwarts":
	print(letter)

#Program 2	
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
for name in houses:
	print("House: ", name)

#Program 3
for number in [1, 2, 3, 4, 5]
	print(number)
	
quizzes = [9, 12, 7, 15, 10]
sum = 0

for score in quizzes:
	print(score)
	sum = sum + score
	
print("The sum is ", sum)

#Example 1
for number in range(3):
	print(number)

#Example 2
for number in range(4, 9):
	print(number)

#Example 3
for i in range(-1, -10, -2):
	print(i)

#one parameter
range(stop)

#two parameters
range(start, stop)

#three parameters
range(start, stop, step)