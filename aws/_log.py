import click


def success(message):
    click.echo(click.style(message, fg="green"))


def error(message):
    click.echo(click.style(message, fg="red"))


def warning(message):
    click.echo(click.style(message, fg="yellow"))


def info(message):
    click.echo(click.style(message, fg="blue"))
