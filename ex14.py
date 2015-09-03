from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s!  So good to see you." % user_name
print "How are you doing, %s? Are you doing well or poorly?" % user_name
status = raw_input(prompt)

if(status == "well"):
	print "I'm so glad to hear that %s." % user_name
elif(status == "poorly"):
	print "I'm so sorry to hear that %s." % user_name
else:
	print "idk wat to say to that"

print "Where would you prefer to be right now %s?" % user_name
where = raw_input(prompt)
if(where=="home"):
	print "omg me too"
else:
	print "Oh, cool"

print "And what would you prefer to be doing?"
what = raw_input(prompt)
if(what=="sleeping"):
	print "ughhh u killin me, me too!"
else:
	print "Hm, sounds nice."

print """
I wish we were in %r doing %r too, %r. 
""" % (where, what, user_name)