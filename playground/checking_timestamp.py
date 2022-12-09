import datetime

created_at = "2022-11-26T18:20:33+0000"

created_at_new = datetime.datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S%z")


print(created_at_new)
