# name="Gloria"
#
# for i in name:
#     if(i !=0):
#         print(i)
fruits=["Mangoes","Apples","Oranges","Grapes","Pineapples"]
try:
    for i in range(5):
        print(f"The index and element from the list is {i,fruits[i]}")
except:
    print("index out of range")

nambari=[3,4,5,7]

if len(nambari)>4:
    raise Exception(f"Length of the given list must be less or equal to 3 but its {len(nambari)}")