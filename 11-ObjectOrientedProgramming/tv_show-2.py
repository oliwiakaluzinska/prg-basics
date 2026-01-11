from television import TV

def main():
    tv = TV()
    print(tv.show_status())
    tv.turn_on()
    print(tv.show_status())
    print(tv.show_channels())
    tv.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery'])
    print(tv.show_channels())
    tv.change(5)
    print(tv.show_status())
    tv.turn_off()
    print(tv.show_status())
main()