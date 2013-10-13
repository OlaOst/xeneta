Simple webapp for uploading files and displaying 20 most common words of chosen file.
Useful for testing purposes only - do NOT deploy in a production environment!

How to run:

1. Have python 2.7
2. Install bottle python web framework ('pip install bottle' or 'easy_install -U bottle')
3. git clone https://github.com/OlaOst/xeneta.git to a directory of your choosing
4. cd to directory_of_your_choosing/webapp
5. Run python main.py

That's it... hopefully


Known issues:
* Uploading a file with the same name as an already uploaded file will overwrite the original file.
* Unicode support is lacking - non-ascii characters will split words and will not be shown.
* Files uploaded in encodings other than ANSI or UTF-8 will probably not work.
* There are no checks on the size of uploaded files.