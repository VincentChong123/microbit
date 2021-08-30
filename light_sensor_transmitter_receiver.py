#board1 triggers board2 to transmit board2 light sensor reading to board1
#board1 then send the received value to excel program (where board1 connected to a windows10 PC)
#for board1 to read light level in a dark box that store board2

def on_received_number(receivedNumber):
    dataStreamer.write_number(receivedNumber)
    dataStreamer.write_line()
    basic.show_number(receivedNumber)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_string("A")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_string(receivedString)
    radio.send_number(input.light_level())
    music.play_tone(262, music.beat(BeatFraction.EIGHTH))
radio.on_received_string(on_received_string)

radio.set_group(22)
dataStreamer.set_baud_rate(BaudRate.BAUD_RATE9600)
basic.show_icon(IconNames.HEART)
