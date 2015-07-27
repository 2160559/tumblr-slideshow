from jinja2 import Environment, FileSystemLoader

import click
import json

@click.command()
def make_slideshow():
    """Creates a reveal.js presentation from a scraped Tumblr blog"""
    # Load the JSON post data
    with open('data.json') as posts_file:    
        posts = json.load(posts_file)

    env = Environment(loader=FileSystemLoader('reveal'))
    template = env.get_template('index.html')
    template.stream(posts=posts).dump('reveal/slideshow.html')

    click.echo("ALL DONE")

if __name__ == '__main__':
    make_slideshow()