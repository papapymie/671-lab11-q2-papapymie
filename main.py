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
update_list=summation(list1,list2)
print(update_list)

#หาmin,max
def find_min_max(update_list):
    min_value=min(update_list)
    max_value=max(update_list)
    return min_value , max_value
print(find_min_max(update_list))
