import time
from datetime import timedelta
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please enter any of the following options'chicago, new york city, or washington': ").lower()

        if city not in CITY_DATA:
            print("'It looks like you entered another city name that is not present in the previous options'\n \nRe-input the city name from the available options correctly  ")
            continue

        else:
            break
    


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter any of the months from 'january to june' or enter 'all' to display them all: ").lower()

        months = ['january','february','march','april','may','june']

        if month != "all" and month not in months:
            print("'It looks like you entered a month other than any of the requested months or all'\n \n'Re-input any of the months from the available options correctly'")
            continue

        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter any day of the week name or enter 'all' to display them all: ").lower()

        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday' ]

        if day != "all" and day not in days:
            print("'It looks like you entered something wrong other than any of the days of the week or all'\n \n'Re-input correctly from the available options'")
            continue

        else:
            break


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    # extract month and day of week from Start Time to create new 
    df['month'] = df['Start Time'].dt.strftime("%b") # extract month from Start Time to create new columns
    
    df['day_of_week'] = df['Start Time'].dt.strftime("%A") # extract day of week Start Time to create new columns
    
    # filter by month if applicable
    if month != 'all':

        # filter by month to create the new dataframe
        df = df[df['month'] == month[0:3].title()]


    # filter by day of week if applicable            
    if day != 'all':

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df

    
    

def row_data(df):

    df_sli = 0
    answer = input("Would you like to see the first five raw data? Yes/No: ").title()

    while True:
        if answer == "Yes" or answer == "Y":
            print(df[df_sli:df_sli+5])
            answer = input("Would you like to see the next five raw data? Yes/No: ").title()
            df_sli += 5
            continue
              
        else:
            break

            


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    co_month = df['month'].mode()[0]
    print('Most Frequent Month: {}'.format(co_month))


    # TO DO: display the most common day of week
    co_weekday = df['day_of_week'].mode()[0]
    print('\nMost Frequent Day of Week: {}'.format(co_weekday))


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    co_hour = df['hour'].mode()[0]
    print('\nMost Frequent Start Hour: {}'.format(co_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    co_st = df['Start Station'].mode()[0]
    print('Most Used Start Station: {}'.format(co_st))


    # TO DO: display most commonly used end station
    co_et = df['End Station'].mode()[0]
    print('\nMost Used End Station: {}'.format(co_et))


    # TO DO: display most frequent combination of start station and end station trip
    st_en = (df["Start Station"]+ " And " + df["End Station"]).mode()[0]
    print("\nMost Frequent Combination of Start Station and End Station Trip: {}".format(st_en))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = int(df["Trip Duration"].sum())
    print("Total Travel Time: {}".format(timedelta(seconds= total_time)))


    # TO DO: display mean travel time
    mean_travel = int(df["Trip Duration"].mean())
    print("\nMean Travel Time : {}".format(timedelta(seconds= mean_travel)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user = df["User Type"].value_counts()
    print("Counts Of User Types:\n{}".format(count_user))


    # TO DO: Display counts of gender
    if "Gender" in df:
        count_gen = df["Gender"].value_counts()
        print("\nCounts Of Gender:\n{}".format(count_gen))

    else:
        print("\nThis file does not contain a column for 'Gender' data")

    
    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        ear_birth = int(df["Birth Year"].min())
        print("\nThe Earliest of Year Birth: {}".format(ear_birth))

        rec_birth = int(df["Birth Year"].max())
        print("\nThe Recent of Year Birth: {}".format(rec_birth))

        com_birth = int(df["Birth Year"].mode()[0])
        print("\nThe Common of Year Birth: {}".format(com_birth))

    else:
        print("\nThis file does not contain a column for 'Birth Year' data")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        row_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
