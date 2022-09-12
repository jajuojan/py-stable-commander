"""TBD"""

from engine.command import CommandCollection
from engine.seed import get_random_seed


# pylint: disable=too-few-public-methods
class BashShellExecutor:
    """Execute a command collection."""

    def __init__(self, collection: CommandCollection):
        self._collection = collection

    def execute(self) -> str:
        """Execute the given command collection."""
        return self._generate_bash_commnand(self._collection)

    def _generate_bash_commnand(self, collection: CommandCollection) -> str:
        """Generate commands for the given prompts."""
        lines = [f"mkdir -p {collection.output_directory}"]
        counter = 1
        for command in collection.commands:
            seed_a = command.seed if command.seed is not None else get_random_seed()
            output_file = (
                command.output_file
                if command.output_file is not None
                else collection.file_name_for_command(command)
            )

            init_image = (
                ""
                if command.init_image is None
                else f" --init-image {command.init_image}"
            )
            mask = "" if command.mask is None else f" --mask {command.mask}"
            strength = (
                "" if command.strength is None else f" --strength {command.strength}"
            )
            num_inference_steps = (
                ""
                if command.num_inference_steps is None
                else f" --num-inference-steps={command.num_inference_steps}"
            )
            guidance_scale = (
                ""
                if command.guidance_scale is None
                else f" --guidance-scale {command.guidance_scale}"
            )
            lines.append(
                f'python demo.py --prompt "{command.prompt}" --output "{output_file}" --seed={seed_a}{init_image}{mask}{strength}{num_inference_steps}{guidance_scale}'.strip()
            )
            counter += 1
        return "\n".join(lines)
