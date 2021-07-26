# polybot-schema
[![Python package](https://github.com/AD-SDL/polybot-schema/actions/workflows/python-package.yml/badge.svg)](https://github.com/AD-SDL/polybot-schema/actions/workflows/python-package.yml)

Data Schemas ad Python Tools for the Polybot Project

## Organization

This repository will contain a few different definitions of the data formats:

- *JSON Schema*: [Single Source of Truth] Implementation of the Schema as a JSON file
- *Pydantic*: Implementation of the data format in Pydantic to faciliate the use of data in the format

We also include a few examples of the data to test the schemas in [`examples`](./examples)

## Testing
We perform several automated tests on each commit:

1. Ensure the JSON schemas are valid
2. Ensure the example data files validate properly with the JSON schemas
