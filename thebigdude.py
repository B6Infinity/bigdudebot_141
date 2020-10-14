import discord
from discord.ext import commands
import random
#import re
import json
from PIL import Image, ImageDraw
import os

client = commands.Bot(command_prefix='##')

# 761117900533661697 is not original 141 ID

server = client.get_guild(497085404529295391)

report_list = []
ban_list = []


checkrankhere_id = 733350151107772497
whoiswho_id = 765166961977327618
reporthere_id = 761886625130479636
op_id = 742801844274855986
interrogationward_id = 765169070805876746
dhatterimakichu_id = 733361383319666709

ROLES = {
    "Rookie": 723091423313788980,
    "Private": 760039583181307904,
    "Sergeant": 760039967878938644,
    "Lieutenant": 760040217649479721
}



def in_channel(*channels):
    def predicate(ctx):
        return ctx.channel.id in channels
    return commands.check(predicate)

'''
def FindURL(string): 
  
    # findall() has been used  
    # with valid conditions for urls in string 
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)       
    return [x[0] for x in url]'''

def findPercent(xp, level):
    
    #xp
    #level

    end_point = (level+1)**4
    start_point = level**4
    xp = xp - start_point
    end_point = end_point - start_point
    #start_point = start_point-start_point


    percentage = int((xp/end_point)*100)
    return percentage



##### INITIALISE BOT
@client.event
async def on_ready():
    activity = discord.Game(name="type '!BIG_help' or '!help' for a BIG help", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is BIG!")

# GET LANGUAGE AND STUFF
'''
@client.event
async def on_reaction_add(reaction, user):
    print("REACT")
    Channel = client.get_channel(764531845894373376)
    if reaction.message.channel.id == Channel:
        if reaction.emoji == '🔵':
            await reaction.message.channel.send("YES")
        

        #Role = discord.utils.get(user.server.roles, name="YOUR_ROLE_NAME_HERE")
        #await client.add_roles(user, Role)'''



#####




########### PART OF LEVEL UP FUNCTIONALITY: -

async def update_data(users, user):
    if not str(user.id) in users:
        users[str(user.id)] = {}
        users[str(user.id)]['name'] = user.name
        users[str(user.id)]['experience'] = 0
        users[str(user.id)]['level'] = 1
        users[str(user.id)]['reports'] = 0
        users[str(user.id)]['rank'] = 0
    role_names = [role.name for role in user.roles]
    users[str(user.id)]['roles'] = role_names
    users[str(user.id)]['profile_pic'] = str(user.avatar_url)

async def add_experience(users, user, exp):
    users[str(user.id)]['experience'] += exp

async def level_up(users, user, author):
    experience = users[str(user.id)]['experience']
    lvl_start = users[str(user.id)]['level']
    lvl_end = int(experience ** (1/4))
    
    if lvl_start < lvl_end:
        
        users[str(user.id)]['level'] = lvl_end
        congm = f"Ya know... You just leveled up on the TASK FORCE 141! Congrats dude! You're on level {lvl_end} now! Ain't that great! Keep typing! ⌨"

        if lvl_end == 2:
            await client.add_roles(author, ROLES['Rookie'])
        elif lvl_end == 8:
            await client.add_roles(author, ROLES['Private'])
        elif lvl_end == 18:
            await client.add_roles(author, ROLES['Sergeant'])
        elif lvl_end == 30:
            await client.add_roles(author, ROLES['Lieutenant'])
        
        
        
        
        

        await author.send(congm)

async def rank_update(users):
    xps = []
    names = []
    for user in users:
        xps.append(users[user]['experience'])
        names.append(user)

    #print(names, xps)
    #sort
    for j in range(len(xps)):
    #initially swapped is false
        swapped = False
        i = 0
        while i<len(xps)-1:
            #comparing the adjacent elements
            if xps[i]<xps[i+1]:
                #swapping
                xps[i],xps[i+1] = xps[i+1],xps[i]
                names[i],names[i+1] = names[i+1],names[i]
                #Changing the value of swapped
                swapped = True
            i = i+1
        #if swapped is false then the list is sorted
        #we can stop the loop
        if swapped == False:
            break
    #print(names, xps)
    #
    rank = 1
    for name in names:
        users[name]['rank'] = rank
        rank += 1
        
    
######### PART OF LEVEL UP FUNCTIONALITY: - !
###### REPORT PATROL ########


async def patrol_reports():
    with open('users.json', 'r') as f:
            users = json.load(f)
    
    '''
    for user in users:
        reports = users[user]['reports']
        if reports % 10 == 0 and reports!=0:
            users'''
    
    
    
    ops = []
    for user in users:
        if 'OP' in users[user]['roles']:
            ops.append(user)


    for user in users:
        reports = users[user]['reports']

        if reports % 10 == 0 and reports!=0:
            
            users[user]['reports'] += 1
            with open('users.json', 'w') as f:
                json.dump(users, f)

            name = users[user]['name']

            await client.get_channel(765169070805876746).send(f"***{name}*** has been reported ***{reports}* times** at ***TASK FORCE 141* HQ**... You might wanna **check it out and take action!**⚠⚠' <@&{op_id}>")
            '''
            for op in ops:
                msg = f'⚠⚠**KNOCK KNOCK!** Mr. OP? *{name}* has been reported ***{reports}* times** at ***TASK FORCE 141* HQ**... You might wanna **check it out and take action!**⚠⚠'
                #await client.get_role
                await client.get_user(int(op)).send(msg)'''
            
    

    
        


####### REPORT PATROL:  -  !




################ DISSY SHOITY

@client.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)
    ####CODE
    await update_data(users, member)
    with open('users.json', 'w') as f:
        json.dump(users, f)


