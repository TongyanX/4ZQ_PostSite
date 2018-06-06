import json
from datetime import datetime


GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id = 0


def init():
    global entries, next_id
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
        for entry in entries:
            if entry["id"] > next_id:
                next_id = entry["id"] + 1
    except:
        print('Couldn\'t open', GUESTBOOK_ENTRIES_FILE)
        entries = []


def get_entries():
    global entries
    return entries


def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    entry = {"author": name, "text": text, "timestamp": time_string, "id": next_id}
    entries.insert(0, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
        next_id += 1
    except:
        print("ERROR! Could not write entries to file.")


def delete_entry(post_id):
    """?"""
    global entries, GUESTBOOK_ENTRIES_FILE
    for entry in entries:
        if entry["id"] == int(post_id):
            entries.remove(entry)
            break
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except ValueError:
        print("ERROR! Could not write entries to file.")


def edit_entry(post_id, message):
    """?"""
    global entries, GUESTBOOK_ENTRIES_FILE
    for entry in entries:
        if entry["id"] == int(post_id):
            entry["text"] = message
            now = datetime.now()
            time_string = now.strftime("%b %d, %Y %-I:%M %p")
            entry["timestamp"] = time_string
            break
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except ValueError:
        print("ERROR! Could not write entries to file.")
