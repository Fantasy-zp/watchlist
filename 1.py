from turtle import title


print(len('大萨达'))


title = '3'
year = '3'
print(title == None)
if not title or not year or len(year) != 4 or len(title) > 60:
    print('Invalid input.')  # 显示错误提示
else:
    print("good!")

if title:
    print(True)
