# YOUR CODE HERE
list1=[]
list2=[]
n=int(input()) #จำนวนรอบ

#เพิ่มเลขเข้าลิสต์
for i in range (n):
    x=int(input())
    list1.append(x)
for i in range (n):
    y=int(input())
    list2.append(y)

#บวกเลขแต่ละตัวในลิสต์
def summation(list1,list2):
    update_list=[]
    for i in range(n):
        total = list1[i]+list2[i]
        update_list.append(total)
    return update_list
result=summation(list1,list2)
print(result)

#หาmin,max
def find_min_max(result):
    max_value = result[0]
    min_value = result[0]
    for j in result:
        if j > max_value:
            max_value=j
        if j < min_value:
            min_value=j
    return min_value , max_value
print(find_min_max(result))
