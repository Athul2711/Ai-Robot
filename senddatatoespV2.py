import requests
import time
import re
import portalocker
import errno

def send_request(url):
    try:
        response = requests.get(url, timeout=2)
        print(f"Request sent to {url}, Response: {response.status_code}")
    except Exception as e:
        print(f"ERROR: {e}")

def process_file(filename):
    max_retries = 3
    retry_delay = 1  # in seconds
    unlock_delay = 2  # in seconds

    for attempt in range(max_retries):
        try:
            lines_to_keep = []
            with open(filename, 'r') as file:
                portalocker.lock(file, portalocker.LOCK_SH)
                for line in file:
                    line = line.strip()
                    match = re.match(r'^(\d+):(http.+)$', line)
                    if match:
                        delay = int(match.group(1))
                        original_url = match.group(2)
                        ip_address = "192.168.137.140"  # Replace this with your variable IP address
                        parts = original_url.split("//")
                        if len(parts) >= 2:
                            scheme = parts[0] + "//"
                            url_without_scheme = parts[1]
                            url_parts = url_without_scheme.split("/")
                            if len(url_parts) >= 2:
                                host_and_path = url_parts[0]
                                rest_of_url = "/".join(url_parts[1:])
                                modified_url = f"{scheme}{ip_address}/{rest_of_url}"
                                print(f"Original URL: {original_url}")
                                print(f"Modified URL: {modified_url}")
                                print(f"Waiting for {delay} milliseconds before sending request to {modified_url}")
                                time.sleep(delay / 1000)
                                send_request(modified_url)
                            else:
                                print(f"Skipping line: {line} - URL format error")
                                lines_to_keep.append(line)
                        else:
                            print(f"Skipping line: {line} - URL format error")
                            lines_to_keep.append(line)
                    else:
                        print(f"Skipping line: {line} - Incorrect format")
                        lines_to_keep.append(line)

            with open(filename, 'w') as file:
                portalocker.lock(file, portalocker.LOCK_EX)
                for line in lines_to_keep:
                    file.write(line + '\n')
            time.sleep(unlock_delay)  # Add delay to unlock the file before the next iteration
            break  # If the file processing was successful, break out of the retry loop
        except IOError as e:
            if e.errno == errno.EACCES:
                print("Permission denied. Retrying...")
                time.sleep(retry_delay)
            else:
                print(f"Error: {e}")
                break
        except KeyboardInterrupt:
            print("Keyboard interrupt detected. Stopping the process.")
            break


def main():
    filename = "requests.txt"  # Change this to your file name
    while True:
        try:
            process_file(filename)
        except KeyboardInterrupt:
            print("Keyboard interrupt detected. Stopping the process.")
            break


if __name__ == "__main__":
    main()
