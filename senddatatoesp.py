import requests
import time
import re
import portalocker

def send_request(url):
    try:
        response = requests.get(url,timeout=2)
        print(f"Request sent to {url}, Response: {response.status_code}")
    except:
        print("ERROR")

def process_file(filename):


    try:
        lines_to_keep = []
        with open(filename, 'r') as file:
##            portalocker.lock(file, portalocker.LOCK_SH)
            for line in file:
                line = line.strip()
                match = re.match(r'^(\d+):(http.+)$', line)
                if match:
                    delay = int(match.group(1))
                    original_url = match.group(2)
                    ip_address = "192.168.137.122"  # Replace this with your variable IP address
                    # Split the URL into parts
                    parts = original_url.split("//")
                    if len(parts) >= 2:
                        scheme = parts[0] + "//"
                        url_without_scheme = parts[1]
                        # Split the URL without the scheme by "/"
                        url_parts = url_without_scheme.split("/")
                        if len(url_parts) >= 2:
                            host_and_path = url_parts[0]
                            rest_of_url = "/".join(url_parts[1:])
                            # Replace the IP address
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
##            portalocker.lock(file, portalocker.LOCK_EX)
            for line in lines_to_keep:
                file.write(line + '\n')
    except KeyboardInterrupt:
            print("Keyboard interrupt detected. Stopping the process.")



            

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
