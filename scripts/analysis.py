import pandas as pd
import re
import operator
import argparse
import json
import sys

#df = pd.DataFrame()
#dfTwilight = pd.DataFrame()
#dfAppleJack = pd.DataFrame()
#dfRarity = pd.DataFrame()
#dfPinkie = pd.DataFrame()
#dfRainbow = pd.DataFrame()
#dfFluttershy = pd.DataFrame()

non_dict_twilight = {}
non_dict_apple = {}
non_dict_rarity = {}
non_dict_pinkie = {}
non_dict_rainbow = {}
non_dict_flutter = {}

with open('../data/words_alpha.txt') as file:
        alphatxt = set(word.strip().lower() for word in file)

non_dictionary_words = {"non_dictionary_items":
    {"twilight" : 0,
    "applejack" : 0,
    "rarity"    : 0,
    "pinkie"    : 0,
    "rainbow"   : 0,
    "fluttershy": 0,
    
}}

twilight_mentions1 = {
    "applejack" : 0,
    "rarity"    : 0,
    "pinkie"    : 0,
    "rainbow"   : 0,
    "fluttershy": 0,
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

twilight_follow_on = {
    "applejack" : 0,
    "rarity"    : 0,
    "pinkie"    : 0,
    "rainbow"   : 0,
    "fluttershy": 0,
    "other"     : 0,
}
apple_follow_on = {
    "twilight" : 0,
    "rarity"    : 0,
    "pinkie"    : 0,
    "rainbow"   : 0,
    "fluttershy": 0,
    "other"     : 0,
}
rarity_follow_on = {
    "twilight"  : 0,
    "applejack" : 0,
    "pinkie"    : 0,
    "rainbow"   : 0,
    "fluttershy": 0,
    "other"     : 0,
}

pinkie_follow_on = {
    "twilight"  : 0,
    "applejack" : 0,
    "rarity"    : 0,
    "rainbow"   : 0,
    "fluttershy": 0,
    "other"     : 0,
}

rainbow_follow_on = {
    "twilight"  : 0,
    "applejack" : 0,
    "rarity"    : 0,
    "pinkie"    : 0,
    "fluttershy": 0,
    "other"     : 0,
}

fluttershy_follow_on = {
    "twilight"  : 0,
    "applejack" : 0,
    "rarity"    : 0,
    "pinkie"    : 0,
    "rainbow"   : 0,
    "other"     : 0,
}




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o',help='where to print')
    parser.add_argument('src_file' , help='The file passed should be a csv')

    args = parser.parse_args()

    src_file = args.src_file

    df = pd.read_csv(src_file)
    df = df[['pony','dialog']]
    dfTwilight = df.loc[df['pony'].str.contains('Twilight Sparkle',case=True)]
    dfAppleJack = df.loc[df['pony'].str.contains('Applejack',case=True) ]
    dfRarity = df.loc[df['pony'].str.contains('Rarity',case=True)  ]
    dfPinkie = df.loc[df['pony'].str.contains('Pinkie Pie',case=True) ]
    dfRainbow = df.loc[df['pony'].str.contains('Rainbow Dash',case=True)]
    dfFluttershy = df.loc[df['pony'].str.contains('Fluttershy',case=True)]
    
    
    
    total = speech_acts(dfTwilight) + speech_acts(dfAppleJack) + speech_acts(dfRarity)+speech_acts(dfPinkie)+speech_acts(dfRainbow)+speech_acts(dfFluttershy)
    twilight_speech_acts = speech_acts(dfTwilight)
    twilight_frac = "{:.2f}".format((twilight_speech_acts/float(total)))
    apple_speech_acts = speech_acts(dfAppleJack)
    apple_frac = "{:.2f}".format((apple_speech_acts/float(total)))
    rarity_speech_acts = speech_acts(dfRarity)
    rarity_frac = "{:.2f}".format((rarity_speech_acts/float(total)))
    pinkie_speech_acts = speech_acts(dfPinkie)
    pinkie_frac = "{:.2f}".format((pinkie_speech_acts/float(total)))
    rainbow_speech_acts = speech_acts(dfRainbow)
    rainbow_frac = "{:.2f}".format((rainbow_speech_acts/float(total)))
    flutter_speech_acts = speech_acts(dfFluttershy)
    flutter_frac = "{:.2f}".format((flutter_speech_acts/float(total)))


    my_dict_verbosity = {"verbosity":
                        {"twilight":twilight_frac ,"applejack":apple_frac , "rarity":rarity_frac , "pinkie":pinkie_frac , "rainbow":rainbow_frac , "fluttershy":flutter_frac}}

    all_mentions(dfTwilight,dfAppleJack,dfRarity,dfPinkie,dfRainbow,dfFluttershy)
    follow_on_comments(df,'Twilight Sparkle')
    follow_on_comments(df,'Applejack')
    follow_on_comments(df,'Rarity')
    follow_on_comments(df,'Pinkie Pie')
    follow_on_comments(df,'Rainbow Dash')
    follow_on_comments(df,'Fluttershy')

    mentions = {"mentions":
    {"twilight":twilight_mentions1,
    "applejack" : applejack_mentions1,
    "rarity"    : rarity_mentions1,
    "pinkie"    : pinkie_mentions1,
    "rainbow"   : rainbow_mentions1,
    "fluttershy": fluttershy_mentions1,

    }}

  
    
    follow_on = {"follow_on_comments":
    {"twilight"  : twilight_follow_on,
    "applejack" : apple_follow_on,
    "rarity"    : rarity_follow_on,
    "pinkie"    : pinkie_follow_on,
    "rainbow"   : rainbow_follow_on,
    "fluttershy": fluttershy_follow_on,

}}
    
    

    non_dict_twilight = non_dictionary_twilight(dfTwilight)
    non_dict_apple = non_dictionary_apple(dfAppleJack)
    non_dict_rarity = non_dictionary_rarity(dfRarity)
    non_dict_pinkie = non_dictionary_pinkie(dfPinkie)
    non_dict_rainbow = non_dictionary_rainbow(dfRainbow)
    non_dict_flutter = non_dictionary_flutter(dfFluttershy)
    
    twilight_list = non_dict_twilight.keys()
    non_dictionary_words["non_dictionary_items"]["twilight"] = twilight_list
    apple_list = non_dict_apple.keys()
    non_dictionary_words["non_dictionary_items"]["applejack"] = apple_list
    rarity_list = non_dict_rarity.keys()
    non_dictionary_words["non_dictionary_items"]["rarity"] = rarity_list
    pinkie_list = non_dict_pinkie.keys()
    non_dictionary_words["non_dictionary_items"]["pinkie"] = pinkie_list
    rainbow_list = non_dict_rainbow.keys()
    non_dictionary_words["non_dictionary_items"]["rainbow"] = rainbow_list
    fluttershy_list = non_dict_flutter.keys()
    non_dictionary_words["non_dictionary_items"]["fluttershy"] = fluttershy_list

    json_string_ver = json.dumps(my_dict_verbosity)
    json_string_mentions = json.dumps(mentions)
    json_string_follow = json.dumps(follow_on)
    json_string_non_dict = json.dumps(non_dictionary_words)
    if args.o is None:
        print(json_string_ver)
        print(json_string_mentions)
        print(json_string_follow)
        print(json_string_non_dict)
    else:
            with open(args.o , 'w') as f:
                sys.stdout = f
                print(json_string_ver)
                print(json_string_mentions)
                print(json_string_follow)
                print(json_string_non_dict)

                
                
                
              
                
        
def empty_non_dict(twilight):
    twilight_mentions1 = {
        "applejack" : 0,
        "rarity"    : 0,
        "pinkie"    : 0,
        "rainbow"   : 0,
        "fluttershy": 0,
    }
    

    

    

def mentions(author , mention):
    tempdf = author.loc[author['dialog'].str.contains(mention , case=True)]
    counter = tempdf.dialog.str.count(mention).sum()
    return counter




def twilight_mentions(df ,pony):

    return mentions(df , pony)

def apple_mentions(df , pony):

    return mentions(df , pony)

def rarity_mentions(df , pony):

    return mentions(df , pony)


def pinkie_mentions(df , pony):

    return mentions(df , pony)


def rainbow_mentions(df , pony):

    return mentions(df , pony)


def flutter_mentions(df , pony):

    return mentions(df , pony)

def all_mentions(df1 , df2 , df3 , df4 , df5 , df6):
    total_twilight_mentions = twilight_mentions(df1 ,'Pinkie') + twilight_mentions(df1,'Applejack') + twilight_mentions(df1,'Rarity')  + twilight_mentions(df1,'Rainbow') + twilight_mentions(df1,'Fluttershy')
   
    pinkieovertotal = "{:.2f}".format((twilight_mentions(df1,'Pinkie')/float(total_twilight_mentions)))
    twilight_mentions1["pinkie"] = pinkieovertotal
    applejackovertotal = "{:.2f}".format((twilight_mentions(df1,'Applejack')/float(total_twilight_mentions)))
    
    twilight_mentions1["applejack"] = applejackovertotal
    rarityovertotal = "{:.2f}".format((twilight_mentions(df1,'Rarity')/float(total_twilight_mentions)))
    twilight_mentions1["rarity"] = rarityovertotal
    rainbowovertotal = "{:.2f}".format((twilight_mentions(df1,'Rainbow')/float(total_twilight_mentions)))
    twilight_mentions1["rainbow"] = rainbowovertotal
    flutterovertotal = "{:.2f}".format((twilight_mentions(df1,'Fluttershy')/float(total_twilight_mentions)))
    twilight_mentions1["fluttershy"] = flutterovertotal
    
    
    
    total_apple_mentions = apple_mentions(df2,'Pinkie') + apple_mentions(df2,'Twilight') + apple_mentions(df2,'Rarity')  + apple_mentions(df2,'Rainbow') + apple_mentions(df2,'Fluttershy')

    pinkieovertotal1 = "{:.2f}".format((apple_mentions(df2,'Pinkie')/float(total_apple_mentions)))
    applejack_mentions1["pinkie"] = pinkieovertotal1
    twilightovertotal1 = "{:.2f}".format((apple_mentions(df2,'Twilight')/float(total_apple_mentions)))
    applejack_mentions1["twilight"] = twilightovertotal1
    rarityovertotal1 = "{:.2f}".format((apple_mentions(df2,'Rarity')/float(total_apple_mentions)))
    applejack_mentions1["rarity"] = rarityovertotal1
    rainbowovertotal1 = "{:.2f}".format((apple_mentions(df2,'Rainbow')/float(total_apple_mentions)))
    applejack_mentions1["rainbow"] = rainbowovertotal1
    flutterovertotal1 = "{:.2f}".format((apple_mentions(df2,'Fluttershy')/float(total_apple_mentions)))
    applejack_mentions1["fluttershy"] = flutterovertotal1

  
    
    total_rarity_mentions = rarity_mentions(df3,'Pinkie') + rarity_mentions(df3,'Twilight') + rarity_mentions(df3,'Applejack')  + rarity_mentions(df3,'Rainbow') + rarity_mentions(df3,'Fluttershy')

    pinkieovertotal2 = "{:.2f}".format((rarity_mentions(df3,'Pinkie')/float(total_rarity_mentions)))
    rarity_mentions1["pinkie"] = pinkieovertotal2 
    twilightovertotal2 = "{:.2f}".format((rarity_mentions(df3,'Twilight')/float(total_rarity_mentions)))
    rarity_mentions1["twilight"] = twilightovertotal2 
    applejackovertotal2 = "{:.2f}".format((rarity_mentions(df3,'Applejack')/float(total_rarity_mentions)))
    rarity_mentions1["applejack"] = applejackovertotal2 
    rainbowovertotal2 = "{:.2f}".format((rarity_mentions(df3,'Rainbow')/float(total_rarity_mentions)))
    rarity_mentions1["rainbow"] = rainbowovertotal2 
    flutterovertotal2 = "{:.2f}".format((rarity_mentions(df3,'Fluttershy')/float(total_rarity_mentions)))
    rarity_mentions1["fluttershy"] = flutterovertotal2 

    

    total_pinkie_mentions = pinkie_mentions(df4,'Rarity') + pinkie_mentions(df4,'Twilight') + pinkie_mentions(df4,'Applejack')  + pinkie_mentions(df4,'Rainbow') + pinkie_mentions(df4,'Fluttershy')

    rarityovertotal3 = "{:.2f}".format((pinkie_mentions(df4,'Rarity')/float(total_pinkie_mentions)))
    pinkie_mentions1["rarity"] = rarityovertotal3
    twilightovertotal3 = "{:.2f}".format((pinkie_mentions(df4,'Twilight')/float(total_pinkie_mentions)))
    pinkie_mentions1["twilight"] = twilightovertotal3
    applejackovertotal3 = "{:.2f}".format((pinkie_mentions(df4,'Applejack')/float(total_pinkie_mentions)))
    pinkie_mentions1["applejack"] = applejackovertotal3
    rainbowovertotal3 = "{:.2f}".format((pinkie_mentions(df4,'Rainbow')/float(total_pinkie_mentions)))
    pinkie_mentions1["rainbow"] = rainbowovertotal3
    flutterovertotal3 = "{:.2f}".format((pinkie_mentions(df4,'Fluttershy')/float(total_pinkie_mentions)))
    pinkie_mentions1["fluttershy"] = flutterovertotal3

    

    total_rainbow_mentions = rainbow_mentions(df5,'Pinkie') + rainbow_mentions(df5,'Twilight') + rainbow_mentions(df5,'Applejack')  + rainbow_mentions(df5,'Rarity') + rainbow_mentions(df5,'Fluttershy')

    rarityovertotal4 = "{:.2f}".format((rainbow_mentions(df5,'Rarity')/float(total_rainbow_mentions)))
    rainbow_mentions1["rarity"] = rarityovertotal4
    twilightovertotal4 = "{:.2f}".format((rainbow_mentions(df5,'Twilight')/float(total_rainbow_mentions)))
    rainbow_mentions1["twilight"] = twilightovertotal4
    applejackovertotal4 = "{:.2f}".format((rainbow_mentions(df5,'Applejack')/float(total_rainbow_mentions)))
    rainbow_mentions1["applejack"] = applejackovertotal4
    pinkieovertotal4 = "{:.2f}".format((rainbow_mentions(df5,'Pinkie')/float(total_rainbow_mentions)))
    rainbow_mentions1["pinkie"] = pinkieovertotal4
    flutterovertotal4 = "{:.2f}".format((rainbow_mentions(df5,'Fluttershy')/float(total_rainbow_mentions)))
    rainbow_mentions1["fluttershy"] = flutterovertotal4

   
    

    total_flutter_mentions = flutter_mentions(df6,'Pinkie') + flutter_mentions(df6,'Twilight') + flutter_mentions(df6,'Applejack')  + flutter_mentions(df6,'Rarity') + flutter_mentions(df6,'Rainbow')

    rarityovertotal5 = "{:.2f}".format((flutter_mentions(df6,'Rarity')/float(total_flutter_mentions)))
    fluttershy_mentions1["rarity"] = rarityovertotal5
    twilightovertotal5 = "{:.2f}".format((flutter_mentions(df6,'Twilight')/float(total_flutter_mentions)))
    fluttershy_mentions1["twilight"] = twilightovertotal5
    applejackovertotal5 = "{:.2f}".format((flutter_mentions(df6,'Applejack')/float(total_flutter_mentions)))
    fluttershy_mentions1["applejack"] = applejackovertotal5
    pinkieovertotal5 = "{:.2f}".format((flutter_mentions(df6,'Pinkie')/float(total_flutter_mentions)))
    fluttershy_mentions1["pinkie"] = pinkieovertotal5
    rainbowovertotal5 = "{:.2f}".format((flutter_mentions(df6,'Rainbow')/float(total_flutter_mentions)))
    fluttershy_mentions1["rainbow"] = rainbowovertotal5

    
    
    
def speech_acts(temp_df):

    list1 = temp_df.index.values.tolist()
    rows = temp_df.shape[0]

    for i in range(len(list1)):
        if i>0:
            if (list1[i] == list1[i-1]+1):
                rows = rows - 1
    return rows



def follow_on_comments(df,pony1):

    

    list1 = df.pony.values.tolist()
    #print(list1)

    if (pony1 == 'Twilight Sparkle'):
        follow_apple_countt = 0
        follow_rarity_countt = 0
        follow_pinkie_countt = 0
        follow_rainbow_countt = 0
        follow_flutter_countt = 0
        other_countt = 0
        
        for i in range(len(list1)-1):
            if ((list1[i].find(pony1)!=-1)):
                if  (list1[i+1].find('Applejack')!= -1):
                    follow_apple_countt = follow_apple_countt + 1

                elif (list1[i+1].find('Rarity')!= -1):
                        follow_rarity_countt = follow_rarity_countt + 1

                elif ((list1[i+1].find('Pinkie')!= -1)):
                        follow_pinkie_countt = follow_pinkie_countt + 1

                elif ((list1[i+1].find('Rainbow')!= -1)):
                        follow_rainbow_countt = follow_rainbow_countt + 1

                elif ((list1[i+1].find('Fluttershy')!= -1)):
                        follow_flutter_countt = follow_flutter_countt + 1

                else:
                        other_countt= other_countt + 1

        total_follow_twilight = follow_apple_countt + follow_rarity_countt + follow_pinkie_countt + follow_rainbow_countt + follow_flutter_countt + other_countt
        a_fract = "{:.2f}".format((follow_apple_countt/float(total_follow_twilight)))
        twilight_follow_on["applejack"] = a_fract
        r_fract = "{:.2f}".format((follow_rarity_countt/float(total_follow_twilight)))
        twilight_follow_on["rarity"] = r_fract
        p_fract = "{:.2f}".format((follow_pinkie_countt/float(total_follow_twilight)))
        twilight_follow_on["pinkie"] = p_fract
        ra_fract = "{:.2f}".format((follow_rainbow_countt/float(total_follow_twilight)))
        twilight_follow_on["rainbow"] = ra_fract
        f_fract = "{:.2f}".format((follow_flutter_countt/float(total_follow_twilight)))
        twilight_follow_on["fluttershy"] = f_fract
        o_fract = "{:.2f}".format((other_countt/float(total_follow_twilight)))
        twilight_follow_on["other"] = o_fract

        
        
        

        
          
    if (pony1 == 'Applejack'):
        follow_twilight_counta = 0
        follow_rarity_counta = 0
        follow_pinkie_counta = 0
        follow_rainbow_counta = 0
        follow_flutter_counta = 0
        other_counta = 0

        for i in range(len(list1)-1):
            if ((list1[i].find(pony1)!=-1)):
                if  (list1[i+1].find('Twilight Sparkle')!= -1):
                    follow_twilight_counta = follow_twilight_counta + 1

                elif (list1[i+1].find('Rarity')!= -1):
                        follow_rarity_counta = follow_rarity_counta + 1

                elif ((list1[i+1].find('Pinkie')!= -1)):
                        follow_pinkie_counta = follow_pinkie_counta + 1

                elif ((list1[i+1].find('Rainbow')!= -1)):
                        follow_rainbow_counta = follow_rainbow_counta + 1

                elif ((list1[i+1].find('Fluttershy')!= -1)):
                        follow_flutter_counta = follow_flutter_counta + 1

                else:
                        other_counta= other_counta + 1

            
        total_follow_apple = follow_twilight_counta + follow_rarity_counta + follow_pinkie_counta + follow_rainbow_counta + follow_flutter_counta +other_counta
        t_fraca = "{:.2f}".format((follow_twilight_counta/float(total_follow_apple)))
        apple_follow_on["twilight"] = t_fraca
        r_fraca = "{:.2f}".format((follow_rarity_counta/float(total_follow_apple)))
        apple_follow_on["rarity"] = r_fraca
        p_fraca = "{:.2f}".format((follow_pinkie_counta/float(total_follow_apple)))
        apple_follow_on["pinkie"] = p_fraca
        ra_fraca = "{:.2f}".format((follow_rainbow_counta/float(total_follow_apple)))
        apple_follow_on["rainbow"] = ra_fraca
        f_fraca = "{:.2f}".format((follow_flutter_counta/float(total_follow_apple)))
        apple_follow_on["fluttershy"] = f_fraca
        o_fraca = "{:.2f}".format((other_counta/float(total_follow_apple)))
        apple_follow_on["other"] = o_fraca
        

        
             
            
    if (pony1 == 'Rarity'):

        follow_twilight_countr = 0
        follow_apple_countr = 0
        follow_pinkie_countr = 0
        follow_rainbow_countr = 0
        follow_flutter_countr = 0
        other_countr = 0

        for i in range(len(list1)-1):
            if ((list1[i].find(pony1)!=-1)):
                if  (list1[i+1].find('Applejack')!= -1):
                    follow_apple_countr = follow_apple_countr + 1

                elif (list1[i+1].find('Twilight Sparkle')!= -1):
                        follow_twilight_countr = follow_twilight_countr + 1

                elif ((list1[i+1].find('Pinkie')!= -1)):
                        follow_pinkie_countr = follow_pinkie_countr + 1

                elif ((list1[i+1].find('Rainbow')!= -1)):
                        follow_rainbow_countr = follow_rainbow_countr + 1

                elif ((list1[i+1].find('Fluttershy')!= -1)):
                        follow_flutter_countr = follow_flutter_countr + 1

                else:
                        other_countr= other_countr + 1
            
        total_follow_rarity = follow_twilight_countr + follow_apple_countr + follow_pinkie_countr + follow_rainbow_countr + follow_flutter_countr+other_countr
        t_fracr = "{:.2f}".format((follow_twilight_countr/float(total_follow_rarity)))
        rarity_follow_on["twilight"] = t_fracr
        a_fracr = "{:.2f}".format((follow_apple_countr/float(total_follow_rarity)))
        rarity_follow_on["applejack"] = a_fracr
        p_fracr = "{:.2f}".format((follow_pinkie_countr/float(total_follow_rarity)))
        rarity_follow_on["pinkie"] = p_fracr
        ra_fracr = "{:.2f}".format((follow_rainbow_countr/float(total_follow_rarity)))
        rarity_follow_on["rainbow"] = ra_fracr
        f_fracr = "{:.2f}".format((follow_flutter_countr/float(total_follow_rarity)))
        rarity_follow_on["fluttershy"] = f_fracr
        o_fracr = "{:.2f}".format((other_countr/float(total_follow_rarity)))
        rarity_follow_on["other"] = o_fracr

      


    if (pony1 == 'Pinkie Pie'):

        follow_twilight_countp = 0
        follow_apple_countp = 0
        follow_rarity_countp = 0
        follow_rainbow_countp = 0
        follow_flutter_countp = 0
        other_countp = 0

        for i in range(len(list1)-1):
            if ((list1[i].find(pony1)!=-1)):
                if  (list1[i+1].find('Applejack')!= -1):
                    follow_apple_countp = follow_apple_countp + 1

                elif (list1[i+1].find('Rarity')!= -1):
                        follow_rarity_countp = follow_rarity_countp + 1

                elif ((list1[i+1].find('Twilight Sparkle')!= -1)):
                        follow_twilight_countp = follow_twilight_countp + 1

                elif ((list1[i+1].find('Rainbow')!= -1)):
                        follow_rainbow_countp = follow_rainbow_countp + 1

                elif ((list1[i+1].find('Fluttershy')!= -1)):
                        follow_flutter_countp = follow_flutter_countp + 1

                else:
                        other_countp= other_countp + 1

        total_follow_pinkie = follow_twilight_countp + follow_apple_countp + follow_rarity_countp + follow_rainbow_countp + follow_flutter_countp + other_countp
        t_fracp = "{:.2f}".format((follow_twilight_countp/float(total_follow_pinkie)))
        pinkie_follow_on["twilight"] = t_fracp 
        a_fracp = "{:.2f}".format((follow_apple_countp/float(total_follow_pinkie)))
        pinkie_follow_on["applejack"] = a_fracp
        r_fracp = "{:.2f}".format((follow_rarity_countp/float(total_follow_pinkie)))
        pinkie_follow_on["rarity"] = r_fracp
        ra_fracp = "{:.2f}".format((follow_rainbow_countp/float(total_follow_pinkie)))
        pinkie_follow_on["rainbow"] = ra_fracp
        f_fracp = "{:.2f}".format((follow_flutter_countp/float(total_follow_pinkie)))
        pinkie_follow_on["fluttershy"] = f_fracp
        o_fracp = "{:.2f}".format((other_countp/float(total_follow_pinkie)))
        pinkie_follow_on["other"] = o_fracp
    
       

    if (pony1 == 'Rainbow Dash'):

        follow_twilight_countra = 0
        follow_apple_countra = 0
        follow_rarity_countra = 0
        follow_pinkie_countra = 0
        follow_flutter_countra = 0
        other_countra = 0

        for i in range(len(list1)-1):
            if ((list1[i].find(pony1)!=-1)):
                if  (list1[i+1].find('Applejack')!= -1):
                    follow_apple_countra = follow_apple_countra + 1

                elif (list1[i+1].find('Rarity')!= -1):
                        follow_rarity_countra = follow_rarity_countra + 1

                elif ((list1[i+1].find('Pinkie')!= -1)):
                        follow_pinkie_countra = follow_pinkie_countra + 1

                elif ((list1[i+1].find('Twilight Sparkle')!= -1)):
                        follow_twilight_countra = follow_twilight_countra + 1

                elif ((list1[i+1].find('Fluttershy')!= -1)):
                        follow_flutter_countra = follow_flutter_countra + 1

                else:
                        other_countra= other_countra + 1

        total_follow_rainbow = follow_twilight_countra + follow_apple_countra + follow_rarity_countra + follow_pinkie_countra + follow_flutter_countra + other_countra
        t_fracra = "{:.2f}".format((follow_twilight_countra/float(total_follow_rainbow)))
        rainbow_follow_on["twilight"] = t_fracra
        a_fracra = "{:.2f}".format((follow_apple_countra/float(total_follow_rainbow)))
        rainbow_follow_on["applejack"] = a_fracra
        r_fracra = "{:.2f}".format((follow_rarity_countra/float(total_follow_rainbow)))
        rainbow_follow_on["rarity"] = r_fracra
        p_fracra = "{:.2f}".format((follow_pinkie_countra/float(total_follow_rainbow)))
        rainbow_follow_on["pinkie"] = p_fracra
        f_fracra = "{:.2f}".format((follow_flutter_countra/float(total_follow_rainbow)))
        rainbow_follow_on["fluttershy"] = f_fracra
        o_fracra = "{:.2f}".format((other_countra/float(total_follow_rainbow)))
        rainbow_follow_on["other"] = o_fracra
        
    if (pony1 == 'Fluttershy'):

        follow_twilight_countf = 0
        follow_apple_countf = 0
        follow_rarity_countf = 0
        follow_pinkie_countf = 0
        follow_rainbow_countf = 0
        other_countf = 0

        for i in range(len(list1)-1):
            if ((list1[i].find(pony1)!=-1)):
                if  (list1[i+1].find('Applejack')!= -1):
                    follow_apple_countf = follow_apple_countf + 1

                elif (list1[i+1].find('Rarity')!= -1):
                        follow_rarity_countf = follow_rarity_countf + 1

                elif ((list1[i+1].find('Pinkie')!= -1)):
                        follow_pinkie_countf = follow_pinkie_countf + 1

                elif ((list1[i+1].find('Rainbow')!= -1)):
                        follow_rainbow_countf = follow_rainbow_countf + 1

                elif ((list1[i+1].find('Twilight Sparkle')!= -1)):
                        follow_twilight_countf = follow_twilight_countf + 1

                else:
                        other_countf= other_countf + 1
            

        total_follow_flutter = follow_twilight_countf + follow_apple_countf + follow_rarity_countf + follow_pinkie_countf + follow_rainbow_countf + other_countf
        t_fracf = "{:.2f}".format((follow_twilight_countf/float(total_follow_flutter)))
        fluttershy_follow_on["twilight"] = t_fracf
        a_fracf = "{:.2f}".format((follow_apple_countf/float(total_follow_flutter)))
        fluttershy_follow_on["applejack"] = a_fracf
        r_fracf = "{:.2f}".format((follow_rarity_countf/float(total_follow_flutter)))
        fluttershy_follow_on["rarity"] = r_fracf
        p_fracf = "{:.2f}".format((follow_pinkie_countf/float(total_follow_flutter)))
        fluttershy_follow_on["pinkie"] = p_fracf
        ra_fracf = "{:.2f}".format((follow_rainbow_countf/float(total_follow_flutter)))
        fluttershy_follow_on["rainbow"] = ra_fracf
        o_fracf = "{:.2f}".format((other_countf/float(total_follow_flutter)))
        fluttershy_follow_on["other"] = o_fracf
        

def non_dictionary_twilight(df):
   

    row_list = df.dialog.tolist()
    #print(row_list)
    non_dict = {}

    for item in list(row_list):
        result = re.sub(r'[^a-zA-Z]', " ", str(item))
        array = result.split()
        for i in array:
            if (i.lower() in alphatxt) == False:
                if i.lower() in non_dict:
                    non_dict[i.lower()]+=1
                else:
                    non_dict[i.lower()] = 1
            
    return dict(sorted(non_dict.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])

    #print(non_dict_twilight)


def non_dictionary_apple(df):
    with open('../data/words_alpha.txt') as file:
        alphatxt = set(word.strip().lower() for word in file)

    row_list = df.dialog.tolist()
    non_dict = {}
    

    for item in list(row_list):
        result = re.sub(r'[^a-zA-Z]', " ", str(item))
        array = result.split()
        for i in array:
            if (i.lower() in alphatxt) == False:
                if i.lower() in non_dict:
                    non_dict[i.lower()]+=1
                else:
                    non_dict[i.lower()] = 1
            
    return dict(sorted(non_dict.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])           


def non_dictionary_rarity(df):
    with open('../data/words_alpha.txt') as file:
        alphatxt = set(word.strip().lower() for word in file)

    row_list = df.dialog.tolist()
    non_dict = {}
    

    for item in list(row_list):
        result = re.sub(r'[^a-zA-Z]', " ", str(item))
        array = result.split()
        for i in array:
            if (i.lower() in alphatxt) == False:
                if i.lower() in non_dict:
                    non_dict[i.lower()]+=1
                else:
                    non_dict[i.lower()] = 1
            
    return dict(sorted(non_dict.iteritems(), key=operator.itemgetter(1), reverse=True)[:5]) 
       

def non_dictionary_pinkie(df):
    with open('../data/words_alpha.txt') as file:
        alphatxt = set(word.strip().lower() for word in file)

    row_list = df.dialog.tolist()
    non_dict = {}
    

    for item in list(row_list):
        result = re.sub(r'[^a-zA-Z]', " ", str(item))
        array = result.split()
        for i in array:
            if (i.lower() in alphatxt) == False:
                if i.lower() in non_dict:
                    non_dict[i.lower()]+=1
                else:
                    non_dict[i.lower()] = 1
            
    return dict(sorted(non_dict.items(), key=operator.itemgetter(1), reverse=True)[:5])


def non_dictionary_rainbow(df):
    with open('../data/words_alpha.txt') as file:
        alphatxt = set(word.strip().lower() for word in file)

    row_list = df.dialog.tolist()
    non_dict = {}
    

    for item in list(row_list):
        result = re.sub(r'[^a-zA-Z]', " ", str(item))
        array = result.split()
        for i in array:
            if (i.lower() in alphatxt) == False:
                if i.lower() in non_dict:
                    non_dict[i.lower()]+=1
                else:
                    non_dict[i.lower()] = 1
            
    return dict(sorted(non_dict.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])

def non_dictionary_flutter(df):
    with open('../data/words_alpha.txt') as file:
        alphatxt = set(word.strip().lower() for word in file)

    row_list = df.dialog.tolist()
    non_dict = {}
    

    for item in list(row_list):
        result = re.sub(r'[^a-zA-Z]', " ", str(item))
        array = result.split()
        for i in array:
            if (i.lower() in alphatxt) == False:
                if i.lower() in non_dict:
                    non_dict[i.lower()]+=1
                else:
                    non_dict[i.lower()] = 1
            
    return dict(sorted(non_dict.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])




if __name__ == '__main__':
	main()
