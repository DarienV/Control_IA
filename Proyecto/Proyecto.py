import numpy as np

def perceptron_training5(X, y, w, Eta):
    num_features = X.shape[1]
    weights = np.full(num_features, w)
    epoch = 0

    for _ in range(5):
        
        for i in range(len(X)):
            u = np.dot(weights, X[i])
            y_pred = np.sign(u)

            if y_pred != y[i]:
                weights += Eta * (y[i] - y_pred) * X[i]
                error = True

        epoch += 1

    return weights, epoch

def perceptron_training(X, y, w, Eta):
    num_features = X.shape[1]
    weights = np.full(num_features, w)
    epoch = 0

    while True:
        error = False

        for i in range(len(X)):
            u = np.dot(weights, X[i])
            y_pred = np.sign(u)

            if y_pred != y[i]:
                weights += Eta * (y[i] - y_pred) * X[i]
                error = True

        epoch += 1
        if not error:
            break

    return weights, epoch

# Example usage
X = np.array([[-1, 0.1, 0.4, 0.7], [-1, 0.3, 0.7, 0.2], [-1, 0.6, 0.9, 0.8], [-1, 0.5, 0.7, 0.1]])
y = np.array([1, -1, -1, 1])
w = [0.1, 0.75]
Eta = [0.5, 0.9]

save_path = "C:\\Users\\didie\\Documents\\BUAP_Prim23\\Control_IA\\Proyecto\\"
outfile = open(save_path + "Perceptron_outdata.csv", "w")
outfile.write("w,Eta,Weights,Epochs\n")

for n in w:
    for m in Eta:
        weights5, epochs5 = perceptron_training5(X, y, n, m)
        print("Weights:", weights5)
        print("Number of epochs:", epochs5)
        outfile.write("{},{},{},{}\n".format(str(n), str(m), str(weights5), str(epochs5)))

print("\n")
        
for n in w:
    for m in Eta:
        weights, epochs = perceptron_training(X, y, n, m)
        print("Weights:", weights)
        print("Number of epochs:", epochs)
        outfile.write("{},{},{},{}\n".format(str(n), str(m), str(weights), str(epochs)))

outfile.close()