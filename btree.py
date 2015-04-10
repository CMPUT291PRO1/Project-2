import bsddb3 as bsddb
import Create
import time

DA_FILE = "/tmp/nmcarrol_db/sample_db"

# get option from Base function
def keySearch_Btree(f):
	
	print("BTREE key search")
	print("==========================================================")
	
	try:
		db = bsddb.btopen(DA_FILE,"r")
	except:
		print("Error opening database.")	
	
	key = input("Please enter your key:").encode(encoding='UTF-8')
	
	# record staring time
	start_time = time.time()
	
	if db.has_key(key):
		value = db[key]
		print("The value to key '", key.decode(encoding = 'UTF-8'),"' is "\
			  , value.decode(encoding = 'UTF-8'))

		# number of retrieved data is one since key is unique
		print("Record retrieved: 1")	
	else:
		print("This key does not exist in the database.")

	# IMPORTANT: CLOSE THE DATABASE
	try:
		db.close()
	except Exception as e:
		print (e)
		
	# record ending time
	end_time = time.time()
	# compute time consumed
	print("Time used on BTREE key search is", end_time - start_time)
	f.write(key.decode(encoding = 'UTF-8') + "\n" + value.decode(encoding = 'UTF-8') + "\n\n")
	

def valueSearch_Btree(f):
	
	print("BTREE value search")
	print("==========================================================")	
	
	try:
		db = bsddb.btopen(DA_FILE,"r")
	except:
		print("Error opening database.")
	
	data = input("Please enter data value:").encode(encoding='UTF-8')
	
	# record staring time
	start_time = time.time()

	retrievedKeys = []

	for key in db.keys():	
		if db[key] == data:
			retrievedKeys.append(key.decode(encoding = 'UTF-8'))

			# record ending timekeySearch_Btree()
			end_time = time.time()
			# compute time consumed
			print("Time used on BTREE key search is", end_time - start_time)
		
			# print result
			print("Retrieved records: ", len(retrievedKeys))
			print("Keys referring to this data: ", retrievedKeys)
		
	if not retrievedKeys:
		print("Data does not exist in database.")
		
	for key in retrievedKeys:
		f.write(key + "\n" + data.decode(encoding = 'UTF-8') + "\n\n")
		
	# IMPORTANT: CLOSE THE DATABASE
	try:
		db.close()
	except Exception as e:
		print (e)
		
	

def rangeSearch_Btree(f):
	
	print("BTREE range search")
	print("==========================================================")
	
	try:
		db = bsddb.btopen(DA_FILE,"r")
	except:
		print("Error opening database.")
	
	checking = True
	while checking:
		checking = False
		lower = input("Please enter lower bound:").encode(encoding = 'UTF-8')
		upper = input("Please enter upper bound:").encode(encoding = 'UTF-8')
		if lower > upper:
			print("Invalid range. Try again.")
			checking = True
	
	# record staring time
	start_time = time.time()
	
	in_range_keys = []
	keys = db.keys()
	for i in range(len(db)):
		if keys[i] >= lower and keys[i] <= upper:
			in_range_keys.append(keys[i])
	
	print("Retrieved record: ", len(in_range_keys))
	
	# record ending time
	end_time = time.time()
	# compute time consumed
	print("Time used on BTREE key search is", end_time - start_time)
	
	for i in range(len(in_range_keys) ):
		key = in_range_keys[i].decode(encoding = 'UTF-8')
		value = db[in_range_keys[i]].decode(encoding = 'UTF-8')
		f.write(key + "\n" + value+ "\n\n")
	
	# IMPORTANT: CLOSE THE DATABASE
	try:
		db.close()
	except Exception as e:
		print (e)

if __name__ == "__main__":
	f = open("answers.txt", 'w')
	Create.bTree()
	keySearch_Btree(f)
	valueSearch_Btree(f)
	rangeSearch_Btree(f)
