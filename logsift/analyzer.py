def analyze_logs(logs):
    security_events = []
    for log in logs:
        if "ERROR" in log or "UNAUTHORIZED" in log:
            security_events.append(log + '\n')
    return security_events