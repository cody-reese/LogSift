def parse_logs(raw_logs):
    parsed_logs = []
    for log in raw_logs:
        parsed_logs.extend(log.splitlines())
    return parsed_logs