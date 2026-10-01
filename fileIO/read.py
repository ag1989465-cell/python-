f=open("C:/Users/hi/.vscode/py/python/fileIO/name.txt","r")
# read_data=f.readlines()
# read_data=f.read()
read_data=f.readline()
#f.write("this is new line")
print(read_data)
f.close()
# x= creates a new file if not exist and open it in write mode
#a=add data to the file if exist or create a new file and open it in write mode
#b= opens a file in binary mode
#t= opens a file in text mode
#+= opens a file in read and write mode
#r+= opens a file in read and write mode