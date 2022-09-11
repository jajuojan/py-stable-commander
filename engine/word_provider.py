"""TBD"""
import os
from random import randint
from typing import Dict, List, Optional


class RandomWordProvider:
    """Random word provider."""

    def __init__(self, source_directories: Optional[List[str]] = None) -> None:
        if source_directories is None:
            source_directories = ["~/ext_src/progrock-stable/settings/"]
        self._source_directories = self._process_source_directories(source_directories)
        self._categories = self._read_words()

    def _process_source_directories(self, source_directories: List[str]) -> List[str]:
        new_dirs = []
        for directory in source_directories:
            new_dirs.append(os.path.abspath(os.path.expanduser(directory)))
        print(new_dirs)
        return new_dirs

    def _read_words(self) -> Dict[str, List[str]]:
        """Read random words from the file."""
        # TODO: processing for non txt files
        # TODO: support for recursing into subdirectories
        # TODO: support for config (eg. flatten subdirs -> names)
        res = {}
        for base_dir in self._source_directories:
            for filename in os.listdir(base_dir):
                full_filename = os.path.join(base_dir, filename)
                if filename.endswith(".txt") and os.path.isfile(full_filename):
                    category = filename.split(".")[0]
                    with open(full_filename, "r") as filename:
                        lines = filename.readlines()
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
