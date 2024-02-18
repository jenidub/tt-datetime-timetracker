import csv
import utils
import datetime
from dateutil.relativedelta import *

def start_tracking(client, description):
    print(f"Start tracking {description} for {client}")

    # TODO: Grab the current time and store it as a string in start_time
    # in the format: HH:MM(AM/PM) YYYY-MM-DD
    # for example: 09:40AM 2023-08-11
    
    now = datetime.datetime.now()
    format_string = "%I:%M%p %Y-%m-%d"
    start_time = now.strftime(format_string)

    # Code to append a new job to the CSV
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', lineterminator='')
        writer.writerow([client, description, start_time, ''])


def stop_tracking():
    print("Stopping tracking")

    # TODO: Grab the current time and store it as a string in end_time
    # in the format: HH:MM(AM/PM) YYYY-MM-DD
    # for example: 09:40AM 2023-08-11

    now = datetime.datetime.now()
    format_string = "%I:%M%p %Y-%m-%d"
    end_time = now.strftime(format_string)

    # Code to append a new job to the CSV
    with open('data.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([end_time])


def display_all_totals(client):
    print(f"Calculating time spent on all jobs for {client}...")
    client_jobs = utils.get_by_client(client)

    # references
    total = relativedelta()
    format_string = "%I:%M%p %Y-%m-%d"

    #function instructions
    print(client)
    for entry in client_jobs:
        start_time = entry["start_time"]
        end_time = entry["end_time"]

        start_time_dt = datetime.datetime.strptime(start_time, format_string)
        end_time_dt = datetime.datetime.strptime(end_time, format_string)
        duration = relativedelta(end_time_dt, start_time_dt)

        print(f"{entry["description"]} - {duration.hours} hours {duration.minutes} minutes")
        total += duration
    
    print(f"TOTAL FOR {client}: {total.hours} hours {total.minutes} minutes")


def display_range_totals(client, dates_str_list):
    print(f"Calculating time spent on jobs for {client} in the specified range...")
    client_jobs = utils.get_by_client(client)

    # dates_str_list contains 2 date strings in the format YYYY-MM-DD
    # TODO: turn the two date strings in dates_str_list to datetime objects and store in range_start_dt and range_end_dt
    format_string_range = "%Y-%m-%d"
    range_start_dt = datetime.datetime.strptime(dates_str_list[0], format_string_range)
    range_end_dt = datetime.datetime.strptime(dates_str_list[1], format_string_range) + relativedelta(hours=23, minutes=59)

    # TODO: filter client_jobs to only include those within the start and end datetimes
    format_string_check = "%I:%M%p %Y-%m-%d"
    total = relativedelta()

    for entry in client_jobs:
        entry_start_time = datetime.datetime.strptime(entry["start_time"], format_string_check)
        entry_end_time = datetime.datetime.strptime(entry["end_time"], format_string_check)

        if range_end_dt >= entry_end_time >= range_start_dt:
            duration = relativedelta(entry_end_time, entry_start_time)
            print(f"{entry["description"]} - {duration.hours} hours {duration.minutes} minutes")
            total += duration
    
    # TODO: List out all the different jobs, and then a total time spent - just like display_all_totals
    print(f"\nTOTAL FOR {client} in the given date range {dates_str_list[0]} to {dates_str_list[1]}:")
    print(f"{total.hours} hours {total.minutes} minutes")
    # test string: 2023-09-01 to 2023-09-08
    

def display_x_days_totals(client, days):
    print(f"Calculating time spent on jobs for {client} in the last {days} days...")
    client_jobs = utils.get_by_client(client)

    # TODO: determine the start and end datetimes for this range
    range_end_dt = datetime.datetime.now()
    range_start_dt = range_end_dt - relativedelta(days=days)
    
    format_string_check = "%I:%M%p %Y-%m-%d"
    total = relativedelta()

    # TODO: filter and display client_jobs to only include those with the start and end datetimes
    for entry in client_jobs:
        entry_start_time = datetime.datetime.strptime(entry["start_time"], format_string_check)
        entry_end_time = datetime.datetime.strptime(entry["end_time"], format_string_check)

        if range_end_dt >= entry_end_time >= range_start_dt:
            duration = relativedelta(entry_end_time, entry_start_time)
            print(f"{entry["description"]} - {duration.hours} hours {duration.minutes} minutes")
            total += duration
   
    # TODO: List out all the different jobs, and then a total time spent - just like display_all_totals
    print(f"\nTOTAL FOR {client} in the last {days} days:")
    print(f"{total.hours} hours {total.minutes} minutes")
