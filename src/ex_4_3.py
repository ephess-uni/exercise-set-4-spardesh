""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    # Get the list of shutdown events using the get_shutdown_events function
    shutdown_events = get_shutdown_events(logfile)
    
    # Check if there are less than 2 shutdown events, if so, return None
    if len(shutdown_events) < 2:
        return None
    
    # Convert the date fields of the first and last shutdown events to datetime objects
    first_shutdown_time = logstamp_to_datetime(shutdown_events[0].split()[1])
    last_shutdown_time = logstamp_to_datetime(shutdown_events[-1].split()[1])
    
    # Calculate the difference in time between the two events
    time_difference = last_shutdown_time - first_shutdown_time
    
    return time_difference  # Return the resulting timedelta object


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
