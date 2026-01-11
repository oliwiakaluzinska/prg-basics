from television import TV

def main():
    tv = TV()
    tv.turn_on()
    print(tv.show_status())
    tv.turn_off()
    print(tv.show_status())
main()