def parse_logs(raw_logs):
    parsed_logs = []
    for raw_log in raw_logs:
        # add additional parsing logic
        # add regexes to organize each line
        parsed_log = raw_log.strip()
        parsed_logs.append(parsed_log)
    return parsed_logs