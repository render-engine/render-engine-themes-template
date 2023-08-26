# {{cookiecutter.theme_name}}

{{cookiecutter.description}}

## How to use this theme

1. Install the theme

   ```python
   pip install {{cookiecutter.project_name}}
   ```

2. Import the theme into your project

   ```python
   from render_engine import Site
   from {{cookiecutter.project_name}} import {{cookiecutter.theme_class}}

   app = Site()
   app.register_theme({{cookiecutter.theme_class}})
   ```
