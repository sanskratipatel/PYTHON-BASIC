# Seek(), tell() and truncate() function In Python 

# The seek() method sets the file's current position at the offset.
# The tell() method returns the current position of the file cursor.


with open("PYTHON-BASIC/10test.txt" ,'r') as f :
    print(type(f))  # <class '_io.TextIOWrapper'>
    f.seek(5)  # Move to the beginning of the file  
    print(f.tell())  # Output: 5 it tell current position of the file cursor
    data =f.read(10)  # Read 10 characters from the current position
    print(data)  # Output: ' guys thi' 

with open("PYTHON-BASIC/10test1.txt" ,'w') as f :
    f.write("hello guys this is me")  # Write to the file 
    f.truncate(10) 

with open("PYTHON-BASIC/10test1.txt" ,'r') as f :
    print(f.read())  # Output: 'hello gui' (truncated to 10 characters)
   