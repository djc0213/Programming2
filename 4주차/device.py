class Device():
    name = None
    whatfor = None
    def instruct(self):
        print(f'{self.name} is for {self.whatfor}')

iphone = Device()
iphone.name = 'iPhone 13 Pro'
iphone.whatfor = 'phone call'
iphone.instruct()

keyboard = Device()
keyboard.name = 'Keychron K8'
keyboard.whatfor = 'input'
keyboard.instruct

mouse = Device()
mouse.name = 'MX vertical'
mouse.whatfor = 'pointing'
mouse.instruct()