import array as myarray
new_arr = myarray.array('i',[3,4,5,6,7,8,9,10])
new_arr.append(15)
new_arr.insert(0,2)
new_arr[5]=4
new_arr.pop(9)
new_arr = new_arr[::-1]
new_arr.sort(1)
for i in range(0,len(new_arr)):
    print(new_arr[i],end=" ")
    