"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_tap_test_class

from tap_text_anywhere.tap import Tap_text_anywhere

SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    # TODO: Initialize minimal tap config
}


# Run standard built-in tap tests from the SDK:
TestTap_text_anywhere = get_tap_test_class(
    tap_class=Tap_text_anywhere,
    config=SAMPLE_CONFIG,
)


# TODO: Create additional tests as appropriate for your tap.
