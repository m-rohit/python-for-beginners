class Enemy:
    life = 3

    def attack(self):
        print("och!")
        self.life -=3

        def checkLife(self):
            if self.life <=0:
                print('I am dead')
            else:
                print(str(self.life) + "life left")

                enemy1 = Enemy()
                enemy2 = Enemy()

                enemy1.attack()
                enemy2.attack()
                enemy1.checkLife()
                enemy2.checkLife()