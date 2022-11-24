phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

new_phrase = plist[1:3] + plist[-7:-9:-1] + plist[-5:-7:-1]

new_phrase = ''.join(new_phrase)
print(plist)
print(new_phrase)
