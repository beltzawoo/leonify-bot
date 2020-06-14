import discord
import random
import asyncio
import os

client = discord.Client()

prefix = 'leon!'


async def error_message(message, error_text):
    embed = discord.Embed(title="Erreur !",
                          description=error_text, color=0xff0000)
    permissions_denied = await message.channel.send(embed=embed)
    await asyncio.sleep(2)
    await permissions_denied.delete()
    await message.delete()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity = discord.Activity(name='les loulous :3 | leon!help', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith(prefix + 'help'):
        embed = discord.Embed(title="Infos et aide", color=0x0475e4)
        embed.add_field(name="Commandes Fun 🎲",
                        value="""leon!fursona
leon!gay <truc>
leon!love <truc1/truc2>
leon!choix <choix1/choix2>""",
                        inline=False)
        embed.add_field(name="Commandes Utilitaires ⚙",
                        value="""leon!purge <nombre>
leon!embed <texte>""",
                        inline=False)
        embed.add_field(name="Informations ❓",
                        value="leon!info",
                        inline=False)
        await message.author.send(embed=embed)
        await message.add_reaction("👍")

    if message.content.startswith(prefix + 'gay'):

        tested_thing = message.content[8:]
        gay_percentage = str(random.randint(1, 100))
        if tested_thing == "":
            await error_message(message, "Il faut préciser qui ou quoi je dois tester ! :c")
            return
        if int(gay_percentage) <= 33:
            orientation = "hétérosexuel"
        elif int(gay_percentage) <= 66:
            orientation = "bisexuel"
        elif int(gay_percentage) <= 89:
            orientation = "homosexuel"
        else:
            orientation = "très gay. Mais pshhhh, entre nous, moins que beltza lol"

        embed = discord.Embed(
            title="Est-ce que ce truc est gay ?",
            description="""Selon mes pouvoirs de furry, je peux dire sans aucun doute (ou pas) que {} est gay à {}% !
Pour info, {} est donc {} !""".format(
                tested_thing, gay_percentage, tested_thing, orientation), color=0xff00ff)
        await message.channel.send(embed=embed)

    if message.content.startswith(prefix + 'fursona'):

        species_list = ["loup", "renard", "chien", "dragon", "chat", "tigre", "lion", "lapin", "raccoon", "putois",
                        "cheval", "loutre", "ours", "coyote", "hyène", "oiseau", "souris", "kangourou", "gryphon",
                        "écureuil", "chacal", "sergal", "protogen", "dutch angel dragon", "manokit", "requin", "chauve-souris"]
        colour_list = ["rouge", "orange", "jaune", "vert(e)", "bleu(e)", "violet", "rose", "noir(e)", "blanc(he)",
                       "marron", "gris", "turquoise", "kaki", "rose bonbon", "magenta", "crème", "rouge sang", "brun",
                       "pourpre", "beige", "améthyste", "argent", "aubergine", "azur", "bleu métal", "or", "caramel",
                       "carmin", "chocolat", "citrouille", "cramoisi", "cuivre", "émeraude", "framboise", "grenat",
                       "indigo", "lavande", "menthe", "olive", "rouge feu", "saphir", "vanille", "mauve"]

        personality_list = ["amical", "gentil", "sympa", "chiant", "coquin", "méchant", "sournois", "vaniteux",
                            "généreux", "respectueux", "facile", "adorable", "mignon", "strict", "cool", "peureux",
                            "soumis", "conforme", "malicieux", "taquineur", "froid", "attentioné", "fermé",
                            "coopératif", "combatif", "courageux", "rude", "courtois", "engagé", "indécisif",
                            "enthousiaste", "rancunier", "rigide", "reconnaissant", "humble", "honnêtte", "hypocritte",
                            "mature", "immature", "optimiste", "pessimiste", "ponctuel", "naïf", "responsable",
                            "sincère", "confiant", "gay", "hétéro"]

        love_list = ["l'animation", "cuisiner", "les jeux de rôle", "le bowling", "la calligraphie",
                     "jouer aux cartes", "les échecs", "dessiner", "la progammation", "écrire", "jouer aux jeux vidéos",
                     "suivre la fashion", "apprendre des langues", "résoudre des casse-têtes", "jongler",
                     "faire du karaoke", "écouter de la musique", "la magie", "le nail art", "les Rubik's Cube",
                     "sculpter", "chanter", "les séries Netflix", "éditer Wikipédia", "faire du Yoga", "sucer",
                     "troller", "regarder des lives sur Twitch", "faire l'idiot", "manger de la beux", "Discord",
                     "les renards", "les cerises", "les framboises", "les aubergines", "les bananes", "e621", "reddit",
                     "manger", "regarder du dessin furry", "la limonade"]

        fur_species = random.choice(species_list)
        fur_colour = random.choice(colour_list)
        fur_personality = random.choice(personality_list)
        fur_love = random.choice(love_list)

        embed = discord.Embed(title="Générateur de Fursona",
                              description="""Alors, voilà le concept...
Ta fursona serait un(e) {} {}, qui serait plutôt {}, et qui adore {} !
J'espère que ça t'aide >w<\"""".format(fur_species, fur_colour, fur_personality, fur_love),
                              color=0xb2ff30)
        await message.channel.send(embed=embed)

    if message.content.startswith(prefix + 'choix'):

        arguments_only = message.content[11:]
        if "/" not in arguments_only:
            await error_message(message, 'Il faut me dire les deux choses à tester, comme par exemple McDo/Quick !')
            return
        split_arguments = arguments_only.split("/")
        reply_list = ["{}, bien sûr !", "Je choisis {} sans hésiter !",
                      "Un peu de doute, mais je pense que {} est mieux !", "C'est une question ? {} bien sûr !"
                      "Je préfère {}, franchement.", "Rien n'est meilleur que {} !" "Team {} ! >w<"]

        embed = discord.Embed(title="Le choix magique",
                              description=random.choice(reply_list).format(random.choice(split_arguments)),
                              color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith(prefix + "love"):

        arguments_only = message.content[9:]
        if "/" not in arguments_only:
            await error_message(message, 'Il faut me dire les deux choses à tester, comme par exemple Léon/Vagus !')
            return
        split_arguments = arguments_only.split("/")
        reply_list = ["Alors, d'après mon aura de furry, {} et {} sont compatibles à {}% ! Ca fera 50€.",
                      "Hmmmm, {} et {} ? Je vais dire... {}% !",
                      "Laisse moi voir... {} et {} sont compatibles à {}% !",
                      "Après réflexion, il me semble que {} et {} soient compatibles à {}% ! Vwalà ! >w<"]
        embed = discord.Embed(title="L'amour est dans l'air... Ou pas",
                                  description=random.choice(reply_list).format(split_arguments[0], split_arguments[1],
                                                                        random.randint(1, 100)), color=0xff00ff)
        await message.channel.send(embed=embed)

    if message.content.startswith(prefix + "purge"):
        await message.delete()
        if message.author.permissions_in(message.channel).manage_messages:
            if message.content[11:] == "":
                await error_message(message, "Il faut préciser combien de messages il faut que j'enlève !")
                return
            messages_to_delete = int(message.content[11:])
            await message.channel.purge(limit=messages_to_delete)
        else:
            await error_message(message, "Il faut avoir la permission \"Gérer les messages !\"")

    if message.content.startswith(prefix + "embed"):
        if message.author.permissions_in(message.channel).manage_messages:
            embed_content = message.content[10:]
            if embed_content == "":
                await error_message(message, "Il faut me dire quoi dire >w<\"")
                return
            embed = discord.Embed(description=embed_content, color=0x85ffd7)
            await message.channel.send(embed=embed)
            await message.delete()
        else:
            await error_message(message, "Il faut avoir la permission \"Gérer les messages !\"")
    if message.content.startswith(prefix + "info"):
        embed=discord.Embed(title="Informations", description="Voici des informations sur Leonify !")
        embed.set_thumbnail(url=str(client.user.avatar_url))
        embed.add_field(name="Github :", value="https://github.com/beltzawoo/leonify-bot", inline=False)
        AppInfo=await client.application_info()
        embed.add_field(name="Créateur :", value=AppInfo.owner.name + "#" + AppInfo.owner.discriminator, inline=False)
        embed.add_field(name="Nombre de Serveurs :", value=len(client.guilds), inline=False)
        embed.add_field(name="Nombre d'Utilisateurs :", value=len(client.users), inline=False)
        embed.add_field(name="Invitation :", value="https://discord.com/oauth2/authorize?client_id={}&scope=bot&permissions=268823630".format(AppInfo.id), inline=False)
        embed.add_field(name="Librairie :", value="discord.py", inline=False)
        await message.channel.send(embed=embed)

client.run(os.environ.get('BOT_TOKEN'))
