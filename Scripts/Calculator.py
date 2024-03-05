# import asyncio
# import discord
# from discord.ext import commands
# from tkinter import END, Text as textbox

# EMMB = discord
# EMMB.Embed = discord.Embed

# Rise: commands.Bot = commands.Bot(
#     command_prefix="?", self_bot=True, intents=discord.Intents.all()
# )

# Use `?Calculator add 1 2` to add 1 and 2, and get the result 3!
@Rise.command()
async def Calculator(ctx, operation: str, num1: float, num2: float):
    from typing import Union
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
    def simple_calculator(operation: str, num1: float, num2: float) -> Union[float, str]:
        return "Did you complete the challenge?"

    try:
        await ctx.message.delete()
        result = simple_calculator(operation, num1, num2)
        await ctx.send(result)
    except Exception as e:
        await error_handler(ctx, e)