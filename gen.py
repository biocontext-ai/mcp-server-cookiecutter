import os
import shutil

from cookiecutter.main import cookiecutter

# from cookiecutter.log import configure_logger
# configure_logger(stream_level="DEBUG")

BASE_DIR = os.path.dirname(__file__)

OUTPUT_DIR = os.path.join(BASE_DIR, "temp")

PACKAGE_NAME = "testmcp"

if not os.path.isdir(OUTPUT_DIR):
    # Create output dir
    os.mkdir(OUTPUT_DIR)


if os.path.isdir(os.path.join(OUTPUT_DIR, PACKAGE_NAME)):
    # Remove old code from temp dir
    shutil.rmtree(os.path.join(OUTPUT_DIR, PACKAGE_NAME))


cookiecutter(
    template=BASE_DIR,
    output_dir=OUTPUT_DIR,
    extra_context={
        "project_name": PACKAGE_NAME,
        "package_name": PACKAGE_NAME,
        "project_description": "This is a generated test mcp package.",
        "author_full_name": "Author1",
        "author_email": "author1@example.com",
        "github_user": "author1",
        "github_repo": "test-mcp",
    },
    no_input=True,
    overwrite_if_exists=True,
)
