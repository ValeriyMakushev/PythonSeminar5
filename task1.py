# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = 'Напишите абв напиабв програбвмму программуабв, удаляющую из \
    этого абв текста все вабвс слова, содерабващие содержащие "абв"'
def del_some_words(text):
    text = list(filter(lambda x : 'абв' not in x, text.split() ))
    return " ". join(text)

text = del_some_words(text)
print(text)