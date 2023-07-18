# Dopt Users Python Library

[![pypi](https://img.shields.io/pypi/v/dopt-users-python-client.svg)](https://pypi.python.org/pypi/dopt-users-python-client)
[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)

## Installation

Add this dependency to your project's build file:

```bash
pip install fern-dopt-users
# or
poetry add fern-dopt-users
```

## Usage

```python
from dopt.client import DoptUsers

client = DoptUsers(api_key="YOUR_API_KEY)
client.identify_user(
  identifier="my-user-id",
  properties={
    "bar": "foo"
  }
);
```

## Async Client

```python
import asyncio
from dopt.client import AsyncDoptUsers

async_client = AsyncDoptUsers(api_key="YOUR_API_KEY)

async def identify_user() -> None:
    client.identify_user(
      identifier="my-user-id",
      properties={
        "bar": "foo"
      }
    );

asyncio.run(identify_user())
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. Additions made directly to this library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest opening an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
