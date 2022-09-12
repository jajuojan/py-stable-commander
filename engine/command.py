"""TBD"""

import dataclasses
from dataclasses import dataclass, field
from typing import List, Optional, Union

from engine.seed import get_random_seed


# pylint: disable=too-many-instance-attributes
@dataclass
class Command:
    """Command to be executed."""

    prompt: str
    output_file: Optional[str] = None
    seed: int = field(default_factory=get_random_seed)
    init_image: Optional[str] = None
    mask: Optional[str] = None
    strength: Optional[float] = None
    num_inference_steps: Optional[int] = None
    guidance_scale: Optional[float] = None

    def clone(self) -> "Command":
        """Clone the command."""
        clone = Command(self.prompt + "")
        for key, value in dataclasses.asdict(self).items():
            setattr(clone, key, value)
        return clone


@dataclass
class CommandCollection:
    """Collection of commands to be executed."""

    commands: List[Command] = field(default_factory=lambda: [])
    output_directory: Optional[str] = None

    def append(self, command: Command) -> None:
        """Append a Command to the collection."""
        self.commands.append(command)

    def file_name_for_command(
        self, command: Union[Command, int], injection: Optional[str] = None
    ) -> str:
        """Get the file name for the given command."""
        if isinstance(command, int):
            command = self.commands[command]
        if command.output_file is not None:
            return command.output_file
        if command in self.commands:
            if injection is None:
                injection = ""
                if command.strength is not None:
                    injection += f"__strength_{command.strength}"
                if command.num_inference_steps is not None:
                    injection += f"__steps_{command.num_inference_steps}"
            return f"{self.output_directory}/{self.commands.index(command)+1:03}{injection}.png"
        raise ValueError("Command not found in collection.")
