item_data = {'alpha': (3, 25),
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
             'mu': (2, 20)
             }


def extract_dimensions(data_dict):
    weights = [data_dict[key][0] for key in data_dict]
    profits = [data_dict[key][1] for key in data_dict]
    return weights, profits


def create_table(data_dict, max_weight):
    weights, profits = extract_dimensions(data_dict)
    num_items = len(profits)
    
    table = [[0 for _ in range(max_weight + 1)] for _ in range(num_items + 1)]

    for i in range(num_items + 1):
        for w in range(max_weight + 1):
            if i == 0 or w == 0:
                table[i][w] = 0
            elif weights[i - 1] <= w:
                table[i][w] = max(profits[i - 1] + table[i - 1][w - weights[i - 1]], table[i - 1][w])
            else:
                table[i][w] = table[i - 1][w]
    return table, weights, profits


def select_items(data_dict, max_weight):
    table, weights, profits = create_table(data_dict, max_weight)
    num_items = len(profits)
    result = table[num_items][max_weight]
    remaining_weight = max_weight
    selected = []
    
    for i in range(num_items, 0, -1):
        if result <= 0:
            break
        if result == table[i - 1][remaining_weight]:
            continue
        else:
            selected.append((weights[i - 1], profits[i - 1]))
            result -= profits[i - 1]
            remaining_weight -= weights[i - 1]
    
    chosen_keys = []

    for selection in selected:
        for key, value in data_dict.items():
            if value == selection:
                chosen_keys.append(key)
                data_dict.pop(key)
                break

    return chosen_keys


if __name__ == '__main__':
    total_profit = 15
    removed_keys = []
    data_dict = {'alpha': (3, 25),
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
                 'mu': (2, 20)
                 }
    while total_profit > 10:
        selection = select_items(data_dict, 9)
        temp_selection = [key for key in selection]

        total_profit = 15
        for key in item_data:
            if key in selection:
                total_profit += item_data[key][1]
            else:
                total_profit -= item_data[key][1]

        bag_limit = 3
        for i in range(1, bag_limit + 1):
            pos = 0
            while pos < bag_limit:
                for key in selection:
                    if pos + item_data[key][0] <= bag_limit:
                        for _ in range(item_data[key][0]):
                            print(f'[{key}],', end=' ')
                        selection.remove(key)
                        pos += item_data[key][0]
            print('')

        removed_keys.append(temp_selection[0])

        data_dict = {'alpha': (3, 25),
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
                     'mu': (2, 20)
                     }
        
        for key in removed_keys:
            data_dict.pop(key)

        print(total_profit)
