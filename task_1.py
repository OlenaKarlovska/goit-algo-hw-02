import queue
import time
import random

requests_queue = queue.Queue()
request_id = 0
def generate_request():
    global request_id
    request_id += 1
    request = f"Заявка №{request_id}"
    requests_queue.put(request)
    print(f"Створено {request}")
def process_request():
    if not requests_queue.empty():
        request = requests_queue.get()
        print(f"[Обробляється {request}")
    else:
        print("Черга пуста, заявок немає")
try:
    while True:
        if random.choice([True, False]):
            generate_request()
        process_request()
        time.sleep(1)
except KeyboardInterrupt:
    print("\n[!] Програма завершена користувачем")