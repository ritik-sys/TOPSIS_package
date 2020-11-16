import numpy as np
import pandas as pd
import copy
import sys
import os
# --------------------------------------------------------------------------------------


def normalize(data):
    root_of_squares = []
    for col in data.T[1:]:
        root_of_squares.append(np.sqrt((np.sum(col*col))))
    for i in range(0, len(data)):
        k = 0
        for j in range(1, len(data)):
            data[i][j] /= root_of_squares[k]
            k += 1
    return data
# -----------------------------------------------------------------------------------------


def assign_weights(data, weights):
    weight_norm_data = copy.deepcopy(data)
    for i in range(len(data)):
        k = 0
        for j in range(1, len(data)):
            weight_norm_data[i][j] = data[i][j]*weights[k]
            k += 1
    return weight_norm_data
# -----------------------------------------------------------------------------------------


def Ideal_nonIdeal(data, impacts):
    ideal_best = []
    ideal_worst = []
    k = 0
    for i in range(1, data.shape[1]):
        if impacts[k] == '+':
            ideal_best.append(np.amax(data[:, i], axis=0))
            ideal_worst.append(np.amin(data[:, i], axis=0))
        else:
            ideal_worst.append(np.amax(data[:, i], axis=0))
            ideal_best.append(np.amin(data[:, i], axis=0))
        k += 1
    return ideal_best, ideal_worst
# -----------------------------------------------------------------------------------------


def euclidean_distance(data, ideal_best, ideal_worst):
    best_euc_distance = []
    worst_euc_distance = []
    for row in data:
        b = 0.0
        w = 0.0
        j = 0
        for i in range(1, data.shape[1]):
            b += np.sqrt((row[i]-ideal_best[j])*(row[i]-ideal_best[j]))
            w += np.sqrt((row[i]-ideal_worst[j])*(row[i]-ideal_worst[j]))
            j += 1
        best_euc_distance.append(b)
        worst_euc_distance.append(w)
    return best_euc_distance, worst_euc_distance
# -----------------------------------------------------------------------------------------


def performance_score_rank(best_euc_distance, worst_euc_distance):
    score = []
    for i in range(len(best_euc_distance)):
        score.append(
            worst_euc_distance[i]/(best_euc_distance[i]+worst_euc_distance[i]))
    score = np.array(score)
    order = (-1*score).argsort()
    ranks = order.argsort()
    return score, ranks+1
# -----------------------------------------------------------------------------------------


def TOPSIS(data, weights, impacts, output):
    df = pd.read_csv(data, index_col=None)
    data = df.values
    normalised_data = normalize(data)
    weight_normalised_data = assign_weights(normalised_data, weights)
    ideal_best, ideal_worst = Ideal_nonIdeal(weight_normalised_data, impacts)
    best_euc_dist, worst_euc_dist = euclidean_distance(
        weight_normalised_data, ideal_best, ideal_worst)
    scores, rank = performance_score_rank(best_euc_dist, worst_euc_dist)
    df1 = pd.DataFrame(scores, columns=["Topsis Score"])
    df2 = pd.DataFrame(rank, columns=["Rank"])
    final_df = pd.concat([df, df1, df2], axis=1)
    final_df.to_csv(output, index=False)


# -----------------------------------------------------------------------------------------
# TOPSIS("./mobile.csv", [0.25, 0.25, 0.25, 0.25],
#        ['-', '+', '+', '+'], "output.csv")
