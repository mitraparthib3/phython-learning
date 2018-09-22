# this program slices email username and domin name

print('hello there!')
email = input('type your email address here: ')
slicingPoint = email.index('@');
userName = email[:slicingPoint]
domainName = email[slicingPoint:].lstrip("@")

output = "your user name is {}. your domain is {}."

print(output.format(userName, domainName));
