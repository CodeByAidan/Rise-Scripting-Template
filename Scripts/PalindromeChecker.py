# import asyncio
# import discord
# from discord.ext import commands
# from tkinter import END, Text as textbox
#
# Rise: commands.Bot = commands.Bot(
#     command_prefix="?", self_bot=True, intents=discord.Intents.all()
# )


# Use `?PalindromeChecker <word>` to check if the given word is a palindrome
@Rise.command()
async def PalindromeChecker(ctx, word: str):
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
    def is_palindrome(word: str) -> bool:
        return "Did you complete the challenge?"

    try:
        await ctx.message.delete()
        palindrome = is_palindrome(word=word)
        await ctx.send(palindrome)
    except Exception as e:
        await error_handler(ctx, e)