# def privileged_check(fn):
#     '''权限验证功能的装饰器'''
#     print(1)
#     def fx(n, x):
#         print("权限验证中.....")
#         fn(n, x)
#     return fx
#
# def send_message(fn):
#     '''实现业务操作完成后发送短消息的功能'''
#     print(2)
#     def fy(n, x):
#         fn(n, x)  # 先操作，再发消息
#         print("正在发短消息给:", n, '...')
#     return fy
#
#
# # -------- 以下是魏老师写的程序--------
# @privileged_check
# @send_message
# def savemoney(name, x):
#     print(name, '存钱', x, '元')
#
# @send_message
# @privileged_check
# def withdraw(name, x):
#     print(name, '取钱', x, '元')
#
# # -----以下是调用者小张写的程序---------
# savemoney('小王', 200)
# savemoney('小赵', 400)
#
# withdraw('小李', 500)