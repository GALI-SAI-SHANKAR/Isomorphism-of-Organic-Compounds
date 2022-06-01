import numpy as np

# # Example Matrix
# adj_matrix_c1 = np.array([[0, 1, 0, 0, 0],
#                           [1, 0, 1, 0, 1],
#                           [0, 1, 0, 1, 1],
#                           [0, 0, 1, 0, 1],
#                           [0, 1, 1, 1, 0]])
#
# adj_matrix_c2 = np.array([[0, 1, 1, 1, 0],
#                           [1, 0, 1, 0, 0],
#                           [1, 1, 0, 1, 0],
#                           [1, 0, 1, 0, 1],
#                           [0, 0, 0, 1, 0]])


def degrees(adj_matrix):
    n = adj_matrix.shape[0]
    degree_sequence = []
    y = np.asarray(adj_matrix)
    for i in range(n):
        count = np.count_nonzero(y[i] == 1)
        degree_sequence.append(count)
    return degree_sequence


def degrees_positions(adj_matrix):
    n = adj_matrix.shape[0]
    keys = range(n)
    d = dict(zip(keys, ([] for _ in keys)))
    y = np.asarray(adj_matrix)
    for i in range(n):
        count = np.count_nonzero(y[i] == 1)
        d[i].append(count)
    return d


def next_positions(node):
    y = np.asarray(node)
    next_nodes = []
    for i in range(len(y)):
        if y[i] == 1:
            next_nodes.append(i)
    return next_nodes


from operator import itemgetter


def GraphMatcher(adj_matrix_c1, adj_matrix_c2):
    adj_matrix_equal = np.array_equal(adj_matrix_c1, adj_matrix_c2, equal_nan=True)
    if adj_matrix_equal:
        return True
    else:
        nodes_equal = adj_matrix_c1.shape == adj_matrix_c1.shape
        if nodes_equal:
            if np.array_equal(np.sort(degrees(adj_matrix_c1)), np.sort(degrees(adj_matrix_c2)), equal_nan=True):
                if np.array_equal(degrees(adj_matrix_c1), degrees(adj_matrix_c2), equal_nan=True):
                    return True
                else:
                    n = adj_matrix_c1.shape[0]
                    x = degrees_positions(adj_matrix_c1)
                    y = degrees_positions(adj_matrix_c2)
                    nodes_x = sorted(x.items(), key=itemgetter(1))[:n]
                    nodes_y = sorted(y.items(), key=itemgetter(1))[:n]
                    visited_nodes_x = []
                    visited_nodes_y = []

                    flag = False

                    for i in range(n):
                        if nodes_x[i][0] == nodes_x[i][0]:
                            next_nodes_x = next_positions(adj_matrix_c1[nodes_x[i][0]])
                            next_nodes_y = next_positions(adj_matrix_c2[nodes_y[i][0]])
                            nnl = len(next_nodes_x)
                            visited_nodes_x.append(nodes_x[i][0])
                            visited_nodes_y.append(nodes_y[i][0])
                            print('visited nodes : ', visited_nodes_x, visited_nodes_y)
                            print('next noodes : ', next_nodes_x, next_nodes_y)

                            j = 0
                            while j < nnl:
                                if x.get(next_nodes_x[j]) == y.get(next_nodes_y[j]):
                                    print('Selected Nodes : ', next_nodes_x[j], next_nodes_y[j])
                                    visited_nodes_x.append(next_nodes_x[j])
                                    visited_nodes_y.append(next_nodes_y[j])
                                    print('visited nodes : ', visited_nodes_x, visited_nodes_y)

                                    next_nodes_x = next_positions(adj_matrix_c1[next_nodes_x[j]])
                                    next_nodes_y = next_positions(adj_matrix_c2[next_nodes_y[j]])

                                    next_nodes_x = list(set(next_nodes_x).difference(visited_nodes_x))
                                    next_nodes_y = list(set(next_nodes_y).difference(visited_nodes_y))
                                    print('next nodes : ', next_nodes_x, next_nodes_y)

                                    nnl = len(next_nodes_x)
                                    flag_next = True
                                else:
                                    break

                                if flag_next:
                                    j = 0
                                else:
                                    j += 1

                                if not next_nodes_x:
                                    flag = True
                                    break
                            if flag:
                                flag = True
                                break

                            visited_nodes_x = []
                            visited_nodes_y = []
                    return flag
            else:
                return False
        else:
            return False

#
# if GraphMatcher(adj_matrix_c1, adj_matrix_c2):
#     print('Isomorphic')
# else:
#     print('Not Isomorphic')
