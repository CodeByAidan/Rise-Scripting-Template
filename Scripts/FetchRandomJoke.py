# import asyncio
# import discord
# from discord.ext import commands
# from tkinter import END, Text as textbox
#
# Rise: commands.Bot = commands.Bot(
#     command_prefix="?", self_bot=True, intents=discord.Intents.all()
# )

# Use `?FetchRandomJoke` to get a random joke
@Rise.command()
async def FetchRandomJoke(ctx):
    import contextlib

    async def error_handler(ctx, e: Exception) -> None:
        """
        Error Handler for the script

        Args:
            ctx (commands.Context): The context of the command.
            e (Exception): The exception that was raised.

        Returns:
            None
        """
        error_message: str = f"Error: {type(e).__name__} - {str(e)}"
        with contextlib.suppress(Exception):
            textbox.insert(END, "\n\n" + error_message)
        print(error_message)
        await ctx.send(error_message)


    # insert your solution function here:
    def fetch_joke() -> str:
        return "Did you complete the challenge?"

    try:
        await ctx.message.delete()
        joke = fetch_joke()
        await ctx.send(joke)
    except Exception as e:
        await error_handler(ctx, e)
