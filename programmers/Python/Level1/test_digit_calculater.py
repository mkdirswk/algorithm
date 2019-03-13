# month : 총 기간, plus : 증감액, first : 초기금액, rate : 이자율, WMtest : 주중 or 월중입금

month = 24
plus = 1000
first = 1000
rate = 3.5
WMtest = 'w'


def answer(month, plus, first, rate, WMtest):

    total = first
    count = 0
    if WMtest == 'w':
        count = 4
    elif WMtest == 'm':
        count = 1
    for i in range(month * count):
        total += (plus * (i + 1))

    total = total * ((100 + rate) / 100)

    return total


print(answer(month, plus, first, rate, WMtest))