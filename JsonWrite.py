import json  # list, dict, str, int, float, bool

d={"name":"Jean", "values":[56,78,89], "flag": True}

import datetime as dt

today=dt.date.today()
# # print(today)

d={"name":"Jean", "values":[56,78,89], "flag": True, "today": today}

# print(d)

with open("data.json", "w") as f:
    json.dump(d, f)