
import os
import multiprocessing
import ctypes
import requests
import hashlib
import uuid


url = ["http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
"https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg",
"http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg"];

fileHashes = []

def download_file(url, file_name=None): 
	r = requests.get(url, allow_redirects=True)
	file = file_name if file_name else str(uuid.uuid4())
	open(file, 'wb').write(r.content)
	fileHashes.append(hashlib.md5(open(file,'rb').read()).hexdigest())


def parent_child(): 
    pid = os.fork()

    if pid > 0:
        status = os.wait()
        print("Parent process: ", os.getpid())

  
    else:
        print("Child process : ", os.getpid())

        for x in url:
            download_file(x)


          

def chech_files():
    len_ = len(fileHashes)
    for i in range(len_):
        for j in range(i+1,len_):
            if(fileHashes[i] == fileHashes[j]):
                print("this index", i, "and this index of array", j, "is the same with each other")


libc = ctypes.CDLL(None)
syscall = libc.syscall

syscall(os.getpid())
    
parent_child()

process = multiprocessing.Process(target=chech_files, args=( ))


process.start()

process.join()
