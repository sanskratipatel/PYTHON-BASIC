import os 

if  (not os.path.exists("data")):
     os.mkdir("data")  

for i in range(0,100):
     print(f"Creating folder data/Day{i+1}")
    # os.mkdir(f"data/Day{i+1}")   
    # os.rename(f"data/Day{i+1}" , f"data/temp{i+1}") 
    # os.remove(f"data/temp{i+1}")

    
folders = os.listdir("data")
# print(folders) 
for i in range(len(folders)):
    print(folders[i])
    # if folders[i].startswith("Day"):
        # os.rename(f"data/{folders[i]}", f"data/Day-{i+1}") 
        # print(f"Renamed {folders[i]} to Day-{i+1}")
    