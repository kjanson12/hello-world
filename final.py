class Auto:
    def __init__(self):
        self.__make = input('Enter make of vehicle: ')
        self.__model = input('Enter model of vheicle: ')
        self.__color = input('Enter color of vehicle: ')
        self.__year = int(input('Enter year of vehicle: '))
        self.__mileage = int(input('Enter mileage of vehicle: '))
    def __str__(self):
        return('%d %s %s Color: %s Mileage: %d' % (self.__year, self.__make, self.__model, self.__color, self.__mileage))

inventory = []
def add():
    inventory.append(Auto())
def update(i):
    inventory[i] = Auto()
def remove(i):
    inventory.pop(i)

while 1==1:
    print("""
  1. Add auto
  2. Delete auto
  3. View all autos
  4. Update auto
  5. Export all autos to text file
  6. Exit
    """)
    ans = int(input('Which option do you choose? '))
    if ans == 1:
        add()
    elif ans == 2:
        remove(int(input('Which auto do you want to remove? '))-1)
    elif ans == 3:
        for i in inventory:
            print(i)
    elif ans == 4:
        update(int(input('Which auto do you want to update? '))-1)
    elif ans == 5:
        f = open('auto_inventory.txt', 'w')
        for i in inventory:
            f.write(str(i))
            f.write('\n')
        f.close()
    elif ans == 6:
        exit()

        
