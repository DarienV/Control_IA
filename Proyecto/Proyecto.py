import numpy as np

w = 0.75
Eta = 0.9
def perceptron_training(X, y, learning_rate=Eta):
    num_features = X.shape[1]
    weights = np.full(num_features, w)
    epoch = 0

    while True:
        error = False

        for i in range(len(X)):
            u = np.dot(weights, X[i])
            y_pred = np.sign(u)

            if y_pred != y[i]:
                weights += learning_rate * (y[i] - y_pred) * X[i]
                error = True

        epoch += 1
        if not error:
            break

    return weights, epoch

# Example usage
X = np.array([[-1, 0.1, 0.4, 0.7], [-1, 0.3, 0.7, 0.2], [-1, 0.6, 0.9, 0.8], [-1, 0.5, 0.7, 0.1]])
y = np.array([1, -1, -1, 1])

weights, epochs = perceptron_training(X, y)
print("Weights:", weights)
print("Number of epochs:", epochs)

save_path = "C:\\Users\\didie\\Documents\\BUAP_Prim23\\Control_IA\\Proyecto\\"
outfile = open(save_path + "Perceptron_w({})_Eta({}).csv".format(str(w),str(Eta)), "w")
outfile.write("# of Execution,Weights,Epochs\n")

execution = []
for i in range(5):
    weights, epochs = perceptron_training(X, y)
    print("Weights:", weights)
    print("Number of epochs:", epochs)
    execution.append(i)
    outfile.write("{},{},{}\n".format(str(execution[i]), str(weights), str(epochs)))

outfile.close()