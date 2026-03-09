# Port-Scanner

A multi-threaded TCP port scanner built in Python using socket programming to detect open ports and services.

## Overview

This tool scans a target IP address for open ports across the most commonly used TCP ports. It uses Python's `concurrent.futures` module to run scans in parallel, making it faster.

## Features

- Multi-threaded scanning using `ThreadPoolExecutor`
- Scans 12 of the most common TCP ports
- Displays scan start and end timestamps
- Clean output
- 
## Usage

```bash
python port_scanner.py
```

You will be prompted to enter a target IP address:

```
Enter target IP address: 192.168.1.1
```

## Example Output

```
Scanning target: 192.168.1.1
Scanning started at: 2026-03-09 10:00:00
--------------------------------------------------
[OPEN] Port 22
[OPEN] Port 80
[OPEN] Port 443
--------------------------------------------------
Scan complete at: 2026-03-09 10:00:03
```

## Ports Scanned

| Port | Service |
|------|---------|
| 21   | FTP     |
| 22   | SSH     |
| 23   | Telnet  |
| 25   | SMTP    |
| 53   | DNS     |
| 80   | HTTP    |
| 110  | POP3    |
| 139  | NetBIOS |
| 143  | IMAP    |
| 443  | HTTPS   |
| 445  | SMB     |
| 3389 | RDP     |

## Disclaimer

This tool is intended for educational purposes and authorised network testing only. Do not use it against systems you do not have explicit permission to scan. Unauthorised port scanning may be illegal in your jurisdiction.
