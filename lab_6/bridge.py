from abc import ABCMeta, abstractmethod


class Appliance(metaclass=ABCMeta):
    @abstractmethod
    def enabled(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class AC(Appliance):
    def __init__(self):
        self.enabled = False

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self._enabled = enabled

    def start(self):
        print('AC is ON successfully!!!')
        self.enabled = True

    def stop(self):
        print('AC is OFF successfully!!!')
        self.enabled = False


class Refrigerator(Appliance):
    def __init__(self):
        self.enabled = False

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self._enabled = enabled

    def start(self):
        print('Refrigerator is ON successfully!!!')
        self.enabled = True

    def stop(self):
        print('Refrigerator is OFF successfully!!!')
        self.enabled = False


class Fan(Appliance):
    def __init__(self):
        self.enabled = False

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self._enabled = enabled

    def start(self):
        print('Fan is ON successfully!!!')
        self.enabled = True

    def stop(self):
        print('Fan is OFF successfully!!!')
        self.enabled = False


class TV(Appliance):
    def __init__(self):
        self.enabled = False

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self._enabled = enabled

    def start(self):
        print('TV is ON successfully!!!')
        self.enabled = True

    def stop(self):
        print('TV is OFF successfully!!!')
        self.enabled = False


class GateOpener(Appliance):
    def __init__(self):
        self.enabled = False

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self._enabled = enabled

    def start(self):
        print('Gate is OPENED successfully!!!')
        self.enabled = True

    def stop(self):
        print('AC is CLOSED successfully!!!')
        self.enabled = False


class Switch(metaclass=ABCMeta):
    def __init__(self, appliance: Appliance):
        self.appliance = appliance

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class AutomaticRemoteController(Switch):
    def __init__(self, appliance: Appliance):
        super().__init__(appliance)

    def turn_on(self):
        print('Automatic Remote Controller has just worked')
        print('The one is trying to turn on an appliance . . .')
        if self.appliance.enabled:
            print('SOMETHING WENT WRONG!!!')
        else:
            self.appliance.start()

    def turn_off(self):
        print('Automatic Remote Controller has just worked')
        print('The one is trying to turn off an appliance . . .')
        if self.appliance.enabled:
            self.appliance.start()
        else:
            print('SOMETHING WENT WRONG!!!')


class ManualRemoteController(Switch):
    def __init__(self, appliance):
        super().__init__(appliance)

    def turn_on(self):
        print('Manual Remote Controller has just worked')
        print('The one is trying to turn on an appliance . . .')
        if self.appliance.enabled:
            print('SOMETHING WENT WRONG!!!')
        else:
            self.appliance.start()

    def turn_off(self):
        print('Manual Remote Controller has just worked')
        print('The one is trying to turn off an appliance . . . ')
        if self.appliance.enabled:
            self.appliance.start()
        else:
            print('SOMETHING WENT WRONG!!!')


# The client code
tv = TV()
ARC = AutomaticRemoteController(tv)
ARC.turn_off()

refrigerator = Refrigerator()
MRC = ManualRemoteController(refrigerator)
MRC.turn_on()
