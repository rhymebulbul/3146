from microbit import *
"""
Samples data from sensors periodically,
Outputs sensor name & data via serial
"""
sample_count = 0
download = Image('07870:''07870:''78887:''07870:''00700:')
tick = Image('00007:''00077:''70770:''77700:''07000:')
cross = Image('70007:''07070:''00700:''07070:''70007:')
# Image formats to display progress
while True:
    #elapsed = running_time()
    l = display.read_light_level()
    # Reads in light level
    if l:
        display.show(sample_count % 10)
        # Increments sample count
        print("light")
        # Outputs sensor type to serial
        sleep(500)
        print(l)
        display.show(download)
        # Outputs data to serial
        sample_count += 1
        sleep(500)
        display.show(tick)
        # Confirms progress on display
    else:
        display.show(cross)
    sleep(3599000)

    t = temperature()
    # Reads in temperature level
    if t:
        display.show(sample_count % 10)
        # Increments sample count
        print("tempe")
        # Outputs sensor type to serial
        sleep(500)
        print(t)
        display.show(download)
        # Outputs data to serial
        sample_count += 1
        sleep(500)
        display.show(tick)
        # Confirms progress on display
    else:
        display.show(cross)
    sleep(3599000)
