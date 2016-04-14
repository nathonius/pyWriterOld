import json

class Project:
    def __init__(self, filepath):
        self.projectDict = None
        with open(filepath) as fp:
            self.projectDict = json.load(fp)

    def __getattr__(self, item):
        try:
            return self.projectDict[item]
        except:
            raise AttributeError
