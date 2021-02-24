from Engine import Engine


class DCEngine(Engine):
    def __init__(self) -> None:
        super().__init__()

    def start(self) -> None:
        super().start()

    def stop(self) -> None:
        super().stop()

    def getstatus(self) -> object:
        return super().getstatus()
