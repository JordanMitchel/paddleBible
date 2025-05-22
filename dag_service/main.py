import subprocess

def start_airflow():
    """
    Starts Airflow scheduler and webserver.
    """
    print("🚀 Starting Airflow services...")

    # Initialize the database
    subprocess.run(["airflow", "db", "init"], check=True)

    # Start the scheduler
    subprocess.Popen(["airflow", "scheduler"])

    # Start the webserver
    subprocess.run(["airflow", "webserver", "--port", "8080"], check=True)

if __name__ == "__main__":
    start_airflow()
