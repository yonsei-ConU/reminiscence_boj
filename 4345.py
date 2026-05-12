import io, os
from datetime import datetime, timedelta, timezone
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='utf-8')
input_ = reader.readline
sinput = text_reader.readline
def minput(): return map(int, input_().split())


output = []
timezones = {'UTC': (0, 0), 'GMT': (0, 0), 'BST': (1, 0), 'IST': (1, 0), 'WET': (0, 0), 'WEST': (1, 0), 'CET': (1, 0),
             'CEST': (2, 0), 'EET': (2, 0), 'EEST': (3, 0), 'MSK': (3, 0), 'MSD': (4, 0), 'AST': (-4, 0), 'ADT': (-3, 0),
             'NST': (-4, 30), 'NDT': (-3, 30), 'EST': (-5, 0), 'EDT': (-4, 0), 'CST': (-6, 0), 'CDT': (-5, 0),
             'MST': (-7, 0), 'MDT': (-6, 0), 'PST': (-8, 0), 'PDT': (-7, 0), 'HST': (-10, 0), 'AKST': (-9, 0),
             'AKDT': (-8, 0), 'AEST': (10, 0), 'AEDT': (11, 0), 'ACST': (9, 30), 'ACDT': (10, 30), 'AWST': (8, 0)}
for _ in range(int(input_())):
    l = list(sinput().split())
    if len(l) == 3:
        tz1, tz2 = (timezones[i] for i in l[1:])
        if l[0] == 'noon':
            cur_time = datetime(2024, 10, 30, 12, 0, 0, tzinfo=timezone(timedelta(hours=tz1[0], minutes=tz1[1])))
        else:
            assert l[0] == 'midnight'
            cur_time = datetime(2024, 10, 30, 0, 0, 0, tzinfo=timezone(timedelta(hours=tz1[0], minutes=tz1[1])))
    else:
        h, m = map(int, l[0].split(':'))
        if h == 12: h = 0
        tz1, tz2 = (timezones[i] for i in l[2:])
        if l[1] == 'p.m.':
            h += 12
        else:
            assert l[1] == 'a.m.'
        cur_time = datetime(2024, 10, 30, h, m, 0, tzinfo=timezone(timedelta(hours=tz1[0], minutes=tz1[1])))
    converted = cur_time.astimezone(timezone(timedelta(hours=tz2[0], minutes=tz2[1])))
    ah = converted.hour
    am = converted.minute
    if not ah and not am:
        output.append('midnight')
    elif ah == 12 and not am:
        output.append('noon')
    elif not ah:
        output.append(f"12:{am:02} a.m.")
    elif ah < 12:
        output.append(f"{ah}:{am:02} a.m.")
    elif ah == 12:
        output.append(f"12:{am:02} p.m.")
    else:
        output.append(f"{ah - 12}:{am:02} p.m.")

os.write(1, '\n'.join(output).encode())
os._exit(0)
