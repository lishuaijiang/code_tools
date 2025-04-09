

class NotifierBase:
    def notify(self, *args, **kwargs):
        raise NotImplementedError("Please implement this method")
