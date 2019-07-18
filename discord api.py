import discord
import re
import tokens

TOKEN = tokens.getToken()

client = discord.Client()
replace_with = '!@#$%^&*()\':;.,><UwU--_--=+`~\|][}{[/?'

def vulgar(msg):
    bad = False
    clean_msg = None 
    temp_msg = re.sub(r"[^a-zA-Z0-9]+", '', msg.lower())
    
    for i in banned:
        if i in temp_msg:
            if bad:
                temp_msg = clean_msg
            start = temp_msg.find(i)
            p_start = min(temp_msg[:start].find(" "),start)
            if p_start != -1:
                start = p_start
            else: 
                start =0
                
            end = max(temp_msg[start:].find(" "),len(temp_msg))
            potential = temp_msg[start:end]

            if potential.strip() not in white_list:
                clean_msg = re.sub(re.escape(i), replace_with[:len(i)-1],temp_msg)
                bad = True



    if bad:
        return clean_msg

    return bad



@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    cleaned_msg = vulgar(message.content.lower())
    if cleaned_msg:
        await client.delete_message(message)
        cleaned_msg = 'Watch your mouth! {0.author.mention}:\n <{1}>'.format(message,cleaned_msg)
        await client.send_message(message.channel, cleaned_msg)
    
        


banned=set()
white_list = set()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
    with open('BadWords.txt','r') as bad_words:
        for line in bad_words:
            banned.add(line.strip())
    with open('whitelist.txt','r') as white:
        for line in white:
            white_list.add(line.strip().lower())


client.run(TOKEN)