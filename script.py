import json
import re

to_js = []

with open('/proc/mounts', 'r') as mo: 
    for n, line in enumerate(mo, 1): # Читаем файл построчно
        line = line.rstrip('\n')
        line = re.split(r' ', line) # Делим строку по пробелам
        line[3] = re.sub(r'rw\S+', 'rw', line[3]) # после прав доступа через запятую идет то, что нам не нужно, удаляем
        line[3] = re.sub(r'ro\S+', 'ro', line[3])
        tmp_dict = {'FSNAME': f'{line[0]}', 'FSTYPE': f'{line[2]}', 'PERMISSION': f'{line[3]}'}
        to_js.append(tmp_dict)

to_js = json.dumps(to_js) # Преобразуем к JSON


        