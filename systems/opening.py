import time

from engine.system import System


class OpeningSystem(System):

    def on_start(self):

        lines = [
            "You've had enough of your hometown.",
            "",
            "There is nothing left here but dead-end jobs,",
            "shitty bars, and the same three people",
            "complaining that there is no good music anymore.",
            "",
            "So you've decided to escape the only way that makes sense:",
            "",
            "FORM A BAND.",
            "",
            "Find some fellow degenerates.",
            "Buy a van.",
            "Write some songs.",
            "And hit the road.",
            "",
            "Maybe you'll make it big.",
            "",
            "Maybe you'll make enough money to afford gas.",
            "",
            "Either way...",
            "",
            "THE ROAD IS WAITING.",
        ]

        for line in lines:
            print(line)
            time.sleep(0.08)

        print()
        input("Press ENTER to continue...")
        print()


def create(world):

    return OpeningSystem(world)