import time

class Cannon:
    def __init__(self, name, hp, ammo, power, fps):
        self.name = name
        self.hp = hp
        self.ammo = ammo
        self.power = power
        self.fps = fps
        self.print_status()
    
    def print_status(self):
        print('[status report]', self)

    def __str__(self):
        return f'{self.name}: hp={self.hp} | ammo={self.ammo} | power={self.power} | fps={self.fps}'

    def is_alive(self):
        return self.hp > 0

    def fire(self, target):
        if self.ammo <= 0:
            print(f'{self.name}: out of ammo')
            return
        if not target.is_alive():
            print(f'{target.name} is already dead.')
            return
        print(f'{self.name}: boom! -> {target.name}')
        self.ammo -= 1
        target.hp -= self.power
        if target.hp <= 0:
            print(f'{target.name}: is terminated.')
            target.hp = 0

    def fire_for_a_sec(self):
        delay = 1 /self.fps
        for _ in range(self.fps):
            if self.ammo > 0:
                print('boom')
                self.ammo -=1
                time.sleep(delay)
            else:
                print('out of ammo')
        print('ammo left:', self.ammo)

if __name__ == '__main__':
    me = Cannon('jh',100, 5, 25, 6)
    ta = Cannon('st', 200, 10, 5, 3)
    me.fire(ta)
    ta.fire(me)
    me.print_status()
    ta.print_status()
    me.fire_for_a_sec()
    ta.fire_for_a_sec()