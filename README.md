## Building from this repo

> **Important** this section should be removed from your version.

### Clone from this template

- visit this repo on GitHub
- select "Use this Template"
- create a unique name for your theme

### Replacing variables

There are some templates that you should replace with your variables.

`PACKAGE_NAME` - The name of the package (minus the "render_engine")
`PROJECT_NAME` - The proper name of the package (What you would see in the README TITLE)
`THEME_CLASS` - The name of the theme as it will be imported

> \*\*> [!WARNING]
> Reminder Remove this section

## How to use this theme

1. Install the theme

   ```python
   pip install <render_engine_PACKAGE_NAME>
   ```

2. Import the theme into your project

```python
from render_engine import Site
from <PACKAGE_NAME> import <THEME_CLASS>


app = Site()
app.register_theme(<THEME_CLASS>)
```
