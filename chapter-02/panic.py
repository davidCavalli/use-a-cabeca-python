phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

on = 'on tap'
for word in phrase:
    if word not in on:
        plist.remove(word)
plist.remove(' ')
plist.pop()
plist.insert(2, ' ')
plist.insert(4, plist.pop())

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
