from pathlib import Path
from jinja2 import Environment, FileSystemLoader

project_path = Path(__file__).resolve().parent.parent

templates_path = project_path / "templates"

env = Environment(
    loader=FileSystemLoader(templates_path)
)

template = env.get_template("newsletter_template.html")


def render_newsletter(kpis):

    rendered_html = template.render(**kpis)

    output_path = project_path / "output"
    output_path.mkdir(exist_ok=True)

    output_file = output_path / "weekly_newsletter.html"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(rendered_html)

    print("Newsletter created successfully!")
    print(output_file)
