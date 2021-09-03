a = int(input('Jumlah : '))
print("Contoh 1 0 Menu_1")
menu_list = []
for i in range(a):
    menu = input('Input Menu : ')
    menu = menu.split()
    menu_list.append(menu)
for i in menu_list:
    if i[1]=='0':
        print(i[2].replace('_',' '))
        for b in menu_list:
            if b[1] == i[0]:
                print('.....', b[2].replace('_', ' '))
                for c in menu_list:
                    if c[1] == b[0]:
                        print('..........', c[2].replace('_',' '))