with open('proxy_list.txt') as f:
    content = f.readlines()
content = map(lambda proxy: 'http://'+proxy, content)
with open('http_proxy_list.txt', 'w+') as f:
    f.writelines(content)
