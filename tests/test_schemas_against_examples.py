from pathlib import Path
import json

from jsonschema import Draft7Validator, RefResolver
from pytest import mark

schema_path = Path(__file__).parent / '../json'
example_path = Path(__file__).parent / '../examples'


def _make_validator(schema_name: str) -> Draft7Validator:
    with schema_path.joinpath(schema_name).open() as fp:
        schema_dict = json.load(fp)
    return Draft7Validator(schema_dict, resolver=RefResolver('file:///{}/'.format(schema_path), schema_dict))


@mark.parametrize(
    "example", ['template.json']
)
def test_template(example):
    validator = _make_validator('template.json')
    with example_path.joinpath(example).open() as fp:
        example_dict = json.load(fp)
    validator.validate(example_dict)
