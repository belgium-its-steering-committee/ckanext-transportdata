import click


@click.group(short_help="transportdata CLI.")
def transportdata():
    """transportdata CLI.
    """
    pass


@transportdata.command()
@click.argument("name", default="transportdata")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [transportdata]
