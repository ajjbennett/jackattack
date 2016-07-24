C_COLOR_BLACK=(0,0,0)
C_COLOR_WHITE=(255,255,255)
C_COLOR_RED=(255,0,0)
C_COLOR_ORANGE=(255,102,0)
C_COLOR_BLUE=(0,0,255)
C_COLOR_LBLUE=(0,102,255)
C_COLOR_CREAMY_BLUE=(96,168,193)
C_COLOR_VLBLUE=(153, 204, 255)
C_COLOR_GREEN=(0,255,0)
C_COLOR_MEDIUM_GREEN=(84,140,33)
C_COLOR_SNOT_GREEN=(190,207,68)  ## yellowy color
C_COLOR_RANDOM=(144,22,33)
C_COLOR_YELLOW=(255,255,0)
C_COLOR_PURPLE=(118,59,160)
C_COLOR_MEDIUM_PURPLE=(118,59,160)
C_COLOR_LPURPLE=(105,89,221)
C_COLOR_PINK=(255,153,204)
C_COLOR_AQUA=(0, 255, 255)
C_COLOR_INDIGO=(49, 30, 156)
C_COLOR_SNATA_FE=(179,107,87)
C_COLOR_SADDLE_BROWN=(130,79,17)
C_COLOR_CRAB_APPLE=(126,54,40)

#C_COLOR_INDIGO2=(49,30,156)

C_COLOR_ENEMY_BLOOD=(57,255,20)

C_GROUND_COLOR=(222,222,222)


# default level contains a template od defaults, any attriubtes in this and not in specific lelevl, it will inherit them

