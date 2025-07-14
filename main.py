import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True  # Needed to read message content

bot = commands.Bot(command_prefix="\\", intents=intents)

task_list = []


@bot.event
async def on_ready():
    print(f"[INFO] Bot is ready! Logged in as {bot.user}")


@bot.command("hello")
async def hello(ctx):
    """Responds with a greeting message and adds a reaction."""
    await ctx.message.add_reaction("👋")


@bot.command("cls")
async def cls(ctx):
    """Clears the channel messages."""
    await ctx.channel.purge()


@bot.command("todo:")
async def todo(ctx, *, message: str):
    """Adds a task to the to-do list with optional tags.
    USAGE: \\todo: <task message> tags: <tag1, tag2, ...>"""
    if "tags:" in message:
        tags = message.split("tags:")[1].strip().split(",")
        tags = [tag.strip() for tag in tags if tag.strip()]
        message = message.split("tags:")[0].strip()
    else:
        tags = []
    if not message:
        await ctx.send("Please provide a task to add to your to-do list.")
        return
    task_list.append(
        {
            "message": message,
            "user": ctx.author.id,
            "timestamp": ctx.message.created_at,
            "tags": tags,
            "done": False,
        }
    )
    await ctx.message.add_reaction("✅")


@bot.command("list")
async def list_tasks(ctx):
    """Lists all tasks in the to-do list."""
    if not task_list:
        await ctx.send("Your to-do list is empty.")
        return
    for i in range(len(task_list)):
        task = task_list[i]
        done_icon = "✅" if task["done"] else "❌"
        tags = ", ".join(task["tags"]) if task["tags"] else "No tags"
        await ctx.send(
            f"{done_icon} Task {i + 1}: {task['message']} | Tags: {tags} | Added by: <@{task['user']}> at {task['timestamp']}"
        )


@bot.command("done:")
async def mark_done(ctx, task_number: int):
    """Marks a task as done by its number.
    USAGE: \\done: <task number>"""
    if 0 < task_number <= len(task_list):
        task_list[task_number - 1]["done"] = True
        await ctx.message.add_reaction("✅")
    else:
        await ctx.send("Invalid task number. Please provide a valid number.")


@bot.command("remove:")
async def remove_task(ctx, task_number: int):
    """Removes a task from the to-do list by its number.
    USAGE: \\remove: <task number>"""
    if 0 < task_number <= len(task_list):
        removed_task = task_list.pop(task_number - 1)
        await ctx.send(f"Removed task: {removed_task['message']}")
        await ctx.message.add_reaction("🗑️")
    else:
        await ctx.send("Invalid task number. Please provide a valid number.")


@bot.command("clear")
async def clear_tasks(ctx):
    """Clears all tasks from the to-do list."""
    global task_list
    task_list = []
    await ctx.send("All tasks have been cleared.")
    await ctx.message.add_reaction("🗑️")


@bot.command("edit:")
async def edit_task(ctx, task_number: int, *, new_message: str):
    """Edits a task in the to-do list by its number.
    USAGE: \\edit: <task number> <new message>"""
    if 0 < task_number <= len(task_list):
        task_list[task_number - 1]["message"] = new_message
        await ctx.send(f"Task {task_number} has been updated to: {new_message}")
        await ctx.message.add_reaction("✏️")


load_dotenv()
token = os.getenv("DISCORD_TOKEN")
if token is None:
    print("[ERROR] DISCORD_TOKEN not found in .env file")
    exit(1)
try:
    print("[INFO] Token successfully loaded token from .env file.")
    bot.run(token)
except discord.errors.LoginFailure:
    print("[ERROR] Invalid Discord token. Please check your .env file.")
except Exception as e:
    print(f"[ERROR] An unexpected error occurred: {e}")
