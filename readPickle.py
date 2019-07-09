import pickle

with open("data.pickle", 'r') as fr:
    data = pickle.load(fr)
print(data)
