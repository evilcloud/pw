import click

@click.command()
@click.argument('location')
@click.option('--fuck', '-f', is_flag=True, help='Profanity mode')
@click.option('--username', '-u', is_flag=True, help='Generates username of up to 10 charachters long (not placed into the cliboard)')

def main(location, fuck, username):
    print(f"I'm a beautiful CLI ✨\nand the location is {location}\nProfanity: {fuck}")

if __name__ == "__main__":
    main()