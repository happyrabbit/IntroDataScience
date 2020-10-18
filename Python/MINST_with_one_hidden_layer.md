---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.6.0
  kernelspec:
    display_name: Python 3
    name: python3
---

<!-- #region id="view-in-github" colab_type="text" -->
<a href="https://colab.research.google.com/github/happyrabbit/IntroDataScience/blob/master/Python/MINST_with_one_hidden_layer.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
<!-- #endregion -->

<!-- #region id="wIstG9VsPyb2" colab_type="text" -->
# Packages

Import packages for the notebook.
<!-- #endregion -->

```python id="2e5WqQGj2tlo" colab_type="code" colab={}
import numpy as np
import math
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout
import matplotlib.pyplot as plt
```

<!-- #region id="9-m2iScR3RvE" colab_type="text" -->
# Load Data

Let's load the MINST data set. 
<!-- #endregion -->

```python id="QgbepWh429f2" colab_type="code" colab={"base_uri": "https://localhost:8080/", "height": 51} outputId="45bf4316-6c87-4e4e-9db1-069889ae23a0"
(X_train, y_train), (X_test, y_test) = mnist.load_data()

img_width = X_train.shape[1]
img_height = X_train.shape[2]

# one hot encode outputs
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
```

```python id="dTRwGbNJ4Faj" colab_type="code" colab={"base_uri": "https://localhost:8080/", "height": 102} outputId="2da35aac-6be9-4f80-9086-c0734d394dad"
print('The shape of X_train is: ' + str(X_train.shape)) 
print('The shape of y_train is: ' + str(y_train.shape)) 
print('The shape of X_test is: ' + str(X_test.shape)) 
print('The shape of y_test is: ' + str(y_test.shape))
print('I have %d traning and %d testing examples!' %(X_train.shape[0], X_test.shape[0])) 
```

<!-- #region id="Qq1P18bhWT3A" colab_type="text" -->
Check some of the input images 
<!-- #endregion -->

```python id="7hsXDMtEWc-C" colab_type="code" colab={"base_uri": "https://localhost:8080/", "height": 282} outputId="89818acf-79d2-48b4-8eca-fff491c0d888"
# assign the number of the image to show
img_id = 10
plt.imshow(X_train[img_id], cmap='gray')
print("Label: "+ str(np.where(y_train[img_id] ==1)[0]))
```

<!-- #region id="ZH2gGO_yRfW4" colab_type="text" -->
Scale and reshape the inputs and outputs.
<!-- #endregion -->

```python id="og6T69tsP-OD" colab_type="code" colab={"base_uri": "https://localhost:8080/", "height": 85} outputId="7d322eeb-af7d-42d9-e422-4cabb74ba8bf"
# Scale the input
X_train = X_train / 255.
X_test = X_test / 255.

# Flatten the input
X_train = np.array([X_train[i].flatten() for i in range(0,X_train.shape[0])])
X_test = np.array([X_test[i].flatten() for i in range(0,X_test.shape[0])])

# Reshape the input and output
X_train = X_train.T
X_test = X_test.T
y_train = y_train.T
y_test = y_test.T

print('The shape of X_train is: ' + str(X_train.shape)) 
print('The shape of y_train is: ' + str(y_train.shape)) 
print('The shape of X_test is: ' + str(X_test.shape)) 
print('The shape of y_test is: ' + str(y_test.shape))
```

<!-- #region id="dfufnet5VBPQ" colab_type="text" -->
# One Hidden Layer Neural Network
<center><img src="https://raw.githubusercontent.com/happyrabbit/course2020/master/slides/02DeepLearning/DNN/images/1hiddenexp.png" width="700"/></center>

<!-- #endregion -->

<!-- #region id="VPgV2WF7Do4I" colab_type="text" -->
# Defining the neural network structure

- `n_x` -- the size of the input layer
- `n_h` -- the size of the hidden layer
- `n_y` -- the size of the output layer

<!-- #endregion -->

<!-- #region id="Sa4lvy8dCx8B" colab_type="text" -->
#  Initialize the model's parameters

- Initialize the weights matrices, $W_1$ and $W_2$, with random values.
- Initialize the bias vectors, $b_1$ and $b_2$, as zeros.
<!-- #endregion -->

