import pickle
file = open("num_pickles.dat","wb")

numbers=[10,20,30,40,50]

pickle.dump(numbers,file) #writes it into this file

file.close()
file=open("num_pickles.dat","rb")
data=pickle.load(file)
print(data)
file.close()