import pathlib

from jinja2 import PackageLoader
from render_engine.utils.themes import Theme
# Add plugins here

<THEME_CLASS> = Theme(
    prefix = <PREFIX>,
    loader=PackageLoader(f"<PROJECT_NAME>", "templates"),
    static_dir= pathlib.Path(__file__).parent / "static",
    plugins = [],
    filters = {},
)
