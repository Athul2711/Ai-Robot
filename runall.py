import multiprocessing
import subprocess

def run_script(script):
    subprocess.run(["python", script], check=True)

if __name__ == "__main__":
    script1 = "senddata.py"  # Replace with the filename of your first script
    script2 = "senddatatoespV2.py"  # Replace with the filename of your second script

    # Create processes for each script
    p1 = multiprocessing.Process(target=run_script, args=(script1,))
    p2 = multiprocessing.Process(target=run_script, args=(script2,))

    try:
        # Start the processes
        p1.start()
        p2.start()

        # Wait for both processes to finish
        p1.join()
        p2.join()
    except KeyboardInterrupt:
        # Terminate both processes if a KeyboardInterrupt is detected
        p1.terminate()
        p2.terminate()
