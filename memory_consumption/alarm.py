import subprocess, time, requests

def check_memory() -> float:
    output = subprocess.check_output(["free", "-m"])
    output = output.decode('utf-8')
    output_lines = output.split('\n')
    memory_info = output_lines[1].split()

    total_memory = int(memory_info[1])
    used_memory = int(memory_info[2])
    free_memory = int(memory_info[3])
    print(total_memory, used_memory, free_memory)

    return (used_memory / total_memory) * 100

if __name__ == "__main__":
    while True:
        memory_percent = check_memory()
        if memory_percent > 90:
            requests.post(
                "http://127.0.0.1:8080/create", 
                headers={"Content-Type": "application/json"}, 
                data=json.dumps({"message": "High memory usage detected"}),
            )
        time.sleep(5)

