""""
Sample.py
~~~~~~~~~

This script demonstrates the use of various libraries and modules to perform:

- typing for type hints
- requests for fetching a webpage
- BeautifulSoup for parsing HTML
- faker for generating fake user data
- json for converting data to JSON

To use, simply run the command `?Sample` or `?sample` in the chat.

I recommend using `?sendmode image` instead of `?sendmode embed` for this script.
"""

import asyncio
import contextlib
import json
from typing import Dict, List

import requests
from bs4 import BeautifulSoup
from faker import Faker


# Use `?Sample` or `?sample` to run the script!
@Rise.command(
    alias=["Sample", "sample"],
    help="Demonstrates the use of various libraries and modules.",
    usage="?Sample",
)
async def Sample(ctx):
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

    # Additional function for demonstration
    # Fetching a webpage and parsing it using BeautifulSoup
    def fetch_webpage_title(url: str) -> str:
        """
        Fetches the title of a webpage

        Args:
            url (str): The URL of the webpage

        Returns:
            str: The title of the webpage
        """
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.title.string
        return title

    try:
        await ctx.message.delete()

        # Fetching a webpage title as a sample
        url = "https://example.com"
        webpage_title = fetch_webpage_title(url)
        await ctx.send(f"Title of the webpage: {webpage_title}")

        # Generating and sending fake user data as JSON
        fake = Faker()
        users: List[Dict[str, str]] = []
        for _ in range(3):
            user = {
                "name": fake.name(),
                "email": fake.email(),
                "address": fake.address(),
                "phone_number": fake.phone_number(),
            }
            users.append(user)
        users_json = json.dumps(users, indent=4)

        embed = EMMB.Embed(
            title="Fake User Data",
            description=f"Generated fake user data as JSON\n\n{users_json}",
            # color=colors.get(h['color'])
            color=0x0000FF,
        )
        # embed.set_thumbnail(url=f"{h['thumbnail']}")
        embed.set_thumbnail(
            url="https://web.archive.org/web/20240305181000if_/https://p16-sign-useast2a.tiktokcdn.com/obj/tos-useast2a-p-0037-euttp/1d14aebd766a46cfb9727db078199d64_1708043920?x-expires=1709744400&x-signature=VwpwOl6swsnRnv6RYvH0k7AECZU%3D"
        )
        embed.set_footer(
            # text=f"{h['footertext']}",
            # icon_url=f"{h['footer_icon_url']}"
            text="Footer Text",
            icon_url="https://web.archive.org/web/20240305181151if_/https://media.tenor.com/0Eg3EhvWV2cAAAAe/tole-tole-cat.png",
        )
        await imagemode(ctx, embed)
        await asyncio.sleep(1)

        await ctx.send(f"Fake User Data (JSON):\n```json\n{users_json}\n```")
    except Exception as e:
        await error_handler(ctx, e)
