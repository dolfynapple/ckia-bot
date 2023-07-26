import discord
import responses


async def send_message(user_id, msg, user_msg, is_private):
    if "<@1119114390017409044>" in user_msg:
        try:
            response = responses.handle_response(user_id, user_msg)
            await msg.author.send(response) if is_private else await msg.channel.send(response)
        except Exception as e:
            print(e)
    else:
        return


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    TOKEN = 'MTExOTExNDM5MDAxNzQwOTA0NA.GqbRpe.9UxliMNs0g-2pbuxq89aSVmM_qmvPGojgFBP10'
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_id = str(message.author.id)
        user_msg = str(message.content)
        channel = str(message.channel)

        print(f"{username} id: {user_id} said:{user_msg} in:{channel}")

        if user_msg[0] == '!':
            user_msg = user_msg[1:]
            await send_message(user_id, message, user_msg, is_private=True)
        else:
            await send_message(user_id, message, user_msg, is_private=False)

    client.run(TOKEN)
