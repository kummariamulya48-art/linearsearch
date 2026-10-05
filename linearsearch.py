def linearsearch(a,el):
  ar=[]
  for i in range(len(a)):
    if a[i]==el:
      #print(f'{el} is found at {i} index ')
      ar.append(i)
  return ar
  

a=[12,2,44,23,14,65,14]
print(linearsearch(a,14))

def  binarysearch(a,el):
  

a=[6,7,11,14,17,20]
binarysearch(a,14)
def linearsearch(a,el):
  ar=[]
  for i in range(len(a)):
    if a[i]==el:
      print(f'{el} is found at {i} index ')
      return i
  

a=[12,2,44,23,14,65,14]
print(linearsearch(a,14))
