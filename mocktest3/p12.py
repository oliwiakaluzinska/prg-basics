def f(dates):
    import re
    result = []
    dates = dates.split(',')
    pattern = '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'
    for i in dates:
        if re.match(pattern, i):
            result.append(i)

    return result

if __name__ == "__main__":
    dates = "2021-1-3,05/12/2024,1998-12-11,9 maj 2007,2001-12-07,15-09-2011"
    print(f(dates))