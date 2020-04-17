import requests

# requestsr = requests.get('http://httpbin.org/get')
# print(r.text)


def get_proxy():
    return requests.get("http://118.24.52.95:5010/get/").text


def getHtml():
    retry_count = 5
    proxy = get_proxy()
    print(proxy)
    while retry_count > 0:
        try:
            html = requests.get('http://httpbin.org/get', proxies={"http": "http://{}".format(proxy)})
            return html.text
        except Exception:
            retry_count -= 1
    return None


print(getHtml())
