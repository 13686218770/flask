from fdfs_client.client import Fdfs_client

client = Fdfs_client(r'E:\py\django\dailyfresh\utils\fdfs\client.conf')
ret = client.upload_by_filename(r'E:\py\django\dailyfresh\utils\fdfs\1.jpg')
print('ok')
print(ret)
