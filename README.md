# `tap-text-anywhere`

text-anywhere tap class.

Built with the [Meltano Singer SDK](https://sdk.meltano.com).

## Capabilities

* `catalog`
* `state`
* `discover`
* `about`

## Settings

| Setting                | Required | Default | Description |
|:-----------------------|:--------:|:-------:|:------------|
| stream_name            | False    | file    | The name of the stream that is output by the tap. |
| protocol               | True     | None    | The protocol to use to retrieve data. One of `file` or `s3`. |
| filepath               | True     | None    | The path to obtain files from. Example: `/foo/bar`. Or, for `protocol==s3`, use `s3-bucket-name` instead. |
| file_regex             | False    | None    | A regex pattern to only include certain files. Example: `.*\.csv`. |
| s3_anonymous_connection| False    |       0 | Whether to use an anonymous S3 connection, without any credentials. Ignored if `protocol!=s3`. |
| AWS_ACCESS_KEY_ID      | False    | None    | The access key to use when authenticating to S3. Ignored if `protocol!=s3` or `s3_anonymous_connection=True`. Defaults to the value of the environment variable of the same name. |
| AWS_SECRET_ACCESS_KEY  | False    | None    | The access key secret to use when authenticating to S3. Ignored if `protocol!=s3` or `s3_anonymous_connection=True`. Defaults to the value of the environment variable of the same name. |
| caching_strategy       | False    | once    | *DEVELOPERS ONLY* The caching method to use when `protocol!=file`. One of `none`, `once`, or `persistent`. `none` does not use caching at all. `once` (the default) will cache all files for the duration of the tap's invocation, then discard them upon completion. `peristent` will allow caches to persist between invocations of the tap, storing them in your OS's temp directory. It is recommended that you do not modify this setting. |
| chunk_size             | False    | once    | Size of text chunks to make up a record. |
| chunk_overlap          | False    | None    | Overlap between the text chunks. |


A full list of supported settings and capabilities is available by running: `tap-text-anywhere --about`

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-text-anywhere --about
```

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

### Source Authentication and Authorization

<!--
Developer TODO: If your tap requires special access on the source system, or any special authentication requirements, provide those here.
-->

## Usage

You can easily run `tap-text-anywhere` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-text-anywhere --version
tap-text-anywhere --help
tap-text-anywhere --config CONFIG --discover > ./catalog.json
```

## Developer Resources

Follow these instructions to contribute to this project.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-text-anywhere` CLI interface directly using `poetry run`:

```bash
poetry run tap-text-anywhere --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

<!--
Developer TODO:
Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any "TODO" items listed in
the file.
-->

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-text-anywhere
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-text-anywhere --version
# OR run a test `elt` pipeline:
meltano elt tap-text-anywhere target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
