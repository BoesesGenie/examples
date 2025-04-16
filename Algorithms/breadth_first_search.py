from collections import deque

example = {
    'root': ['first', 'second', 'third'],
    'first': ['fifth'],
    'second': ['fourth', 'fifth'],
    'third': ['sixth', 'seventh'],
    'fourth': [],
    'fifth': [],
    'sixth': [],
    'seventh': []
}

def breadth_first_search(graph, start, condition):
    search_queue = deque()
    search_queue += graph[start]
    searched = set()

    while search_queue:
        current = search_queue.popleft()

        if current in searched:
            continue

        if condition(current):
            return current

        search_queue += graph[current]
        searched.add(current)

    return None

print(breadth_first_search(example, 'root', lambda x : x.endswith('th')))
