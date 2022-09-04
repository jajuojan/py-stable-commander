"""TBD"""
from typing import Callable, Optional, TypeVar

from engine.command import Command, CommandCollection

T = TypeVar("T", int, float)


class IterationGenerator:
    """Generate commands for an iteration."""

    def __init__(self, collection: CommandCollection):
        self._collection = collection
        self._check_input()
        self._base_command = self._collection.commands[0]

    def _check_input(self) -> None:
        """Check the input for the given command collection."""
        if len(self._collection.commands) != 1:
            raise ValueError("Collection length should be 1")

    def _iterate_over_steps(
        self,
        iteration_func: Callable[[Command, T], Command],
        start: T,
        stop: T,
        step: T,
    ) -> CommandCollection:
        new_collection = CommandCollection(
            output_directory=self._collection.output_directory
        )
        counter = start
        while counter <= stop:
            new_command = self._base_command.clone()
            new_command = iteration_func(new_command, counter)
            new_collection.append(new_command)
            counter += step

        return new_collection

    def generate_inference_steps_iteration(
        self, start: int = 1, stop: int = 32, step: int = 1
    ) -> CommandCollection:
        """Generate commands for an inference steps iteration."""

        def _inc_inference(command: Command, i: int) -> Command:
            command.num_inference_steps = i
            return command

        return self._iterate_over_steps(_inc_inference, start, stop, step)

    def generate_strength_steps_iteration(
        self, start: float = 0.0, stop: float = 1.0, step: float = 0.1
    ) -> CommandCollection:
        """Generate commands for a strength steps iteration."""
        # Todo: round the values to look nicer in CLI
        def _inc_strength(command: Command, i: Optional[float]) -> Command:
            command.strength = i
            return command

        return self._iterate_over_steps(_inc_strength, start, stop, step)

    def generate_guidance_scale_steps_iteration(
        self, start: float = 0.0, stop: float = 20.0, step: float = 1.0
    ) -> CommandCollection:
        """Generate commands for a guidance_scale steps iteration."""

        def _inc_guidance(command: Command, i: Optional[float]) -> Command:
            command.guidance_scale = i
            return command

        return self._iterate_over_steps(_inc_guidance, start, stop, step)


# TODO:
# init_image: Optional[str] = None
# mask: Optional[str] = None
