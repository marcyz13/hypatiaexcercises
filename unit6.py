excercise = "Excercise 6!"
print(excercise)

myfile = open('/home/hypatian/hypatia-excercises/inputfile.txt')
file_contents = myfile.read()
myfile.close()
print(file_contents)

outputfile = open('outputfile.txt', "w")
outputfile.write(file_contents)
outputfile.close()
