#! python3
# mapIt.py- launches a map in the browser using an address
# from the clipboard or command line
import webbrowser, sys

if len(sys.argv) > 1:
    # get address from command line.
    address = ''.join(sys.argv[1:])

# TODO: Get address from clipboard
