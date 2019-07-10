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
		
		if parsed_url.hostname == 'github.com':
			path = parsed_url.path
			last_path = path.split("/")[-1]
			
			is_directory = last_path.find(".") == -1
			if not is_directory:
				ext = last_path.split(".")[-1]
			else:
				ext = None
				
			if not is_directory and ext == "ipynb":	
				new_url = COLAB_URL + parsed_url.path
				webbrowser.open_new_tab(new_url)
			else:
				print('This page is directory or not jupyter notebook.')
		else:
			print('This script is intended to be run from github.')
	else:
		print('No input URL found.')

if __name__ == '__main__':
	main()
