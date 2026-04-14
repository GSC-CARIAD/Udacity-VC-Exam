import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
months = ['january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('> Enter the data you are interested in:')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("Please enter the city (one of: Chicago, New York City, Washington): ")
            city = city.lower()
            # city = CITY_DATA.get(city_str)
            if city not in CITY_DATA:
                print("City '{}' is unknown! Allowed are: {}".format(city, list(CITY_DATA.keys()) ))
            else:
                break
        except KeyboardInterrupt:
            return

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            prompt = "Please enter the month (either 'all' or 'January' .. 'June'): "
            month = input(prompt)
            month = month.lower()
            if (month in months) or (month.lower() == 'all'):
                break
            else:
                print("Month '{}' is invalid! Allowed are: 'all' or {}".format(month, months))
        except KeyboardInterrupt:
            return
        except Exception as e:
            print(e)
            print("Month '{}' is unknown! Allowed are: {}".format(month, months ))

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            weekday_str = input("Please enter the day of the week (either 'all' or 'Monday' ... 'Sunday'): ")
            weekday_str = weekday_str.title()
            if (weekday_str not in days_of_week) and (weekday_str.lower() != 'all'):
                print("Weekday '{}' is invalid! Allowed are: 'all' or {}".format(weekday_str, days_of_week))
            else:
                day = weekday_str
                break
        except KeyboardInterrupt:
            return

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
