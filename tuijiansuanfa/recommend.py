# -*- coding: utf-8 -*-
import math  # py3


def load_matrix():
    matrix = {}
    f = open("traintxt.txt")
    columns = f.readline().split(',')

    for line in f:
        scores = line.split(',')
        # print scores
        for i in range(len(scores))[1:]:
            matrix[(scores[0], columns[i])] = scores[i].strip("\n")

    return matrix


def sim_distance(matrix, row1, row2):
    columns = set(map(lambda l: l[1], matrix.keys()))
    si = filter(
        lambda l: matrix.has_key((row1, l)) and matrix[(row1, l)] != "" and matrix.has_key((row2, l)) and matrix[(row2, l)] != "", columns)
    if len(si) == 0:
        return 0
    sum_of_distance = sum([pow(float(matrix[(row1, column)]) - float(matrix[(row2, column)]), 2) for column in si])
    return 1 / (1 + math.sqrt(sum_of_distance))


def top_matches(matrix, row, similarity=sim_distance):
    rows = set(map(lambda l: l[0], matrix.keys()))
    scores = [(similarity(matrix, row, r), r) for r in rows if r != row]
    scores.sort()
    scores.reverse()
    return scores


def transform(matrix):
    rows = set(map(lambda l: l[0], matrix.keys()))
    columns = set(map(lambda l: l[1], matrix.keys()))
    transform_matrix = {}
    for row in rows:
        for column in columns:
            transform_matrix[(column, row)] = matrix[(row, column)]
    return transform_matrix


def get_recommendations(matrix, row, similarity=sim_distance):
    rows = set(map(lambda l: l[0], matrix.keys()))
    columns = set(map(lambda l: l[1], matrix.keys()))

    sum_of_column_sim = {}
    sum_of_column = {}

    for r in rows:
        if r == row:
            continue
        sim = similarity(matrix, row, r)
        if sim <= 0:
            continue

        for c in columns:
            if matrix[(r, c)] == "":
                continue

            sum_of_column_sim.setdefault(c, 0)
            sum_of_column_sim[c] += sim
            sum_of_column.setdefault(c, 0)
            sum_of_column[c] += float(matrix[(r, c)]) * sim

    scores = [(sum_of_column[c] / sum_of_column_sim[c], c) for c in sum_of_column]
    scores.sort()
    scores.reverse()
    return scores


if __name__ == '__main__':

    matrix1 = load_matrix()
    # print(type(matrix1))
    # print("matrix:", matrix1)
    # print "Kai Zhou and Shuai Ge's distance:", sim_distance(matrix1, "Kai Zhou", "Shuai Ge")

    print("请输入需要查询的人名：")
    person = raw_input()
    print("与" + person + "口味相似的人:")
    # print(top_matches(matrix1, person))
    similar_list_person = top_matches(matrix1, person)
    for m in range(5):
        print(similar_list_person[m][1].strip())
        print(similar_list_person[m][0])

    trans_matrix = transform(matrix1)
    # print "trans:", trans_matrix
    print("------------------------")
    print("推荐给" + person + "的菜:")
    recommend_list = get_recommendations(matrix1, person)
    for m in range(5):
        print(recommend_list[m][1].strip())
        print(recommend_list[m][0])
    print("------------------------")
    print("请输入需要查询的菜名：")
    dish = raw_input()
    print("与" + dish + "类似的菜:")
    similar_list_item = top_matches(trans_matrix, dish)
    for m in range(5):
        print(similar_list_item[m][1].strip())

    # trans_matrix = transform(matrix)
    # print get_recommendations(trans_matrix,  "Friends")