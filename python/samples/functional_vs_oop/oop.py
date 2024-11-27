class Train:
    def __init__(self, train_sets):
        self.__train_sets = train_sets

    def couple(self, train_set):
        self.__train_sets.append(train_set)

    def length(self):
        total = 0
        for train_set in self.__train_sets:
            total += train_set.length
        return total

    def weight(self):
        total = 0
        for train_set in self.__train_sets:
            total += train_set.weight
        return total


class TrainSet:
    def __init__(self, weight, length):
        self.weight = weight
        self.length = length
