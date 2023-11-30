import heapq

def calculate_distance(city1, city2):
    return abs(city1[0] - city2[0]) + abs(city1[1] - city2[1])

def total_distance(path, cities):
    total = 0
    for i in range(len(path) - 1):
        total += calculate_distance(cities[path[i]], cities[path[i+1]])
    total += calculate_distance(cities[path[-1]], cities[path[0]])
    return total

def a_star_tsp(cities):
    num_cities = len(cities)
    initial_state = tuple([0] + [float('inf')] * (num_cities - 1))
    open_set = [(total_distance([0, i], cities), [0, i]) for i in range(1, num_cities)]
    heapq.heapify(open_set)
    closed_set = set()

    while open_set:
        f, current_path = heapq.heappop(open_set)
        current_state = tuple(current_path)

        if current_state in closed_set:
            continue

        closed_set.add(current_state)

        if len(current_path) == num_cities:
            return current_path, f

        last_city = current_path[-1]
        for next_city in range(num_cities):
            if next_city not in current_path:
                g = total_distance(current_path + [next_city], cities)
                h = total_distance([next_city, 0], cities)
                heapq.heappush(open_set, (g + h, current_path + [next_city]))

    return None

def main():
    num_cities = int(input("Enter the number of cities: "))
    cities = []

    for i in range(num_cities):
        x, y = map(int, input(f"Enter the coordinates of city {i+1} (x y): ").split())
        cities.append((x, y))

    best_path, min_distance = a_star_tsp(cities)

    print("Best path:", "->".join(str(city) for city in best_path))
    print("Minimum distance:", min_distance)

if __name__ == "__main__":
    main()
