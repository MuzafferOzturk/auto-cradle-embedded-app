from Enums import EngineStatusEnum


class Engine(object):
    __status = EngineStatusEnum.IDLE

    def __init__(self) -> None:
        super().__init__()

    def start(self) -> None:
        self.__status = EngineStatusEnum.START
        print('Start Engine')

    def stop(self) -> None:
        self.__status = EngineStatusEnum.STOP
        print('Stop Engine')

    def getstatus(self) -> object:
        return self.__status.name
