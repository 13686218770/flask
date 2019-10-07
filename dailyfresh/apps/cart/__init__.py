#顺序查找
# def a(l,k):
#     for x in range(len(l)):
#         if l[x]==k:
#             return x
#     else:
#         return 0
# if __name__ == '__main__':
#     l=[1,20,3,4,5,6,7,8,9,10,11,12,13]
#     k=13
#     res=a(l,k)
#     if res==0:
#         print('no')
#     else:
#         print('查找成功,元素下标为：%d'%res)

#二分查找
# def b(l,k,left,right):
#     middle=(left+right)//2
#     if left>right:
#         return 0
#     if k>l[middle]:
#         left=middle+1
#         return b(l,k,left,right)
#     elif k<l[middle]:
#         right=middle-1
#         return b(l, k, left, right)
#     else:
#         return middle
# if __name__ == '__main__':
#     l=[1,2,3,4,5,6,7,8,9,10,11,12,13]
#     k=13
#     res=b(l,k,0,len(l)-1)
#     if res==0:
#         print('no')
#     else:
#         print('查找成功,元素下标为%d'%res)

#冒泡排序
# def f(x):
#     for j in range(len(x)):
#         for i in range(len(x)-j-1):
#             if x[i]>x[i+1]:
#                 x[i],x[i+1]=x[i+1],x[i]
#     else:
#         print('次数为:', j)
#         return x
#
# if __name__ == '__main__':
#     #排序前
#     l=[100, 190, 165, 170, 155, 108, 139, 175, 160, 180]
#     res=f(l)
#     print('排序后：',res)

# #插入排序
# def f(l):
#     for x in range(1,len(l)):
#         m=l[x]
#         pos=x
#         for y in range(x-1,-1,-1):
#             if l[y]>m:
#                 l[y+1]=l[y]
#                 #插入位置
#                 pos=y
#             else:
#                 # m=l[y+1]
#                 # 插入位置
#                 pos=y+1
#                 break
#         l[pos]=m
# if __name__ == '__main__':
#     l=[80, 70, 30, 50, 69, 78, 90, 100, 65, 88]
#     f(l)
#     print('排序后为：',l)

#快速排序
# def quick(value):
#     # 递归退出条件
#     if len(value) < 2:
#         return value
#     # 设置关键数据
#     mark = value[0]
#     # 找出所有小于关键数据的
#     small = [x for x in value if x < mark]
#     # 找出所有等于关键数据的
#     equal = [x for x in value if x == mark]
#     # 找出所有大于关键数据的
#     big = [x for x in value if x > mark]
#     # 从小到大顺序排序
#     return quick(small) + equal + quick(big)
# if __name__ == "__main__":
#     # 原始数据
#     value = [80, 70, 30, 50, 69, 78, 90, 100, 65, 88]
#     print('排序前:', value)
#     # 快速排序
#     value = quick(value)
#     print('排序后：',value)

