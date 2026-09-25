from pathlib import Path

import tomllib

CONFIG_PATH = Path(__file__).with_name("units.toml")


def load_config():
    with CONFIG_PATH.open("rb") as file:
        return tomllib.load(file)


config = load_config()

metric = config["units"]["metric"]["factors"]
mass = config["units"]["mass"]["factors"]
temperature = list(
    config["units"]["temperature"]["units"].keys()
)

types = [
    list(metric.keys()),
    list(mass.keys()),
    temperature,
]

to_base = {
    **metric,
    **mass,
}
