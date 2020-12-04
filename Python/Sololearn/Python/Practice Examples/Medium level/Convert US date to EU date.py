months = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}
raw = input()
us_format = list(map(str, raw.split(" ")))
try:
    for (k, v) in months.items():
        if v == str(us_format[0]):
            month = k
            date, year = list(map(str, us_format[1].split(",")))
            print(str(date)+"/"+str(month)+"/"+str(year))
            break
    else:
        raise EOFError
except:
    month, date, year = list(map(str, raw.split("/")))
    print(str(date)+"/"+str(month)+"/"+str(year))
