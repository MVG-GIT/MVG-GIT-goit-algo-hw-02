from queuerecs import RequestQueue

request_queue = RequestQueue()
request_id = 0

while True:
    action = input("| Options: \n| 'g' - generate a request\n| 'p' - process a request\n| 'q' - to exit\nInput: ").lower()
    if action == 'g':
        request_id = request_queue.generate_request(request_id)
    elif action == 'p':
        request_queue.process_request()
    elif action == 'q':
        print("Goodbye!")
        break
    else:
        print("Unknown input. Try again?")
