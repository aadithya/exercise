def knapsack(weigths, max_weight):
    max_value = 0
    if not max_weight:
        return 0
    for weight in weights:
        if max_weight - weight.w >= 0:
            max_value = max(max_value, weight.v + knapsack(weights, max_weight-weight.w))
    return max_value

t = {}
def dp_knapsack(weights, max_weight):
    global t
    max_value = 0
    if not max_weight:
        return 0
    if max_weight in t:
        return t[max_weight]
    for weight in weights:
        if max_weight - weight.w >= 0:
            max_value = max(max_value, weight.v + knapsack(weights, max_weight-weight.w))
    t[max_weight] = max_value
    return max_value

def zero_knapsack(weights, max_weight):
    t = [[0 for i in range(max_weight + 1)] for weight in weights]
    for i in range(len(weights)):
        for j in range(1, max_weight+1):
            if not i:
                t[i][j] = 0 if j < weights[i].w else weights[i].v
            if weights[i].w <= j:
                t[i][j] = max(t[i-1][j], t[i-1][j-weights[i].w] + weights[i].v)
            else:
                t[i][j] = t[i-1][j]

    return t[len(weights) - 1][max_weight]

class Weight():
    def __init__(self, weight, value):
        self.w = int(weight)
        self.v = int(value)

if __name__ == "__main__":
    weights = [ Weight(*val.split(":")) for val in raw_input("Enter the weights: ").split(',')]
    max_weight = int(raw_input("Enter the max weight: "))
    print knapsack(weights, max_weight)
    print dp_knapsack(weights, max_weight)
    print zero_knapsack(weights, max_weight)

