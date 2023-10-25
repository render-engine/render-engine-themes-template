import pathlib

from jinja2 import PackageLoader
from render_engine.utils.themes import Theme
# Add plugins here

{{cookiecutter._theme_name}} = Theme(
    loader=PackageLoader(f"{{cookiecutter.project_name}}", "templates"),
    static_dir= pathlib.Path(__file__).parent / "static",
    plugins = [],
    filters = {},
)