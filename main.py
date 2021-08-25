import discord
import os
from replit import db
from keep_alive import keep_alive
from discord.ext.commands import has_permissions

from discord.ext import commands

def get_prefix(client, message):
	if 'prefix' not in db.keys():
		db['prefix'] = dict()
	if str(message.guild.id) not in dict(db['prefix']):
		return '$'
	return str(dict(db['prefix'])[str(message.guild.id)])

client = commands.Bot(command_prefix = get_prefix)

client.remove_command('help')

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if 'prefix' not in db.keys():
        db['prefix'] = dict()

    if str(message.guild.id) in list(dict(db['prefix']).keys()):
        prefix = dict(db['prefix'])[str(message.guild.id)]
    else:
        prefix = '$'

    if msg.startswith('$cleardb'):
        if message.author.id != 715658349382860802 and message.author.id != 808401180980019211:
            await message.channel.send("Nice try but you're not Tocas or bobthefam")
            return
        for i in db.keys():
            del db[i]
        await message.channel.send("db cleared")

    if msg.startswith('$fetch '):
      	if message.author.id != 715658349382860802 and message.author.id != 808401180980019211:
        	await message.channel.send("Nice try but you're not Tocas or bobthefam")
        	return
      	await message.channel.send(dict(db[msg[7:]]))

    '''if msg.startswith(prefix + 'help'):
		helpmessage = discord.Embed(title="List of Commands",description="Math Problem Dispenser is an awesome discord bot made by Tocas#5027 and and bobthefam#6969. It can give you problems from a wide variety of contests, all while being clear and simple to use!",color=discord.Color.blue())
		
		helpmessage.add_field(name=prefix + "help", value="Shows this message", inline=False)

		#helpmessage.add_field(name=prefix + "amc8",value="Gives you an AMC 8 problem of your choice. The syntax is as follows: `" + prefix + "amc8 [year] [problem number from 1 to 25]`.", inline=False)


        helpmessage.add_field(name=prefix + 'amc12',value='Gives you an AMC 12 problem of your choice. The syntax is as follows: `' + prefix + 'amc12 [year] [a/b (only if year is 2002 and up)] [problem number from 1 to 25]`',inline=False)
		
		helpmessage.add_field(name=prefix + "aime",value="Gives you an AIME problem of your choice. The syntax is as follows: `" + prefix + "aime [year] [i/ii (only if year is 2000 and up)] [problem number from 1 to 15]`.",inline=False)
        await message.channel.send(embed=helpmessage)'''
    await client.process_commands(message)


@client.command()
@has_permissions(administrator = True)
async def prefix(ctx, content = None):
	if content == None:
		await ctx.send("Hallo what is the prefix?")

	else:
		a = dict(db['prefix'])
		a[ctx.guild.id] = content
		db['prefix'] = a
		await ctx.send('Prefix changed to `' +content + '`')


@client.command()
async def amc10(message, *, rest = None):
	if rest == None:
		await message.send("What AMC10 problem do you want?")
	else:
		try:
			if int(rest.split()[0]) < 2000 or int(rest.split()[0]) > 2019:
				await message.channel.send('thats not a valid year')
				return
			elif int(rest.split()[0]) < 2002:
				if len(rest.split()) != 2:
					await message.channel.send('thats not a valid format')
					return
				if int(rest.split()[1]) > 25 or int(rest.split()[1]) < 1:
					await message.channel.send('thats not a valid problem number')
					return
				else:
					url = 'https://mathproblemdispenserbotstorage.web.app/AMC/' + rest.split()[0] + '/10/' + rest.split()[1] + '/statement.png'
					await message.channel.send(url)
			else:
				if len(rest.split()) != 3:
					await message.channel.send('thats not a valid format')
					return
				if rest.split()[1].lower() != 'a' and rest.split()[1].lower() != 'b':
					await message.channel.send('for the second parameter, put either a or b')
					return
				if int(rest.split()[2]) > 25 or int(rest.split()[2]) < 1:
					await message.channel.send('thats not a valid problem number')
					return
				else:
					url = 'https://mathproblemdispenserbotstorage.web.app/AMC/' + rest.split()[0] + '/10' + rest.split()[1].upper() + '/' + rest.split()[2] + '/statement.png'
					await message.channel.send(url)
		except:
			await message.channel.send('something went wrong, are you sure you put integers for the year and problem number?')


