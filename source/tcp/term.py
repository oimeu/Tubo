import configparser 
#from start import *

print("Welcome to Tubo, terminal of NVTBT Videos in version 0.0.1! >//<\nTo know you Host, send 'ifconfig' in you terminal.\nTo help for commands, send help.")
notConnected = "Not connected"

while True:

    terminal = input("tubo > ")

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
           # case "start":
           # run()
        case "set": 
            if len(parameterCommand) == 2:
                key = parameterCommand[0]
                value = parameterCommand[1]

                match key:
                    case "host":
                        print("Host set at {}".format(value))
                    case "port":
                        print("Port set at {}".format(value))

                    case _:
                        print("Unknown parameter")
            else:
                print("Error value")
                
        case _:
            print("Unknown command.".format(command))

