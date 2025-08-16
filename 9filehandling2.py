f = open("PYTHON-BASIC/9test2.txt",'r')  
i = 0
while True:
    i = i+1
    line =  f.readline()  # Read one line at a time
    if not line:
        break
    # print(line, end='')  # Print the line without adding extra newlinei 
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"Line {i}: {m1}, {m2}, {m3}")
    print(line)