import enum, os

__all__ = [
    "ML",
    "DL",
    "SUPERVISED",
    "UNSUPERVISED"
]

class ML(enum.Enum):
    Decision_Tree = (enum.auto(), "의사결정나무")

class DL(enum.Enum()):
    CNN = (enum.auto(), "합성곱신경망")
    RNN = (enum.auto(), "재귀신경망")

class SUPERVISED(enum.Enum()):
    pass

class UNSUPERVISED(enum.Enum()):
    pass