```python id="DGbe96XiQhW2" colab_type="code" colab={}
def initialize_parameters(n_x, n_h, n_y):
    """
    Argument:
    n_x -- size of the input layer
    n_h -- size of the hidden layer
    n_y -- size of the output layer
    
    Returns:
    params -- python dictionary containing your parameters:
                    W1 -- weight matrix of shape (n_h, n_x)
                    b1 -- bias vector of shape (n_h, 1)
                    W2 -- weight matrix of shape (n_y, n_h)
                    b2 -- bias vector of shape (n_y, 1)
    """
        
    W1 = np.random.randn(n_h, n_x) * 0.001
    b1 = np.zeros(shape=(n_h, 1))
    W2 = np.random.randn(n_y, n_h) * 0.001
    b2 = np.zeros(shape=(n_y, 1))
    
    assert (W1.shape == (n_h, n_x))
    assert (b1.shape == (n_h, 1))
    assert (W2.shape == (n_y, n_h))
    assert (b2.shape == (n_y, 1))
    
    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}
    
    return parameters
```

<!-- #region id="Duea8jLXHMEm" colab_type="text" -->
# Defining Activation Functions and the Gradients
<!-- #endregion -->

```python id="hbupxz65Hm6S" colab_type="code" colab={}
def ReLU(Z1):
    """
    Argument:
    Z1 -- the input of hidden layer activation function
    
    Returns:
    A1 -- activations from the hidden layer
    """
    A1 = np.maximum(Z1, 0)
    return A1

def ReLU_dev(Z1):
    """
    Argument:
    Z1 -- the input of hidden layer activation function
    
    Returns:
    dZ1 -- gradient of ReLU given input Z1
    """
    positive = Z1 > 0
    dZ1 = np.zeros(Z1.shape)
    dZ1[positive] = 1
    return dZ1

def softmax(Z2):
    """
    Argument:
    Z2 -- the input of output layer activation function
    
    Returns:
    A2 -- activations from the hidden layer
    """
    exp_scores = np.exp(Z2 - Z2.max(axis = 0, keepdims=True))
    A2 = exp_scores / exp_scores.sum(axis = 0, keepdims=True)
    return A2
```

<!-- #region id="YkS9OaatW8NF" colab_type="text" -->
# Loss and Accuracy

<!-- #endregion -->

```python id="f8Cskf4wWdcH" colab_type="code" colab={}
def compute_cost(A2, Y, parameters):
    """
    Computes the cross-entropy cost given in equation (13)
    
    Arguments:
    A2 -- The sigmoid output of the second activation, of shape (10, number of examples)
    Y -- "true" labels vector of shape (10, number of examples)
    parameters -- python dictionary containing your parameters W1, b1, W2 and b2
    
    Returns:
    cost -- cross-entropy cost given equation (13)
    """
    m = Y.shape[1] # number of example
    # Retrieve W1 and W2 from parameters
    W1 = parameters['W1']
    W2 = parameters['W2']
    
    # Compute the cross-entropy cost
    logprobs = np.multiply(np.log(A2), Y)
    cost = - np.sum(logprobs) / m
    
    cost = np.squeeze(cost)     # makes sure cost is the dimension we expect. 
                                # E.g., turns [[17]] into 17 
    assert(isinstance(cost, float))
    return cost
```

<!-- #region id="V4hoXxx9FLw4" colab_type="text" -->
# Forward Propagation
<!-- #endregion -->

```python id="ujmmyE0CEysi" colab_type="code" colab={}
def forward_propagation(X, parameters):
    """
    Argument:
    X -- input data of size (n_x, m)
    parameters -- python dictionary containing your parameters (output of initialization function)
    
    Returns:
    A2 -- The sigmoid output of the second activation
    cache -- a dictionary containing "Z1", "A1", "Z2" and "A2"
    """
    # Retrieve each parameter from the dictionary "parameters"
    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']
    
    # Implement Forward Propagation to calculate A2 (probabilities)
    Z1 = np.dot(W1, X) + b1
    A1 = ReLU(Z1)
    Z2 = np.dot(W2, A1) + b2
    A2 = softmax(Z2)
    
    assert(A2.shape == (10, X.shape[1]))
    
    cache = {"Z1": Z1,
             "A1": A1,
             "Z2": Z2,
             "A2": A2}
    
    return A2, cache
```

