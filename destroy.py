import os
import bsddb3 as bsddb

DA_FILE = "/tmp/my_db/sample_db"

def destroy():
	try:
		db = bsddb.btopen(DA_FILE,"r")
		db.close()
		os.system("rm /tmp/my_db/sample_db")
		print("Database destroyed.")
	except Exception as Error:
		print(Error)
    
if __name__ == "__main__":
	destroy()
