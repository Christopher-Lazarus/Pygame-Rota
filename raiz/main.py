import pygame as pg


class Game:
    def __init__(self, title:str)->None:
        pg.init()
        self.__screen = pg.display.set_mode(SIZE, 0, 32)
        pg.set_label(title)
        self.__running = False

    @property
    def running(self) -> bool:
        return self.__running

    @running.set
    def running(self, valeu: bool) -> None:
        self.__running = value
    
    def __handle_events(self) -> None:
        for event in PG.event.get():
            if event.type == pg.QUIT:
                self.running = False
                return

    def __draw(self) -> None:
        if not self.running:
            return

        #
        pg.display.flip()
        self.__clock.tick(FPS)

    def start(self):
        self.running = True

        while self.__running:
            self.__handle_events()
            self.__draw()

        return self

    def finish(self) -> None:
        #
        pg.quit()


if __name__ == '__main__':
    Game('Jogo - Rotas')\
    .start()\
    .finish()