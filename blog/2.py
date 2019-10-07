# with open("1.py") as file:
#     print(file.read())

#排序查找
# def a(list,key):
#     for i in range(len(list)):
#         if list[i]==key:
#             return i
#     else:
#         return -1
# if __name__ == '__main__':
#     list=[2,51,6,7,9,10,34,5,67,9]
#     key=34
#     res=a(list,key)
#     if res==-1:
#         print('查找失败')
#     else:
#         print('查找成功下标为%s'%res)

# #二分查找
# def b(list,key,left,right):
#     if left>right:
#         return -1
#     midle=(left+right)//2
#     if list[midle]>key:
#         return b(list,key,left,midle-1)
#     elif list[midle]<key:
#         return b(list,key,midle+1,right)
#     else:
#         return midle
# if __name__ == '__main__':
#     list=[1,3,5,7,8,9,11,23,45,67,77,80,99]
#     key=1
#     res=b(list,key,0,len(list)-1)
#     if res==-1:
#         print('查找失败')
#     else:
#         print('查找成功，下标为%s'%res)

# #快速排序
# def quick(list):
#     if len(list)<2:
#         return list
#     mark=list[0]
#     small=[x for x in list if x<mark]
#     equle=[x for x in list if x==mark]
#     big=[x for x in list if x>mark]
#     return quick(small)+equle+quick(big)
# if __name__ == '__main__':
#     list=[20,45,23,12,6,9,10,45,67,89,35,68,25]
#     print('排序前list=',list)
#     resp=quick(list)
#     print('排序后list=',resp)

# # 冒泡排序
# def bubble(value):
#     # 外部循环: 对应走访数据的次数
#     for i in range(len(value)-1):#取0-8
#         # 设置标志位
#         flag = False
#         # 内部循环: 对应每次走访数据时,相邻数据对比次数
#         for j in range(len(value)-i-1):#取0-8
#             # 取从小到大排序
#             # 如果前者大于后者,则两者交换
#             if value[j] > value[j+1]:#j+1取到了下标9
#                 value[j],value[j+1]=value[j+1],value[j]
#                 # 数据交换,标志为True
#                 flag = True
#                 # print('第%s次value为%s'%(i,value))
#         # 检查是否进行数据交换
#         # 若未发生数据交换,则证明剩余数据有序
#         # 无需进行下一次数据的走访
#         if flag is False:
#             # 跳出外部循环
#             break
#     # 打印遍历次数
#     print("遍历次数", i)
# if __name__ == "__main__":
#     # 原始数据
#     value = [200, 100, 148, 139, 155, 160, 165, 170, 175, 180, 190]
#     print("排序前,", value)
#     # 冒泡排序
#     bubble(value)
#     print("排序后:", value)

#插入排序
def insert(list):
    for i in range(1,len(list)):
        temp=list[i]
        pos = i
        for j in range(i-1,-1,-1):#i-1取到了下标0
            if list[j]>=temp:
                list[j+1]=list[j]
                pos=j
            else:
                pos=j+1
                break
        list[pos]=temp
if __name__ == '__main__':
    list=[4,200,79,23,45,68,90,56,24,58]
    print('排序前',list)
    insert(list)
    print('排序后',list)