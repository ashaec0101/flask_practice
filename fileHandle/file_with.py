import pickle

numbers=[1,2,3,4,5,6,7]

with open("num_pick.txt","wb") as file:
    pickle.dump(numbers,file)

    #no need to close using with which is called the Context Manager.

with open("num_pick.txt""rb") as file:
    data=pickle.load(file)