levelconfig={
   'default':{
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'ledge_color':C_COLOR_WHITE,
        'ledge_touched_color':C_COLOR_ORANGE,
        'ledge_all_touched_color':C_COLOR_GREEN,
        'ledge_platform_bonus':1000,
        #'ledge_delay_speed':10,
        'ledge_mult':7
        },
   '1':{
        'level_name':'The Attack Begins', 
        'speed':2,
        'time':2000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_INDIGO,
        'brick_border_color':C_COLOR_SNOT_GREEN
        },
   '2':{
        'level_name':'Touch Tone', 
        'speed':2,
        'time':2000,
        'enemy_color':C_COLOR_YELLOW,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_LPURPLE,
        'brick_border_color':C_COLOR_INDIGO
        },
   '3':{
        'level_name':'Hydrophobia', 
        'speed':2,
        'time':1000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_LPURPLE,
        'brick_border_color':C_COLOR_INDIGO
        },
   '4':{
        'level_name':'Upstairs Downstairs', 
        'speed':2,
        'time':2000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_GREEN,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_WHITE,
        'brick_border_color':C_COLOR_MEDIUM_PURPLE
        },
   '5':{
        'level_name':'Big Block', 
        'speed':2,
        'time':2000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_WHITE,
        'brick_border_color':C_COLOR_MEDIUM_GREEN
        },
   '6':{
        'level_name':'Water Bridge Down', 
        'speed':2,
        'time':2000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_VLBLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_INDIGO,
        'brick_border_color':C_COLOR_SNOT_GREEN,
        'ledge_color':C_COLOR_VLBLUE,
        'ledge_touched_color':C_COLOR_PURPLE
        },
   '7':{
        'level_name':'Puzzle I', 
        'speed':2,
        'time':2000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_SNATA_FE,
        'brick_border_color':C_COLOR_CREAMY_BLUE,
        'ledge_color':C_COLOR_WHITE,
        'ledge_touched_color':C_COLOR_BLUE
        },
   '8':{
        'level_name':'Goalpost', 
        'speed':2,
        'time':2000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_WHITE,
        'brick_border_color':C_COLOR_SNOT_GREEN,
        'ledge_color':C_COLOR_WHITE,
        'ledge_touched_color':C_COLOR_BLUE
        },
   '9':{
        'level_name':'Sidebars', 
        'speed':2,
        'time':1000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_SADDLE_BROWN,
        'brick_border_color':C_COLOR_INDIGO
        },
   '10':{
        'level_name':'Pyramid I', 
        'speed':2,
        'time':2000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_INDIGO,
        'brick_border_color':C_COLOR_WHITE
        },
   '11':{
        'level_name':'Manifestation', 
        'speed':2,
        'time':2000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_INDIGO,
        'brick_border_color':C_COLOR_SNOT_GREEN
        },
   '12':{
        'level_name':'Hard Climb', 
        'speed':2,
        'time':2000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_SNOT_GREEN,
        'brick_border_color':C_COLOR_INDIGO
        },
   '13':{
        'level_name':'Hidden Horsie', 
        'speed':2,
        'time':2000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_WHITE,
        'brick_border_color':C_COLOR_CRAB_APPLE
        },
   '14':{
        'level_name':'Crypt of Death', 
        'speed':2,
        'time':2000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_SADDLE_BROWN,
        'brick_border_color':C_COLOR_SNOT_GREEN
        },
   '15':{
        'level_name':'Splash Down', 
        'speed':2,
        'time':1000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_SNOT_GREEN,
        'brick_border_color':C_COLOR_CRAB_APPLE,
        'ledge_delay_speed':3
        },
   '16':{
        'level_name':'Platform Puzzle II', 
        'speed':2,
        'time':3000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_BLACK,
        'brick_border_color':C_COLOR_YELLOW,
        'ledge_delay_speed':3
        },
   '17':{
        'level_name':'Slide Rule', 
        'speed':2,
        'time':2000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_PURPLE,
        'brick_border_color':C_COLOR_WHITE,
        'ledge_delay_speed':3
        },
   '18':{
        'level_name':'Platform Puzzle III', 
        'speed':2,
        'time':2000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_BLACK,
        'brick_border_color':C_COLOR_BLUE,
        'ledge_delay_speed':3
        },
   '19':{
        'level_name':'Tower Of Babel', 
        'speed':2,
        'time':2000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_PINK,
        'brick_border_color':C_COLOR_YELLOW,
        'ledge_delay_speed':3
        },
   '20':{
        'level_name':'Isolation Island', 
        'speed':2,
        'time':1000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_WHITE,
        'brick_border_color':C_COLOR_BLUE,
        'ledge_delay_speed':3
        },
   '21':{
        'level_name':'Let Me Out', 
        'speed':2,
        'time':1000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_WHITE,
        'brick_border_color':C_COLOR_INDIGO,
        'ledge_delay_speed':3
        } ,
   '22':{
        'level_name':'Thumb Getting Tired?', 
        'speed':2,
        'time':1000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_BLACK,
        'brick_border_color':C_COLOR_YELLOW,
        'ledge_delay_speed':3
        },
   '23':{
        'level_name':'Hop Scotch', 
        'speed':2,
        'time':1000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_GREEN,
        'brick_border_color':C_COLOR_BLUE,
        'ledge_delay_speed':3
        },
   '24':{
        'level_name':'Socrates', 
        'speed':2,
        'time':2000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_VLBLUE,
        'brick_border_color':C_COLOR_WHITE,
        'ledge_delay_speed':3
        } ,
   '25':{
        'level_name':'Think Fast', 
        'speed':2,
        'time':2000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_AQUA,
        'brick_border_color':C_COLOR_INDIGO,
        'ledge_delay_speed':3
        } ,
   '26':{
        'level_name':'lillys clean bedroom', 
        'speed':2,
        'time':1000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_AQUA,
        'brick_border_color':C_COLOR_INDIGO,
        'ledge_delay_speed':3
        } ,
   '27':{
        'level_name':'lillys clean bedroom', 
        'speed':2,
        'time':1000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_AQUA,
        'brick_border_color':C_COLOR_INDIGO,
        'ledge_delay_speed':3
        } ,
   '28':{
        'level_name':'lillys clean bedroom', 
        'speed':2,
        'time':1000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_AQUA,
        'brick_border_color':C_COLOR_INDIGO,
        'ledge_delay_speed':3
        } ,
   '29':{
        'level_name':'lillys clean bedroom', 
        'speed':2,
        'time':1000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_AQUA,
        'brick_border_color':C_COLOR_INDIGO,
        'ledge_delay_speed':3
        } ,
   '30':{
        'level_name':'lillys clean bedroom', 
        'speed':2,
        'time':1000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_AQUA,
        'brick_border_color':C_COLOR_INDIGO,
        'ledge_delay_speed':3
        } ,
   '31':{
        'level_name':'lillys clean bedroom', 
        'speed':2,
        'time':1000,
        'enemy_color':C_COLOR_GREEN,
        'ground_tiles_color':C_COLOR_BLUE,
        'ground_tiles_etched_color':C_COLOR_BLACK,
        'brick_color':C_COLOR_AQUA,
        'brick_border_color':C_COLOR_INDIGO,
        'ledge_delay_speed':3
        }   		
}