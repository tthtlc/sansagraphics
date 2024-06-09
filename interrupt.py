import signal

def signal_handler(signal, frame):
        print('u pressed ctrl-c')
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
###signal.pause()
