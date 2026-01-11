class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def change(self, channel_no):
        self.channel_no = channel_no

    def show_status(self):
        if self.is_on:
            return f'TV is on and channel number is: {self.channel_no}'
        else:
            return 'TV is off'