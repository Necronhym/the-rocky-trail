from engine.system import System


class BandCreationSystem(System):

    def on_start(self):

        print("Band Creation")
        print("-------------")
        print()

        band_name = input(
            "Band name: "
        )

        genre = input(
            "Genre: "
        )

        print()
        print(
            f"Welcome, {band_name}."
        )

        print(
            f"Genre: {genre}"
        )


def create(world):

    return BandCreationSystem(world)