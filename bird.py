class Bird:
    """Class for Bird representation"""
    def __init__(self, name):
        """Initializing name and number of eggs"""
        self.name = name
        self.eggs = 0

    def fly(self):
        """Returns message"""
        return "I can fly!"

    def countEggs(self):
        """Returns number of eggs"""
        return self.eggs

    def __repr__(self):
        """Method for representation"""
        if self.eggs == 0 or self.eggs >= 2:
            return "{} has {} eggs".format(self.name, self.eggs)
        return "{} has {} egg".format(self.name, self.eggs)

    def layEgg(self):
        """Adds one more egg"""
        self.eggs += 1
        return self.eggs


class Penguin(Bird):
    """Class for Penguin representation"""
    def fly(self):
        """Returns message"""
        return "No flying for me."

    def swim(self):
        """Returns message"""
        return "I can swim!"


class MessengerBird(Bird):
    """Class for message representation"""
    def __init__(self, name, message=""):
        """Initializing name and message"""
        super().__init__(name)
        self.message = message

    def deliverMessage(self):
        """Returns message"""
        return self.message
