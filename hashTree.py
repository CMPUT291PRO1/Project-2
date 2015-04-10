'''
Created on Apr 9, 2015

@author: Nic
'''
import bsddb3 as bsddb
import time
import sys

DA_FILE = "/tmp/nmcarrol_db/sample_db"




    

def valueSearch_Hashtree(file):
    
    file = open("answers", 'w')
    
    print("HashTree value search")
    print("==========================================================")    
    
    try:
        db = bsddb.hashopen(DA_FILE,"r")
    except:
        print("Error opening database.")
    
    data = input("Please enter data value:").encode(encoding='UTF-8')
    
    # record staring time
    start_time = time.time()

    retrievedKeys = []

    for key in db.keys():    
        if db[key] == data:
            retrievedKeys.append(key.decode(encoding = 'UTF-8'))
            
            
    # compute time consumed
    print("Time used on HashTree key search is", time.time()-start_time)
        
    # print result
    print("Retrieved records: ", len(retrievedKeys))

        
    if not retrievedKeys:
        print("Data does not exist in database.")
        
    for key in retrievedKeys:
        file.write(key + "\n" + data + "\n\n")
        
    
    # IMPORTANT: CLOSE THE DATABASE
    try:
        db.close()
    except Exception as e:
        print (e)
        
    

def rangeSearch_Hashtree(file):
    
    
    print("HashTree range search")
    print("==========================================================")
    
    try:
        db = bsddb.hashopen(DA_FILE,"r")
    except:
        print("Error opening database.")
            
    # record staring time
    start_time = time.time()
    
    checking = True
    while checking:
        checking = False
        lower = input("Please enter lower bound:").encode(encoding = 'UTF-8')
        upper = input("Please enter upper bound:").encode(encoding = 'UTF-8')
        if lower > upper:
            print("Invalid range. Try again.")
            checking = True
    
    in_range_keys = []
    keys = db.keys()
    for i in range(len(db)):
        if keys[i] >= lower and keys[i] <= upper:
            in_range_keys.append(keys[i])
    
    print("Retrieved record: ", len(in_range_keys))
    

    # compute time consumed
    print("Time used on HashTree key search is", time.time()-start_time)
    
    for i in range(len(in_range_keys) ):
        key = in_range_keys[i].decode(encoding = 'UTF-8')
        value = db[in_range_keys[i]].decode(encoding = 'UTF-8')
        file.write(key + "\n" + value + "\n\n")
        
    # IMPORTANT: CLOSE THE DATABASE
    try:
        db.close()
    except Exception as e:
        print (e)
    
        
def keySearch_Hashtree(file):
    
    print("HashTree key search")
    print("==========================================================")
    
    try:
        db = bsddb.hashopen(DA_FILE,"r")
    except:
        print("Error opening database.")    
    
    key = input("Please enter your key:").encode(encoding='UTF-8')
    
    # record staring time
    start_time = time.time()
    
    if db.has_key(key):
        value = db[key]
        file.write(key + "\n" + value + "\n\n")

        # number of retrieved data is one since key is unique
        print("Record retrieved: 1")    
    else:
        print("This key does not exist in the database.")

    # IMPORTANT: CLOSE THE DATABASE
    try:
        db.close()
    except Exception as e:
        print (e)
        
    # compute time consumed
    print("Time used on HashTree key search is", time.time()-start_time)
    
    
