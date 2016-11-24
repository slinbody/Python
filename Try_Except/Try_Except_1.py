#!/usr/bin/python3
while True:
    try:
        input = int(input("輸入整數:"))
        print('{0} is {1}'.format(input,'奇數' if input % 2 else '偶數'))
        del input
    except ValueError:
        print('請輸入數字')
    else:
        print("else:沒錯,我才執行")
    finally:
        print("finally我最後一定會執行")
