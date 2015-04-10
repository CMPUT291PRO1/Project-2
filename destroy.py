import os
import bsddb3 as bsddb

DA_FILE = "/tmp/nmcarrol_db/sample_db"

def destroy():
	try:
		os.system("rm /tmp/nmcarrol_db/sample_db")
		print("Database destroyed.")
	except Exception as Error:
		print(Error)
		
if __name__ == "__main__":
	destroy()
