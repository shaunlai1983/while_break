while True:
	mode = input('模式切換:1 ,2, Q:')
	if mode == '1' :      #請記得用 == 判斷不是用 一個 =
		print('Enter Mode 1')
	elif mode == '2':
		print('Enter mode 2')
	elif mode == 'Q':
		print('Quit the program now')
		break
	else :
		print('錯誤!只能輸入1 , 2 , Q')


