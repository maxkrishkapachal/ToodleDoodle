import os
import discord
import keep_alive
import toodleDoodleApp

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  def check(msg):
        return msg.author == message.author and msg.channel == message.channel

  if message.author == client.user:
    return
  if message.content.startswith("Toodle!") or message.content.startswith("Doodle!"):
    if message.content == 'Toodle!' or message.content == 'Doodle!':
      await message.channel.send("Toodle Doodle \U0001F413!\n\nI'm here to help you keep track of all your To Do's \U0001F4CB! Try these commands after the initial call of 'Toodle!' or 'Doodle!' to get the best use out of me!\n\nadd - add new tasks to the list.\n\ndelete - delete a task from the list\n\ncheck - check off a task that you've completed\n\ntodo - list all the tasks on the list")
    elif message.content == 'Toodle! add' or message.content == 'Doodle! add':
      await message.channel.send("What's the name of the task you want to add?")
      newTaskName = await client.wait_for("message", check=check)
      await message.channel.send("What date is this task due?")
      newTaskDue = await client.wait_for("message", check=check)
      await message.channel.send("Any notes you want to add about it?")
      newTaskNotes = await client.wait_for("message", check=check)
      toodleDoodleApp.newTask(newTaskName.content, newTaskDue.content, newTaskNotes.content)
      await message.channel.send("Great! Your task was created!")
      
    elif message.content == 'Toodle! delete' or message.content == 'Doodle! delete':
      await message.channel.send("Pick the number of the task you want to delete:")
      allToDos = toodleDoodleApp.getTasks()
      for str in allToDos:
        await message.channel.send(str)
      taskNum = await client.wait_for("message", check=check)
      toodleDoodleApp.deleteTask(int(taskNum.content))
      await message.channel.send("Great! Your task was deleted!")

    elif message.content == 'Toodle! check' or message.content == 'Doodle! check':
      await message.channel.send("Pick the number of the task you've completed:")
      allToDos = toodleDoodleApp.getTasks()
      for str in allToDos:
        await message.channel.send(str)
      taskNum = await client.wait_for("message", check=check)
      toodleDoodleApp.checkTask(int(taskNum.content))
      await message.channel.send("Congrats on completing your task!")
    elif message.content == 'Toodle! todo' or message.content == 'Doodle! todo':
      allToDos = toodleDoodleApp.getTasks()
      for str in allToDos:
        await message.channel.send(str)

  


keep_alive.keep_alive()
client.run(os.getenv('TOKEN'))