from sklearn.tree import DecisionTreeClassifier

class CustomDecisionTreeClassifier(DecisionTreeClassifier):
    def __init__(self, custom_param=None, **kwargs):
        super().__init__(**kwargs)
        self.custom_param = custom_param