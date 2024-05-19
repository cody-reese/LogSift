def analyze_logs(parsed_logs):
    security_events = []
    for log in parsed_logs:
        if "ERROR" in log or "UNAUTHORIZED" in log:
            security_events.append(log)
    return security_events