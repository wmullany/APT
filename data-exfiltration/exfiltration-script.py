import time

def exfiltrate_data():
    sensitive_data = "This is sensitive data."
    print(f"Exfiltrating data: {sensitive_data}")
    time.sleep(2)  # Simulate time taken for exfiltration
    print("Data exfiltration complete.")

if __name__ == "__main__":
    exfiltrate_data()
