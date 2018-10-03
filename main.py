import random

# Guilds of Ravnica has 53 rares and 15 mythic rares

def AddRareColors( card_number, guilds ):
    if card_number <= 3:        # 3 White rares
        guilds[ "Selesnya" ] += 1
        guilds[ "Boros" ] += 1
    elif card_number <= 6:   # 3 Blue rares
        guilds[ "Izzet" ] += 1
        guilds[ "Dimir" ] += 1
    elif card_number <= 9:   # 3 Black rares
        guilds[ "Dimir" ] += 1
        guilds[ "Golgari" ] += 1
    elif card_number <= 12:  # 3 Red rares
        guilds[ "Izzet" ] += 1
        guilds[ "Boros" ] += 1
    elif card_number <= 16:  # 4 Green rares
        guilds[ "Golgari" ] += 1
        guilds[ "Selesnya" ] += 1
    elif card_number <= 23:  # 7 Izzet rares
        guilds[ "Izzet" ] += 1
    elif card_number <= 30:  # 7 Dimir rares
        guilds[ "Dimir" ] += 1
    elif card_number <= 37:  # 7 Golgari rares
        guilds[ "Golgari" ] += 1
    elif card_number <= 43:  # 6 Selesnya rares
        guilds[ "Selesnya" ] += 1
    elif card_number <= 50:  # 7 Boros rares
        guilds[ "Boros" ] += 1
    # And 3 colorless rares that add nothing

def AddMythicColors( card_number, guilds ):
    if card_number <= 1:        # 1 White mythic rare
        guilds[ "Selesnya" ] += 1
        guilds[ "Boros" ] += 1
    elif card_number <= 2:   # 1 Red mythic rare
        guilds[ "Izzet" ] += 1
        guilds[ "Boros" ] += 1
    elif card_number <= 3:   # 1 Green mythic rare
        guilds[ "Golgari" ] += 1
        guilds[ "Selesnya" ] += 1
    elif card_number <= 5:   # 2 Izzet mythic rares
        guilds[ "Izzet" ] += 1
    elif card_number <= 9:   # 4 Dimir mythic rares
        guilds[ "Dimir" ] += 1
    elif card_number <= 11:  # 2 Golgari mythic rares
        guilds[ "Golgari" ] += 1
    elif card_number <= 13:  # 2 Selesnya mythic rares
        guilds[ "Selesnya" ] += 1
    else:                       # 2 Boros mythic rares
        guilds[ "Boros" ] += 1

# For the purposes of this Monte Carlo simulation, the seeded pack doesn't really affect this calculation.
# We are only considering rares and players generally pick the guilds evenly. I don't know if seeded packs
# can have foils or foil rares, and if so if they necessarily match the color of the pack. I'll simplify
# the calculation by assuming they are the same as other packs.

random.seed()
distribution = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0 }

for n_prerelease in range( 10000 ):
    luckiest_player_rare_count = 0
    for n_player in range( 120 ):
        guild_rares = { "Izzet": 0, "Dimir": 0, "Golgari": 0, "Selesnya": 0, "Boros": 0 }
        for n_pack in range( 6 ):
            rare_is_mythic = ( random.randint( 1, 8 ) == 1 )
            if rare_is_mythic:
                card_number = random.randint( 1, 15 )
                AddMythicColors( card_number, guild_rares )
            else:
                card_number = random.randint( 1, 53 )
                AddRareColors( card_number, guild_rares )
            pack_has_rare_foil = ( random.randint( 1, 36 ) == 1 )
            if ( pack_has_rare_foil ):
                foil_is_mythic = ( random.randint( 1, 8 ) == 1 )
                if foil_is_mythic:
                    foil_card_number = random.randint( 1, 15 )
                    AddMythicColors( card_number, guild_rares )
                else:
                    foil_card_number = random.randint( 1, 53 )
                    AddRareColors( card_number, guild_rares )
        most_common_rare_count = 0
        for guild, quantity in guild_rares.items():
            if quantity > most_common_rare_count:
                most_common_rare_count = quantity
        if most_common_rare_count > luckiest_player_rare_count:
            luckiest_player_rare_count = most_common_rare_count
    distribution[ luckiest_player_rare_count ] += 1

for k, v in distribution.items():
    if v != 0:
        print "In %d prerelease%s, the luckiest player had %d rares in the same guild." % ( v, ( "", "s" )[ v != 1 ], k )
