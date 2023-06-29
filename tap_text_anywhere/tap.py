"""text-anywhere tap class."""

from __future__ import annotations

import os

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_text_anywhere import streams


class Tap_text_anywhere(Tap):
    """text-anywhere tap class."""

    name = "tap-text-anywhere"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "stream_name",
            th.StringType,
            required=False,
            default="file",
            description="The name of the stream that is output by the tap.",
        ),
        th.Property(
            "protocol",
            th.StringType,
            required=True,
            allowed_values=["file", "s3"],
            description="The protocol to use to retrieve data. One of `file` or `s3`.",
        ),
        th.Property(
            "filepath",
            th.StringType,
            required=True,
            description=(
                "The path to obtain files from. Example: `/foo/bar`. Or, for "
                "`protocol==s3`, use `s3-bucket-name` instead."
            ),
        ),
        th.Property(
            "file_regex",
            th.RegexType,
            description=(
                "A regex pattern to only include certain files. Example: `.*\\.csv`."
            ),
        ),
        th.Property(
            "s3_anonymous_connection",
            th.BooleanType,
            default=False,
            description=(
                "Whether to use an anonymous S3 connection, without any credentials. "
                "Ignored if `protocol!=s3`."
            ),
        ),
        th.Property(
            "AWS_ACCESS_KEY_ID",
            th.StringType,
            default=os.getenv("AWS_ACCESS_KEY_ID"),
            description=(
                "The access key to use when authenticating to S3. Ignored if "
                "`protocol!=s3` or `s3_anonymous_connection=True`. Defaults to the "
                "value of the environment variable of the same name."
            ),
        ),
        th.Property(
            "AWS_SECRET_ACCESS_KEY",
            th.StringType,
            default=os.getenv("AWS_SECRET_ACCESS_KEY"),
            description=(
                "The access key secret to use when authenticating to S3. Ignored if "
                "`protocol!=s3` or `s3_anonymous_connection=True`. Defaults to the "
                "value of the environment variable of the same name."
            ),
        ),
        th.Property(
            "caching_strategy",
            th.StringType,
            default="once",
            allowed_values=["none", "once", "persistent"],
            description=(
                "*DEVELOPERS ONLY* The caching method to use when `protocol!=file`. "
                "One of `none`, `once`, or `persistent`. `none` does not use caching "
                "at all. `once` (the default) will cache all files for the duration of "
                "the tap's invocation, then discard them upon completion. `peristent` "
                "will allow caches to persist between invocations of the tap, storing "
                "them in your OS's temp directory. It is recommended that you do not "
                "modify this setting."
            ),
        ),
        th.Property(
            "chunk_size",
            th.IntegerType,
            default="once",
            description=("Size of text chunks to make up a record."),
        ),
        th.Property(
            "chunk_overlap",
            th.IntegerType,
            description=("Overlap between the text chunks."),
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.text_anywhereStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [streams.TextStream(self, name=self.config["stream_name"])]


if __name__ == "__main__":
    Tap_text_anywhere.cli()
