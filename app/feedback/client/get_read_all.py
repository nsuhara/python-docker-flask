"""app/feedback/client/get_read_all.py
"""
import requests

from feedback.client import URL

url = '{url}?process=back_end&request=read_all'.format(**{
    'url': URL
})

res = requests.get(url=url)

print(res.status_code)
print(res.text)
