from engine.engine import Engine


def main():
    engine = Engine()
    engine.load_systems()
    engine.start()


if __name__ == "__main__":
    main()