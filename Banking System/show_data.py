import pickle
from pprint import pprint

filename = "user_stats"

try:
    with open(filename, "rb") as fileobj:
        users = pickle.load(fileobj)
except:
    users=[]

pprint(users)