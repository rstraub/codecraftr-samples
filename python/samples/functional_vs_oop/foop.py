from dataclasses import dataclass


@dataclass(frozen=True)
class TrainSet:
    weight: int
    length: int


@dataclass(frozen=True)
class Train:
    train_sets: tuple[TrainSet, ...]

    def couple(self, train_set):
        return Train(self.train_sets + (train_set,))

    def decouple(self):
        return Train(self.train_sets[:-1])

    def length(self):
        lengths = map(lambda ts: ts.length, self.train_sets)
        return sum(lengths)

    def weight(self):
        weights = map(lambda ts: ts.weight, self.train_sets)
        return sum(weights)
