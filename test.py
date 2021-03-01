import os
from os import scandir

from discord.ext import commands
from dotenv import load_dotenv

from todo import add_todo
class Something:
    def __init__(self):
        self.butts = 1

#comment
load_dotenv()
token=os.getenv('DISCORD_TOKEN')
guild=os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

work_todos=[]
personal_todos=[]

# test
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='add')
async def add(ctx, priority, description, date, list):
    todo = add_todo(work_todos if list == "work" else personal_todos, priority, description, date)
    response='You just added a new todo:\n' + str(todo)
    await ctx.send(response)

@bot.command(name='get')
async def get(ctx, lst_name=None):
    if lst_name == None:
        todos = personal_todos + work_todos
    elif lst_name == 'work':
        todos = work_todos
    else: 
        todos = personal_todos

    if len(todos) == 0:
        await ctx.send("There are no todos!")
    response = ""
    for idx, todo in enumerate(todos):
        response += f'\nid:{idx}\n{str(todo)}'
    await ctx.send(response)
    
#comment
@bot.command(name='strike')
async def strike(ctx, id, lst_name):
    if lst_name == 'work':
        todos = work_todos
    else:
        todos = personal_todos

    removed_todo = todos[int(id)]
    del todos[int(id)]
    await ctx.send(f'The following todo has been removed:\n {str(removed_todo)}')

@bot.command(name="destroy")
async def destroy(ctx, lst_name=None):
    if lst_name == None:
        todos = personal_todos + work_todos
    elif lst_name == 'work':
        todos = work_todos
    else: 
        todos = personal_todos

    for  todo in todos:
        del todo
        print(todos)
    await ctx.send("All todos have been removed from the list")

bot.run(token)