import array as *;

val = array('i', [1,2,3,4,5,3,5,2,3,4,6])


print(val)

for i in range (0,6):
    print(val[i], end="")

print('\n')

for i in val:
    print(i, end=" ")

for i in range(0, len(val)):
    print(val[i], end=" ")

print('\n')
print(val.typecode)

val.reverse()

for i in range(0,len(val)):
    print(val[i], end=" ")


val.insert(1, 99)
val.append(100) # Inset element at last
val[2] = 200

copyArray = array(val.typecode, (x for x in val))

for i in range(0, len(copyArray )):
    print(copyArray[i], end=" ")

copyArray.pop(3) # Index
copyArray.remove(3) # Value