@client.command()
async def amc12(message, *, rest = None):
	if rest == None:
		await message.send("What AMC12 problem do you want?")
	else:
		try:
			if int(rest.split()[0]) < 2000 or int(rest.split()[0]) > 2019:
				await message.channel.send('thats not a valid year')
				return
			elif int(rest.split()[0]) < 2002:
				if len(rest.split()) != 2:
					await message.channel.send('thats not a valid format')
					return
				if int(rest.split()[1]) > 25 or int(rest.split()[1]) < 1:
					await message.channel.send('thats not a valid problem number')
					return
				else:
					url = 'https://mathproblemdispenserbotstorage.web.app/AMC/' + rest.split()[0] + '/12/' + rest.split()[1] + '/statement.png'
					await message.channel.send(url)
			else:
				if len(rest.split()) != 3:
					await message.channel.send('thats not a valid format')
					return
				if rest.split()[1].lower() != 'a' and rest.split()[1].lower() != 'b':
					await message.channel.send('for the second parameter, put either a or b')
					return
				if int(rest.split()[2]) > 25 or int(rest.split()[2]) < 1:
					await message.channel.send('thats not a valid problem number')
					return
				else:
					url = 'https://mathproblemdispenserbotstorage.web.app/AMC/' + rest.split()[0] + '/12' + rest.split()[1].upper() + '/' + rest.split()[2] + '/statement.png'
					await message.channel.send(url)
		except:
			await message.channel.send('something went wrong, are you sure you put integers for the year and problem number?')


@client.command()
async def aime(message, *, rest = None):
	if rest == None:
		await message.send("What AIME problem do you want?")

	else:
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
					await message.channel.send(url)
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
					await message.channel.send(url)
				else:
					url = 'https://mathproblemdispenserbotstorage.web.app/AIME/' + rest.split()[0] + '/2/' + rest.split()[2] + '/statement.png'
					await message.channel.send(url)
		except:
			await message.channel.send('an error happened somewhere along the processing of your command, are you sure you put in integers for the year and problem number?')

