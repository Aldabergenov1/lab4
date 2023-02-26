import datetime

without_micro_sec = datetime.datetime.today().replace(microsecond=0)

print(without_micro_sec)