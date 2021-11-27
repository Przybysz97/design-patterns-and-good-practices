class Singleton:
    _INSTANCE = None

    def __init__(self):
        raise NotImplementedError('Creation of singleton instance with constructor is forbidden')

    @classmethod
    def get_instance(cls):
        if not cls._INSTANCE:
            cls._INSTANCE = cls.__new__(cls)
        return cls._INSTANCE


if __name__ == '__main__':
    instance_1 = Singleton.get_instance()
    instance_2 = Singleton.get_instance()
    assert instance_1 is instance_2
