import sys

level = ""
score = input("Please input score:")
if score >= 0 and score < 60:
	level = "D"
elif score >=60 and score < 70:
	level = "C"
elif score >=70 and score < 90:
	level = "B"
elif score >=90 and score <= 100:
	level = "A"
else:
	print("score: " + str(score) + " is invalid")
	sys.exit(-1)

print("score: " + str(score) + ", level: " + level)