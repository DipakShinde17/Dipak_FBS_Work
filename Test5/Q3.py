
data = [[101,"seema",45000],[340,"rajani",13000],[210,"tannu",14000],[320,"suresh",35000]]

def sortt(data):
    for i in range(1,len(data)):
        for j in range(0,len(data)-i):
            if(data[j] > data[j+1]):
                data[j],data[j+1] = data[j+1],data[j]

    return data

data = [[101,"seema",45000],[340,"rajani",13000],[210,"tannu",14000],[320,"suresh",35000]]
print("after sorting list :",data)
res = sortt(data)
print(res)

