file=open("data.txt","r") 

#Read Entire File
content = file.read()
print(content)

#Read One line
line=file.readline()
#print(line)

#Read all lines
lines=file.readlines()
print(lines)

file.close() #Close the file