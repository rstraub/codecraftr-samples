from dataclasses import dataclass


@dataclass(frozen=True)
class TrainSet:
    weight: int
    length: int


@dataclass(frozen=True)
class Train:
    composition: tuple[TrainSet, ...]

    def couple(self, train_set):
        return Train(self.composition + (train_set,))

    def decouple(self):
        return Train(self.composition[:-1])

    def length(self):
        lengths = map(lambda ts: ts.length, self.composition)
        return sum(lengths)

    def weight(self):
        weights = map(lambda ts: ts.weight, self.composition)
        return sum(weights)