@client.event
async def on_member_remove(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await client.get_channel(dhatterimakichu_id).send("https://tenor.com/viewdhat-teri-maa-ki-nawazuddin-siddiqui-nawaz-haraamkhor-shweta-tripathi-gif-18052201")
    
    await client.get_channel(dhatterimakichu_id).send(member.mention)
    if str(member.id) in users:
        users.pop(str(member.id))

    with open('users.json', 'w') as f:
        json.dump(users, f)





## ON MESSAGE

@client.event
async def on_message(msg):
    

    #if 'B6 Infinity' in msg.content:
    #   await msg.delete()

    
    ####### LEVEL TTHE SHIT! #############
    with open('users.json', 'r') as f:
        users = json.load(f)
    ####CODE
    if not msg.author.bot:
        await update_data(users, msg.author)

    role_names = [role.name for role in msg.author.roles]
    xpplus = 5
    if 'SPETSNAZ' in role_names:
        xpplus = 0
    
    
    if not msg.author.bot:
        await add_experience(users, msg.author, xpplus)
        await level_up(users, msg.author, msg.author)
        await rank_update(users)
    with open('users.json', 'w') as f:
        json.dump(users, f)
    ################ LEVELED! ##############
    
    await patrol_reports()

    ##### RANKED!##############

    if 'just left the server' in msg.content:
        if str(msg.author.id) == str(159985870458322944): 
            #if the speaker is MEE6
            
            await msg.channel.send("https://tenor.com/view/dhat-teri-maa-ki-nawazuddin-siddiqui-nawaz-haraamkhor-shweta-tripathi-gif-18052201")



    ######## MEE 6 SHUT UP

    if '!whocreatedBIGdude' in msg.content:
        await msg.channel.send("https://tenor.com/view/sab-janna-hai-is-bhadwe-ko-tvf-gif-18519512")
        await msg.channel.send(f"btw... I was coded by B6 :grin:")

    if "https://discord.gg/" in msg.content:
        await msg.delete()
        await msg.channel.send(f"Uhm... {msg.author.mention}, Sorry I had to delete that, because I thought you were sending links to somewhere... Which is not allowed here... sorry! 😅")

    

    if '!age' in msg.content:
        await msg.channel.send('Do I look like your birth-certificate? :unamused:')

    if '!leaderboard' in msg.content:
        if 'check-rank-here' not in str(msg.channel):
            await msg.channel.send(f"{msg.author.mention}\nDude! That `command` isn't supposed to be here! You are supposed to {client.get_channel(checkrankhere_id).mention}")
        else:
            leaderboard = ''

            with open('users.json', 'r') as f:
                users = json.load(f)
            
            count = 0
            for user in users:
                count += 1

            for i in range(1, count+1):
                for user in users:
                    if users[user]['rank'] == i:
                        leaderboard = leaderboard + f"**{users[user]['rank']}**. {users[user]['name']} **({users[user]['experience']}/({(users[user]['level']+1)**4})** \n"
            await msg.channel.send(leaderboard)

    if '!rank' in msg.content:
        if 'check-rank-here' not in str(msg.channel):
            await msg.channel.send(f"{msg.author.mention}\nDude! That `command` isn't supposed to be here! You are supposed to {client.get_channel(checkrankhere_id).mention}")
        else:
            with open('users.json', 'r') as f:
                users = json.load(f)

            # Drawing The Image
            
            total_w = 834
            total_h = 182
            width = 800
            height = 30

            image = Image.new('RGB', (total_w, total_h), (18, 57, 36))
            
            draw = ImageDraw.Draw(image)
            # Calculate The Percent Width
            



            percentage = findPercent(users[str(msg.author.id)]['experience'], users[str(msg.author.id)]['level'])
            percent_width = int((percentage/100) * width)

            draw.rectangle((0,0,percent_width,total_h), (4, 177, 67))
            image.save('UP.png')
            with open('UP.png', 'rb') as im:
                picture = discord.File(im)
            
            text = f"Yo! {msg.author.mention}, you are at level **{users[str(msg.author.id)]['level']}** with an experience of **{users[str(msg.author.id)]['experience']}/{(users[str(msg.author.id)]['level']+1)**4}**. Your rank is **{users[str(msg.author.id)]['rank']}**!... KEEP TYPING!"
            await msg.channel.send(file=picture, content=text)
            
            


    if '!BIG_help' in msg.content or '!help' in msg.content:
        embed = discord.Embed(title="THE BIG HELP IS HERE!", description="Think of this as the user manual of me, uhm THE BIG DUDE! uhm... the bo- you know what? you get it, right? okay...!", color = discord.Color.dark_gold())

        embed.add_field(name="SO HERE ARE SOME STUFF I CAN DO!...", value="Yeah... It's all me!", inline=False)
        embed.add_field(name="!rank", value="Place this in the #check-rank-here text channel and I'll tell your rank, exp and stuff in the server\nPS: If you type, you gain xp!", inline=False)
        embed.add_field(name="!leaderboard", value="Place this in the #check-rank-here text channel and I'll tell you the leaderboard of the server", inline=False)
        embed.add_field(name="##whois @<mention a dude>", value="Place this in the #who-is-who text channel and I'll tell you about the dude that you just mentioned\n(P.S: Look out for their favourite hobby! 🤭)", inline=False)
        embed.add_field(name="##report @<mention a bad guy>", value="Place this in the #report-here text channel and I'll accept your report and btw, tell your friends to report that bad guy as well! we only take action if that mentioned dude has like... 10 reports or so\n(P.S: DO NOT REPORT UNNECESSARILY! You could be in trouble for that, as you might be questioned by those in charge your reason to single report. We all want to keep this a good place...! ☺)", inline=False)
        embed.add_field(name="##del_report @<mention a good guy>", value="Place this in the #report-here text channel and I'll accept your negative report. This is basically deletion of a report from the total reports of that particular person. So if you think a guy is falsely accused, this is the command you're looking for!", inline=False)
        
        embed.add_field(name="DONTS", value="Type:-\n\n !whocreatedBIGdude\n!age", inline=False)

        embed.add_field(name="WHAT!?...", value="NOT ENOUGH TO PLEASE YOU, WELL THEN MAYBE ASK B6 TO UPDATE ME!", inline=False)
        embed.set_footer(icon_url = "", text = "Oh... and btw, if you feel troubled and did not get those stuff above 👆🏻, message m- NO! DON'T EVER DO THAT AGAIN! READ THE CHUNK OF TEXT AGAIN... OKAY? you are just thinking of requesting another of these messages aren't you you filthy human? Fine... I'm bound by 1s and 0s... GO ahead and I'll send you all these blabber once again and spam you... hehe 😁😐😑")
        
        await msg.author.send(embed=embed)
        embed.set_thumbnail(url = msg.author.avatar_url)
        #await msg.channel.send(embed=embed)
        await msg.channel.send(f"Ayo {msg.author.mention}! Check your DM!")
    
    
    await client.process_commands(msg)



@client.command(aliases=['user','info'])
#@commands.has_permissions(kick_members=True)
async def whois(ctx, member:discord.Member):

    if 'who-is-who' not in str(ctx.message.channel):
        
        await ctx.message.channel.send(f"This is not the place... to know {client.get_channel(whoiswho_id).mention}!")
    else:
        with open('users.json', 'r') as f:
            users = json.load(f)

        
        
        

        embed = discord.Embed(title=member.name, description = member.mention, color = discord.Color.green())
        embed.add_field(name = "ID", value = member.id, inline = True)
        role_names = [role.name for role in member.roles]
        #role_names = users[str(member.id)]['roles']
        if '@everyone' in role_names and len(role_names) == 1:
            role_names.remove('@everyone')
            role_names.append("~NO ROLES GIVEN~")
        embed.add_field(name = "Highest Role", value = role_names[len(role_names)-1], inline = True)

        random_verbs = ['eating', 'beating', 'screwing', 'drilling', 'molesting', 'clicking', 'knitting', 'clapping', 'slapping', 'kicking', 'kissing', 'cheering', 'blessing', 'praising', 'dominating', 'breaking', 'taking', 'scratching', 'bullying', 'shaking', 'cutting', 'chatting with', 'cursing', 'abusing', 'programming', 'bribing']
        random_nouns = ['it', 'children', 'elders', 'dogs', 'fishes', 'cats', 'men', 'males', 'women', 'grandparents', 'parents', 'computers', 'females', 'robots', 'americans', 'indians', 'terrorists', 'koreans', 'superstars']
        v = random_verbs[random.randint(0, len(random_verbs)-1)] + ' ' + random_nouns[random.randint(0, len(random_nouns)-1)]
        embed.add_field(name = "Favourite Hobby", value = v.upper(), inline = False)

            

        await update_data(users, member)
        with open('users.json', 'w') as f:
            json.dump(users, f)

        embed.add_field(name = "Experience", value = users[str(member.id)]['experience'], inline = False)
        embed.add_field(name = "Rank", value = users[str(member.id)]['rank'], inline = True)
        if users[str(member.id)]['reports'] >= 6:
            embed.add_field(name = "Reports", value = users[str(member.id)]['reports'], inline = False)
            
        embed.set_thumbnail(url = member.avatar_url)
            

        embed.set_footer(icon_url=ctx.author.avatar_url, text = f"Oh... I'm sorry... {ctx.author.name} requested this... 😐")
        await ctx.send(embed=embed)

@client.command()
async def report(ctx, member:discord.Member):
    #print(f"report accepted from {ctx.author.name}, reported: {member.id}, {member.name}!")
    if 'report-here' not in str(ctx.message.channel):
        
        await ctx.message.channel.send(f"HANDS UP!🔫 SOMEONE DOING BAD STUFF!? {client.get_channel(reporthere_id).mention}")
    else:

        if member.bot:
            await ctx.message.channel.send("Do you really think a bot can violate rules? :unamused:")
            await ctx.message.channel.send("Technology ain't there yet kiddo!")
        else:

            with open('users.json', 'r') as f:
                users = json.load(f)
            await update_data(users, member)
            users[str(member.id)]['reports'] += 1
            
            with open('users.json', 'w') as f:
                json.dump(users, f)
            if users[str(member.id)]['reports'] >= 8:
                
                await ctx.message.channel.send(f"Report accepted! You better get a lawyer {member.mention}!")
            else:
                await ctx.message.channel.send("Report accepted!")
            
@client.command()
async def clear_reports(ctx, member:discord.Member):
    if 'interrogation-ward' in str(ctx.message.channel):
        with open('users.json', 'r') as f:
            users = json.load(f)
        reps = users[str(member.id)]['reports']
        users[str(member.id)]['reports'] = 0
        with open('users.json', 'w') as f:
                json.dump(users, f)
        await client.get_channel(interrogationward_id).send(f"REMOVED {reps} REPORT(S) from {users[str(member.id)]['name']}")

@client.command()
async def del_report(ctx, member:discord.Member):
    if 'report-here' not in str(ctx.message.channel):
        
        await ctx.message.channel.send(f"HANDS DOWN!🔫 SOMEONE DOING GOOD STUFF!? {client.get_channel(reporthere_id).mention}")
    else:
        with open('users.json', 'r') as f:
            users = json.load(f)
        await update_data(users, member)
        if users[str(member.id)]['reports'] > 0:
            users[str(member.id)]['reports'] -= 1
            if users[str(member.id)]['reports'] % 10 == 0 and users[str(member.id)]['reports'] != 0:
                users[str(member.id)]['reports'] -= 1


            with open('users.json', 'w') as f:
                json.dump(users, f)

                
            await ctx.message.channel.send(f"Deducted! {member.mention} has {users[str(member.id)]['reports']} reports now!")
        else:
            await ctx.message.channel.send("Dude's reports are already at 0! STOP SPAMMING DUDE!!")
        
        with open('users.json', 'w') as f:
            json.dump(users, f)

@client.command()
async def givememe(ctx):
    #pass
    
    await ctx.message.channel.send(':construction_site: :construction: :negative_squared_cross_mark: :red_circle: :warning: ***COMMAND UNDER PROGRESS... CHECK BACK LATER WHEN ITS DONE!*** :construction_site: :construction: :negative_squared_cross_mark: :red_circle: :warning: ')
    
@client.command()
async def terminateBOT(ctx):
    if ctx.author.id == 497084701337714689 or ctx.author.id == 698788128500220016:
        await ctx.author.send("⚠⚠TERMINATING BOT RIGHT NOW!⚠⚠")
        quit()
    else:
        await ctx.message.channel.send("AHEM... WHO ARE YOU? :unamused:")

##commands: ytvid {stream youtube video}, reaction role to select languages




#run the client with the token
client.run(os.getenv('token'))
