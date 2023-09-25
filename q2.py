def getMinTime(task_memory, task_type, max_memory):
    # Create a dictionary with task types as keys and memory requirements as values
    tasks_dict = {}
    for i in range(len(task_type)):
        if task_type[i] not in tasks_dict:
            tasks_dict[task_type[i]] = []
        tasks_dict[task_type[i]].append(task_memory[i])

    # Sort memory requirements for each task type in descending order
    for ttype, mems in tasks_dict.items():
        tasks_dict[ttype] = sorted(mems, reverse=True)

    # Calculate time
    time = 0
    for ttype, mems in tasks_dict.items():
        while mems:
            # If only one task remains or two tasks together exceed max_memory, process one task
            if len(mems) == 1 or mems[0] + mems[-1] > max_memory:
                time += 1
                mems.pop(0)
            # If two tasks can be processed together, do so
            else:
                time += 1
                mems.pop(0)
                mems.pop(-1)

    return time




# Example usage
# task_memory = [2, 3, 5, 4, 1]
# task_type = [1, 2, 1, 2, 1]
# max_memory = 6
# print(getMinTime(task_memory, task_type, max_memory))  # Expected output: 4




print(getMinTime([7, 2, 3, 9], [1, 2, 1, 3], 10))  # Output: 4
