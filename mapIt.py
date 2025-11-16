import webbrowser, sys, pyperclip

print(sys.argv)

print(len(sys.argv))
if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])
else:
    address = pyperclip.paste()
    
webbrowser.open('https://www.google.com/maps/place/' + address)