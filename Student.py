class student(object):

    def __init__(self):
        dictionary = {}
        self.dictionary = dictionary

    def add_dic_item(self, key, value):
        """Adds an item to the dictionary"""
        self.dictionary[key] = value