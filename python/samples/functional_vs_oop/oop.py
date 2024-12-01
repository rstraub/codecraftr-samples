class Train:
    def __init__(self, composition):
        self.composition = composition

    def couple(self, train_set):
        self.composition.append(train_set)

    def decouple(self):
        self.composition.pop()

    def length(self):
        lengths = [train_set.length for train_set in self.composition]
        return sum(lengths)

    def weight(self):
        weights = [train_set.weight for train_set in self.composition]
        return sum(weights)


class TrainSet:
    def __init__(self, weight, length):
        self.weight = weight
        self.length = length
