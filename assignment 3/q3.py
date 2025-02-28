import random


class Ecosystem:
    def __init__(self, river_length, num_fish, num_bears):
        # Initialize the river
        self.river = [None] * river_length

        # Populate the river with fish and bears
        
       
            
        # Fish are represented by 'F', bears are represented by 'B', 'N' represents an empty space
        # Todo: randomly place the fish and bears in the river
        
        for i in range (num_fish):
            location = random.randint(0,river_length -1)#Take a random space in the river
            while self.river[location] is not None:# If the place has already been occupied
                location = random.randint(0,river_length -1)# Try again
            self.river[location] = 'F'

        for i in range (num_bears):# The same as above
            location = random.randint(0,river_length -1)
            while self.river[location] is not None:
                location = random.randint(0,river_length -1)
            self.river[location] = 'B'

        # display the initial river
        print(self.display_river())

    def simulate(self, steps):
        for _ in range(steps):
            # Create a copy of the river to update animals' positions
            new_river = self.river.copy()
            old_river = self.river

            # Todo: move the animals in the river
            for i in range(len(self.river)):
              
              # The fish is mainly the same of the bear, just chek the comment above
              if (self.river[i] == 'F' and old_river[i] != None ) or (self.river[i] == 'B' and old_river[i] == 'B'):
                    move_direction = random.choice([-1, 0, 1])# Randomly choice its direction to moves
                    new_location = i + move_direction# define the new location
                    
                    if 0 <= new_location < len(self.river) and self.river[new_location] is None:
                        new_river[new_location] = self.river[i]
                        self.river[i] = None
                        new_river[i] = None
                         
                    elif self.river[i]== 'F':
                        if 0 <= new_location < len(self.river) and self.river[new_location] == 'B' and new_location != i :#When the fish meet the bear
                            new_river[i] = None# The fish die
                            self.river[i] = None
                        elif 0 <= new_location < len(self.river) and self.river[new_location] == 'F' and new_location != i:
                            empty_indices = [j for j in range(len(self.river)) if new_river[j] is None]
                            if empty_indices:
                                new_animal_index = random.choice(empty_indices)
                                new_river[new_animal_index] = 'F'
                                
                                
                    elif self.river[i] == 'B':# If it is a bear
                    
                        if 0 <= new_location < len(self.river) and self.river[new_location] == 'B' and new_location != i:#If the animal is about to mate
                            empty_indices = [j for j in range(len(self.river)) if self.river[j] is None]#Find all the empty space
                            if empty_indices:#If there is any empty space
                                new_animal_index = random.choice(empty_indices)# Randomly choice its birthplace
                                new_river[new_animal_index] = 'B'# Assign the chosen place with this type of animal
                                old_river[new_animal_index] = 'B'
                        elif 0 <= new_location < len(self.river) and self.river[new_location] == 'F' and new_location != i:#If the bear meet the fish
                             new_river[new_location] = 'B'# Now stand the bear
                             new_river[i] = None# The bear is moved
                    
              self.river = new_river 
                        
                    
                        
                    
              
              
            # Update the river state
            self.river = new_river

            # desplay the river
            print(self.display_river())

    def display_river(self):
        return ''.join(['N' if x is None else x for x in self.river])


if __name__ == '__main__':
    # Example usage
    ecosystem = Ecosystem(river_length=3, num_fish=1, num_bears=1)  # River of length 10, with 3 fish and 2 bears
    ecosystem.simulate(steps=2)
    ecosystem = Ecosystem(river_length=10, num_fish=3, num_bears=2)  # River of length 10, with 3 fish and 2 bears
    ecosystem.simulate(steps=5)
    ecosystem = Ecosystem(river_length=8, num_fish=2, num_bears=1)  # River of length 10, with 3 fish and 2 bears
    ecosystem.simulate(steps=10)
    ecosystem = Ecosystem(river_length=10, num_fish=3, num_bears=2)  # River of length 10, with 3 fish and 2 bears
    ecosystem.simulate(steps=10)
