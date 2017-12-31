from . import apply

class commandFactory():
    def createCommand(self, selectType):
        if (selectType == 'apply'):
            return apply.apply()