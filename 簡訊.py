#寄送簡訊
from twilio.rest import Client   #Client is object(class)

account_sid = 'AC81c61d95f5c2b8157f68e8a7138d6d2a'
auth_token = 'cae43f6ffae2e458286e5436b2098259'

client = Client(account_sid, auth_token)

message = client.messages.create(
	to='+886932530813',
	from_='+16208402844',
	body='你好')
