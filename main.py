import os, platform
from logsift import collector, parser, analyzer, reporter

def main():
    log_directory = "/var/log/"
    all_events = []

    # Walk through the directory tree
    for root, dirs, files in os.walk(log_directory):
        for file in files:
            events = []
            file_path = os.path.join(root, file)

            # Collect the contents of the log file
            log = collector.collect_log(file_path)

            # Parse the log into a more readable format
            parsed_log = parser.parse_logs(log)

            # Analyze the parsed log for security events
            events = analyzer.analyze_logs(parsed_log)
            all_events.append(events)
    
    # Generate the security event report
    reporter.create_report(events)        

    print("Security report finished.")

if __name__ == "__main__":
    main()