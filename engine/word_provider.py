"""TBD"""
import os
from random import randint
from typing import Dict, List


class RandomWordProvider:
    """Random word provider."""

    def __init__(self) -> None:
        self._categories = self._read_words()

    def _read_words(self) -> Dict[str, List[str]]:
        """Read random words from the file."""
        res = {}
        base_dir = os.path.expanduser("~/ext_src/progrock-stable/settings/")
        for filename in os.listdir(base_dir):
            category = filename.split(".")[0]
            with open(base_dir + filename, "r", encoding="utf-8") as handle:
                lines = handle.readlines()
            res[category] = lines
        return res

    def get_random_word(self, category: str) -> str:
        """Get a random word from the given category."""
        ind = randint(0, len(self._categories[category]) - 1)
        return self._categories[category][ind].strip()

    @property
    def adjective(self) -> str:
        """Get a random adjective."""
        return self.get_random_word("adjective")

    @property
    def artist(self) -> str:
        """Get a random artist."""
        return self.get_random_word("artist")

    @property
    def concept_artist(self) -> str:
        """Get a random concept artist."""
        return self.get_random_word("concept_artist")

    @property
    def genre(self) -> str:
        """Get a random genre."""
        return self.get_random_word("genre")

    @property
    def site(self) -> str:
        """Get a random site."""
        return self.get_random_word("site")

    @property
    def style(self) -> str:
        """Get a random style."""
        return self.get_random_word("style")
