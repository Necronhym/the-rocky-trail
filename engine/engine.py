from pathlib import Path
import importlib.util

import yaml

from engine.world import World


class Engine:

    def __init__(self):

        self.world = World()
        self.systems = []

        self.root = Path(__file__).parent.parent

        self.system_directory = (
            self.root / "systems"
        )

        self.config_path = (
            self.root
            / "config"
            / "conf.yaml"
        )

    def load_systems(self):

        with open(
            self.config_path,
            "r",
            encoding="utf-8"
        ) as file:

            config = yaml.safe_load(file)

        systems = config.get(
            "systems",
            []
        )

        for system_config in systems:

            name = system_config["name"]
            phase = system_config["phase"]

            path = (
                self.system_directory
                / f"{name}.py"
            )

            if not path.exists():

                raise FileNotFoundError(
                    f"Configured system "
                    f"'{name}' does not exist: "
                    f"{path}"
                )

            system = self._load_system(path)

            system.phase = phase

            self.systems.append(system)

    def _load_system(self, path):

        module_name = (
            f"system_{path.stem}"
        )

        spec = (
            importlib.util
            .spec_from_file_location(
                module_name,
                path
            )
        )

        if (
            spec is None
            or spec.loader is None
        ):

            raise RuntimeError(
                f"Could not load system: "
                f"{path}"
            )

        module = (
            importlib.util
            .module_from_spec(spec)
        )

        spec.loader.exec_module(module)

        if not hasattr(
            module,
            "create"
        ):

            raise RuntimeError(
                f"System '{path.name}' "
                "does not expose create()"
            )

        return module.create(
            self.world
        )

    def get_systems_by_phase(
        self,
        phase
    ):

        return [
            system
            for system in self.systems
            if system.phase == phase
        ]

    def start(self):

        print(
            "================================"
        )

        print(
            "          ROCKY TRAIL"
        )

        print(
            "================================"
        )

        print()

        startup_systems = (
            self.get_systems_by_phase(
                "startup"
            )
        )

        for system in startup_systems:

            if hasattr(
                system,
                "on_start"
            ):

                system.on_start()