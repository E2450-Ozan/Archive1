def convertMilsec(milliseconds):
    sec = milliseconds // 1000
    min = sec // 60
    sec = sec % 60
    hour = min // 60
    min = min % 60
    return f'{hour} hour(s)'*(hour != 0) + f' {min} minute(s)'*(min != 0) + f' {sec} second(s)' *(sec != 0) or f'{milliseconds} millisecond(s)' * (milliseconds < 1000)
print(convertMilsec(45))