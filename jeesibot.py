import discord
import os
import requests
import random
import time
import json
import discord.ext
from gifit import gifit
from myyntitekstit import myyntitekstit
from musattimet import musat

#from keep_alive import keep_alive

juhlijat = []
client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event

async def on_ready():
  print("We have logged in as {0.user}".format(client))
  print("Bot is now ready and operational")
@client.event
async def on_message(message):
  if message.author == client.user: 
    return
    
  if message.content.startswith("!dnd"):
    await message.channel.send("**ÄÄNESTYS:** Mikä päivä pelataan? \r:one: = ma :two: = ti :three: = ke :four: = to :five: = pe :six: = la :seven: = su")

  if message.content.startswith(('!scrim', '!scrims' , '!scrimit')):
    await message.channel.send(gifit[random.randint(0,(len(gifit)-1))] )
    await message.channel.send(myyntitekstit[random.randint(0,(len(myyntitekstit)-1))])

  if message.content.startswith('!teevoileipa'):
    await message.channel.send(":sandwich: ole hyvä!")

  if message.content.startswith(('!rockmyday' , '!rockyourday' , '!ryd')):
    quote = get_quote()
    print("Sent following quote to server: " + quote +"\r\r" )
    await message.channel.send(quote)
    
  if message.content.startswith('!taustamelua'):
    random.shuffle(musat)

    for biisi in musat:
      await message.channel.send("!play " + biisi)
  
  if message.content.startswith(('!jeesi' , '!jeesibot')):
    await message.channel.send("Jeesibotti tässä terve!\rOsaan seuraavat käskyt:\r!scrim / !scrims / !scrimit: Luo scrimikutsun tajunnanräjäyttävällä mainostekstillä :D \r !rockmyday / !rockyourday / !ryd: Tuo mietelauseen, joka mullistaa elämäsi\r !teevoileipa: Tekee voileivän \r!wappujuhlaIN: lisää sinut wappujuhlija listalle\\r!wappujuhlaOUT: poistaa wappujuhlalistalta\r")

  if message.content.startswith('!wappujuhlaIN'):
    kirjoittaja = message.author
    if kirjoittaja not in juhlijat:
      juhlijat.append(kirjoittaja)
    msg = 'Sinut {kirjoittaja.mention} on lisätty wappujuhlijoihin'.format(message)
    await message.channel.send(msg)

  if message.content.startswith('!wappujuhlaOUT'):
    kirjoittaja = message.author
    if kirjoittaja in juhlijat:
      juhlijat.remove(kirjoittaja)
    msg = 'Sinut {kirjoittaja.mention} on poistettu wappujuhlijoista'.format(message)
    await message.channel.send(msg)

client.run(os.getenv("TOKEN"))


