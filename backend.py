import time
di={}
def create(key,value,timeout=0):
    if key in di:
        print("ERROR: Key already exist")
    else:
        if key.isalpha() and len(key)<=32:
            if len(di)<=(1024*1024*1024) and value<=(16*1024*1024):
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                di[key]=l 
                print("Key added")
            else:
                print("ERROR: Memory limit exceeded")
        else:
            print("ERROR: Invalid key name")
            
def read(key):
    if key not in di:
        print("ERROR: Key does not exist")
    else:
        b=di[key]
        if b[1]==0:
            print(str(b[0]))
        else:
            if time.time()<b[1]:
                print(str(b[0]))
            else:
                print("ERROR: Time to live exceeded")

def delete(key):
    if key not in di:
        print("ERROR: Key does not exist")
    else:
        b=di[key]
        if b[1]==0:
            del(di[key])
            print("Key deleted")
        else:
            if time.time()<b[1]:
                del(di[key])
                print("Key deleted")
            else:
                print("ERROR: Time to live exceeded")
                
