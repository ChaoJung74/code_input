code = 'a1357246'
i = 0
while i < 3:
	code_input = input('請輸入密碼：')
	if code_input == code:
		print('登入成功！')
		break
	elif i < 2:
			times_left = 2 - i
			print('密碼錯誤，還剩下', times_left, '次機會')
			i = i +1
	else:
		print('密碼錯誤，不能再猜了！')
		break
