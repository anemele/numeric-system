import click

from .core import NS_int, decimal_to_gray, gray_to_decimal
from .log import logger


class OrderedGroup(click.Group):
    def list_commands(self, _):
        return self.commands.keys()


@click.group(cls=OrderedGroup)
def cli():
    """Numeric System.

    Convert any number with any format to another."""


@cli.command(name='int')
@click.argument('number')
@click.argument('to', type=int)
@click.option('--base', type=int, default=10)
@click.option('--char-set', required=False)
def convert_int(number: str, to: int, base: int, char_set: str | None = None):
    logger.debug(f'{number=}')
    logger.debug(f'{to=}')
    logger.debug(f'{base=}')
    logger.debug(f'{char_set=}')

    try:
        ret = NS_int(char_set).convert(number, to, base=base)
        print(f'({base}){number} --> {ret}')
    except (TypeError, ValueError) as e:
        print(e)


@cli.command(name='gray')
@click.argument('number', type=int)
@click.option('-t/--to-gray', is_flag=True, default=True)
@click.option('-f/--from-gray', is_flag=True, default=False)
def cli_gray(number: int, t: bool, f: bool):
    logger.debug(f'{number=}')
    logger.debug(f'{t=}')
    logger.debug(f'{f=}')

    if (t and f) or (not t and not f):
        logger.error('cannot set to and from flag in the same time')
        return

    if t:
        ret = decimal_to_gray(number)
    elif f:
        ret = gray_to_decimal(number)
    else:
        return
    print(f'{number} --> {ret}')
