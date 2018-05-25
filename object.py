print("hwdp")
x = 50;
print(x)
x = "chuj w dupie"
print(x)
print(len(x))# lenght
print("subString  1: ", x[2:])
print("subString  1: ", x)
print("subString  2: ", x[2:8])
print("subString  last 3 letters : ", x[-3:])
print("czy zawiera chuj ? " , ("chuj" in x))
#listy
list = []
print("dlugos  pustej listy ", len(list))
list.append("zul")
list.append("bezdomny")
list.append("cygan")
list.append("menalos")
print(list)
print("dlugos   listy ", len(list))
print(list[1])
list.insert(0,"raffi")
print(list)
del(list[-2 :])
print(list)
#super operacje na listach
list2 =[]
list2.append(1)
list2.append(2)
list2.append(3)

list3 =[]
list3.append(1)
list3.append(2)
list3.append(3)

print(list2+list3)
list3.append(list)
print(list3 )

#imutable list
x = 1,2,3,4,5,6,7
  