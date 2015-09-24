# We need to measure the performance of our model
# For that, we'll use some evaluation techniques

def divide_data(data):
    # divide data into k+1 components
    # out of these k will be used to test and
    # the remaining 1 segment will be used for evaluation
    k_segment = []
    one_segment = []
    return (k_segment, one_segment)

def train(data):
    # train our model using the data
    model = {}
    return model

def predict(model, test_data):
    # given a learned model predict the values for the test_data
    prediction = []
    return prediction

def evaluae(predicted_outcome, actual_outcome):
    error = 0
    for i in len(predicted_outcome):
        predicted_value = predicted_outcome[i]
        expected_value = actual_outcome[i]
        error+=distance(predicted_value,actual_value)
    performance = performance_from_error(error)
    return performance

def performance_from_error(error):
    # convert error value to performance
    # for example
    performance = 1/error
    return performance

def distance(predicted, actual):
    # measure how accurately are we predicting
    distance = predicted - actual
    return distance

def main(data):
    training_data, test_data = divide_data(data)
    model = train(training_data)
    prediction = predict(model,test_data)
    performance = evaluate(prediction,truth)
    print performance
