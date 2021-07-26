from jsonschema import Draft7Validator, RefResolver
from pathlib import Path
import json

# Find all the schemas
schema_path = Path(__file__).parent / '..' / 'json'
schemas = schema_path.rglob('*.json')

# Loop through to make sure they are all valid
for schema in schemas:
    print(f'Checking {schema.relative_to(schema_path)}...', end="")

    # Load in the schema
    with open(schema) as fp:
        schema = json.load(fp)

    # Pull in the references
    validator = Draft7Validator(Draft7Validator.META_SCHEMA,
                                resolver=RefResolver('file:///{}/'.format(schema_path), schema))
    validator.validate(schema)
    print('OK')
