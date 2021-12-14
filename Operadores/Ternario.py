lockdown = False

grana = 300
status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuuu'

print (status)