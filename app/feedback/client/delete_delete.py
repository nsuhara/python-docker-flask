"""app/feedback/client/delete_delete.py
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
        'param1': 'delete',
        'param2': 1
    }
})
headers = {
    'Content-Type': 'application/json'
}

res = requests.delete(url=url, data=data, headers=headers)

print(res.status_code)
print(res.text)
