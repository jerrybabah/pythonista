import appex
import clipboard
from googletrans import Translator


def translate():
	if not appex.is_running_extension():
		print('Pythonista 앱에서 실행됐습니다. 테스트 데이터를 이용합니다.\n')
		text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
	else:
		# 드래그해서 선택했거나 복사한 문장(단어)이 사용된다.
		text = appex.get_text() or clipboard.get()
		
		if text:
			print(f'<입력된 텍스트>\n{text}')
			
			translation = Translator().translate(text, dest='ko')
			print('\n')
			print(f'<번역한 결과>\n{translation.text}')
		
		else:
			print('입력된 텍스트가 없습니다.\n번역할 문장을 드래그 선택하거나 복사한 후 이용하세요')


if __name__ == '__main__':
	translate()
