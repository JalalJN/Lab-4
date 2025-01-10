# Define the dictionaries for items and their properties
item_props = {'q': (3, 25),
              'z': (2, 15),
              'e': (2, 15),
              'n': (2, 20),
              'u': (1, 5),
              'v': (1, 15),
              'y': (3, 20),
              'o': (1, 25),
              'g': (1, 15),
              'b': (1, 10),
              'l': (2, 20),
              'h': (2, 20)}

all_item_props = item_props.copy()  # A copy to use for later calculations

# Function to extract weights and values as separate lists
def get_weights_values(props):
    wt_list = [info[0] for info in props.values()]
    val_list = [info[1] for info in props.values()]
    return wt_list, val_list

# Function to build the dynamic programming table
def create_dp_table(props, max_cap):
    wt_list, val_list = get_weights_values(props)
    total_items = len(val_list)
    
    # Initialize a DP table
    dp_grid = [[0] * (max_cap + 1) for _ in range(total_items + 1)]

    # Populate the table using the knapsack algorithm
    for idx in range(1, total_items + 1):
        for rem_cap in range(1, max_cap + 1):
            if wt_list[idx - 1] <= rem_cap:
                dp_grid[idx][rem_cap] = max(
                    val_list[idx - 1] + dp_grid[idx - 1][rem_cap - wt_list[idx - 1]],
                    dp_grid[idx - 1][rem_cap]
                )
            else:
                dp_grid[idx][rem_cap] = dp_grid[idx - 1][rem_cap]
    
    return dp_grid, wt_list, val_list

# Function to determine the selected items from the DP table
def get_selected_items(props, max_cap):
    dp_grid, wt_list, val_list = create_dp_table(props, max_cap)
    total_items = len(val_list)
    rem_value = dp_grid[total_items][max_cap]
    rem_cap = max_cap
    chosen = []

    # Backtrack through the table to find the items
    for idx in range(total_items, 0, -1):
        if rem_value <= 0:
            break
        if rem_value != dp_grid[idx - 1][rem_cap]:
            chosen.append((wt_list[idx - 1], val_list[idx - 1]))
            rem_value -= val_list[idx - 1]
            rem_cap -= wt_list[idx - 1]

    chosen_items = []
    for wt_val in chosen:
        for itm, attrib in props.items():
            if attrib == wt_val:
                chosen_items.append(itm)
                props.pop(itm)
                break
    
    return chosen_items

# Main execution
if __name__ == '__main__':
    selected_items = get_selected_items(item_props, 7)
    
    # Calculate the adjusted total
    final_value = 15
    for itm, (wt, val) in all_item_props.items():
        if itm in selected_items:
            final_value += val
        else:
            final_value -= val

    print(final_value)