<!-- #region id="OdQpBDdnaQIO" colab_type="text" -->
# Backward Propagation
<!-- #endregion -->

```python id="y8KONXGME3Y_" colab_type="code" colab={}
def backward_propagation(parameters, cache, X, Y):
    """
    Implement the backward propagation using the instructions above.
    
    Arguments:
    parameters -- python dictionary containing our parameters 
    cache -- a dictionary containing "Z1", "A1", "Z2" and "A2".
    X -- input data of shape (784, number of examples)
    Y -- "true" labels vector of shape (10, number of examples)
    
    Returns:
    grads -- python dictionary containing your gradients with respect to different parameters
    """
    m = X.shape[1]
    
    # First, retrieve W1 and W2 from the dictionary "parameters".
    W1 = parameters['W1']
    W2 = parameters['W2']
        
    # Retrieve also A1 and A2 from dictionary "cache".
    A1 = cache['A1']
    A2 = cache['A2']
    Z1 = cache['Z1']
    Z2 = cache['Z2']
    
    # Backward propagation: calculate dW1, db1, dW2, db2. 
    dZ2= A2 - Y
    dW2 = (1 / m) * np.dot(dZ2, A1.T)
    db2 = (1 / m) * np.sum(dZ2, axis=1, keepdims=True)
    dZ1 = np.multiply(np.dot(W2.T, dZ2), ReLU_dev(Z1))
    dW1 = (1 / m) * np.dot(dZ1, X.T)
    db1 = (1 / m) * np.sum(dZ1, axis=1, keepdims=True)
    
    grads = {"dW1": dW1,
             "db1": db1,
             "dW2": dW2,
             "db2": db2}
    
    return grads
```

```python id="WyVadBizc4Kc" colab_type="code" colab={}
def update_parameters(parameters, grads, learning_rate= 0.1, l2 = 0):
    """
    Updates parameters using the gradient descent update rule given above
    
    Arguments:
    parameters -- python dictionary containing your parameters 
    grads -- python dictionary containing your gradients 
    learning_rate -- a number between 0 to 1
    l2 -- parameter for l2 penality, a number >= 0
    
    Returns:
    parameters -- python dictionary containing your updated parameters 
    """
    # Retrieve each parameter from the dictionary "parameters"
    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']
    
    # Retrieve each gradient from the dictionary "grads"
    dW1 = grads['dW1'] + np.sum(l2*W1)
    db1 = grads['db1'] 
    dW2 = grads['dW2'] + np.sum(l2*W2)
    db2 = grads['db2'] 
    
    # Update rule for each parameter
    W1 = W1 - learning_rate * dW1
    b1 = b1 - learning_rate * db1
    W2 = W2 - learning_rate * dW2
    b2 = b2 - learning_rate * db2
    
    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}
    
    return parameters
```

<!-- #region id="NON-Sf9QdFnb" colab_type="text" -->
# Build Your Own Neural Network 
<!-- #endregion -->

