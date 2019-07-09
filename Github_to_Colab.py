import appex
import webbrowser
from urllib.parse import urlparse

COLAB_URL = 'https://colab.research.google.com/github'


def main():
	if not appex.is_running_extension():
		print('This script is intended to be run from the sharing extension.')
		return
	else:
		url = appex.get_url()
	
	if url:
		parsed_url = urlparse(url)
		new_url = COLAB_URL + parsed_url.path
		webbrowser.open_new_tab(new_url)
	else:
		print('No input URL found.')

if __name__ == '__main__':
	main()
