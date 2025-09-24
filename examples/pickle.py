import os
import pickle

obj1 = "this is a string"
obj2 = ["this", "is", "a", "list"]

FILEPATH = "file.dat"

with open(FILEPATH, "wb") as f:
    pickle.dump(obj1, f)  # object, file object
    pickle.dump(obj2, f)

with open(FILEPATH, "rb") as f:
    try:
        while True:
            print(pickle.load(f))
    except EOFError:
        print("Caught EOFError. Reached the end.")

os.remove(FILEPATH)
