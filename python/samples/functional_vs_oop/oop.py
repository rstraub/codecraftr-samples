class Train:
    def __init__(self, train_sets):
        self.train_sets = train_sets

    def couple(self, train_set):
        self.train_sets.append(train_set)

    def decouple(self):
        self.train_sets.pop()

    def length(self):
        lengths = [train_set.length for train_set in self.train_sets]
        return sum(lengths)

    def weight(self):
        weights = [train_set.weight for train_set in self.train_sets]
        return sum(weights)


class TrainSet:
    def __init__(self, weight, length):
        self.weight = weight
        self.length = length
