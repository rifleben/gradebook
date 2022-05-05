"""

A simple gradebook type program in an effort to better understand lists and the .append() and .remove()
methods

"""
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# add a new grade to list
gradebook.append(["computer science", 100])
# add a new grade to list
gradebook.append(["visual arts", 93])
# theoretic change of grade
gradebook[-1][1] = 98
# changing a numeric grade to a Pass/Fail value
gradebook[2].remove(85)
gradebook[2].append("Pass")

#creating full gradebook
full_gradebook = last_semester_gradebook + gradebook
#verify results that gradebooks combined
print(full_gradebook)
