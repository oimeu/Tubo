import toml
from start import *
from client import *

print("Welcome to Tubo, terminal of NVTBT Videos in version 0.0.1! >//<\nTo know you Host, send 'ifconfig' in you terminal.\nTo help for commands, send help.")
notConnected = "Not connected"

checkConnection = "Not Connected" 
# Configurations of the toml

with open('config.toml', 'r') as f:
	config = toml.load(f)

print(config['network']['host'])
# Terminal Logic
while True:

    terminal = input("tubo ({})> ".format(checkConnection))

    parameter = terminal.split()

    if not parameter:
        continue

    command = parameter[0]
    parameterCommand = parameter[1:]

    match command:
        case "help":
            print("""
            help - Know commands from Tubo
            start - Start a NVTBT server
            connect HOST PORT - Connect a NVTBT server
            set - Set configure archive from $HOME/.config/Tubo
            """)
        case "exit":
            break
        case "start":
            run(config['network']['host'], config['network']['port'])
        case "set": 
            if len(parameterCommand) == 2:
                key = parameterCommand[0]
                value = parameterCommand[1]

                match key:
                    case "host":
                        print("Host set at {}".format(value))
                        config['network']['host'] = value
                    case "port":
                        print("Port set at {}".format(value))
                        config['network']['port'] = value
                    case _:
                        print("Unknown parameter")
            else:
                print("Error value")

            with open('config.toml', 'w') as f:
               toml.dump(config, f)

        case "connect":
            if len(parameterCommand) == 2:
                host = parameterCommand[0]
                port = int(parameterCommand[1])

                connect(host, port)
        case _:
            print("Unknown command.".format(command))

