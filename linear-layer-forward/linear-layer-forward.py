def linear_layer_forward(X, W, b): 
    i = len(X) 
    k = len(X[0]) 
    j = len(W[0]) 
    Y = [[0 for col in range(j)] for row in range(i)] 
    for i_ in range(i): 
        for j_ in range(j): 
            for k_ in range(k): 
                Y[i_][j_] += X[i_][k_] * W[k_][j_] 
            Y[i_][j_] += b[j_] 
    return Y