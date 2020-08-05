import base64
import jwt


encoded_jwt = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
print(encoded_jwt)  # b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lIjoicGF5bG9hZCJ9.Joh1R2dYzkRvDkqv3sygm5YyK8Gi4ShZqbhK2gxcs2U'


token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lIjoicGF5bG9hZCJ9.Joh1R2dYzkRvDkqv3sygm5YyK8Gi4ShZqbhK2gxcs2U'
print(jwt.decode(token, verify=False))  # {'some': 'payload'}     # token.encode() also works


print(jwt.decode(token, 'secret'))  # {'some': 'payload'}
# print(jwt.decode(token, 'wrong_secret'))  # jwt.exceptions.InvalidSignatureError: Signature verification failed
