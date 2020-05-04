"""app/feedback/client/get_read_one.py
"""
import requests

from feedback.client import URL

url = '{url}?process=back_end&request=read_one&id={id}'.format(**{
    'url': URL,
    'id': 1
})

res = requests.get(url=url)

print(res.status_code)
print(res.text)
