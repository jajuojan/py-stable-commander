"""TBD"""

import os
from datetime import datetime

from engine.command import Command, CommandCollection
from engine.executor import BashShellExecutor
from engine.iteration_generator import IterationGenerator
from engine.word_provider import RandomWordProvider


def generate_output_dir() -> str:
    """Create the output directory."""
    date_time = datetime.now().strftime("%Y-%d-%m_%H-%M-%S")
    return os.path.abspath(f"output/{date_time}")


def create_random_collection(amount: int = 20) -> CommandCollection:
    """Create a randomized collection."""
    r_p = RandomWordProvider()
    collection = CommandCollection(output_directory=generate_output_dir())
    for _ in range(amount):
        collection.append(
            Command(
                prompt=f"something something, {r_p.adjective}, {r_p.adjective}, {r_p.adjective}, {r_p.genre}, {r_p.style}, art by {r_p.artist} and {r_p.artist} and {r_p.artist}"
            )
        )
    return collection


def create_inference_iteration_collection(command: Command) -> CommandCollection:
    """Create a collection of inference iterations."""

    collection = CommandCollection(
        output_directory=generate_output_dir(),
        commands=[command],
    )
    return IterationGenerator(collection).generate_inference_steps_iteration()


def create_strength_iteration_collection(command: Command) -> CommandCollection:
    """Create a collection of strength iterations."""

    collection = CommandCollection(
        output_directory=generate_output_dir(),
        commands=[command],
    )
    return IterationGenerator(collection).generate_strength_steps_iteration()


def _main() -> None:
    collection = create_random_collection(10)
    # collection = create_inference_iteration_collection(
    #    Command(
    #        "Something",
    #        seed=123,    )
    # )
    # collection = create_strength_iteration_collection(
    #    Command(
    #        "Something",
    #        seed=123,
    #        init_image="my_image.png",
    #        mask="my_image.png",
    #    )
    # )
    bash_command = BashShellExecutor(collection).execute()
    print(bash_command)


if __name__ == "__main__":
    _main()