@client.command()
async def add(message, *, rest=None):
	if 'attempt' not in db.keys():
		db['attempt'] = dict()
	if rest == None:
		await message.channel.send('Hallo where is the problem')
	
	else:
		if rest.split()[0].lower() not in ['aime', 'amc10', 'amc12', 'amc8']:
			await message.channel.send('Bruh thats not a valid contest')
			return
		if str(message.author.id) not in dict(db['attempt']).keys():
			db['attempt'][str(message.author.id)] = [[],[],[]] # lists are currently attempting, solved, and gave up.
		if rest.split()[0].lower() == 'aime':
			try:
				if int(rest.split()[1]) < 1983 or int(rest.split()[1]) > 2020:
					await message.channel.send('bruh thats not a valid year')
					return
				elif int(rest.split()[1]) >= 1983 and int(rest.split()[1]) < 2000:
					if len(rest.split()) != 3:
						await message.channel.send('too many/not enough parameters')
						return
					elif int(rest.split()[2]) < 1 or int(rest.split()[2]) > 15:
						await message.channel.send('thats not a valid question number')
						return
					else:
						url = 'https://mathproblemdispenserbotstorage.web.app/AIME/' + rest.split()[1] + '/' + rest.split()[2] + '/statement.png'
						await message.channel.send(url)
						await message.channel.send('Added AIME ' + rest.split()[1] + ', problem ' + rest.split()[2] + ' to your list of problems!')
						a = dict(db['attempt'])[str(message.author.id)]
						a[0].append('AIME/' + str(rest.split()[1]) + '/' + str(rest.split()[2]))
						db['attempt'][str(message.author.id)] = a
				else:
					if len(rest.split()) != 4:
						await message.channel.send('too many/not enough parameters')
						return
					elif rest.split()[2].lower() != 'i' and rest.split()[2].lower() != 'ii':
						await message.channel.send('thats not a valid test number (i or ii)')
						return
					elif int(rest.split()[3]) < 1 or int(rest.split()[3]) > 15:
						await message.channel.send('thats not a valid question number')
						return
					elif rest.split()[2].lower() == 'i':
						url = 'https://mathproblemdispenserbotstorage.web.app/AIME/' + rest.split()[1] + '/1/' + rest.split()[3] + '/statement.png'
						await message.channel.send(url)
						await message.channel.send('Added AIME ' + rest.split()[1] + ' i, problem ' + rest.split()[3] + ' to your list of problems!')
						a = dict(db['attempt'])[str(message.author.id)]
						a[0].append('AIME/' + str(rest.split()[1]) + '/1/' + str(rest.split()[3]))
						db['attempt'][str(message.author.id)] = a
					else:
						url = 'https://mathproblemdispenserbotstorage.web.app/AIME/' + rest.split()[1] + '/2/' + rest.split()[3] + '/statement.png'
						await message.channel.send(url)
						await message.channel.send('Added AIME ' + rest.split()[1] + ' ii, problem ' + rest.split()[3] + ' to your list of problems!')
						a = dict(db['attempt'])[str(message.author.id)]
						a[0].append('AIME/' + str(rest.split()[1]) + '/2/' + str(rest.split()[3]))
						db['attempt'][str(message.author.id)] = a
			except:
				await message.channel.send('an error happened somewhere along the processing of your command, are you sure you put in integers for the year and problem number?')
		elif rest.split()[0].lower() == 'amc10':
			try:
				if int(rest.split()[1]) < 2000 or int(rest.split()[1]) > 2019:
					await message.channel.send('thats not a valid year')
					return
				elif int(rest.split()[1]) < 2002:
					if len(rest.split()) != 3:
						await message.channel.send('thats not a valid format')
						return
					if int(rest.split()[2]) > 25 or int(rest.split()[2]) < 1:
						await message.channel.send('thats not a valid problem number')
						return
					else:
						url = 'https://mathproblemdispenserbotstorage.web.app/AMC/' + rest.split()[1] + '/10/' + rest.split()[2] + '/statement.png'
						await message.channel.send(url)
						await message.channel.send('Added AMC 10 ' + rest.split()[1] + ', Problem ' + rest.split()[2] + ' to your list of problems!')
						a = dict(db['attempt'])[str(message.author.id)]
						a[0].append('AMC/' + rest.split()[1] + '/10/' + rest.split()[2])
						db['attempt'][str(message.author.id)] = a
				else:
					if len(rest.split()) != 4:
						await message.channel.send('thats not a valid format')
						return
					if rest.split()[2].lower() != 'a' and rest.split()[2].lower() != 'b':
						await message.channel.send('for the second parameter, put either a or b')
						return
					if int(rest.split()[3]) > 25 or int(rest.split()[3]) < 1:
						await message.channel.send('thats not a valid problem number')
						return
					else:
						url = 'https://mathproblemdispenserbotstorage.web.app/AMC/' + rest.split()[1] + '/10' + rest.split()[2].upper() + '/' + rest.split()[3] + '/statement.png'
						await message.channel.send(url)
						await message.channel.send('Added AMC 10 ' + rest.split()[1] + rest.split()[2].upper() + ', Problem ' + rest.split()[3] + ' to your list of problems!')
						a = dict(db['attempt'])[str(message.author.id)]
						a[0].append('AMC/' + rest.split()[1] + '/10' + rest.split()[2].upper() + '/' + rest.split()[3])
						db['attempt'][str(message.author.id)] = a
			except:
				await message.channel.send('something went wrong, are you sure you put integers for the year and problem number?')
		elif rest.split()[0].lower() == 'amc12':
			try:
				if int(rest.split()[1]) < 2000 or int(rest.split()[1]) > 2019:
					await message.channel.send('thats not a valid year')
					return
				elif int(rest.split()[1]) < 2002:
					if len(rest.split()) != 3:
						await message.channel.send('thats not a valid format')
						return
					if int(rest.split()[2]) > 25 or int(rest.split()[2]) < 1:
						await message.channel.send('thats not a valid problem number')
						return
					else:
						url = 'https://mathproblemdispenserbotstorage.web.app/AMC/' + rest.split()[1] + '/12/' + rest.split()[2] + '/statement.png'
						await message.channel.send(url)
						await message.channel.send('Added AMC 12 ' + rest.split()[1] + ', Problem ' + rest.split()[2] + ' to your list of problems!')
						a = dict(db['attempt'])[str(message.author.id)]
						a[0].append('AMC/' + rest.split()[1] + '/12/' + rest.split()[2])
						db['attempt'][str(message.author.id)] = a
				else:
					if len(rest.split()) != 4:
						await message.channel.send('thats not a valid format')
						return
					if rest.split()[2].lower() != 'a' and rest.split()[2].lower() != 'b':
						await message.channel.send('for the second parameter, put either a or b')
						return
					if int(rest.split()[3]) > 25 or int(rest.split()[3]) < 1:
						await message.channel.send('thats not a valid problem number')
						return
					else:
						url = 'https://mathproblemdispenserbotstorage.web.app/AMC/' + rest.split()[1] + '/12' + rest.split()[2].upper() + '/' + rest.split()[3] + '/statement.png'
						await message.channel.send(url)
						await message.channel.send('Added AMC 12 ' + rest.split()[1] + rest.split()[2].upper() + ', Problem ' + rest.split()[3] + ' to your list of problems!')
						a = dict(db['attempt'])[str(message.author.id)]
						a[0].append('AMC/' + rest.split()[1] + '/12' + rest.split()[2].upper() + '/' + rest.split()[3])
						db['attempt'][str(message.author.id)] = a
			except:
				await message.channel.send('something went wrong, are you sure you put integers for the year and problem number?')


