def collect_log(file_path):
    # access the file_path object and collect a stream of data
    raw_logs = []

    # attempt to open the file in the supplied file_path
    try:
        with open(file_path, 'r', encoding='utf-8') as log_file:
            raw_logs.append(log_file.read())
    
    # throw and exception if the file doesn't have standard encoding
    except UnicodeDecodeError:
        print(f"Error decoding log file: {file_path}. Skipping...")
        
    return raw_logs