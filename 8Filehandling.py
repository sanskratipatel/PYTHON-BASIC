# f = open("PYTHON-BASIC/test.txt" , 'r') 
# f = open("PYTHON-BASIC/test.txt")  # Open the file in read mode 
f  = open("PYTHON-BASIC/8test.txt", 'rb')  # Open the file in binary form 
text = f.read() 
print(text)
f.close()  




w = open("PYTHON-BASIC/8test1.txt",'w') 
print(w)
w.write("This is a test file.") 
w.close()


a = open("PYTHON-BASIC/8test1.txt",'a')  # Open the file in append mode
a.write("\nThis is an appended line.") 
a.close() 


# OPEN WITH 
with open("PYTHON-BASIC/8test2.txt", 'w') as f:
    f.write("hello bro this is me")
   
