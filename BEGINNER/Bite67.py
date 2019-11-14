from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    days100str = start_100days + timedelta(days = 100)
    return days100str.strftime("%Y-%m-%d")
    

def get_days_between_pb_start_first_joint_pycon():
    daysBetween = pycon_date - pybites_founded
    return daysBetween.days