@client.command()
async def invite(message):
	embed = discord.Embed(title = "Invite Me!", description = "Press this [link](https://discord.com/api/oauth2/authorize?client_id=871519299716661259&permissions=8&scope=bot) to invite me! If you have any questions join this [server](https://discord.gg/43h85cwVXs) so we can help you out!")
	await message.channel.send(embed = embed)

@client.command()
async def support(ctx):
	embed = discord.Embed(title = "Questions?", description = "If you have any questions make sure to join our [support server](https://discord.gg/43h85cwVXs) and make sure to ask our staff questions!")
	await ctx.send(embed = embed)

@client.command()
async def avatar(ctx, member =None):
	if member != None:
		if member in ctx.guild.members:
			em = discord.Embed(description='requested by:\n{0}'.format(ctx.author))
			em.set_thumbnail(url=ctx.author.avatar_url)
			await ctx.send(embed = em)
		else:
			member = ctx.message.author
			em = discord.Embed(description='requested by:\n{0}'.format(ctx.author))
			em.set_thumbnail(url=member.avatar_url)
			await ctx.send(embed = em)
	else:
		em = discord.Embed(description='requested by:\n{0}'.format(ctx.author))
		em.set_thumbnail(url=ctx.author.avatar_url)
		await ctx.send(embed = em)

@client.command()
async def amc8(message, *, rest = None):
	if rest == None:
		await message.channel.send('hallo where is the info')
		return
	
	rest = rest.split()
	if len(rest) != 2:
		await message.channel.send('wrong number of params')
		return
	try:
		year = int(rest[0])
		problem = int(rest[1])
		if year < 1999 or year > 2020:
			await message.channel.send("invalid year")
			return
		if problem < 1 or problem > 25:
			await message.channel.send("invalid problem number")
			return
		await message.channel.send('https://mathproblemdispenserbotstorage.firebaseapp.com/amc8/' + str(year) + '/' + str(problem) + '.jpg')
	except:
		await message.channel.send('something went wrong, are you sure you put in two integers (year and problem number)?')

@client.command()
async def help(message, rest=None):
	helpmessage = discord.Embed(title="List of Commands",description="Math Problem Dispenser is an awesome discord bot made by Tocas#5027 and and bobthefam#6969. It can give you problems from a wide variety of contests, all while being clear and simple to use!",color=discord.Color.blue())
		
	helpmessage.add_field(name="help", value="Shows this message", inline=False)

	helpmessage.add_field(name="amc8",value="Gives you an AMC 8 problem of your choice. The syntax is as follows: `$amc8 [year] [problem number from 1 to 25]`.", inline=False)
	
	helpmessage.add_field(name='amc12',value='Gives you an AMC 12 problem of your choice. The syntax is as follows: `$amc12 [year] [a/b (only if year is 2002 and up)] [problem number from 1 to 25]`',inline=False)
		
	helpmessage.add_field(name="aime",value="Gives you an AIME problem of your choice. The syntax is as follows: `$aime [year] [i/ii (only if year is 2000 and up)] [problem number from 1 to 15]`.",inline=False)
	await message.channel.send(embed=helpmessage)


keep_alive()
client.run(os.environ['TOKEN'])
