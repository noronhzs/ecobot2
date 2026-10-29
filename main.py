import discord 
from discord.ext import commands
import random
from config import TOKEN

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado com {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um ecobot o bot que vai ajudar-te {bot.user} a ser uma pessoa mais sustentável e amiga do ambiente!')

    # ! função de dicas
@bot.command()
async def dicas(ctx):
    await ctx.send(f'Dicas: \n 1. Reciclar é uma excelente forma de reduzir o impacto ambiental. \n 2. Utilize sacolas reutilizáveis ao invés de plásticas. \n 3. Economize água fechando o registro enquanto se ensaboam as mãos.')

    #* funão de passo a passo para compostagem
@bot.command()
async def passo_a_passo(ctx):
    await ctx.send(f'Passo a passo para compostagem: \n 1. Escolha um local adequado para o seu compostor, de preferência em um lugar ventilado e com sombra. \n 2. Adicione materiais orgânicos, como restos de frutas e vegetais, folhas secas e grama cortada. Evite adicionar carne, laticínios e alimentos processados. \n 3. Misture os materiais regularmente para acelerar o processo de decomposição. \n 4. Mantenha o composto úmido, mas não encharcado. \n 5. Aguarde alguns meses até que o composto esteja pronto para ser usado em seu jardim ou horta.')

#* função de economia de energia
@bot.command()
async def economia_energia(ctx):
    await ctx.send(f'Dicas de economia de energia: \n 1. Desligue os aparelhos eletrônicos quando não estiverem em uso. \n 2. Utilize lâmpadas LED, que consomem menos energia e têm maior durabilidade. \n 3. Aproveite a luz natural durante o dia, abrindo cortinas e persianas. \n 4. Ajuste a temperatura do ar-condicionado e aquecedor para níveis confortáveis, evitando excessos. \n 5. Faça manutenção regular dos equipamentos para garantir eficiência energética.')    

# ! função de economia de água
@bot.command()
async def economia_agua(ctx):
    await ctx.send(f'Dicas de economia de água: \n 1. Feche a torneira enquanto escova os dentes ou ensaboa as mãos. \n 2. Reaproveite a água da chuva para regar plantas e jardins. \n 3. Conserte vazamentos em torneiras e encanamentos o mais rápido possível. \n 4. Utilize máquinas de lavar roupas e louças apenas com carga completa. \n 5. Opte por chuveiros e torneiras com dispositivos economizadores de água.')   

#* função de transporte sustentável
@bot.command()
async def transporte_sustentavel(ctx):
    await ctx.send(f'Dicas de transporte sustentável: \n 1. Utilize transporte público sempre que possível, reduzindo o número de veículos nas ruas. \n 2. Opte por caminhar ou andar de bicicleta para trajetos curtos, promovendo saúde e reduzindo a emissão de poluentes. \n 3. Compartilhe caronas com amigos, familiares ou colegas de trabalho para diminuir o número de veículos em circulação. \n 4. Considere a utilização de veículos elétricos ou híbridos, que possuem menor impacto ambiental. \n 5. Planeje suas viagens e rotas para otimizar o uso do transporte e reduzir o consumo de combustível.')

bot.run(TOKEN)
