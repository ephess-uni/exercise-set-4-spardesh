""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
    events = []  # Initialize an empty list to store shutdown events    
    # Open the log file for reading
    with open(logfile, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Check if the line contains "Shutdown initiated"
            if "Shutdown initiated" in line:
                # If so, append it to the list after stripping any leading or trailing spaces
                events.append(line.strip())  
    
    return events  # Return the list of shutdown events


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
