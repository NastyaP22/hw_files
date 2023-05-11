with open('1.txt', 'rt', encoding='utf-8') as file1, open('2.txt', 'rt', encoding='utf-8') as file2, \
open('3.txt', 'rt', encoding='utf-8') as file3, open('res_file', 'w', encoding='utf-8') as res:
    info = {}
    info['file1'] = len(file1.readlines())
    info['file2'] = len(file2.readlines())
    info['file3'] =len(file3.readlines())
    sorted_values = sorted(info.values())
    sorted_info = {}
    for value in sorted_values:
        for key in info.keys():
            if info[key] == value:
                sorted_info[key] = value
    for file, str_count in sorted_info.items():
        if file == 'file1':
            res.write(file1.name + '\n')
            res.write(str(str_count) + '\n')
            file1.seek(0)
            res.writelines(file1)
            res.write('\n')
        elif file == 'file2':
            res.write(file2.name + '\n')
            res.write(str(str_count) + '\n')
            file2.seek(0)
            res.writelines(file2)
            res.write('\n')
        else:
            res.write(file3.name + '\n')
            res.write(str(str_count) + '\n')
            file3.seek(0)
            res.writelines(file3)
            res.write('\n')
     



        