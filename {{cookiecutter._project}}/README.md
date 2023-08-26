# {{cookiecutter.theme_name}}

{{cookiecutter.theme_description}}

## How to use this theme

1. Install the theme
   ```python
   pip install {{cookiecutter.project}}
   ```

2. Import the theme into your project
   ```python
   from render_engine import Site
   from {{cookiecutter.project}} import {{cookiecutter.theme_class}}

   app = Site()
   app.register_theme({{cookiecutter.theme_class}})
   ```