dates = {'1400-01-12': 'start', '1400-01-14': 'stop', '1400-02-07': 'start', '1400-02-11': 'stop', '1400-11-16': 'start', '1400-11-23': 'stop',
         '1400-11-26': 'start', '1400-12-02': 'stop', '1400-12-13': 'start', '1401-02-04': 'stop', '1401-06-02': 'start', '1401-08-05': 'stop', '1401-11-30': 'start'}


def place(dates, date, status):
    if dates.get(date) == None:
        dates.update({date: status})
        keys = sorted(dates.keys())
        dates_new = {}
        for i in keys:
            dates_new.update({i: dates[i]})
        if keys[0] == date:
            dates_new.pop(date)
            return dates_new
        if status == 'start':
            if dates_new[keys[keys.index(date) - 1]] == 'start':
                dates_new.pop(date)
                return dates_new
            else:
                dates_new.pop(keys[keys.index(date) + 1])
                return dates_new
        else:
            if dates_new[keys[keys.index(date) + 1]] == 'stop':
                dates_new.pop(keys[keys.index(date) + 1])
                return dates_new
            else:
                dates_new.pop(date)
                return dates_new
    else:
        keys = sorted(dates.keys())
        if keys[0] == date:
            return dates
        else:
            if dates[date] == status:
                return dates
            else:
                if keys[-1] == date:
                    dates.pop(date)
                    return dates
                else:
                    dates.pop(keys[keys.index(date) + 1])
                    dates.pop(date)
                return dates


print(place(dates, '1400-01-01', 'stop'))
