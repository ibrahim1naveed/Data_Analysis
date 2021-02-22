twilight_mentions1 = {
    "applejack" : 0,
    "rarity"    : 0,
    "pinkie"    : 0,
    "rainbow"   : 0,
    "fluttershy": 0,
}

pinkie_mentions1 = {
    "twilight"  : 0,
    "applejack" : 0,
    "rarity"    : 0,
    "rainbow"   : 0,
    "fluttershy": 0,

}

rainbow_mentions1 = {
    "twilight"  : 0,
    "applejack" : 0,
    "rarity"    : 0,
    "pinkie"    : 0,
    "fluttershy": 0,

}

fluttershy_mentions1 = {
    "twilight"  : 0,
    "applejack" : 0,
    "rarity"    : 0,
    "pinkie"    : 0,
    "rainbow"   : 0,
}
applejack_mentions1 = {
    "twilight" :  0,
    "rarity"    : 0,
    "pinkie"    : 0,
    "rainbow"   : 0,
    "fluttershy": 0,
}

rarity_mentions1 = {
    "twilight"  : 0,
    "applejack" : 0,
    "pinkie"    : 0,
    "rainbow"   : 0,
    "fluttershy": 0,

}
def mentions_dict(ponyName):
    if ponyName == 'twilight':
        return twilight_mentions1.get('twilight' , -1)
    elif ponyName == 'applejack':
        return applejack_mentions1.get('applejack' , -1)
    elif ponyName == 'rarity':
        return rarity_mentions1.get('rarity' , -1)
    elif ponyName == 'pinkie':
        return pinkie_mentions1.get('pinkie', -1)
    elif ponyName == 'rainbow':
        return rainbow_mentions1.get('rainbow' , -1)
    elif ponyName == 'fluttershy':
        return fluttershy_mentions1.get('fluttershy' , -1)
