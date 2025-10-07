import pickle

with open("data.pick", "rb") as f:
    newd=pickle.load(f)
    
print(newd, type(newd))