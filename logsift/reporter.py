import os
from datetime import datetime

def create_report(events):
    # Set report directory path as a subdirectory named "Reports" in the current working directory
    report_directory = os.path.join(os.getcwd(), "Reports")

    # Ensure report directory exists
    if not os.path.exists(report_directory):
        os.makedirs(report_directory)

    # Get current UTC date and time
    current_utc_time = datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S')

    # Construct report file path with UTC date time included
    report_file_name = f"security_report_{current_utc_time}.txt"
    report_file_path = os.path.join(report_directory, report_file_name)

    with open(report_file_path, 'w') as report:
        report.write("Security Report\n")
        for event in events:
            report.write(str(event) + "\n\n")