#Step1
classmates = ['Kelvin', 'Travis', 'Mary','Alan', 'Gia']
print("Classmates:", classmates)

print("Total students:",len(classmates))
print("First students:",(classmates[0]))
print("Second students:",(classmates[1]))
print("Third students:",(classmates[2]))
print("Fourth students:",(classmates[3]))
print("Fifth students:",(classmates[4]))
print("First-three students:",(classmates[:3]))
print("Last students:",(classmates[-1]))

print("Adding a student")
classmates.append("Miguel")
print(classmates)

print("Removing a student" )
classmates.remove("Alan")
print(classmates)

print("Sorting Alaphabetically" )
classmates.sort()
print(classmates)

print("Reversed list" )
classmates.reverse()
print(classmates)
