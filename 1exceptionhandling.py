a =  "hello"
try: 
    b = 5//0 
    a1 = [1,2,3,4,5] 
    print(a1[10])
except ZeroDivisionError as e : 
    print("Caught exception",e) 
except IndexError as e :
    print("Caught exception",e)
except Exception as e :
    print("Caught exception", e)
print("Continuing with the program...") 

try : 
    a = [1,2,3,4,5] 
    print(a[10])
except Exception as he : 
    print("Caught exception", he) 
    print("This is a fallback message.")