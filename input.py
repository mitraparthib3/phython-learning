# ask user for name
name = input('hey there! whats your name? : ')
# ask user for age
age = input('hello ' + name + '! whats your age? : ');
# ask user location
location = input('Where do you live ' + name + ' ? :'); 
# ask hobby
hobby = input('What do you do in free time ? :');
# create text
userGist = 'This is {}. I am {} old. I love to stay in {}. My hobby is {}';
finalString = userGist.format(name, age, location, hobby);
# print in output
print(finalString);
