import os

#os.mkdir('hello')

#os.rmdir('hello')

#os.rename('bg2.gif', 'bg22.gif')

#if os.path.exists()

#filename = 'text101.txt'
banned_words = []

def get_words(filename):
    with open(filename, encoding='utf-8') as file:
        text = file.read()
        text = text.replace('\n', ' ')
        charbanned = [',', '.', '!', '?', '-', ';']
        for c in charbanned:
            text = text.replace(c,'')
        #text = text.replace('!', '')
        text.lower()
        words = text.split()
        #words.sort()
        return words

def get_words_dict(words, banned_words):
    word_dict = dict()


    for word in words:
        if word not in banned_words:
            if word in word_dict:
                word_dict[word] = word_dict[word] + 1
            else:
                word_dict[word] = 1

    return word_dict

def main():
    filename = input('enter file path: ')
    if not os.path.exists(filename):
        print('file not find')
    else:
        words = get_words(filename)
        words_dict = get_words_dict(words, banned_words)
        print(f'Count words = {len(words)}')
        print(f'count uq words = {len(words_dict)}')
        print('All wword: ')
        for word in words_dict:
            print(word.ljust(20), words_dict[word])


if __name__ == '__main__':
    main()


