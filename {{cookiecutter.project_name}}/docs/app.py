from render_engine.collection import Collection
from render_engine.page import Page
from render_engine.parsers.markdown import MarkdownPageParser
from render_engine.site import Site

from {{cookiecutter.project_name}} import {{cookiecutter.__class_name}}

app = Site()
app.output_path = "docs/output"
app.site_vars.update ({
    "SITE_TITLE": f"{{Theme Name}}",
    "SITE_URL": "https://kjaymiller.github.io/render_engine_theme_kjaymiller/",
    "OWNER": {
        "name": f"{{cookiecutter.author}}",
        "email": f"{{cookiecutter.email}}",
    },
    "NAVIGATION": [
        {
            "text": "Docs",
            "url": "/docs.html",
        },
        {
            "test": "GitHub",
            "url": "https://github.com/kjaymiller/render_engine_kjaymiller_theme",
        }    
    ],
    "theme": {}
})
app.register_themes({{theme_name}})

@app.collection
class Docs(Collection):
    content_path = 'docs/pages'
    template = "page.html"
    Parser = MarkdownPageParser
    parser_extras = {"markdown_extras": ["fenced-code-blocks", "codehilite", "header-ids"]}
    has_archive = True
    archive_template = "blog_list.html"

@app.page
class Index(Page):
    template = "page.html"
    title = ""
    slug = "index"
    Parser = MarkdownPageParser
    content_path = "README.md"
    parser_extras = {"markdown_extras": ["fenced-code-blocks", "codehilite"]}
