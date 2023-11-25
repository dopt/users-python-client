# Dopt Users Python Library

[![pypi](https://img.shields.io/pypi/v/dopt-users-python-client.svg)](https://pypi.python.org/pypi/dopt-users-python-client)
[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://buildwithfern.com/?utm_source=dopt/users-python-client/readme)

## Installation

Add this dependency to your project's build file:

```bash
pip install dopt-users-python-client 
# or
poetry add dopt-users-python-client
```

## Usage

```python
from dopt.client import DoptApi

client = DoptApi(api_key="YOUR_API_KEY")
client.users.identify_user(
    identifier="todd_solondz",
    properties={
        "first_name": "todd",
        "last_name": "solondz",
    },
)
```

## Async Client

```python
import asyncio
from dopt.client import AsyncDoptApi

async_client = AsyncDoptApi(api_key="users-usersKey_Mw==")

async def identify_user() -> None:
    client.users.identify_user(
        identifier="todd_solondz",
        properties={
            "first_name": "todd",
            "last_name": "solondz",
        },
    )

asyncio.run(identify_user())
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. Additions made directly to this library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest opening an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!

