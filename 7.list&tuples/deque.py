from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives

queue
#["Eric", "John", "Michael", "Terry", "Graham"]

queue.popleft()                 # The first to arrive now leaves

queue.popleft()                 # The second to arrive now leaves

queue                           # Remaining queue in order of arrival
#["Michael", "Terry", "Graham"]