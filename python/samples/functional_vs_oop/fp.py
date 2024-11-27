def couple_train(train, train_set):
    return train + (train_set,)


def decouple_train(train):
    return train[:-1]


def train_length(train):
    lengths = map(lambda train_set: train_set["length"], train)
    return sum(lengths)


def train_weight(train):
    weights = map(lambda train_set: train_set["weight"], train)
    return sum(weights)
