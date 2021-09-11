import requests

urls = []

for index, url in enumerate(urls):
    r = requests.get(url)

    open(f'input/{index}.jpg', 'wb').write(r.content)
