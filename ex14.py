from sys import argv

script, user_name = argv
prompt = '>'

print('Hello %s, I\'m the %s script' % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes =input(prompt)
print('where do you live %s'% user_name)
lives = input(prompt)
print('what kind of computer do you have %s'% user_name)
computer= input(prompt)

print("""
	Alright, so you said %r about liking me.
	you live in %r. Not sure where that is.
	And you hava a %r computer. Nice
	"""%(likes, lives, computer))