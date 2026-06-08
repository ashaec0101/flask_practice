file=open("numbers.txt","wb") #writing binary
file.write(bytes([10,20,20,40]))

file.close()
#open again and read
file=open("numbers.txt","rb")
data=file.read()
print(data)
file.close()