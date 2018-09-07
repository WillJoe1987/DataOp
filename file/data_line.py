class data_line():

    def __init__(self, config):
        self.config = config

    def get_template(self):
        if hasattr(self.config,'template'):
            return self.config.template
        else :
            return ' '
