"""app/feedback/client/post_upsert.py
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
        'param1': 'upsert',
        'param2': [
            {
                'id': 1,
                'service': 'service1',
                'title': 'title1',
                'detail': 'add as new record1'
            },
            {
                'id': 2,
                'service': 'service2',
                'title': 'title2',
                'detail': 'add as new record2'
            },
            {
                'id': 1,
                'service': 'service3',
                'title': 'title3',
                'detail': 'update from record1 to new record3'
            }
        ]
    }
})
headers = {
    'Content-Type': 'application/json'
}

res = requests.post(url=url, data=data, headers=headers)

print(res.status_code)
print(res.text)
