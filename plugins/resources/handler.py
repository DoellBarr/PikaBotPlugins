import os
try:
    from pikabot import bot, bot2, bot3, bot4
    i1 = bot.uid
    i2 = bot2.uid
    i3 = bot3.uid
    i4 = bot4.uid

except BaseException:
    pass


def pikaa(a, shortname):
    try:
        AS = os.environ.get(f"{shortname}", None).split('|')
        if a.sender_id == i1:
            return AS[0]
        if a.sender_id == i2:
            return AS[1]
        if a.sender_id == i3:
            return AS[2]
        if a.sender_id == i4:
            return AS[3]
        else:
            pass
    except BaseException:
        pass
