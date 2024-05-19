def generate_report(security_events, report_file):
    with open(report_file, 'w') as f:
        for event in security_events:
            f.write(f"{event}\n")