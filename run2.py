import sys
import collections


# Константы для символов ключей и дверей
keys_char = [chr(i) for i in range(ord('a'), ord('z') + 1)]
doors_char = [k.upper() for k in keys_char]


def get_input():
    """Чтение данных из стандартного ввода."""

    return [list(line.strip()) for line in sys.stdin]


def solve(data):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] #Все возможные пути куда может пойти робот
    n, m = len(data), len(data[0]) #Размеры лабиринта(n-кол-во строк, m-кол-во столбцов)
    total_keys = set() #Множество всех ключей в лабиринте
    starts = [] #список стратовых координат роботов

    #Пробегаемся по всей карте, если встречаем символ @ то запоминаем его(это позиция робота), если символ ключ то сохраняем его
    for i in range(n):
        for j in range(m):
            char = data[i][j]
            if char == '@':
                starts.append((i, j))
            elif char in keys_char:
                total_keys.add(char)

    #Применяем поиск в ширину
    visited = set()
    q = collections.deque()

    init_state = (tuple(starts), str(), 0) #Стартовое состояние
    q.append(init_state)
    visited.add((tuple(starts), str()))

    while q:
        positions, keys, steps = q.popleft()
        if len(keys) == len(total_keys):  #Условие завершения
            return steps

        for i in range(4):  # Проходим по всем 4 роботам
            x, y = positions[i]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < m):
                    continue

                char = data[nx][ny]
                if char == '#':
                    continue

                new_keys = set(keys)   #множество на случай нахождения ключей(будем добавлять новые ключи если что-то найдем)

                if char in doors_char:
                    if char.lower() not in keys:
                        continue  # дверь закрыта

                if char in keys_char:
                    new_keys.add(char)

                #Сохраняем состояние, так как робот переместился
                new_positions = list(positions)
                new_positions[i] = (nx, ny)
                new_state = (tuple(new_positions), str(new_keys))

                if new_state not in visited:
                    visited.add(new_state)
                    q.append((tuple(new_positions), new_keys, steps + 1))

    return -1



def main():
    data = get_input()
    result = solve(data)
    print(result)


if __name__ == '__main__':
    main()