```python id="QtghT07DdOCA" colab_type="code" colab={}
def nn_model(X, Y, n_h, num_iterations=10000, print_cost=False, learning_rate= 0.1, l2 = 0):
    """
    Arguments:
    X -- dataset of shape (784, number of examples)
    Y -- labels of shape (10, number of examples)
    n_h -- size of the hidden layer
    num_iterations -- Number of iterations in gradient descent loop
    print_cost -- if True, print the cost every 1000 iterations
    learning_rate -- a number between 0 to 1
    l2 -- parameter for l2 penality, a number >= 0
    
    Returns:
    parameters -- parameters learnt by the model. They can then be used to predict.
    costs -- a list of cost per 100 interations
    """
    
    np.random.seed(1)
    n_x = X.shape[0]
    n_y = Y.shape[0]
    costs = []
    
    # Initialize parameters, then retrieve W1, b1, W2, b2. Inputs: "n_x, n_h, n_y". Outputs = "W1, b1, W2, b2, parameters".
    parameters = initialize_parameters(n_x, n_h, n_y)
    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']
    
    # Loop (gradient descent)

    for i in range(0, num_iterations):
         
        # Forward propagation. Inputs: "X, parameters". Outputs: "A2, cache".
        A2, cache = forward_propagation(X, parameters)
        
        # Cost function. Inputs: "A2, Y, parameters". Outputs: "cost".
        cost = compute_cost(A2, Y, parameters)
 
        # Backpropagation. Inputs: "parameters, cache, X, Y". Outputs: "grads".
        grads = backward_propagation(parameters, cache, X, Y)
 
        # Gradient descent parameter update. Inputs: "parameters, grads". Outputs: "parameters".
        parameters = update_parameters(parameters, grads, learning_rate= learning_rate, l2 = l2)
        
        # Print the cost every 1000 iterations
        if print_cost and i % 1000 == 0:
          print ("Cost after iteration %i: %f" % (i, cost))
        if i % 100 == 0:
          costs.append(cost)

    return parameters, costs
```

```python id="jb5eD9qOduZK" colab_type="code" colab={"base_uri": "https://localhost:8080/", "height": 187} outputId="0600bc01-b4d2-4d67-c54c-4431d9fb191c"
# Build a model with a n_h-dimensional hidden layer
parameters, costs = nn_model(X_train, y_train, n_h = 4, num_iterations=10000, print_cost=True)
```

```python id="vgv_l_WfDoce" colab_type="code" colab={"base_uri": "https://localhost:8080/", "height": 279} outputId="0738ad84-32b7-47d6-db9f-a4fa53dc7b9f"
# plot the cost
plt.plot(costs)
plt.ylabel('cost')
plt.xlabel('epochs (per 100)')
plt.show()
```

```python id="jmVWTypFYLI1" colab_type="code" colab={}
def predict(parameters, X):
    """
    Using the learned parameters, predicts a class for each example in X
    
    Arguments:
    parameters -- python dictionary containing your parameters 
    X -- input data of size (n_x, m)
    
    Returns
    predictions -- vector of predictions of our model
    """
    
    # Computes probabilities using forward propagation, and classifies to 0/1 using 0.5 as the threshold.
    A2, cache = forward_propagation(X, parameters)

    predictions = np.argmax(A2, axis = 0)
    return predictions
```

```python id="rdGHLTyTI6Gs" colab_type="code" colab={"base_uri": "https://localhost:8080/", "height": 34} outputId="a840d99b-41a0-4d5d-e837-c52371b8e6d1"
yhat_test = predict(parameters, X_test)
y = np.argmax(y_test, axis = 0)
np.mean(yhat_test == y)
```

<!-- #region id="9Xx-OKoSExSy" colab_type="text" -->
# Mini-Batch Gradient descent

Let's update the parameters using mini-batches gradient descent.
<!--
- Shuffle: Create a shuffled version of the training set (X, Y) as shown below. Each column of X and Y represents a training example. Note that the random shuffling is done synchronously between X and Y. Such that after the shuffling the $i^{th}$ column of X is the example corresponding to the $i^{th}$ label in Y. The shuffling step ensures that examples will be split randomly into different mini-batches.
- Partition: Partition the shuffled (X, Y) into mini-batches of size mini_batch_size (here 64). Note that the number of training examples is not always divisible by mini_batch_size. The last mini batch might be smaller, but you don't need to worry about this. When the final mini-batch is smaller than the full mini_batch_size
-->
<!-- #endregion -->

