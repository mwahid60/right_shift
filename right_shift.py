kumpulan_nama = ['andi', 'budi', 'charlie', 'doni', 'jojo', 'adam']

def shift(list, step):
    i = 0
    x = len(list)
    while True:
        if step == i:
            del list[x:len(list)]
            print(list)
            break
        else:
            list.insert(0,list[(x-1)])
            i += 1

shift(kumpulan_nama,5)