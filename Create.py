import bsddb3 as bsddb
import random
import os

DB_SIZE = 100000
SEED = 10000000
DA_FILE = "/tmp/nmcarrol_db/sample_db"

if not os.path.exists("/tmp/nmcarrol_db/"):
    os.makedirs("/tmp/nmcarrol_db/")




def dbOpen (option):
    
    if(option == "btree"):
        bTree()
    elif(option == "hash"):
        hashTree()
    elif(option == "indexfile"):
        index()
    else:
        print("Incorrect option exiting.")
        
def bTree():
    # Make sure you run "mkdir /tmp/my_db" first!
    try:
        db = bsddb.btopen(DA_FILE, "w")
    except:
        print("DB doesn't exist, creating a new one")
        db = bsddb.btopen(DA_FILE, "c")
    random.seed(SEED)
 
    for index in range(DB_SIZE):
        krng = 64 + get_random()
        key = ""
        for i in range(krng):
            key += str(get_random_char())
        vrng = 64 + get_random()
        value = ""
        for i in range(vrng):
            value += str(get_random_char())
        print (key)
        print (value)
        print ("")
        key = key.encode(encoding='UTF-8')
        value = value.encode(encoding='UTF-8')
        db[key] = value
    try:
        db.close()
    except Exception as e:
        print (e)
 
def hashTree():
    try:
        db = bsddb.hashopen(DA_FILE, "w")
    except:
        print("DB doesn't exist, creating a new one")
        db = bsddb.hashopen(DA_FILE, "c")
    random.seed(SEED)
 
    for index in range(DB_SIZE):
        krng = 64 + get_random()
        key = ""
        for i in range(krng):
            key += str(get_random_char())
        vrng = 64 + get_random()
        value = ""
        for i in range(vrng):
            value += str(get_random_char())
        print (key)
        print (value)
        print ("")
        key = key.encode(encoding='UTF-8')
        value = value.encode(encoding='UTF-8')
        db[key] = value
    try:
        db.close()
    except Exception as e:
        print (e)
        
def index():
    pass
    
def get_random():
    return random.randint(0, 63)

def get_random_char():
    return chr(97 + random.randint(0, 25))
    pass
