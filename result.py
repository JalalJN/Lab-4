data_storage = {'alpha': (3, 25),
                'beta': (2, 15),
                'gamma': (2, 15),
                'delta': (2, 20),
                'epsilon': (1, 5),
                'zeta': (1, 15),
                'eta': (3, 20),
                'theta': (1, 25),
                'iota': (1, 15),
                'kappa': (1, 10),
                'lambda': (2, 20),
                'mu': (2, 20)}

reference_data = {'alpha': (3, 25),
                  'beta': (2, 15),
                  'gamma': (2, 15),
                  'delta': (2, 20),
                  'epsilon': (1, 5),
                  'zeta': (1, 15),
                  'eta': (3, 20),
                  'theta': (1, 25),
                  'iota': (1, 15),
                  'kappa': (1, 10),
                  'lambda': (2, 20),
                  'mu': (2, 20)}


def extract_dimensions(storage):
    weights = [storage[key][0] for key in storage]
    values = [storage[key][1] for key in storage]
    return weights, values


def build_table(storage, capacity):
    weights, values = extract_dimensions(storage)
    num_items = len(values)
    
    table = [[0 for _ in range(capacity + 1)] for _ in range(num_items + 1)]

    for i in range(num_items + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                table[i][w] = 0
            elif weights[i - 1] <= w:
                table[i][w] = max(values[i - 1] + table[i - 1][w - weights[i - 1]], table[i - 1][w])
            else:
                table[i][w] = table[i - 1][w]
    return table, weights, values


def determine_selection(storage, capacity):
    table, weights, values = build_table(storage, capacity)
    num_items = len(values)
    max_value = table[num_items][capacity]
    remaining_capacity = capacity
    chosen_items = []
    
    for i in range(num_items, 0, -1):
        if max_value <= 0:
            break
        if max_value == table[i - 1][remaining_capacity]:
            continue
        else:
            chosen_items.append((weights[i - 1], values[i - 1]))
            max_value -= values[i - 1]
            remaining_capacity -= weights[i - 1]
    
    selected_keys = []

    for item in chosen_items:
        for key, value in storage.items():
            if value == item:
                selected_keys.append(key)
                storage.pop(key)
                break

    return selected_keys


if __name__ == '__main__':
    selection_result = determine_selection(data_storage, 9)
    interim_result = selection_result

    total_score = 15
    for key in reference_data:
        if key in interim_result:
            total_score += reference_data[key][1]
        else:
            total_score -= reference_data[key][1]

    max_capacity = 3
    for step in range(1, max_capacity + 1):
        current_load = 0
        while current_load < max_capacity:
            for key in selection_result:
                if current_load + reference_data[key][0] <= max_capacity:
                    for _ in range(reference_data[key][0]):
                        print(f'[{key}],', end=' ')
                    selection_result.remove(key)
                    current_load += reference_data[key][0]
        print('')

    print(total_score)
