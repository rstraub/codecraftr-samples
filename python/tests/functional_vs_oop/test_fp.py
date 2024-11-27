from samples.functional_vs_oop.fp import (
    couple_train,
    decouple_train,
    train_length,
    train_weight,
)


def test_couple_increases_weight_length_and_trainsets():
    train = ({"length": 150, "weight": 1000},)

    coupled = couple_train(train, {"length": 75, "weight": 500})

    assert train_length(coupled) == 150 + 75
    assert train_weight(coupled) == 1000 + 500
    assert len(coupled) == 2


def test_decouple_decreases_weight_length_and_trainsets():
    train = ({"length": 150, "weight": 1000}, {"length": 75, "weight": 500})

    decoupled = decouple_train(train)

    assert train_length(decoupled) == 150
    assert train_weight(decoupled) == 1000
    assert len(decoupled) == 1
