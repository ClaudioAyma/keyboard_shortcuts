import keyboard
import asyncio

with open('keywords.txt') as file:
    txt = file.read()


def split_text(text):
    data = []
    text = text.split('----')
    for i in text:
        if i != '':
            data.append(i)
    return data


def app(text):
    items = []
    data = split_text(text)
    for item in data:
        items.append(get_key_text(item))

    for item in items:
        keyboard.add_abbreviation(item[0], item[1])
        print('key: {}\ntext: {}'.format(item[0], item[1]))


def get_key_text(item):
    list_item = item.strip('\n').split('\n')
    key = list_item[0]
    _text = list_item[1:]
    text = ''
    for line in _text:
        text += line + '\n'
    return [key, text]


app(txt)


loop = asyncio.get_event_loop()
try:
    loop.run_forever()
finally:
    loop.close()

