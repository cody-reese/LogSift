# LogSift
Security Log Analysis Tool
Introduction

The Security Log Analysis Tool is a command-line utility designed to gather logs from multiple sources and generate reports on security events. It provides a streamlined way to analyze log data and identify potential security threats within a system or network.
Features

    Log Gathering: Collect logs from various sources including system logs, network logs, application logs, etc.
    Customizable Sources: Configure the tool to gather logs from specific sources based on user-defined criteria.
    Security Event Detection: Analyze log data to detect security events such as unauthorized access attempts, suspicious network activity, etc.
    Report Generation: Generate detailed reports summarizing security events detected during log analysis.
    Easy Integration: Seamlessly integrate the tool into existing security workflows or automation scripts.

# Installation

Clone the repository:

    bash
    
    git clone https://github.com/cody-reese/LogSift.git

Navigate to the project directory:

    bash

    cd LogSift

Install dependencies (if any):

    pip install -r requirements.txt

# Usage

Configure log sources by editing the config.yml file.
Run the tool:

    python logsift.py

    Follow the on-screen prompts to initiate log gathering and analysis.
    View generated reports in the reports directory.

# Configuration

The config.yml file allows users to customize log sources, analysis parameters, output formats, etc. Refer to the comments within the file for detailed instructions on configuration options.
Example

    Create .yml example

# Example configuration file (config.yml)

log_sources:
  - type: syslog
    path: /var/log/syslog
  - type: apache_access
    path: /var/log/apache/access.log
  - type: firewall
    path: /var/log/firewall.log
