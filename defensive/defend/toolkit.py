from logMonitor import monitor_log
from alert import send_message

def main():
    
    results = monitor_log()

    send_message(results)

main()