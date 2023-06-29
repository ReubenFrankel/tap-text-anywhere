"""Custom client handling, including text-anywhereStream base class."""

from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from singer_sdk.streams import Stream

from tap_text_anywhere.files import FilesystemManager

if TYPE_CHECKING:
    import fsspec


class text_anywhereStream(Stream):
    """Stream class for text-anywhere streams."""

    @cached_property
    def filesystem(self) -> fsspec.AbstractFileSystem:
        """A fsspec filesytem.

        Raises:
            ValueError: If the supplied protocol is not supported.

        Returns:
            A fileystem object of the appropriate type for the user-supplied protocol.
        """
        return FilesystemManager(self.config, self.logger).get_filesystem()
