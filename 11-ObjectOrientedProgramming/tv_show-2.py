from television import TV

def main():
    tv = TV()
    print(tv.show_status())
    tv.turn_on()
    print(tv.show_status())
    tv.show_channels()
    tv.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery'])
    tv.show_channels()
    tv.increase()
    tv.increase()
    tv.change(5)
    print(tv.show_status())
    tv.turn_off()
    print(tv.show_status())
main()