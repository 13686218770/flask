# coding=utf-8

# from .CCPRestSDK import REST
# from CCPRestSDK import REST
from ihome.libs.yuntongxun.CCPRestSDK import REST
# 主帐号
accountSid = '8a216da86a960fd9016aa6484b860df7'

# 主帐号Token
accountToken = '49b517deb28947a98c15c3e5290b182a'

# 应用Id
appId = '8a216da86a960fd9016aa6484bdd0dfe'

# 请求地址，格式如下，不需要写http://
serverIP = 'app.cloopen.com'

# 请求端口
serverPort = '8883'

# REST版本号
softVersion = '2013-12-26'

  # 发送模板短信
  # @param to 手机号码
  # @param datas 内容数据 格式为列表 例如：['12','34']，如不需替换请填 ''
  # @param $tempId 模板Id


class CCP(object):
    """自己封装的发送短信的辅助类"""
    # 用来保存对象的类属性
    instance = None

    def __new__(cls):
        # 判断CCP类有没有已经创建好的对象，如果没有，创建一个对象，并且保存
        # 如果有，则将保存的对象直接返回
        if cls.instance is None:
            obj = super(CCP, cls).__new__(cls)

            # 初始化REST SDK
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)

            cls.instance = obj

        return cls.instance

    def send_template_sms(self, to, datas, temp_id):
        """"""
        # print('01010')
        result = self.rest.sendTemplateSMS(to, datas, temp_id)
        # print(3333)
        # # for k, v in result.iteritems():
        # for k, v in result.items():
        #     if k == 'templateSMS':
        #         # for k, s in v.iteritems():
        #         for k, s in v.items():
        #             print ('%s:%s' % (k, s))
        #     else:
        #         print ('%s:%s' % (k, v))
        # # smsMessageSid:ff75e0f84f05445ba08efdd0787ad7d0
        # # dateCreated:20171125124726
        # # statusCode:000000
        status_code = result.get("statusCode")
        if status_code == "000000":
            # 表示发送短信成功
            return 0
        else:
            # 发送失败
            return -1


if __name__ == '__main__':
    ccp = CCP()
    # ret = ccp.send_template_sms("13686218770", ["1234", "5"], 1)
    # print('ret:',ret)

    
   
