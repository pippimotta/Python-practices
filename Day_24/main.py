with open('../../my_file.txt') as file: # ../../連用為向上兩個根目錄
    contents = file.read()
    print(contents)

# with open('new_file.txt', mode='a') as file: #mode改變只讀'r'/寫入'w/增加'a'
#     file.write('I am the king of the world.')
#     print()
