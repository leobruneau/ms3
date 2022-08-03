import os
from copy import deepcopy
import pytest
from ms3 import Parse
from ms3.utils import first_level_subdirs

# Directory holding your clone of DCMLab/unittest_metacorpus
CORPUS_DIR = "~"


@pytest.fixture(scope="session")
def directory():
    """Compose the path for the test corpus."""
    path = os.path.join(os.path.expanduser(CORPUS_DIR), "unittest_metacorpus")
    if not os.path.isdir(path):
        print(f"Directory does not exist: {path} Clone DCMLab/unittest_metacorpus, checkout ms3_tests branch, "
              f"and specify CORPUS_DIR above.")
    assert os.path.isdir(path)
    return path

@pytest.fixture(
    scope="session",
    params=[
        "hidden_dirs",
        "regular_dirs",
        "everything",
        "chaotic_dirs",
    ]
)
def parse_obj(directory, request):
    if request.param.startswith('everything'):
        p = Parse(directory=directory)
        return p
    p = Parse()
    if request.param == "regular_dirs":
        for subdir in ['ravel_piano', 'sweelinck_keyboard', 'wagner_overtures']:
            add_path = os.path.join(directory, subdir)
            p.add_dir(add_path)
    if request.param == "chaotic_dirs":
        for subdir in ['mixed_files', 'outputs']:
            add_path = os.path.join(directory, subdir)
            p.add_dir(add_path)
    if request.param == "hidden_dirs":
        for subdir in ['.git', '.github']:
            add_path = os.path.join(directory, subdir)
            p.add_dir(add_path)
    return p

@pytest.fixture(
    scope="session",
    params=[
        0,
        1,
        2,
    ],
    ids=[
        "parsed_tsv",
        "parsed_mscx",
        "parsed_all",
    ],
)
def parsed_parse_obj(parse_obj, request):
    p = deepcopy(parse_obj)
    if request.param == 0:
        p.parse_tsv()
    elif request.param == 1:
        p.parse_mscx()
    elif request.param == 2:
        p.parse()
    else:
        assert False
    return p

@pytest.fixture(scope="class")
def parse_objects(parse_obj, request):
    request.cls.parse_obj = parse_obj

@pytest.fixture(scope="class")
def parsed_parse_objects(parsed_parse_obj, request):
    request.cls.parsed_parse_obj = parsed_parse_obj






