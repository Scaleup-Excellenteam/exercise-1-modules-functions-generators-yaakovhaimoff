import random
import datetime


def main():
    '''
    5.1 I dont have vinaigrette
    '''
    start_date = datetime.date(1912, 6, 23)
    end_date = datetime.date(1954, 6, 7)

    # gets the difference of days between both dates
    delta = end_date - start_date

    # getting a random amount of days to add to the start date
    random_date = start_date + datetime.timedelta(days=random.randint(0, delta.days))

    # Check if the random date falls on a Monday
    if random_date.weekday() == 0:
        print(f'The random date {random_date} falls on a Monday, I dont have vinaigrette :(')
    else:
        print(f'The random date {random_date} does not fall on a Monday, I have vinaigrette :)')


if __name__ == '__main__':
    main()
