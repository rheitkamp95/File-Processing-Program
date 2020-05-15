import os

def main():
	directory = input("Please enter the directory that you would like to to save the file in: ")
	filename = input("Please enter the name of the file: ")
	name = input("Please enter your name: ")
	address = input("Please enter your address: ")
	phone_number = input("Please enter your phone number: ")
	if os.path.isdir(directory):
		writeFile = open(os.path.join(directory,filename),'w')
		writeFile.write(name+','+address+','+phone_number+'\n')
		writeFile.close()
		print("File contents: ")
		readFile = open(os.path.join(directory,filename),'r')
		for line in readFile:
			print(line)
			readFile.close()
	else:
		print("Whoops! That directory does not exist.")

main()
input("Please press ENTER to exit.")