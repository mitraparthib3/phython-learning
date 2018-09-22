x = "hello"
lCount = x.count("l");
print(lCount);
#transform
print(x.lower());
print(x.upper());
print(x.capitalize());

print("hello world".title());

#check
print(x.islower());
print(x.isupper());
print(x.isalpha());
print(x.isdigit());
print("1234".upper());
print("1213gjgj".isalnum()) #alphanumeric

#index
print(x.index("l")); #substring
print(x.index("e")); #throws error, but .find method wont thorw error

#strip
print("0000hello0000".strip("0")); #.strip() removes all apaces around 
print("0000hello0000".lstrip("0"));
print("0000hello0000".rstrip("0"));

#slice
#variable[start:end:step]

y = "supermannBatman"

print(y[0:5:1])
print(y[5:9:1])

print(y[9:])

print(y[:5])

print(y[::-1])

# autoindex slice

word = "superbatboatmanfly"

findIndex = word.index("boat");
print(word[findIndex:])
