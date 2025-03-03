myfile = 'start.txt'

a = []
with open(myfile, 'r') as s_file, open('finish.txt', 'w') as f_file:
    start_text = s_file.read()
    start_text = start_text.split('\n')
    for i in start_text:
        if ',' in i:
            a.append(i)

    if len(a) > 0:
        last = str(a[-1])
        index_last_comma = start_text.index(last)
        print(index_last_comma)
        #for i in range(len(start_text)):
        #    if start_text[i].strip() == last.strip():
        #        #last_comma = start_text[i]
        #        index_last_comma = i
        #        break

        start_text.insert((index_last_comma + 1), '*******')
        f_file.write('\n'.join(start_text))
    else:
        start_text.insert((len(start_text) + 1), '*******')
        f_file.write('\n'.join(start_text))





