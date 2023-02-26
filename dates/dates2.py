import datetime

yesterday = datetime.datetime.today() - datetime.timedelta(days = 1)
today = datetime.datetime.today()
tomorrow = datetime.datetime.today() + datetime.timedelta(days = 1)

print("Yesturday:", yesterday, "Today:", today, "Tomorrow:", tomorrow, sep = "\n")