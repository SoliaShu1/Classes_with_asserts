class Channel:
    def __init__(self, name, number, playlist):
        self.name = name
        self.number = number
        self.playlist = playlist

    def getFrequency(self):
        return self.number

    def __str__(self):
        return "Channel {} on {}, playlist: {}".format(self.name, self.number, self.playlist)

    def __eq__(self, other):
        if isinstance(self, Channel) and isinstance(other, Channel):
            if self.name == other.name:
                return True
        return False

    def __hash__(self):
        return hash(tuple(self.playlist))


class Radio:
    def __init__(self, dct, freq):
        self.dct = dct[round(freq, 1)]
        self.freq = freq

    def getCurrentFrequency(self):
        return self.freq

    def getCurrentChannel(self):
        return self.dct
        # for i, val in self.dct.items():
        #     if i == self.freq:
        #         print(val)
        #         return val

    # def __eq__(self, other):
    #     if isinstance(self, Radio) and isinstance(other, Channel):
    #         if self.name == other.name:
    #             return True
    #     return False