```python id="ENpD3RL8ZWMq" colab_type="code" colab={}
def random_mini_batches(X, Y, mini_batch_size = 64):
    """
    Creates a list of random minibatches from (X, Y)
    
    Arguments:
    X -- input data, of shape (input size, number of examples)
    Y -- true "label" of shape (10, number of examples)
    mini_batch_size -- size of the mini-batches, integer
    
    Returns:
    mini_batches -- list of synchronous (mini_batch_X, mini_batch_Y)
    """
    
    m = X.shape[1]                  # number of training examples
    mini_batches = []
        
    # Step 1: Shuffle (X, Y)
    permutation = list(np.random.permutation(m))
    shuffled_X = X[:, permutation]
    shuffled_Y = Y[:, permutation]

    # Step 2: Partition (shuffled_X, shuffled_Y). Minus the end case.
    num_complete_minibatches = math.floor(m/mini_batch_size) # number of mini batches of size mini_batch_size in your partitionning
    for k in range(0, num_complete_minibatches):
        mini_batch_X = shuffled_X[:,k * mini_batch_size:(k + 1) * mini_batch_size]
        mini_batch_Y = shuffled_Y[:,k * mini_batch_size:(k + 1) * mini_batch_size]
        mini_batch = (mini_batch_X, mini_batch_Y)
        mini_batches.append(mini_batch)
    
    # Handling the end case (last mini-batch < mini_batch_size)
    if m % mini_batch_size != 0:
        end = m - mini_batch_size * math.floor(m / mini_batch_size)
        mini_batch_X = shuffled_X[:,num_complete_minibatches * mini_batch_size:]
        mini_batch_Y = shuffled_Y[:,num_complete_minibatches * mini_batch_size:]
        mini_batch = (mini_batch_X, mini_batch_Y)
        mini_batches.append(mini_batch)
    
    return mini_batches
```

```python id="blDQeacfGmA0" colab_type="code" colab={}
def model(X, Y, n_h = 4,  learning_rate= 0.1, l2 = 0, mini_batch_size=64, num_epochs=20, print_cost=True):
    """
    3-layer neural network model which can be run in different optimizer modes.
    
    Arguments:
    X -- input data, of shape (784, number of examples)
    Y -- true "label" of shape (10, number of examples)
    layers_dims -- python list, containing the size of each layer
    learning_rate -- the learning rate, scalar.
    l2 -- l2 panalty parameter
    mini_batch_size -- the size of a mini batch
    num_epochs -- number of epochs
    print_cost -- True to print the cost every 1000 epochs

    Returns:
    parameters -- python dictionary containing your updated parameters
    costs -- a list of cost per 100 epoch 
    """

    costs = []  # to keep track of the cost
    n_x = X.shape[0]
    n_y = Y.shape[0]
    
    # Initialize parameters
    parameters = initialize_parameters(n_x, n_h, n_y)
    
    # Optimization loop
    for i in range(num_epochs):
        
        # Define the random minibatches. We increment the seed to reshuffle differently the dataset after each epoch
        minibatches = random_mini_batches(X, Y, mini_batch_size)

        for minibatch in minibatches:

            # Select a minibatch
            (minibatch_X, minibatch_Y) = minibatch
            
            # Forward propagation. Inputs: "X, parameters". Outputs: "A2, cache".
            A2, cache = forward_propagation(X, parameters)
            
            # Cost function. Inputs: "A2, Y, parameters". Outputs: "cost".
            cost = compute_cost(A2, Y, parameters)
            
            # Backpropagation. Inputs: "parameters, cache, X, Y". Outputs: "grads".
            grads = backward_propagation(parameters, cache, X, Y)
            
            # Gradient descent parameter update. Inputs: "parameters, grads". Outputs: "parameters".
            parameters = update_parameters(parameters, grads, learning_rate= learning_rate, l2 = l2)
        
        if print_cost:
            print("Cost after epoch %i: %f" % (i, cost))
        costs.append(cost)
                
    # plot the cost
    plt.plot(costs)
    plt.ylabel('cost')
    plt.xlabel('epochs')
    plt.title("Learning rate = " + str(learning_rate))
    plt.show()

    return parameters, costs
```

```python id="bgtJmQIJJms3" colab_type="code" colab={"base_uri": "https://localhost:8080/", "height": 635} outputId="f8367269-a535-4b51-87f3-a7228b17e023"
parameters, costs = model(X_train, y_train, num_epochs=20)
```

```python id="ncTf3SUSJ6qX" colab_type="code" colab={"base_uri": "https://localhost:8080/", "height": 34} outputId="34d6e411-a33f-4198-dd9c-c502ae6e20ca"
yhat_test = predict(parameters, X_test)
y = np.argmax(y_test, axis = 0)
np.mean(yhat_test == y)
```

```python id="7hIUGTHnwcoD" colab_type="code" colab={}

```
