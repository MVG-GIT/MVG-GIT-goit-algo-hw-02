from collections import deque

def is_palindrome(string):
    cleaned = ''.join(ch.lower() for ch in string if ch.isalnum())    
    dq = deque(cleaned)
    
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


def is_palindrome_pretty(string):
    result = is_palindrome(string)
    return f'"{string}" is {"a palindrome" if result else "not a palindrome"}.'
