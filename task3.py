import re
import os
import sys

def parse_log_line(line: str) -> dict:
    match = re.match(r"(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})\s+(\w+)\s+(.+)", line)
    if match:
        return {
            "date": match.group(1),
            "time": match.group(2),
            "level": match.group(3),
            "message": match.group(4)
        }

def load_logs(file_path: str) -> list:
    if os.path.exists(file_path):
        with open(file_path, "r") as fin:
            return [line.strip("\n") for line in fin.readlines()]
    return []

def filter_logs_by_level(logs: list, level: str) -> list:
    filt_ = []
    for log in logs:
        log_dict = parse_log_line(log)
        if log_dict and log_dict["level"] == level:
            filt_.append(log_dict)
    return filt_

def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        log_dict = parse_log_line(log)
        if log_dict:
            level = log_dict["level"]
            counts[level] = counts.get(level, 0) + 1
    return counts

def display_log_counts(counts: dict):
    print(f"{'Log Level':<10}|{'Count':<10}")
    print("-" * 10 + "|" + "-" * 10)
    for level, count in counts.items():
        print(f"{level:<10}| {count:<10}")

args = sys.argv[1:]
if len(args) >= 1:
    file_path = args[0]
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(args) == 2:
        level = args[1]
        print(f"\nFiltered Logs for {level} level:")
        logs = load_logs(file_path)
        filtered_logs = filter_logs_by_level(logs, level)
        for log in filtered_logs:
            print(log)
else:
    print("Please provide the log file path as a command-line argument.")