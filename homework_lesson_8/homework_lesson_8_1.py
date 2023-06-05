converting_dict = {"days": 0, "hours": 0, "minutes": 0, "seconds": 0}

# if __name__ == "__main__":
# pass

HOUR_IN_DAY = 24
MIN_IN_DAY = 1440
SEC_IN_DAY = 86400
MIN_IN_HOUR = 60
SEC_IN_HOUR = 3600
SEC_IN_MIN = 60

sec = int(input("Enter value in seconds: "))

days = divmod(sec, SEC_IN_DAY)
hours = divmod(sec, SEC_IN_HOUR)
minutes = divmod(sec, SEC_IN_MIN)
seconds = minutes[1]
print(days, hours, minutes, seconds)
print(converting_dict)
