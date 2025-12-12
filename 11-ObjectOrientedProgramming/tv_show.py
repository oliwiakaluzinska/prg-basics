from tv import TV

def main():
    my_tv = TV()
    
    # Show the TV status (initially off)
    my_tv.show_status()
    
    # Turn the TV on and show the status
    my_tv.turn_on()
    my_tv.show_status()
    
    # Turn the TV off and show the status
    my_tv.turn_off()
    my_tv.show_status()
if __name__ == "__main__":
   main() 