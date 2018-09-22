# build a health potion for video game
# it will have differrernt difficulty levels
# uses varible, random module, print

import random;

initialHealth = 50;
highestLimit = 50;
lowerLimit = 25;
difficulty = 3; #1 easy and 3 hard
potionHealth = int(random.randint(lowerLimit, highestLimit) / difficulty); #force casting to int
health = initialHealth + potionHealth;
print('players difficulty', difficulty);
print('players health', health);
