from message import *
from printcommand import PrintCommand

if __name__ == '__main__':
    msg = Message("master@crow31415.net", "s2213536@s.tsukuba.ac.jp", "hogefugapiyo")
    print_cmd = PrintCommand()
    print_cmd.run(msg)
