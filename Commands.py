import DataHandler
import asyncio

async def check_clear(text, message, username, user_id):
    if text == "/clear":
        await message.channel.send("Clearing messages for last 14 days...")
        async for current_message in message.channel.history():
            await current_message.delete()
            
async def check_cookie(text, message, username, user_id):
    cookie_commands = DataHandler.static_data["give_cookie"]
    if text in cookie_commands:
        print(DataHandler.dynamic_data['cookie count'],user_id)
        try:
            DataHandler.dynamic_data['cookie count'][user_id] +=1
        except KeyError:
            DataHandler.dynamic_data['cookie count'][user_id] = 1
            
        await message.channel.send(f"Hey {username}, have a cookie \U0001F36A!")
        #await message.author.send(f"{username}, you got a cookie from the cookie bot. It looks like this:  \U0001F36A!")
        
        DataHandler.save_dynamic(DataHandler.dynamic_data)

async def check_cookies(text, message, username, user_id):
    commands = DataHandler.static_data["count_cookies"]
    if text in commands:
        async with message.channel.typing():
            await message.channel.send(f"{username}, I'll just count them")
            num_cookies = 0
            try:
                num_cookies = DataHandler.dynamic_data['cookie count'][user_id]
                await message.channel.send(
                    "\n".join(["\U0001F36A "+str(i+1) for i in range(num_cookies)]))

            except KeyError:
                await message.channel.send(f"you have no cookies. Type 'Give me a cookie' to get one!")
            
async def check_cheese(text, message, username, user_id):
    cookie_commands = DataHandler.static_data["give_cheese"]
    if text in cookie_commands:
        try:
            DataHandler.dynamic_data['cheese count'][user_id] +=1
        except KeyError:
            DataHandler.dynamic_data['cheese count'][user_id] = 1
            
        await message.channel.send(f"Hey {username}, have cheese \U0001f9c0!")
        #await message.author.send(f"{username}, you got cheese from the cookie bot. It looks like this:  \U0001f9c0!")
        
        DataHandler.save_dynamic(DataHandler.dynamic_data)

async def check_count_cheese(text, message, username, user_id):
    commands = DataHandler.static_data["count_cheese"]
    if text in commands:
        async with message.channel.typing():
            await message.channel.send(f"{username}, I'll just count them")
            num_cookies = 0
            try:
                num_cookies = DataHandler.dynamic_data['cheese count'][user_id]
                await message.channel.send(
                    "\n".join(["\U0001f9c0 "+str(i+1) for i in range(num_cookies)]))

            except KeyError:
                await message.channel.send(f"you have no cheese. Type 'Give me cheese' to get some!")
            
