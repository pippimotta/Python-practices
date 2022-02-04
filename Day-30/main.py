try: #可能會出錯的statement
    file = open('a_file.txt')
    dic ={'key':'value'}
    print(dic['qwert'])
except FileNotFoundError:
    file = open('a_file.txt','w')
    file.write('something')
except KeyError as error_message:
    print(f'The key{error_message} does not exist.')

else:
    content = file.read()
    print(content)

finally:
    raise TypeError('Hi')