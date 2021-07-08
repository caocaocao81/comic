import jwt

encoded_jwt = jwt.encode({'username':'运维咖啡吧','site':'https://ops-coffee.cn'},'secret_key',algorithm='HS256')

print(encoded_jwt)