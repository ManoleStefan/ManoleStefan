import os


class GenericFile:
    def get_path(self):
        pass

    def get_freq(self):
        pass

    def printf(self):
        pass


class TextAscii:
    path_absolute = ""
    frecvente = 0

    def __init__(self, freq, path):
        self.frecv = freq
        self.path_absolute = path

    def get_path(self):
        return self.path_absolute

    def get_freq(self):
        return self.frecv

    def printf(self):
        print("situatie ", self.get_path())
        print("frecvente ", self.get_freq())


class Binary:
    path_absolute = ""
    frecvente = 0

    def __init__(self, freq, path):
        self.frecvente = freq
        self.path_absolute = path

    def get_path(self):
        return self.path_absolute

    def get_freq(self):
        return self.frecv

    def printf(self):
        print("situatie:", self.get_path())
        print("frecvente: ", self.get_freq())


def frecventa_text(cont):
    frec = []
    for x in range(256):
        frec.append(0)

    for c in cont:
        frec[c] += 1

    return frec


def binary_text(frecv, len):
    p_ideal = len / 256
    aux = 0
    for x in range(256):
        aux += abs(frecv[x] - p_ideal)
    aux /= len
    if aux <= 0.5:
        return True
    return False
