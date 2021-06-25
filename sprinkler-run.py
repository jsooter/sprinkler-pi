import gpiozero
import sys
import time





def main(argv):
    ZONE = 0
    DURATION = 0
    if "-h" in argv or "--help" in argv:
        usage()
    if "-z" in argv:
        ZONE = argv[argv.index("-z")+1]
    if "--zone" in argv:
        ZONE = argv[argv.index("--zone")+1]
    if "-d" in argv:
        DURATION = argv[argv.index("-d")+1]
    if "--duration" in argv:
        DURATION = argv[argv.index("--duration")+1]


    if ZONE and DURATION:
        run(ZONE,DURATION)
    # Triggered by the output pin going high: active_high=True
    # Initially off: initial_value=False

    #relay = gpiozero.OutputDevice(RELAY_PIN, active_high=True, initial_value=False)

    #relay.off() # switch off

    #relay.on() # switch on

    #print(relay.value) # see if on or off

def usage():
    s = """ Usage
    python sprinkler-run.py --zone 5 --duration 15

    -h | --help    Display help text
    -z | --zone    Zone number
    -d | --duration    run time in minutes

    """
    print(s)

def run(zone,duration):
    DURATION = float(duration)
    t_end = time.time() + 60 * DURATION
    RELAY_PIN = zone
    
    relay = gpiozero.OutputDevice(RELAY_PIN, active_high=True, initial_value=False)
    
    print("zone {} on for {} minutes".format(zone,duration))
    
    while time.time() < t_end:
        relay.on()
        
    relay.off()
    print("zone {} off".format(zone))

if __name__ == "__main__":
    main(sys.argv[1:])