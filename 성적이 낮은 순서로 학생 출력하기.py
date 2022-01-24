a= {'홍길동': 95, '이순신': 77}

a = sorted(a.items(), key=lambda item: (-item[1], item[0]))
print(a)