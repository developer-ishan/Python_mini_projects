#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip,sys

if len(sys.argv) < 2:
    bullet = '*'
else:
    bullet = sys.argv[1]

text=pyperclip.paste()

lines=text.split('\n')
for i in range(len(lines)):
    lines[i] = bullet + " " + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)
