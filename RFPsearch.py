import scipy.io as sio
from os.path import dirname, join
from fuzzywuzzy import fuzz

def print_info(x):
    keys = [o for o in dir(x) if not o.startswith("_")]
    for key in keys:
        print("---- ----")
        print(f"{key}:")
        exec(f"print(x.{key})")
        print("---- ----")

# rUser = [ 5, 3 , 2]

def search(rUser):
    current_dir = dirname(__file__)
    file_path = join(current_dir, 'data.mat')
    data = sio.loadmat(file_path, squeeze_me=True, struct_as_record=False)['data']
    print(len(data))
    print("rUser", rUser)
    rNumber = len(rUser)
    AllrType = [None] * (len(data))
    for x in range(0, len(data)):
      AllrType[x] = data[x].rType
    AllrEdge = [None] * (len(data))
    for x in range(0, len(data)):
      AllrEdge[x] = data[x].rEdge
    ForUser = list(filter(lambda x: len(x) == rNumber, AllrType)) 
    ForUser_rEdges = [None] * (len(ForUser))
    i=0

    for x in range(0,len(data)):
      if len(AllrType[x]) == rNumber:
        ForUser_rEdges[i] = AllrEdge[x]
        i = i+1
    
    m = 0
    for x in range(0, len(ForUser)):
      if fuzz.token_sort_ratio(rUser, ForUser[x]) >= m:
        m = (fuzz.token_sort_ratio(rUser, ForUser[x]))
    c=0

    for x in range(0, len(ForUser)):
      if fuzz.token_sort_ratio(rUser, ForUser[x]) == m:
        c = c+1
    


    Required_rType = [None] * (c)
    Required_rEdge = [None] * (c)
    All_datapoints = [None] * (c)
    i=0

    for x in range(0, len(ForUser)):
      if fuzz.token_sort_ratio(rUser, ForUser[x]) == m:
        Required_rType[i] = ForUser[x]
        Required_rEdge[i] = ForUser_rEdges[x]
        All_datapoints[i] = x
        #print("for datapoint "+str(x)+" we have ")
        #print("\n room type as\n ", Required_rType[i])
        #print("\nwe have the adjacencies as\n ", Required_rEdge[i])
        # for j in range(0,len(Required_rEdge[i])):
        #     nptemp = np.delete(Required_rEdge[i][j], 2)
        #     np.reshape(Required_rEdge[i][j], 2)
        #     Required_rEdge[i][j] = nptemp


        i = i+1

    

    # redge = Required_rEdge.tolist()
    redge = []

    for x in Required_rEdge:
        xl = x.tolist()
        

        for y in xl:
            y.pop(2)

        redge.append(xl)

    

        
    
    print("rEdge",redge)
    print("\n\n#####The no. of matched graphs are", len(redge), "#####\n\n")
    return len(Required_rType[0]), redge

# rNumber = int(input("Enter number of rooms (only between 4 and 8) : ")) 


# rUser = list(map(int,input("\nEnter the room types in form of room code : ").strip().split()))[:rNumber] 
  
# print("\nrType for User is - ", rUser)

# search(rUser)