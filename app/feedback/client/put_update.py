"""app/feedback/client/put_update.py
"""
import json

import requests

from feedback.client import URL

url = '{url}'.format(**{
    'url': URL
})
data = json.dumps({
    'process': 'back_end',
    'request': {
        'param1': 'update',
        'param2': {
            'id': 1,
            'service': 'update_service1',
            'title': 'update_title1',
            'detail': 'update_detail1'
        }
    }
})
headers = {
    'Content-Type': 'application/json'
}

res = requests.put(url=url, data=data, headers=headers)

print(res.status_code)
print(res.text)
