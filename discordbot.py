"""
Author          : Sumit Chhabra
Date            : 13-04-2020
Github username : sumcodex
Description     : The code is primarily creating the chatbot that mainly handles following:
                  a) Replies 'Hey' to 'Hi'
                  b) Query Google Search and returns top 5 results for the same.user has to
                     enter '!google <query>' to go for the searches.
                  c) Checks for recent queries entered by the user and returns matching results
                     as per the search history of the user.User has to enter '!recent 
                     <query to be matched>'.
"""
try:
    import discord
    from googlesearch import search
except ImportError:
    import sys
    print(sys.exc_info())
    sys.exit(1)


client = discord.Client()

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    # Replies 'Hey' to 'hi
    if message.content == "hi":
        await message.channel.send("hey")
    # Google Query Serach handling 
    elif message.content.startswith("!recent"):
        try:
            substring = message.content.split("!recent ")[1]
            f = list(open("query.txt", "r"))
            if len(f)>0:
                found = False
                await message.channel.send("Searching for matching recent queries....")
                for line in f:
                    if substring in line:
                        await message.channel.send("Matching Query Found : %s"%line)
                        found = True
                if not found:        
                        await message.channel.send("No matching query found!")
            else:
                await message.channel.send("No matching recent queries found!!")

        except:
            await message.channel.send("??")
    # Recent Query Search handling
    elif message.content.startswith("!google"):
        try:
            query=message.content.split("!google ")[1]
            f = open("query.txt", "a+")
            f.write("\n"+query)
            await message.channel.send("The top-5 google query result for %s are as follows:" % query)
            for search_q in search(query, tld='co.in', num=5, stop=5):
                await message.channel.send("%s"%search_q)
            f.close()
        except:
            await message.channel.send("??")
    else:
        await message.channel.send("??")


client.run('Njk4OTY3MTg4NDYzMTU3Mjg4.XpNjPw.y8zDFa_DKrjk7Z8CQKafiXqn24s')        
