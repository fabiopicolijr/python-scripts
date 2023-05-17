from termcolor import colored


def print_colored(*args, color=None, **kwargs):
    if color:
        colored_text = colored(" ".join(str(arg) for arg in args), color)
        print(colored_text, **kwargs)
    else:
        print(*args, **kwargs)
