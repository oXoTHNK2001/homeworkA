from datetime import date, timedelta

def capitan(data, notes):
    t = timedelta(days=1)
    i = open("capitan.txt", "w")
    for note in notes:
        i.write(str(data) + ': ' +  note + '\n')
        data += t
    i.close()

(capitan(date(1790, 11, 14), [ "корабль тонет ", "я утонул, прощайте "]))
