import discord
import os
from replit import db
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	msg = message.content
	
	if msg.startswith('$help'):
		helpmessage = '''
$help - Shows this message
$cleardb - Clears the db, only doable by Tocas#5027
$add "key" "value" - Adds a key and a value to a db. If the key is already there, then it just appends the value to the list that corresponds to the key.
$fetch key - Gets the value of a key in the database
$del key - Deletes a key from the database
$listkeys - Lists the keys in the database
$listvalues - Lists the values in the database
$delvalue "key" "value" - Deletes a specific value from a list
'''
		await message.channel.send(helpmessage)

	if msg.startswith('$cleardb'):
		if message.author.id == 715658349382860802:
			for i in db.keys():
				del db[i]
			await message.channel.send("Cleared the db")
		else:
			await message.channel.send("bruh you're not tocas smh")
	
	if msg.startswith('$add '):
		rest = msg[5:]
		if rest.count('"') != 4:
			await message.channel.send("bruh format your command correctly smh")
		else:
			for i in range(len(rest)):
				if rest[i] == '"':
					key = rest[i+1:rest[i+1:].find('"')+1]
					rest = rest[rest[i+1:].find('"')+2:]
					break
			for i in range(len(rest)):
				if rest[i] == '"':
					value = rest[i+1:rest[i+1:].find('"')+2]
					break
			if key not in db.keys():
				db[key] = [value]
				await message.channel.send('Added ' + key + ' to the database as a key, with a value of ' + value)
			else:
				if value in db[key]:
					await message.channel.send("Bruh you can't add a value to a list twice")
				else:
					templist = list(db[key])
					templist.append(value)
					db[key] = templist
					await message.channel.send('Added ' + value + ' to the database as a part of ' + key + "'s list")
	
	if msg.startswith('$fetch '):
		rest = msg[7:]
		if rest in db.keys():
			await message.channel.send(list(db[rest]))
		else:
			await message.channel.send("smh that's not even in the database lol")
	
	if msg.startswith('$del '):
		rest = msg[5:]
		if rest in db.keys():
			del db[rest]
			await message.channel.send('Deleted ' + rest + ' from the database')
		else:
			await message.channel.send("Bruh this isn't even in the database smh")
	
	if msg.startswith('$listkeys'):
		await message.channel.send(list(db.keys()))
	
	if msg.startswith('$listvalues'):
		output = ''
		for i in db.keys():
			output += i + ': ' + str(list(db[i])) + '\n'
		await message.channel.send(output)
	
	if msg.startswith('$delvalue '):
		rest = msg[10:]
		if rest.count('"') != 4:
			await message.channel.send('bruh format your message properly smh')
		else:
			for i in range(len(rest)):
				if rest[i] == '"':
					key = rest[i+1:rest[i+1:].find('"')+1]
					rest = rest[rest[i+1:].find('"')+2:]
					break
			if key not in db.keys():
				await message.channel.send("bruh that key isn't even in the database")
			else:
				for i in range(len(rest)):
					if rest[i] == '"':
						value = rest[i+1:rest[i+1:].find('"')+2]
						break
				if value not in db[key]:
					await message.channel.send("bruh that value isn't in the list of the key")
				else:
					templist = db[key]
					templist.remove(value)
					db[key] = templist
					await message.channel.send("Deleted " + value + " from " + key + "'s list in the database")
	
	if msg.startswith('$embed'):
		embed = discord.Embed(
			title="hello!",
			description="cool description!",
			color=discord.Color.blue()
		)
		embed.add_field(name="cool field", value="cool field value")
		await message.channel.send(embed=embed)
	
	if msg.lower().startswith('$aime '):
		rest = msg[6:]
		try:
			if int(rest.split()[0]) < 1983 or int(rest.split()[0]) > 2020:
				await message.channel.send('bruh thats not a valid year')
				return
			elif int(rest.split()[0]) >= 1983 and int(rest.split()[0]) < 2000:
				if len(rest.split()) != 2:
					await message.channel.send('too many/not enough parameters')
					return
				elif int(rest.split()[1]) < 1 or int(rest.split()[1]) > 15:
					await message.channel.send('thats not a valid question number')
					return
				else:
					url = 'https://mathproblemdispenserbotstorage.web.app/AIME/' + rest.split()[0] + '/' + rest.split()[1] + '/statement.png'
			else:
				if len(rest.split()) != 3:
					await message.channel.send('too many/not enough parameters')
					return
				elif rest.split()[1].lower() != 'i' and rest.split()[1].lower() != 'ii':
					await message.channel.send('thats not a valid test number (i or ii)')
					return
				elif int(rest.split()[2]) < 1 or int(rest.split()[2]) > 15:
					await message.channel.send('thats not a valid question number')
					return
				elif rest.split()[1].lower() == 'i':
					url = 'https://mathproblemdispenserbotstorage.web.app/AIME/' + rest.split()[0] + '/1/' + rest.split()[2] + '/statement.png'
				else:
					url = 'https://mathproblemdispenserbotstorage.web.app/AIME/' + rest.split()[0] + '/2/' + rest.split()[2] + '/statement.png'
			await message.channel.send(url)
		except:
			await message.channel.send('an error happened somewhere along the processing of your command, are you sure you put in integers for the year and problem number?')

keep_alive()
client.run(os.environ['TOKEN'])