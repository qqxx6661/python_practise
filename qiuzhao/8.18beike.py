# coding=utf-8
import sys


class Graph(object):
    def __init__(self, maps):
        self.maps = maps
        self.nodenum = self.get_nodenum()
        self.edgenum = self.get_edgenum()

    def get_nodenum(self):
        return len(self.maps)

    def get_edgenum(self):
        count = 0
        for i in range(self.nodenum):
            for j in range(i):
                if self.maps[i][j] > 0 and self.maps[i][j] < 9999:
                    count += 1
        return count

    def kruskal(self):
        res = []
        if self.nodenum <= 0 or self.edgenum < self.nodenum - 1:
            return res
        edge_list = []
        for i in range(self.nodenum):
            for j in range(i, self.nodenum):
                if self.maps[i][j] < 9999:
                    edge_list.append([i, j, self.maps[i][j]])  # 按[begin, end, weight]形式加入
        edge_list.sort(key=lambda a: a[2])  # 已经排好序的边集合

        group = [[i] for i in range(self.nodenum)]
        for edge in edge_list:
            for i in range(len(group)):
                if edge[0] in group[i]:
                    m = i
                if edge[1] in group[i]:
                    n = i
            if m != n:
                res.append(edge)
                group[m] = group[m] + group[n]
                group[n] = []
        return res

    def prim(self):
        res = []
        if self.nodenum <= 0 or self.edgenum < self.nodenum - 1:
            return res
        res = []
        seleted_node = [0]
        candidate_node = [i for i in range(1, self.nodenum)]

        while len(candidate_node) > 0:
            begin, end, minweight = 0, 0, 9999
            for i in seleted_node:
                for j in candidate_node:
                    if self.maps[i][j] < minweight:
                        minweight = self.maps[i][j]
                        begin = i
                        end = j
            res.append([begin, end, minweight])
            seleted_node.append(end)
            candidate_node.remove(end)
        return res




if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip(''))
    cun_list = list(map(int,sys.stdin.readline().strip('').split(' ')))
    dp = [[0 for __ in range(n)] for __ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dp[i][j] = 0
                continue
            dp[i][j] = max(cun_list[i],cun_list[j])


    print(dp)

    graph = Graph(dp)
    # print('邻接矩阵为\n%s' % graph.maps)
    # print('节点数据为%d，边数为%d\n' % (graph.nodenum, graph.edgenum))
    # print('------最小生成树kruskal算法------')
    # print(graph.kruskal())
    # print('------最小生成树prim算法')
    # print(graph.prim())
    print()