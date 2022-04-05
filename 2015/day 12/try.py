data= '''
  {
"MessageId": "250e37a8-d779-48a1-9941-84219a82513e",
"ReceiptHandle": "AQEBjualXe2ywqTgIVmCNI5sKj7r48werf84HHA2BWZimwiEXLFxA/MiPBclK048NZBtOnM3dSDfoiwwqoNTPxTRz+IChd8McziweCxHX6texjAOi/MyAQjCWP+2hJPoxzQgXx9kjnKbepKlcgxhpOiQZe6WiSIq0dXwHHXSA7SP0g9NIR/dU38b+wmo0m2q7MNVfSct967EKF49wow9RHyFMO8iD8fH93PYT9om5NdUha3dvkWnisKcfuO5pZY3LLXPAnuZT/VfqxJjmPqb98iepBfqFb6SpM/02IVSql81XKJEbMBc4zPHp/Uace6e4UDGsn/hPCVsqQsTzrbKCR+ovpkhXipWwTYSlgsLe/o43k0UxhCN8eKhg835KuUkskA3T8C5Q6v6xgznlR7JJuhZpg==",
"MD5OfBody": "bbdc5fdb8be7251f5c910905db994bab",
"Body": "Information about current NY Times fiction bestseller for week of 12/11/2016.",
"Attributes": {"SentTimestamp": "1553851566164"},
"MD5OfMessageAttributes": "d25a6aea97eb8f585bfa92d314504a92",
"MessageAttributes": {"Author": {"StringValue": "John Grisham","DataType": "String"},"Title": {"StringValue": "The Whistler","DataType": "String"},"WeeksOn": {"StringValue": "6","DataType": "Number"}}
  } '''

import json

class Response:

    def __init__(self, data):
        self.__dict__ = json.loads(data)

print(type(data))
response = Response(data)

if hasattr(response , 'MessageId'):
    receipt_handle = response.ReceiptHandle
    print("Received and deleted message: %s" % response.MessageId)

else:
    print('Message not received yet')