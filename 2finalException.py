a = "Hello guys" 

def func1 ():
    try : 
        # b = 5 // 0
        a1 = [1, 2, 3, 4, 5]
        print(a1[1])
    except ZeroDivisionError as e:
        print("Caught exception  hreer", e)
    except Exception as e:
        print("Caught exception", e) 
    finally :
        print("This is the finally block, executing cleanup code.")
    print("Continuing with the program...")
