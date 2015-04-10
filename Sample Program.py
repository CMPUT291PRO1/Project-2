import bsddb3 as bsddb
import Create
import time

DA_FILE = "/tmp/my_db/sample_db"

try:
    db = bsddb.btopen(DA_FILE,"r")
except:
    print("Error opening database.")
    
key = input("Please enter your key")
    
start_time = time.time()
print(db.has_key(key))


print("Time used on BTREE key search is", time.time()-start_time)
        