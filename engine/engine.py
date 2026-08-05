from pathlib import Path
import importlib.util

from engine.world import World


class Engine:

    def __init__(self):
        self.world = World()
        self.systems = []

        self.system_directory = (
            Path(__file__).parent.parent / "systems"
        )

    def load_systems(self):

        for path in self.system_directory.glob("*.py"):

            if path.name.startswith("_"):
                continue

            self._load_system(path)

    def _load_system(self, path):

        module_name = f"system_{path.stem}"

        spec = importlib.util.spec_from_file_location(
            module_name,
            path
        )

        if spec is None or spec.loader is None:
            raise RuntimeError(
                f"Could not load system: {path}"
            )

        module = importlib.util.module_from_spec(spec)

        spec.loader.exec_module(module)

        if not hasattr(module, "create"):
            raise RuntimeError(
                f"System '{path.name}' "
                f"does not expose create()"
            )

        system = module.create(
            self.world
        )

        self.systems.append(system)

    def start(self):

        print("================================")
        print("        ROCKY TRAIL")
        print("================================")
        print()

        for system in self.systems:

            if hasattr(system, "on_start"):
                system.on_start()