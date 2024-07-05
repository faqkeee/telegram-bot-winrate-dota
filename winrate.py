import telebot
import requests
from telebot import types

bot = telebot.TeleBot('') #API bot

@bot.message_handler(commands=['start'])
def start_message(message):

    # Сreate buttons

    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Abaddon')
    btn2 = types.KeyboardButton('Alchemist')
    btn3 = types.KeyboardButton('Ancient Apparition')
    btn4 = types.KeyboardButton('Anti-Mage')
    btn5 = types.KeyboardButton('Arc Warden')
    btn6 = types.KeyboardButton('Axe')
    btn7 = types.KeyboardButton('Bane')
    btn8 = types.KeyboardButton('Batrider')
    btn9 = types.KeyboardButton('Beastmaster')
    btn10 = types.KeyboardButton('Bloodseeker')
    btn11 = types.KeyboardButton('Bounty Hunter')
    btn12 = types.KeyboardButton('Brewmaster')
    btn13 = types.KeyboardButton('Bristleback')
    btn14 = types.KeyboardButton('Broodmother')
    btn15 = types.KeyboardButton('Centaur Warrunner')
    btn16 = types.KeyboardButton('Chaos Knight')
    btn17 = types.KeyboardButton('Chen')
    btn18 = types.KeyboardButton('Clinkz')
    btn19 = types.KeyboardButton('Clockwerk')
    btn20 = types.KeyboardButton('Crystal Maiden')
    btn21 = types.KeyboardButton('Dark Seer')
    btn22 = types.KeyboardButton('Dark Willow')
    btn23 = types.KeyboardButton('Dawnbreaker')
    btn24 = types.KeyboardButton('Dazzle')
    btn25 = types.KeyboardButton('Death Prophet')
    btn26 = types.KeyboardButton('Disruptor')
    btn27 = types.KeyboardButton('Doom')
    btn28 = types.KeyboardButton('Dragon Knight')
    btn29 = types.KeyboardButton('Drow Ranger')
    btn30 = types.KeyboardButton('Earth Spirit')
    btn31 = types.KeyboardButton('Earthshaker')
    btn32 = types.KeyboardButton('Elder Titan')
    btn33 = types.KeyboardButton('Ember Spirit')
    btn34 = types.KeyboardButton('Enchantress')
    btn35 = types.KeyboardButton('Enigma')
    btn36 = types.KeyboardButton('Faceless Void')
    btn37 = types.KeyboardButton('Grimstroke')
    btn38 = types.KeyboardButton('Gyrocopter')
    btn39 = types.KeyboardButton('Hoodwink')
    btn40 = types.KeyboardButton('Huskar')
    btn41 = types.KeyboardButton('Invoker')
    btn42 = types.KeyboardButton('Io')
    btn43 = types.KeyboardButton('Jakiro')
    btn44 = types.KeyboardButton('Juggernaut')
    btn45 = types.KeyboardButton('Keeper of the Light')
    btn46 = types.KeyboardButton('Kunkka')
    btn47 = types.KeyboardButton('Legion Commander')
    btn48 = types.KeyboardButton('Leshrac')
    btn49 = types.KeyboardButton('Lich')
    btn50 = types.KeyboardButton('Lifestealer')
    btn51 = types.KeyboardButton('Lina')
    btn52 = types.KeyboardButton('Lion')
    btn53 = types.KeyboardButton('Lone Druid')
    btn54 = types.KeyboardButton('Luna')
    btn55 = types.KeyboardButton('Lycan')
    btn56 = types.KeyboardButton('Magnus')
    btn57 = types.KeyboardButton('Marci')
    btn58 = types.KeyboardButton('Mars')
    btn59 = types.KeyboardButton('Medusa')
    btn60 = types.KeyboardButton('Meepo')
    btn61 = types.KeyboardButton('Mirana')
    btn62 = types.KeyboardButton('Monkey King')
    btn63 = types.KeyboardButton('Morphling')
    btn64 = types.KeyboardButton('Muerta')
    btn65 = types.KeyboardButton('Naga Siren')
    btn66 = types.KeyboardButton("Nature's Prophet")
    btn67 = types.KeyboardButton('Necrophos')
    btn68 = types.KeyboardButton('Night Stalke')
    btn69 = types.KeyboardButton('Nyx Assassin')
    btn70 = types.KeyboardButton('Ogre Magi')
    btn71 = types.KeyboardButton('Omniknight')
    btn72 = types.KeyboardButton('Oracle')
    btn73 = types.KeyboardButton('Outworld Destroyer')
    btn74 = types.KeyboardButton('Pangolier')
    btn75 = types.KeyboardButton('Phantom Assassin')
    btn76 = types.KeyboardButton('Phantom Lancer')
    btn77 = types.KeyboardButton('Phoenix')
    btn78 = types.KeyboardButton('Primal Beast')
    btn79 = types.KeyboardButton('Puck')
    btn80 = types.KeyboardButton('Pudge')
    btn81 = types.KeyboardButton('Pugna')
    btn82 = types.KeyboardButton('Queen of Pain')
    btn83 = types.KeyboardButton('Razor')
    btn84 = types.KeyboardButton('Riki')
    btn85 = types.KeyboardButton('Rubick')
    btn86 = types.KeyboardButton('Sand King')
    btn87 = types.KeyboardButton('Shadow Demon')
    btn88 = types.KeyboardButton('Shadow Fiend')
    btn89 = types.KeyboardButton('Shadow Shaman')
    btn90 = types.KeyboardButton('Silencer')
    btn91 = types.KeyboardButton('Skywrath Mage')
    btn92 = types.KeyboardButton('Slardar')
    btn93 = types.KeyboardButton('Slark')
    btn94 = types.KeyboardButton('Snapfire')
    btn95 = types.KeyboardButton('Sniper')
    btn96 = types.KeyboardButton('Spectre')
    btn97 = types.KeyboardButton('Spirit Breaker')
    btn98 = types.KeyboardButton('Storm Spirit')
    btn99 = types.KeyboardButton('Sven')
    btn100 = types.KeyboardButton('Techies')
    btn101 = types.KeyboardButton('Templar Assassin')
    btn102 = types.KeyboardButton('Terrorblade')
    btn103 = types.KeyboardButton('Tidehunter')
    btn104 = types.KeyboardButton('Timbersaw')
    btn105 = types.KeyboardButton('Tinker')
    btn106 = types.KeyboardButton('Tiny')
    btn107 = types.KeyboardButton('Treant Protector')
    btn108 = types.KeyboardButton('Troll Warlord')
    btn109 = types.KeyboardButton('Tusk')
    btn110 = types.KeyboardButton('Underlord')
    btn111 = types.KeyboardButton('Undying')
    btn112 = types.KeyboardButton('Ursa')
    btn113 = types.KeyboardButton('Vengeful Spirit')
    btn114 = types.KeyboardButton('Venomancer')
    btn115 = types.KeyboardButton('Viper')
    btn116 = types.KeyboardButton('Visage')
    btn117 = types.KeyboardButton('Void Spirit')
    btn118 = types.KeyboardButton('Warlock')
    btn119 = types.KeyboardButton('Weaver')
    btn120 = types.KeyboardButton('Windranger')
    btn121 = types.KeyboardButton('Winter Wyvern')
    btn122 = types.KeyboardButton('Witch Doctor')
    btn123 = types.KeyboardButton('Wraith King')
    btn124 = types.KeyboardButton('Zeus')

    #put the buttons in place

    markup.row(btn1, btn2, btn3)
    markup.row(btn4, btn5, btn6,)
    markup.row(btn7, btn8, btn9)
    markup.row(btn10, btn11, btn12)
    markup.row(btn13, btn14, btn15)
    markup.row(btn16, btn17, btn18)
    markup.row(btn19, btn20, btn21)
    markup.row(btn22, btn23, btn24)
    markup.row(btn25, btn26, btn27)
    markup.row(btn28, btn29, btn30)
    markup.row(btn31, btn32, btn33)
    markup.row(btn34, btn35, btn36)
    markup.row(btn37, btn38, btn39)
    markup.row(btn40, btn41, btn42)
    markup.row(btn43, btn44, btn45)
    markup.row(btn46, btn47, btn48)
    markup.row(btn49, btn50, btn51)
    markup.row(btn52, btn53, btn54)
    markup.row(btn55, btn56, btn57)
    markup.row(btn58, btn59, btn60)
    markup.row(btn61, btn62, btn63)
    markup.row(btn64, btn65, btn66)
    markup.row(btn67, btn68, btn69)
    markup.row(btn70, btn71, btn72)
    markup.row(btn73, btn74, btn75)
    markup.row(btn76, btn77, btn78)
    markup.row(btn79, btn80, btn81)
    markup.row(btn82, btn83, btn84)
    markup.row(btn85, btn86, btn87)
    markup.row(btn88, btn89, btn90)
    markup.row(btn91, btn92, btn93)
    markup.row(btn94, btn95, btn96)
    markup.row(btn97, btn98, btn99)
    markup.row(btn100, btn101, btn102)
    markup.row(btn103, btn104, btn105)
    markup.row(btn106, btn107, btn108)
    markup.row(btn109, btn110, btn111)
    markup.row(btn112, btn113, btn114)
    markup.row(btn115, btn116, btn117)
    markup.row(btn118, btn119, btn120)
    markup.row(btn121, btn122, btn123)
    markup.row(btn124)



    bot.send_message(message.chat.id, f"Hi, {message.from_user.first_name}, this bot is created to quickly determine the winrate of characters in DOTA 2,"
                                      f" choose the hero you want to know the winrate, for example 'Pudge'", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def get_hero_winrate(message):

    hero_name = message.text.lower()


    hero_url = "https://api.opendota.com/api/heroStats"   # site from which we take info


    hero_stats = requests.get(hero_url).json()

    # looking for a hero
    hero_found = False
    for hero in hero_stats:
        if hero['localized_name'].lower() == hero_name:

            hero_winrate = hero['pro_win'] / hero['pro_pick'] * 100
            bot.send_message(message.chat.id, f"Winrate of the hero {hero_name.capitalize()}: <u><b>{hero_winrate:.2f}%</b></u>, The information is taken from the OpenDota website", parse_mode='html')

            hero_found = True
            break
    # if the hero name is not correct
    if not hero_found:
        bot.send_message(message.chat.id, f"No hero with the name {hero_name.capitalize()} found. Please enter the correct name of the hero")

if __name__ == "__main__":
    bot.polling()
