from samples.functional_vs_oop.oop import Train, TrainSet


def test_couple_increases_weight_length_and_trainsets():
    train = Train([TrainSet(1000, 150)])

    train.couple(TrainSet(500, 75))

    assert train.length() == 150 + 75
    assert train.weight() == 1000 + 500
