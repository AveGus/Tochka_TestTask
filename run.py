import json


def check_capacity(max_capacity: int, guests: list) -> bool:
    guest_event = []
    for guest in guests:
        check_in = guest["check-in"]
        check_out = guest["check-out"]
        guest_event.append((check_in, 1))
        guest_event.append((check_out, -1))
    guest_event.sort(key=sort_key)

    current_guests = 0
    for event in guest_event:
        current_guests += event[1]
        if current_guests > max_capacity:
            return False
    return True

def sort_key(event: tuple[int, int]) -> tuple[int, int]:
    date, change = event
    return date, change

if __name__ == "__main__":
    # Чтение входных данных
    max_capacity = int(input())
    n = int(input())


    guests = []
    for _ in range(n):
        guest_json = input()
        guest_data = json.loads(guest_json)
        guests.append(guest_data)


    result = check_capacity(max_capacity, guests)
    print(result)