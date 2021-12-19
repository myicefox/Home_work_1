time = int(input('duration'))
d, h, m , s = time // 86400 ,time // 3600 % 24 ,time // 60 % 60 , time % 60
print(f'{d} days {h} hour {m} min {s} sec')
