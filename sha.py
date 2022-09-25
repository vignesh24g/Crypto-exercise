import hashlib
  
filename = "sample.txt"
with open(filename,"rb") as f:
    bytes = f.read() 
    hash = hashlib.sha256(bytes).hexdigest();
    print(hash)