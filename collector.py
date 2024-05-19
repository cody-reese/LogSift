import os

def collect_logs(log_directory):
    logs = []
    for filename in os.listdir(log_directory):
        if filename.endswith(".log"):
            with open(os.path.join(log_directory, filename), 'r') as f:
                logs.append(f.read())
    return logs