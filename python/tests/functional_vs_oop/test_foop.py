from samples.functional_vs_oop.foop import Train, TrainSet


def test_couple_increases_weight_length():
    train = Train(
        (TrainSet(1000, 150),)
    )

    coupled = train.couple(TrainSet(500, 75))

    assert coupled.weight() == 1000 + 500
    assert coupled.length() == 150 + 75
    assert len(coupled.composition) == 2
    assert coupled != train


def test_decouple_decreases_weight_length_and_trainsets():
    train = Train((TrainSet(1000, 150), TrainSet(500, 75)))

    decoupled = train.decouple()

    assert decoupled.weight() == 1000
    assert decoupled.length() == 150
    assert len(decoupled.composition) == 1
    assert decoupled != train
