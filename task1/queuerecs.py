import queue

class RequestQueue():
    def __init__(self, request_queue=queue.Queue()):
        self.req_queue = request_queue

    def generate_request(self, request_id):
        request = f"Req{request_id}"
        self.req_queue.put(request)
        print(f'New request "{request}"!')
        return request_id + 1

    def process_request(self):
        if not self.req_queue.empty():
            request = self.req_queue.get()
            print(f'Processing request "{request}"...')
        else:
            print("The queue is empty.")
