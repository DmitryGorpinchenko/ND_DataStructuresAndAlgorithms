class AStarCtx:
    def __init__(self, M, start, goal):
        self.M = M
        self.start = start
        self.goal = goal
        self.open_set = {start}
        self.g = {start: 0}
        self.f = {start: self.__h(start)}
        self.prev = {}

    def has_next(self):
        return len(self.open_set) > 0

    def extract_next(self):
        res = min(self.open_set, key=lambda node: self.f[node])
        self.open_set.remove(res)
        return res

    def reconstruct_path(self):
        res = [self.goal]
        curr = self.goal
        while curr != self.start:
            curr = self.prev[curr]
            res.append(curr)
        res.reverse()
        return res

    def process_neighbours(self, node):
        for neigh in self.__neighbours(node):
            g = self.g[node] + self.__d(node, neigh)
            if (neigh not in self.g) or (g < self.g[neigh]):
                self.g[neigh] = g
                self.f[neigh] = g + self.__h(neigh)
                self.prev[neigh] = node
                self.open_set.add(neigh)

    def __neighbours(self, node):
        return self.M.roads[node]

    def __d(self, node1, node2):
        from math import sqrt
        x1, y1 = self.M.intersections[node1]
        x2, y2 = self.M.intersections[node2]
        return sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def __h(self, node):
        return self.__d(node, self.goal)

def shortest_path(M, start, goal):
    ctx = AStarCtx(M, start, goal)

    while ctx.has_next():
        node = ctx.extract_next()
        if node == ctx.goal:
            return ctx.reconstruct_path()
        else:
            ctx.process_neighbours(node)

    return None
