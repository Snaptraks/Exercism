class InputCell:
    def __init__(self, initial_value):
        self._value = initial_value
        self.listeners = set()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if self._value != val:
            self._value = val
            for listener in self.listeners:
                listener.compute()

    def add_listener(self, listener):
        self.listeners.add(listener)


class ComputeCell(InputCell):
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        self.callbacks = set()
        self.listeners = set()

        for input_ in self.inputs:
            input_.add_listener(self)

    @property
    def value(self):
        return self.compute_function([input_.value for input_ in self.inputs])

    def add_callback(self, callback):
        self.callbacks.add(callback)

    def remove_callback(self, callback):
        self.callbacks.discard(callback)

    def compute(self):
        for callback in self.callbacks:
            callback(self.value)
