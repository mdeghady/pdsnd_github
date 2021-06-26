import time
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
        city = input("Please Enter the city you want (chicago,new york city,washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("\nPlease Enter one of these cities (chicago,new york city,washington)\n")


    # TO DO: get user input for month (all, january, february, ... , june)

    months = ['january', 'february' , 'march', 'april', 'may','june','all']

    while True:
        month = input("Please Enter the month you want(Enter all if you want all months): ").lower()

        if month in months:
            break
        else:
            print("\nmonths of the year are ( january , february ,march ,april,may ,june)  \n please enter one of them or enter all if you want them all\n")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

    while True:
        day = input('Please Enter the day you want(Enter all if you want all days): ').lower()

        if day in days:
            break

        else:
            print("\ndays of the week are  (sunday,monday,tuesday,wednesday,thursday,friday,saturday)\n please enter one of them or enter all if you want them all\n")



    print('-' * 40)
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

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['hour'] = df['Start Time'].dt.hour

    df['month'] = df['Start Time'].dt.month_name()
    df['month'] = df['month'].str.lower()

    df['day'] = df['Start Time'].dt.day_name()
    df['day'] = df['day'].str.lower()

    if month != 'all':
        df = df.loc[df['month'] == month]

    if day != 'all':
        df = df.loc[df['day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_proccesing_time = time.time()

    # TO DO: display the most common month

    if len(df['month'].unique()) != 1:
        most_common_month = df['month'].mode()[0]
        num_of_apperence_of_month = len(df[df['month'] == most_common_month])

        print(f"most common month : {most_common_month}\t counts: {num_of_apperence_of_month}")

    if len(df['day'].unique()) != 1:
        # TO DO: display the most common day of week
        most_common_day = df['day'].mode()[0]
        num_of_apperence_of_day = len(df[df['day'] == most_common_day])

        print(f"most common day : {most_common_day}\t counts: {num_of_apperence_of_day}")

    # TO DO: display the most common start hour

    most_common_hour = df['hour'].mode()[0]
    num_of_apperence_of_hour = len(df[df['hour'] == most_common_hour])

    print(f"most common hour : {most_common_hour}\t counts: {num_of_apperence_of_hour}")

    print("\nThis took %s seconds." % (time.time() - start_proccesing_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_proccesing_time = time.time()

    # TO DO: display most commonly used start station

    most_commonly_used_start_station = df['Start Station'].mode()[0]
    num_of_apperence_of_start_station = len(df[df['Start Station'] == most_commonly_used_start_station])

    print(f"most commonly used start station : {most_commonly_used_start_station}\tcounts : {num_of_apperence_of_start_station}")

    # TO DO: display most commonly used end station

    most_commonly_used_end_station = df['End Station'].mode()[0]
    num_of_apperence_of_end_station = len(df[df['End Station'] == most_commonly_used_end_station])

    print(f"most commonly used end station : {most_commonly_used_end_station}\tcounts : {num_of_apperence_of_end_station}")

    # TO DO: display most frequent combination of start station and end station trip

    combination_of_stations = df['Start Station'] + " to " + df['End Station']
    most_frequent_combination_of_stations = combination_of_stations.mode()[0]
    num_of_combinations = len(combination_of_stations[combination_of_stations == most_frequent_combination_of_stations])

    print(f"most commonly combination of start end stations : {most_frequent_combination_of_stations}\tcounts : {num_of_combinations}")

    print("\nThis took %s seconds." % (time.time() - start_proccesing_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_proccesing_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum()
    days = total_travel_time // 86400
    hours = (total_travel_time % 86400) // 3600
    minutes = (total_travel_time % 86400 % 3600) // 60
    secs = total_travel_time % 86400 % 3600 % 60

    print("The total travel time is {} seconds ; {} days , {} hours, {} minutes & {:.2f} seconds".format(total_travel_time, days, hours, minutes, secs))

    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    print("mean travel time is {:.2f} seconds".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_proccesing_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_proccesing_time = time.time()

    # TO DO: Display counts of user types

    user_type_counts = df['User Type'].value_counts()

    print("User types:")
    for idx, value in zip(user_type_counts.index, user_type_counts):
        print(f"{idx}: {value}")

    # TO DO: Display counts of gender

    try:
        gendre_count = df['Gender'].value_counts()
        print("\nUsers Gender")
        for idx, value in zip(gendre_count.index, gendre_count):
            print(f"{idx}: {value}")
    except KeyError:
        pass

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()
    except KeyError:
        pass

    print("\nThis took %s seconds." % (time.time() - start_proccesing_time))
    print('-' * 40)

def display_data(df):
    first = 0
    last = 4
    showing_data = input("You want to see the data?(y/n)").lower()

    if showing_data =='y':
        while True:
            print(df.iloc[first:last])

            showing_more_data = input("You want to see more data?(y/n)").lower()
            if showing_more_data =='y':
                first += 6
                last +=6
            else:
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
