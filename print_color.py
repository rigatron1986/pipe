COLOR = {
    'blue': '\033[94m',
    'default': '\033[99m',
    'grey': '\033[90m',
    'yellow': '\033[93m',
    'black': '\033[90m',
    'cyan': '\033[96m',
    'green': '\033[92m',
    'magenta': '\033[95m',
    'white': '\033[97m',
    'red': '\033[91m'
}


def print_with_color(message, color='red'):
    print(COLOR.get(color.lower(), COLOR['default']) + message)


print_with_color('hello colorful world!', 'magenta')
print_with_color('hello colorful world!', 'blue')
