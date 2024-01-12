import click 
import secrets
import string

@click.command()
@click('--length', default=20, help='Length of the generated strong password')
def strong_password(length):
    """Generates a strong random password."""
    password = strong_password(length)
    click.echo(f"Strong password: {password}")

def generate_strong_password(length):
    """Generates a strong password."""
    characters =  string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


