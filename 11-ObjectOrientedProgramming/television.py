class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels_list = []
        
    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False
    
    def show_status(self):
        if self.is_on:
            return f'TV is on and channel number is: {self.channel_no}'
        else:
            return 'TV is off'
    
    def set_channels(self, channels_list):
        for i in channels_list:
            self.channels_list.append(i)

    def show_channels(self):
        print('Channels list:')
        number = 1
        if not self.channels_list.empty():
          for i in self.channels_list:
            print(f'{number}. {i}')
            number += 1
        else:
            print('Set channels list')

    def change(self, new_channel_no):
        self.channel_no = new_channel_no

    