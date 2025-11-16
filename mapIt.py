import webbrowser, sys, pyperclip

print(sys.argv)

print(len(sys.argv))
if len(sys.argv) > 1:
    profile = ''.join(sys.argv[1:])
else:
    profile = pyperclip.paste()
    
webbrowser.open('https://www.github.com/' + profile)