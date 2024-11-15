# winzy-notify

[![PyPI](https://img.shields.io/pypi/v/winzy-notify.svg)](https://pypi.org/project/winzy-notify/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/winzy-notify?include_prereleases&label=changelog)](https://github.com/sukhbinder/winzy-notify/releases)
[![Tests](https://github.com/sukhbinder/winzy-notify/workflows/Test/badge.svg)](https://github.com/sukhbinder/winzy-notify/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/winzy-notify/blob/main/LICENSE)

Notify in mac and windows

## Installation

First configure your Winzy project [to use Winzy](https://github.com/sukhbinder/winzy).

Then install this plugin in the same environment as your Winzy application.
```bash
pip install winzy-notify
```
## Usage

To notify using this plugin, you can run the following command:
```bash
winzy notify [-t <title>] <message>
```

Where `<title>` is an optional parameter that specifies the title of the notification. If not provided, it defaults to "Notify".

Example usage:
```bash
winzy notify -t "Hello World" "This is a test message."
```

Even pipes work.

```bash
llm -s "Tell me a Joke" | winzy notify 
```

This will show the joke as notification.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd winzy-notify
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
