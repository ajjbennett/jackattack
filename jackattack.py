#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# andrew bennett
# june 2016
# test
#
# version 
# 1.0 28 july 2016 1 original, contains first 30 levels of this game, is slighty different in display but fundamentally same


import pygame
import pygame.mixer
import time
import random
import datetime
import config
import os
import sys
#import json
import pickle
import platform

pygame.init()

l_prev_jack={}



#cheat codes used while testing and also left in the game as a feature
C_CHEAT_CODE_HELLMODE='h3ll'
C_CHEAT_CODE_RELOAD_LEVEL='relo'
C_CHEAT_CODE_NEXT_LEVEL='next'
C_CHEAT_CODE_PREV_LEVEL='nrev' # cant use the pause key unfortunatly
C_CHEAT_CODE_JACK_IMMORTAL='godd' # cant use the pause key unfortunatly
C_CHEAT_CODE_JACK_UNLIMITED_LIVES='jhul' # cant use the pause key unfortunatly
C_CHEAT_CODE_POOL_BALL_IMAGES='whit' 
C_CHEAT_CODE_JACK_AS_LADYBIRD='ldbg'
C_CHEAT_CODE_EXTRA_LIFE='kool'
C_CHEAT_CODE_DISPLAY_BRICK_NUMBERS="brck" 

C_CHEATS = {C_CHEAT_CODE_HELLMODE: "makes the enemy go crazy",
            C_CHEAT_CODE_RELOAD_LEVEL: "reloads the level incase you get trapped or just want to start again",
            C_CHEAT_CODE_NEXT_LEVEL: "go to the next level",
            C_CHEAT_CODE_PREV_LEVEL:"go to the previous level",
            C_CHEAT_CODE_JACK_IMMORTAL:"makes Jack become immortal, he can't be killed",
            C_CHEAT_CODE_JACK_UNLIMITED_LIVES:"Jack now has unlimited lives",
            C_CHEAT_CODE_POOL_BALL_IMAGES:"the enemy now appear as pool balls",
            C_CHEAT_CODE_JACK_AS_LADYBIRD:"Jack morphs into a ladybug",
            C_CHEAT_CODE_EXTRA_LIFE:"Jack gets an extra life",
            C_CHEAT_CODE_DISPLAY_BRICK_NUMBERS:"Display numbers on the bricks, just cause you can"}


C_HIGHSCORES_FILE="highscores.dat"

C_INSTRUCTIONS_TEXT=['Welcome to Jack Attack, a classic game made in 1983 by Kevin Kieller & John Traynor',
                     'This game is not for sale, just a python port for lovers of the best game of the 80s!',
					 '',
                     'The object of the game is to kill the aliens, by moving Jack and squashing them by either jumping, hopping',
                     'on them, or crushing them with bricks.',
                     '',
                     'Levels can contain platforms which offer a bonus score, but these will dissappear after the time limit',
                     'expires. Jack can land on the ground but he can not swim, so beware of this!',
                     '',
                     'Keys are as follows:',
                     '',
                     '    E=Hop Left, R=Hop Right',
                     '    X=push/pull brick left, C=push/pull brick right... pushing happens before a pull',
                     '    The left,right arrows move the Jack sideways, and the up arrow makes the jack jump up',
                     '    S=Toggle sound, P=toggle Pause, Q=Quit',
                     '',
                     'There are many easter eggs, which are 4 character key sequences which trigger some cheats or funnies',
                     '',
                     'Please note there is an issue with the sound which sometimes causes this game to crash on the Mac, so please disable sound',
                     'if this is the case. This normally happens with the countdown timer at the end of the level' 
                     '',
                     'Hit 1 to start, Q to quit, L to toggle background level, C to view cheats          Andrew Bennett 2016'] 

C_CHEATS_TEXT=['So you decided to cheat, oh well this game can be hard, so why not!',
                     '']

#dt={'d': 2, 'f': 2, 'g': 2, 'q': 5, 'w': 3}
#dt=sorted(dt.iteritems())
st=""

for key, val in C_CHEATS.items():
    st = '"' + key + '"  = ' + val
    C_CHEATS_TEXT.append(st)

C_CHEATS_TEXT.append('')
C_CHEATS_TEXT.append('')
C_CHEATS_TEXT.append('Hit 1 to start, Q to quit, L to toggle background level, I to view Instructions (Andrew Bennett 2016)')  					 


C_FRAMERS_PER_SEC=15 # the timer goes down 4 at a time, so = 60 per second with a setting of 15 here, so 2000 on the timer = approx 33 secs
C_SECONDS_TODELAY_GAME_WHEN_JACK_DIES=5 # number of seconds to keep refreshing after jack dies, this solves ay post bricks stuck in the air etc
C_ENEMY_STUNNED_SPEED=6
C_ENEMY_SPEED_START_MULTIPLIER=1 # number of times slower the enemey will be when they first drop

#C_NUM_LEVELS=31

C_SCORE_KILL_ENEMY=100
C_SCORE_BRICKMOVE=2

# debug defines for testing, can be set to whats needed for testing, or set to appropriate values for game
# cheat codes/easter eggs can be used to flip these during the game
C_START_LEVEL=1
C_START_LIVES=5
C_SCORE_NEW_LIFE_BONUS=5000
C_MAX_LIVES_ALLOWED=9
C_ENABLE_BADDIES_MOVEMENT=True
C_DISPLAY_BADDIES_AS_POOL_BALLS=False # if not true display green aliens, can be toggled with cheat code below
C_DISPLAY_JACK_AS_LADYBIRD=False
C_NUM_BADDIES_OVERRIDE=99
C_DISPLAY_BRICK_NUMBERS=False
C_CAN_JACK_BE_KILLED=True
C_JACK_HAS_UNLIMITED_LIVES=False #if true the lives counter doesnt decrement when they die
C_ENEMIES_FROM_HELL=False

#C_SOUNDS_ON_FOR_DEFECT_MAC_ISSUE=True
C_SOUNDS_ON=True
C_GAME_PAUSED=False

#C_SHOW_BRICK_CNT=False
C_DISPLAY_BLOOD_SPLATTER=True
C_BLIT_TEXT=True




C_INCLUDE_DIR="./include/"

C_BRICK_MOVE_SOUND_FILE=C_INCLUDE_DIR+'brickmove.wav'
C_ENEMY_DEAD_SOUND_FILE=C_INCLUDE_DIR+'enemydead.wav'
C_JACK_DEAD_SOUND_FILE=C_INCLUDE_DIR+'jackdead.wav'
C_SPLASH_SOUND_FILE=C_INCLUDE_DIR+'splash.wav'
C_PLATFORM_SHRINK_SOUND_FILE=C_INCLUDE_DIR+'platform_shrink.wav'
C_PLATFORM_TOUCH_SOUND_FILE=C_INCLUDE_DIR+'platform_touch.wav'
#C_TIMER_WIND_DOWN_SOUND_FILE=C_INCLUDE_DIR+'timedown.wav'


C_ENEMY_IMAGE=C_INCLUDE_DIR+'baddie2.png'
C_JACK_IMAGE=C_INCLUDE_DIR+'jack.png'
C_GODMODE_IMAGE=C_INCLUDE_DIR+'halo.png'
C_HELLMODE_IMAGE=C_INCLUDE_DIR+'hell.png'
C_SOUNDSON_IMAGE=C_INCLUDE_DIR+'soundon.png'
C_SOUNDSOFF_IMAGE=C_INCLUDE_DIR+'soundoff.png'
C_PAUSED_IMAGE=C_INCLUDE_DIR+'paused.png'
C_WATER_IMAGE=C_INCLUDE_DIR+'water.png'
C_LADYBIRD_IMAGE=C_INCLUDE_DIR+'ladybird.png'

#C_FONT_FILE=C_INCLUDE_DIR+'freesansbold.ttf'
#C_FONT_FILE='freesansbold.ttf'
C_FONT_FILE='comicsansms'
C_FONT_SIZE=24
C_FONT=pygame.font.SysFont(C_FONT_FILE, C_FONT_SIZE)

 

C_NOTHING='.'
C_WATER='W'
C_BRICK='B'
C_LEDGE='L'
C_JACK='J'
C_ENEMY='E'
C_GROUND='G'

C_LEFT='left'
C_RIGHT='right'
C_UP='up'
C_DOWN='down'


C_COLOR_BLACK=(0,0,0)
C_COLOR_BG=(0,0,80)

C_COLOR_WHITE=(255,255,255)
C_COLOR_RED=(255,0,0)
C_COLOR_BLUE=(0,0,255)
C_COLOR_LBLUE=(0,102,255)
C_COLOR_GREEN=(0,255,0)
C_COLOR_RANDOM=(144,22,33)
C_COLOR_YELLOW=(255,255,0)
C_GROUND_COLOR=(222,222,222)

C_BRICK_BORDER=10


#C_BLOCK_SIZE=120
C_BLOCK_SIZE_WIDTH=120
C_BLOCK_SIZE_HEIGHT=80

C_HEIGHT_IN_BLOCKS=11
C_WIDTH_IN_BLOCKS=10

C_FRAME_DISPLAY_WIDTH=C_BLOCK_SIZE_WIDTH*C_WIDTH_IN_BLOCKS
C_FRAME_DISPLAY_HEIGHT=int(C_BLOCK_SIZE_HEIGHT*(float(C_HEIGHT_IN_BLOCKS)+.5)) # .5 is the top banner, bottom banner shares it with the ground level which is only .5 deep

C_KEY_UP=pygame.K_UP
C_KEY_DOWN=pygame.K_DOWN
C_KEY_LEFT=pygame.K_LEFT
C_KEY_RIGHT=pygame.K_RIGHT
C_KEY_HOP_LEFT=pygame.K_e
C_KEY_HOP_RIGHT=pygame.K_r
C_KEY_BRICKMOVE_LEFT=pygame.K_x
C_KEY_BRICKMOVE_RIGHT=pygame.K_c
C_KEY_PAUSE=pygame.K_p
C_KEY_SOUNDONOFF=pygame.K_s
C_KEY_START=pygame.K_1
C_KEY_LEVEL_DISP_MOVE=pygame.K_l
C_KEY_LEVEL_SHOW_CHEATS=pygame.K_c
C_KEY_LEVEL_SHOW_INSTRUCTIONS=pygame.K_i

C_KEY_QUIT=pygame.K_q
C_LEDGE_START_MULT=5# dpcified in 10ths, ie 10=full 5 = 5/10 
C_LEDGE_DEC_VAL=1

#C_GROUND_START_MULT=5# dpcified in 10ths, ie 10=full 5 = 5/10 

C_BADDIE_MOVE_DELAY_SECS=3
C_BADDIE_MAX_JUMP_BLOCKS=10
C_BADDIE_MIN_JUMP_BLOCKS=0
C_HUMAN_JUMP_BLOCKS=3

C_EPOCH_START=time.time() # warning this is set in load level too, so not actually a constant, needs tidying up

C_HIGHSCORE_DISPLAY_X_START=C_FRAME_DISPLAY_WIDTH/2 - 100
C_TIMER_DISPLAY_X_START=C_FRAME_DISPLAY_WIDTH-200


gameDisplay=pygame.display.set_mode((C_FRAME_DISPLAY_WIDTH,C_FRAME_DISPLAY_HEIGHT))
pygame.display.set_caption('Jack Attack')
clock=pygame.time.Clock()

#def printd(p_text)

#def printifdiff(p_text,p1,p2,p_print_anyway=False):
#   if str(p1)!=str(p2) or p_print_anyway:
#      print(p_text+' '+str(p1)+' '+str(p2)) 

def ClearScreen(p_clear_code):
   #print(p_clear_code)
   # the top banner and bottom banner are split into components as follows
   # top banner, into thrids {left,center, and right}
   # bottom banner is just as a one esegment entirely 
   #
   # -1 = clear neither of the top or bottom barries
   # 0 = clear all
   # 1 = clear top only
 
   if p_clear_code==0:
      gameDisplay.fill(C_COLOR_BG)
   elif p_clear_code==1: # just blit a black rectangle to the bottom banner
      pygame.draw.rect(gameDisplay,C_COLOR_BG,[0,0,C_FRAME_DISPLAY_WIDTH,C_FRAME_DISPLAY_HEIGHT - (C_BLOCK_SIZE_HEIGHT*.5)]) 
   elif p_clear_code==-1:  # we need to clear the bits between the top and bottom banner first
      pygame.draw.rect(gameDisplay,C_COLOR_BG,[0,(C_BLOCK_SIZE_HEIGHT*.5),C_FRAME_DISPLAY_WIDTH,C_FRAME_DISPLAY_HEIGHT - (C_BLOCK_SIZE_HEIGHT)]) 
      #now we need to blit the individual pies we are erasing
   #else:
      #if p_clear_code==2 or p_clear_code==4: # just blit a black rectangle to the bottom banner
      #   pygame.draw.rect(gameDisplay,C_COLOR_RED,[0,1,C_HIGHSCORE_DISPLAY_X_START-1,C_BLOCK_SIZE_HEIGHT*.5]) 
      #if p_clear_code==3 or p_clear_code==4: # just blit a black rectangle to the bottom banner
      #   #print(C_TIMER_DISPLAY_X_START)
      #   pygame.draw.rect(gameDisplay,C_COLOR_GREEN,[C_TIMER_DISPLAY_X_START,0,200,C_BLOCK_SIZE_HEIGHT*.5]) 
  

def flushkeybuffer():
   for event in pygame.event.get():
      print('flushing key buffer')



def PlaySound(p_sound_file):
   #print ('in lglgg ')
   #printbool(C_SOUNDS_ON)
   if C_SOUNDS_ON:
      if os.path.isfile(p_sound_file):
        #pygame.mixer.stop() 
       
        #while L_SOUND_OBJECT_PLAY.get_busy():
        #       pygame.time.delay(3)
        try:
           sound_object=pygame.mixer.Sound(p_sound_file)
           #L_SOUND_OBJECT=pygame.mixer.Sound(p_sound_file)
           L_SOUND_OBJECT_PLAY=sound_object.play()
           #while L_SOUND_OBJECT_PLAY.get_busy():
           #    pygame.time.delay(3)
        except:
           print('error playing sound'+p_sound_file)   
      else:
         print('cant find file '+p_sound_file)



def printifdiff(p_dic1,p_dic2):
  if p_dic1!=p_dic2:
     #unmatched_item = set(sorted(p_dic1.items())) ^ set(sorted(p_dic2.items()))
     #unmatched_item = set((p_dic1.items())) ^ set((p_dic2.items()))
     unmatched_item = set((p_dic1.items())) - set((p_dic2.items()))
     #for x in unmatched_item:
     #   print (x) 
     for i in unmatched_item:
        print(i) 
     #print (p_dic2)

    

def printr (p_object_array,p_object_type):
   for l_object in p_object_array:
      if l_object['type'] == p_object_type:
         print(l_object)  

def get_jack_dict(p_object_array):
  l_dict={}
  for l_dict in p_object_array:
     if l_dict['type'] == C_JACK:
        break

  return l_dict

def GetSoundFileForObjType(p_type):
   l_s=''
   if p_type==C_WATER:
      l_s=C_SPLASH_SOUND_FILE
   elif p_type==C_ENEMY:
      l_s=C_ENEMY_DEAD_SOUND_FILE
   elif p_type==C_JACK:
      l_s=C_JACK_DEAD_SOUND_FILE
   elif p_type==C_LEDGE:
      l_s=C_PLATFORM_TOUCH_SOUND_FILE
   return l_s     


def remove_object_of_type_from_array(p_object_array,p_type):
   l_cnt=0
   #l_copy[:]=p_object_array
   for l in p_object_array[:]: #[:] is to take a copy of the array so not removing from the one looping on
      if l['type']==p_type:
         #print ('type = '+l['type'])
         if l['type'] != C_LEDGE:
            PlaySound(GetSoundFileForObjType(l['type']))
         p_object_array.remove(l)
         l_cnt+=1
   return l_cnt        


def get_type_count(p_type,p_object_array):
  l_cnt=0
  for l_dict in p_object_array:
     if l_dict['type'] == p_type:
        l_cnt+=1
  return l_cnt

def get_jack_count(p_object_array):
  return get_type_count(C_JACK,p_object_array)

def get_enemy_count(p_object_array):
  return get_type_count(C_ENEMY,p_object_array)

def object_type_can_be_moved(p_type):
   return p_type==C_BRICK

def remove_ledges_from_array(p_object_array,p_level_config_dict,p_game_attributes):
    if (remove_object_of_type_from_array(p_object_array,C_LEDGE)>0):
      adjustbricks(p_object_array,p_level_config_dict,p_game_attributes) 



   
def f_get_object_below_me(p_object,p_object_array):
   for l_object in p_object_array:
      if p_object['y'] + C_BLOCK_SIZE_HEIGHT == l_object['y'] and p_object['x'] == l_object['x']:
          return l_object
   l_object={}
   return l_object

def f_get_object_type_below_me(p_object,p_object_array):
   l_object=f_get_object_below_me(p_object,p_object_array)
   if l_object:
      return l_object['type']
   return C_NOTHING

def p_remove_what_is_below_me(p_object,p_object_array):
   l_object = f_get_object_below_me(p_object,p_object_array)
   if l_object and l_object['type'] != C_LEDGE:
      PlaySound(GetSoundFileForObjType(l_object['type']))
     
      p_object_array.remove(l_object)

def f_something_below_me(p_object,p_object_array):
   l_type=f_get_object_type_below_me(p_object,p_object_array)
   if (l_type==C_NOTHING):
      return False 
   return True

def f_get_object_above_me(p_object,p_object_array,p_how_much_above=1):
   for l_object in p_object_array:
      if p_object['y'] - (C_BLOCK_SIZE_HEIGHT*p_how_much_above) == l_object['y'] and p_object['x'] == l_object['x']:
          return l_object
   l_object=[]
   return l_object

def f_get_object_type_above_me(p_object,p_object_array,p_how_much_above=1):
   l_object=f_get_object_above_me(p_object,p_object_array,p_how_much_above)
   if l_object:
      return l_object['type']
   return C_NOTHING

def f_something_above_me(p_object,p_object_array,p_how_much_above=1):
   l_type=f_get_object_type_above_me(p_object,p_object_array,p_how_much_above)
   if (l_type==C_NOTHING):
      return False 
   return True

def printbool (p_bool):
   if (p_bool):
      print ('True')
   print ('False')




# draws objects that arent living, jack and alien handled in display living things
def drawobjects(p_object_array,p_level_config_dict,p_game_attributes,p_clear_code):#,p_ledge_mult):

   l_time_now=time.time()
   l_total_brick_refresh=0.0 
   l_total_text_refresh=0.0
   
   l_idx=1
   ClearScreen(p_clear_code)

  
   for l_object in p_object_array:
      
      
      

      if l_object['type'] == C_BRICK:
         #if l_object['y'] + C_BLOCK_SIZE_HEIGHT = 
          l_time_b1=time.time()
          if (l_object['y']==C_FRAME_DISPLAY_HEIGHT-C_BLOCK_SIZE_HEIGHT): # if brick on ground level only display half of it
             l_mult=.5
          else:
             l_mult=1
          pygame.draw.rect(gameDisplay,l_object['border_color'],[l_object['x'],l_object['y'],C_BLOCK_SIZE_WIDTH,C_BLOCK_SIZE_HEIGHT*l_mult])
    
          if (l_mult==1):
             pygame.draw.rect(gameDisplay,l_object['fill_color'],[l_object['x']+C_BRICK_BORDER,l_object['y']+C_BRICK_BORDER,C_BLOCK_SIZE_WIDTH-(C_BRICK_BORDER*2),C_BLOCK_SIZE_HEIGHT-(C_BRICK_BORDER*2)   ])
          else:
             pygame.draw.rect(gameDisplay,l_object['fill_color'],[l_object['x']+C_BRICK_BORDER,l_object['y']+C_BRICK_BORDER,C_BLOCK_SIZE_WIDTH-(C_BRICK_BORDER*2),C_BLOCK_SIZE_HEIGHT*l_mult-C_BRICK_BORDER   ])
            
          #do the blood splatter for some fun

         #if l_object['num_times_killed_on_left']>0 or l_object['num_times_killed_on_right']>0:
            #pygame.draw.rect(gameDisplay,config.C_COLOR_ENEMY_BLOOD,[l_object['x'],l_object['y'],C_BRICK_BORDER,C_BLOCK_SIZE_HEIGHT])
          #print('44')  
          if (C_DISPLAY_BLOOD_SPLATTER):

            l_j=1
            while (l_j<=4):
              #print(l_j)
              l_rect_multiplier=-1
              if l_j==1 and l_object['num_times_killed_on_left']>0:
                 l_rect_multiplier=l_object['num_times_killed_on_left']
              elif l_j==2 and l_object['num_times_killed_on_right']>0:     
                 l_rect_multiplier=l_object['num_times_killed_on_right']
              elif l_j==3 and l_object['num_times_killed_on_top']>0:     
                 l_rect_multiplier=l_object['num_times_killed_on_top']
              elif l_j==4 and l_object['num_times_killed_on_bottom']>0:     
                 l_rect_multiplier=l_object['num_times_killed_on_bottom']      
              
              if l_rect_multiplier != -1:
                if l_j<=2:
                   l_rect_product=C_BRICK_BORDER*l_rect_multiplier*C_BLOCK_SIZE_HEIGHT
                else:
                   l_rect_product=C_BRICK_BORDER*l_rect_multiplier*C_BLOCK_SIZE_WIDTH
                   
                
                l_blood_splatter_aggression=1
                l_idx=1
                l_x_pixel_prev=0
                l_y_pixel_prev=0
                while (l_idx<=l_rect_product):
                      
                    if (l_j<=2):
                         l_x_pixel=int(l_idx/C_BLOCK_SIZE_HEIGHT)
                         l_y_pixel=l_idx-(l_x_pixel*C_BLOCK_SIZE_HEIGHT)
                    else:
                         l_y_pixel=int(l_idx/C_BLOCK_SIZE_WIDTH)
                         l_x_pixel=l_idx-(l_y_pixel*C_BLOCK_SIZE_WIDTH)  
                    if (l_idx%l_blood_splatter_aggression==0):
                      #if (l_object['tag']=='84'):
                      #   print('doing blood on '+str(l_idx)+'blood splatter = '+str(l_blood_splatter_aggression))
                      if l_object['num_times_killed_on_left']>0 and l_j==1 and l_y_pixel<=C_BLOCK_SIZE_HEIGHT*l_mult:
                         pygame.draw.rect(gameDisplay,config.C_COLOR_ENEMY_BLOOD,[l_object['x']+l_x_pixel,l_object['y']+l_y_pixel,2,2])
                      elif l_object['num_times_killed_on_right']>0 and l_j==2 and l_y_pixel<=C_BLOCK_SIZE_HEIGHT*l_mult:
                         pygame.draw.rect(gameDisplay,config.C_COLOR_ENEMY_BLOOD,[l_object['x']+C_BLOCK_SIZE_WIDTH-l_x_pixel,l_object['y']+l_y_pixel,2,2])
                      elif l_object['num_times_killed_on_top']>0 and l_j==3:
                         pygame.draw.rect(gameDisplay,config.C_COLOR_ENEMY_BLOOD,[l_object['x']+l_x_pixel,l_object['y']+l_y_pixel,2,2])
                      elif l_object['num_times_killed_on_bottom']>0 and l_j==4 and l_mult==1: # only display if l_mult=1 otherwise brick is off screen on bottom
                         pygame.draw.rect(gameDisplay,config.C_COLOR_ENEMY_BLOOD,[l_object['x']+l_x_pixel,l_object['y']+C_BLOCK_SIZE_HEIGHT-l_y_pixel,2,2])
                    
                    #if (l_object['tag']=='84'):
                    #   print(str(l_x_pixel)+','+str(l_rect_multiplier*5)+','+str(l_x_pixel_prev)+'='+printbool(l_x_pixel-(l_rect_multiplier*5)>l_x_pixel_prev))
             

                    if l_j<=2 and l_x_pixel-(l_rect_multiplier)>l_x_pixel_prev:
                      l_blood_splatter_aggression+=1     
                      l_x_pixel_prev=l_x_pixel
                    elif l_j >=3 and l_y_pixel-l_rect_multiplier>l_y_pixel_prev:
                      l_blood_splatter_aggression+=1     
                      l_y_pixel_prev=l_y_pixel
                    l_idx+=1
              #end while   
              l_j+=1
            #End while
          #end if display blood splatter           

          if C_DISPLAY_BRICK_NUMBERS:
               gameDisplay.blit(C_FONT.render(str(l_object['tag']), True, l_object['border_color']), (l_object['x']+C_BLOCK_SIZE_WIDTH/2, l_object['y']+C_BLOCK_SIZE_HEIGHT/2))
          l_total_brick_refresh=l_total_brick_refresh+(time.time()-l_time_b1)
         #
      elif l_object['type'] == C_LEDGE:
         #l_rect_height=C_BLOCK_SIZE_HEIGHT*max(p_ledge_mult/10,0) 
            #print(p_level_config_dict)
            x=int(p_level_config_dict['ledge_mult'])
            
            l_rect_height=C_BLOCK_SIZE_HEIGHT*max(x/10,0) 
            if (l_object['has_been_touched']):
               if have_all_ledges_been_touched(p_object_array):
                  pygame.draw.rect(gameDisplay,l_object['touched_all_color'],[l_object['x'],l_object['y'],C_BLOCK_SIZE_WIDTH,l_rect_height])
               else:
                  pygame.draw.rect(gameDisplay,l_object['touched_color'],[l_object['x'],l_object['y'],C_BLOCK_SIZE_WIDTH,l_rect_height])   
            else:
               pygame.draw.rect(gameDisplay,l_object['fill_color'],[l_object['x'],l_object['y'],C_BLOCK_SIZE_WIDTH,l_rect_height])
               
      
      elif l_object['type'] == C_GROUND:
         #l_rect_height=C_BLOCK_SIZE_HEIGHT#*max(p_ledge_mult/10,0)
         l_width_as_perc=.03
         l_height_as_perc = l_width_as_perc * C_BLOCK_SIZE_WIDTH / C_BLOCK_SIZE_HEIGHT # need to apply ration between width and height
         
         pygame.draw.rect(gameDisplay,l_object['fill_color'],[l_object['x'],l_object['y'],C_BLOCK_SIZE_WIDTH,C_BLOCK_SIZE_HEIGHT*.5])
         
         l_x_pos=.25 -l_height_as_perc
         while(l_x_pos<=1):
         #just once through the middle only horizon
            #horizontal lines
            if (l_x_pos<=.5):
               pygame.draw.rect(gameDisplay,l_object['border_color'],[l_object['x'],l_object['y'] + (C_BLOCK_SIZE_HEIGHT* (l_x_pos-l_height_as_perc)  )  ,C_BLOCK_SIZE_WIDTH,C_BLOCK_SIZE_HEIGHT*(l_height_as_perc)])
            #vertical lines
            pygame.draw.rect(gameDisplay,l_object['border_color'],[l_object['x'] + (C_BLOCK_SIZE_WIDTH*l_x_pos),l_object['y'] ,C_BLOCK_SIZE_WIDTH*l_width_as_perc,C_BLOCK_SIZE_HEIGHT*.5])
            l_x_pos+=.25

      elif l_object['type'] == C_WATER or l_object['type'] == C_ENEMY or l_object['type'] == C_JACK: # 

      #if l_dude['type'] == C_ENEMY or l_dude['type'] == C_JACK: 
        #l_dict=p_living_array[l_idx]

        #l_img=l_dude['image']
        #l_y=l_dude['y']
        #l_x=l_dude['x']
        
        #gameDisplay.blit(l_img,(l_x,l_y))
  
         gameDisplay.blit(l_object['image'],(l_object['x'],l_object['y']))
      #   pygame.draw.rect(gameDisplay,l_object['fill_color'],[l_object['x'],l_object['y'],C_BLOCK_SIZE_WIDTH,C_BLOCK_SIZE_HEIGHT])
      l_idx+=1
      #pygame.display.update()

      l_time_c1=time.time()
      if (p_clear_code != -1 and C_BLIT_TEXT):
        
          
        if (p_clear_code==0): #if we cleared all lets rebuild the bottom bar
          pygame.draw.rect(gameDisplay,C_COLOR_BLACK,[0 ,C_FRAME_DISPLAY_HEIGHT-(C_BLOCK_SIZE_HEIGHT*.5),C_FRAME_DISPLAY_WIDTH,C_BLOCK_SIZE_HEIGHT])
          
          # Display some text
          #text = font.render('LEVEL ' + str(p_level_config_dict['level']) + ', ' + str(p_level_config_dict['level_name'])+ ', ' + str(p_level_config_dict['speed']), True, C_COLOR_WHITE , (10,C_FRAME_DISPLAY_HEIGHT-(C_BLOCK_SIZE_HEIGHT*.5)))
          l_platform_bonus_str=''
          if (p_level_config_dict['has_ledges']):
             l_platform_bonus_str = ' (' + str(p_level_config_dict['ledge_platform_bonus']) + ')'


          text = C_FONT.render('LEVEL ' + str(p_level_config_dict['level']) + ', ' + str(p_level_config_dict['level_name'] + l_platform_bonus_str), True, C_COLOR_WHITE , (10,C_FRAME_DISPLAY_HEIGHT-(C_BLOCK_SIZE_HEIGHT*.5)))
          gameDisplay.blit(text, (10,C_FRAME_DISPLAY_HEIGHT-(C_BLOCK_SIZE_HEIGHT*.5)))

          l_tuple=(C_FRAME_DISPLAY_WIDTH-400,C_FRAME_DISPLAY_HEIGHT-(C_BLOCK_SIZE_HEIGHT*.5))
          text = C_FONT.render('LIVES ' + str(p_game_attributes['num_lives']), True, C_COLOR_WHITE , l_tuple)
          gameDisplay.blit(text,l_tuple)

          l_img_mult=.3

          if (C_SOUNDS_ON):
             l_img=pygame.image.load(C_SOUNDSON_IMAGE)
          else:
             l_img=pygame.image.load(C_SOUNDSOFF_IMAGE)
            
          l_img=pygame.transform.scale(l_img,(int(C_BLOCK_SIZE_HEIGHT*l_img_mult),int(C_BLOCK_SIZE_HEIGHT*l_img_mult)))
          gameDisplay.blit(l_img,(C_FRAME_DISPLAY_WIDTH-700,C_FRAME_DISPLAY_HEIGHT-(C_BLOCK_SIZE_HEIGHT*.5)))
          if (C_GAME_PAUSED):
             #l_img=get_jack_dict(l_object_array)['image']
             l_img=pygame.image.load(C_PAUSED_IMAGE)
             l_img=pygame.transform.scale(l_img,(int(C_BLOCK_SIZE_HEIGHT*l_img_mult),int(C_BLOCK_SIZE_HEIGHT*l_img_mult)))
             gameDisplay.blit(l_img,(C_FRAME_DISPLAY_WIDTH-650,C_FRAME_DISPLAY_HEIGHT-(C_BLOCK_SIZE_HEIGHT*.5)))

          if C_JACK_HAS_UNLIMITED_LIVES:
             l_img=pygame.image.load(C_JACK_IMAGE)
             l_img=pygame.transform.scale(l_img,(int(C_BLOCK_SIZE_HEIGHT*l_img_mult),int(C_BLOCK_SIZE_HEIGHT*l_img_mult)))
             gameDisplay.blit(l_img,(C_FRAME_DISPLAY_WIDTH-500,C_FRAME_DISPLAY_HEIGHT-(C_BLOCK_SIZE_HEIGHT*.5))) 

          if (not C_CAN_JACK_BE_KILLED):
             #l_img=get_jack_dict(l_object_array)['image']
             l_img=pygame.image.load(C_GODMODE_IMAGE)
             l_img=pygame.transform.scale(l_img,(int(C_BLOCK_SIZE_HEIGHT*l_img_mult),int(C_BLOCK_SIZE_HEIGHT*l_img_mult)))
             gameDisplay.blit(l_img,(C_FRAME_DISPLAY_WIDTH-550,C_FRAME_DISPLAY_HEIGHT-(C_BLOCK_SIZE_HEIGHT*.5)))

          if (C_ENEMIES_FROM_HELL):
             #l_img=get_jack_dict(l_object_array)['image']
             l_img=pygame.image.load(C_HELLMODE_IMAGE)
             l_img=pygame.transform.scale(l_img,(int(C_BLOCK_SIZE_HEIGHT*l_img_mult),int(C_BLOCK_SIZE_HEIGHT*l_img_mult)))
             gameDisplay.blit(l_img,(C_FRAME_DISPLAY_WIDTH-500+(C_BLOCK_SIZE_HEIGHT*l_img_mult*2),C_FRAME_DISPLAY_HEIGHT-(C_BLOCK_SIZE_HEIGHT*.5)))
             



          l_lives=1
          l_img=pygame.image.load(C_JACK_IMAGE)
          #print('hongkongfuey'+str(p_game_attributes['num_lives']))
          l_img=pygame.transform.scale(l_img,(int(C_BLOCK_SIZE_HEIGHT*l_img_mult),int(C_BLOCK_SIZE_HEIGHT*l_img_mult)))
          while (l_lives<=p_game_attributes['num_lives']):
             gameDisplay.blit(l_img,(C_FRAME_DISPLAY_WIDTH-300+(l_lives*30),C_FRAME_DISPLAY_HEIGHT-(C_BLOCK_SIZE_HEIGHT*.5)))
             #time.sleep(3)
             l_lives+=1 

        #if p_clear_code==0: or p_clear_code==1 or p_clear_code==2 or p_clear_code==4: 

        l_tuple=(10,10)
        l_score=p_game_attributes['score']+p_level_config_dict['level_score']
        text = C_FONT.render('SCORE ' + str(l_score), True, C_COLOR_WHITE , l_tuple)
        gameDisplay.blit(text,l_tuple)

        #if p_clear_code==0 or p_clear_code==1: 
  
        l_tuple=(C_HIGHSCORE_DISPLAY_X_START,10)
        l_hscore=p_game_attributes['high_score']#+p_level_config_dict['level_score']
        text = C_FONT.render('HIGH SCORE ' + str(l_hscore), True, C_COLOR_WHITE , l_tuple)
        gameDisplay.blit(text,l_tuple)
       
        #if p_clear_code==0 or p_clear_code==1 or p_clear_code==3 or p_clear_code==4: 

        if (p_level_config_dict['time_left']>0):
            l_tuple=(C_TIMER_DISPLAY_X_START,10)
            text = C_FONT.render('TIME ' + str(p_level_config_dict['time_left']), True, C_COLOR_WHITE , l_tuple)
            gameDisplay.blit(text, l_tuple)
       
        l_total_text_refresh=l_total_text_refresh+(time.time()-l_time_c1)
        #print('called drawobjects'+str((time.time()-l_time_now)*1000)+' '+str(l_total_brick_refresh*1000)+' '+str(l_total_text_refresh*1000)) 
        #L_TOTAL_SECS+=l_total_text_refresh*1000
        #L_TOTAL_CALLS+=1
        #print('a2vg = '+str(L_TOTAL_SECS/L_TOTAL_CALLS))
      #displayLivingThings(p_object_array)

      
         
     
      

            
      #font = pygame.font.SysFont(None, 36)
      #text = font.render("LEVEL " + str(p_level_config_dict['level']), 1, C_COLOR_WHITE)
      #gameDisplay.blit(text, (10,C_FRAME_DISPLAY_HEIGHT-(C_BLOCK_SIZE_HEIGHT*.5)))
         
   
#def drawbrick(p_x,p_y,p_border_color,p_fill_color):
def adjustbricks(p_object_array,p_level_config_dict,p_game_attributes): # these method handles killing of enemies from top down, sideways crushing is handled in is_gap
   l_time_now=time.time()
   l_bricks_adjusted=False
   l_death_occurred=False
   for l_object in p_object_array:
      l_type_below_me = f_get_object_type_below_me(l_object,p_object_array)
      l_object_below_me = f_get_object_below_me(l_object,p_object_array)

      if l_object['type'] == C_BRICK and (l_type_below_me==C_WATER or l_type_below_me==C_NOTHING or l_type_below_me == C_JACK or l_type_below_me==C_ENEMY) and l_object['y']+C_BLOCK_SIZE_HEIGHT < C_FRAME_DISPLAY_HEIGHT:
         l_remove_object=False
         
         if l_type_below_me==C_WATER or l_type_below_me==C_ENEMY or (l_type_below_me==C_JACK and C_CAN_JACK_BE_KILLED):
            p_remove_what_is_below_me(l_object,p_object_array)
            if l_type_below_me==C_JACK or l_type_below_me==C_ENEMY:
               l_object['num_times_killed_on_bottom']+=1
               l_death_occurred=True
               
         l_bricks_adjusted=True
         l_object['y'] += C_BLOCK_SIZE_HEIGHT
         # now that they are removed see whats below the brick now, if another brick set its killed_on_top to true
         
         l_object_below_me = f_get_object_below_me(l_object,p_object_array)
         if  l_death_occurred and l_object_below_me and l_object_below_me['type'] == C_BRICK:
            l_object_below_me['num_times_killed_on_top']+=1   

   #print('called adjust bricks='+str((time.time()-l_time_now)*1000)) 
   #if l_bricks_adjusted==True:
   #    drawobjects(p_object_array,p_level_config_dict,p_game_attributes,-1)  # pass -1 to not bother adjusting the top and bottom bars slows down levels with lots of bricks
   #print('called adjust bricks2='+str((time.time()-l_time_now)*1000))

def f_get_object_at_x_and_y(p_x_pos,p_y_pos,p_object_array):
   for l_object in p_object_array:
      if l_object['y'] == p_y_pos and l_object['x'] == p_x_pos:
         return l_object
   #l_object['type']=C_NOTHING
   l_object=[]
   return l_object

def remove_object_at_x_and_y_pos (p_x_pos,p_y_pos,p_object_array,p_object_type):
   l_object=f_get_object_at_x_and_y(p_x_pos,p_y_pos,p_object_array)
   if l_object['type']==p_object_type:
      p_object_array.remove(l_object)
                  

def f_get_object_type_at_x_and_y(p_x_pos,p_y_pos,p_object_array):
   l_object =  f_get_object_at_x_and_y(p_x_pos,p_y_pos,p_object_array)
   if not l_object:
      return C_NOTHING
   return l_object['type']

def f_get_object_to_the_left(p_living_thing,p_object_array,p_offset=0): #p_offset 0 = direct to right, + equals to right and above, and - below
   #print('lets check brick array for something to right')
   for l_object in p_object_array:
      if p_living_thing['x'] - C_BLOCK_SIZE_WIDTH == l_object['x'] and p_living_thing['y']-(C_BLOCK_SIZE_HEIGHT*p_offset) == l_object['y']:
         return l_object
   l_object=[]
   return l_object                  

def f_get_object_type_to_the_left(p_living_thing,p_object_array,p_offset=0):
   l_object = f_get_object_to_the_left(p_living_thing,p_object_array,p_offset)
   if l_object:
      return l_object['type']
   return C_NOTHING 

def f_get_object_type_to_the_left_using_x_and_y(p_x_pos,p_y_pos,p_object_array):
   l_object = f_get_object_at_x_and_y(p_x_pos,p_y_pos,p_object_array)
   if l_object:
      return l_object['type']
   return C_NOTHING 

def f_something_to_left(p_living_thing,p_object_array,p_offset=0):
   return f_get_object_type_to_the_left(p_living_thing,p_object_array,p_offset)!=C_NOTHING

def f_something_to_left_using_x_and_y(p_x_pos,p_y_pos,p_object_array):
   for l_object in p_object_array:
      if l_object['x']==p_x_pos and l_object['y'] == p_y_pos:
         return f_something_to_left(l_object,p_object_array)
   return false       
   #return f_what_is_to_the_right(p_living_thing,p_object_array,p_offset)!=C_NOTHING

def f_pull_object(p_living_thing,p_brick_array,p_level_config_dict,p_game_attributes,p_direction):
   if (p_direction==C_RIGHT):
      l_mult=-1
   elif (p_direction==C_LEFT):
      l_mult=1
   else:
      return 
  
   #print('lets check brick array for something to left')
   PlaySound(C_BRICK_MOVE_SOUND_FILE)
   for l_brick in p_brick_array:
      if p_living_thing['x'] + (C_BLOCK_SIZE_WIDTH*l_mult) == l_brick['x'] and p_living_thing['y'] == l_brick['y']:
         l_brick['x']-=C_BLOCK_SIZE_WIDTH*l_mult
         p_level_config_dict['level_score']+=C_SCORE_BRICKMOVE
         break # only one brick can be in this position, if there is more than one there is a logic error with bricks
   # this call to adjustbricks has to be outside loop, otherwise a brick above the one being pulled will fall down, and also be pulled(however the break after 1 break solves this as well)
   adjustbricks(p_brick_array,p_level_config_dict,p_game_attributes)  

def f_get_object_to_the_right(p_living_thing,p_object_array,p_offset=0): #p_offset 0 = direct to right, + equals to right and above, and - below
   #print('lets check brick array for something to right')
   for l_object in p_object_array:
      if p_living_thing['x'] + C_BLOCK_SIZE_WIDTH == l_object['x'] and p_living_thing['y']-(C_BLOCK_SIZE_HEIGHT*p_offset) == l_object['y']:
         return l_object
   l_object=[]
   return l_object

def f_get_object_type_to_the_right(p_living_thing,p_object_array,p_offset=0):
   l_object = f_get_object_to_the_right(p_living_thing,p_object_array,p_offset)
   if l_object:
      return l_object['type']
   return C_NOTHING    

def f_something_to_right(p_living_thing,p_object_array,p_offset=0):
   return f_get_object_type_to_the_right(p_living_thing,p_object_array,p_offset)!=C_NOTHING

def f_something_to_right_using_x_and_y(p_x_pos,p_y_pos,p_object_array):
   for l_object in p_object_array:
      if l_object['x']==p_x_pos and l_object['y'] == p_y_pos:
         return f_something_to_right(l_object,p_object_array)
   return false       
   #return f_what_is_to_the_right(p_living_thing,p_object_array,p_offset)!=C_NOTHING

def is_gap(p_x_pos,p_y_pos,p_object_array,p_direction): #these method handles killing of enemies from sideways movemonent, top down is  handled in adjust_bricks
   
   #print(str(p_x_pos)+','+str(p_y_pos))

   #l_object_prior_to_gap=f_get_object_at_x_and_y(p_x_pos,p_y_pos,p_object_array)

   #print (l_object_prior_to_gap)

   l_gap_found=False
   l_kill_array=[]
   l_object_adj_prev=[]

   l_x_mult=0
   l_y_mult=0

   if (p_direction==C_LEFT):
      l_x_mult=-1
   elif (p_direction==C_RIGHT):
      l_x_mult=1
   elif (p_direction==C_UP):
      l_y_mult=-1
   elif (p_direction==C_DOWN):
      l_y_mult=1
   
   p_x_pos+=(C_BLOCK_SIZE_WIDTH * l_x_mult)
   p_y_pos+=(C_BLOCK_SIZE_HEIGHT * l_y_mult)
      #l_orig_x_pos=p_living_thing['x']

   #l_x_pos=p_living_thing['x']-C_BLOCK_SIZE_WIDTH
   while (p_x_pos>=0 and 
          p_x_pos<C_FRAME_DISPLAY_WIDTH and 
          p_y_pos>=0 and 
          p_y_pos<C_FRAME_DISPLAY_HEIGHT and 
          not l_gap_found):
      
      ##if not f_something_to_left(p_living_thing,p_object_array):
      ##l_object_type_adj=f_get_object_type_at_x_and_y(p_x_pos,p_y_pos,p_object_array)
      
      l_object_adj=f_get_object_at_x_and_y(p_x_pos,p_y_pos,p_object_array)
      
      #print('first object adj =')
      #print (l_object_adj)
      l_object_adj2=[]
      
      ##l_object_type_adj=l_object_adj['type']
      ##print('adjacent object type = '+l_object_type_adj)
      
      #if l_object_adj and (l_object_adj['type'] == C_NOTHING or l_object_adj['type']==C_ENEMY):
      
      #while (l_x_pos_next_adj>=0 and l_x_pos_next_adj<C_FRAME_DISPLAY_WIDTH and l_y_pos_next_adj>=0 and l_y_pos_next_adj<C_FRAME_DISPLAY_HEIGHT and 
      #      (l_object_adj and (l_object_adj['type'] == C_ENEMY or l_object_adj['type'] == C_NOTHING):
                  #   l_x_pos_next_adj+=(C_BLOCK_SIZE_WIDTH*l_x_mult)
                  #   l_y_pos_next_adj+=(C_BLOCK_SIZE_HEIGHT*l_y_mult)
                  #   l_object_adj2=f_get_object_at_x_and_y(l_x_pos_next_adj,l_y_pos_next_adj,p_object_array)

      if not l_object_adj or l_object_adj['type']==C_ENEMY:
         if l_object_adj and l_object_adj['type']==C_ENEMY:
            #print('enemy stunned '+str(l_object_adj['image_name']))
            l_object_adj['speed']=C_ENEMY_STUNNED_SPEED # stun it by slowing it down
            l_ok_to_kill_enemy=False
            # we need to get the susbequent adjacent object
            l_x_pos_next_adj=p_x_pos+(C_BLOCK_SIZE_WIDTH*l_x_mult)
            l_y_pos_next_adj=p_y_pos+(C_BLOCK_SIZE_HEIGHT*l_y_mult)
            if l_x_pos_next_adj>=0 and l_x_pos_next_adj<C_FRAME_DISPLAY_WIDTH and l_y_pos_next_adj>=0 and l_y_pos_next_adj<C_FRAME_DISPLAY_HEIGHT: # then within screen bounds 
               #l_object_type_adj2=f_get_object_type_at_x_and_y(l_x_pos_next_adj,l_y_pos_next_adj,p_object_array)
               l_object_adj2=f_get_object_at_x_and_y(l_x_pos_next_adj,l_y_pos_next_adj,p_object_array)
               #print('object type adjacent to enemy = '+l_object_type_adj)
               #if l_object_type_adj2 == C_BRICK or l_object_type_adj2 == C_LEDGE: # can crush enemeny against a brick or a ledge
               if l_object_adj2 and (l_object_adj2['type'] == C_BRICK or l_object_adj2['type'] == C_LEDGE): # can crush enemeny against a brick or a ledge
                  l_ok_to_kill_enemy=True
                  
                      


               
               elif l_object_adj2 and l_object_adj2['type'] == C_ENEMY: # if adjecent object is an emeny we need to move ahead, ie BeeB push right will crush the 2nd e, 1st e just moves to its spot, but it gets stunned thus we set its speed slower
                  #l_object_prior_to_gap=f_get_object_at_x_and_y(p_x_pos,p_y_pos,p_object_array) 
                  p_x_pos+=C_BLOCK_SIZE_WIDTH*l_x_mult
                  p_y_pos+=C_BLOCK_SIZE_HEIGHT*l_y_mult
                  #print('stunning the object')
                  #l_stun_enemy=True
               #elif not l_object_adj2 or l_object_adj2['type']==C_NOTHING:
                  #l_stun_enemy=True

            
            else: # adjecent block is off screen hence we are on the edge
               l_ok_to_kill_enemy=True   
            
            if l_ok_to_kill_enemy:
               #remove_object_at_x_and_y_pos(p_x_pos,p_y_pos,p_object_array,l_object_adj['type'])
               # set these values, they are used to display some disgusting blood splatter
               if p_direction==C_RIGHT:
                  if 'num_times_killed_on_left' in l_object_adj2:
                     l_object_adj2['num_times_killed_on_left']+=1
                  if l_object_adj_prev and l_object_adj_prev['type'] == C_BRICK:
                     l_object_adj_prev['num_times_killed_on_right']+=1  
               elif p_direction==C_LEFT:
                  if 'num_times_killed_on_right' in l_object_adj2:
                     l_object_adj2['num_times_killed_on_right']+=1
                  if l_object_adj_prev and l_object_adj_prev['type'] == C_BRICK:
                     l_object_adj_prev['num_times_killed_on_left']+=1   
              
               l_kill_array.append(l_object_adj)
               #l_gap_found=True
         
         if not l_object_adj2 or l_object_adj2['type'] != C_ENEMY:
            l_gap_found=True
            #if l_object_adj:
            #   print('enemy stunned '+str(l_object_adj['image_name']))
            #   l_object_adj['speed']=C_ENEMY_STUNNED_SPEED # stun it by slowing it down
              
      
      elif l_object_adj and not l_object_adj['can_be_moved']:
         #return false
         break   
      else:
         p_x_pos+=C_BLOCK_SIZE_WIDTH*l_x_mult
         p_y_pos+=C_BLOCK_SIZE_HEIGHT*l_y_mult
         l_object_adj_prev=l_object_adj
         #p_living_thing['x']-=C_BLOCK_SIZE_WIDTH
      #print(str(p_x_pos)+','+str(p_y_pos))  

   for l_enemy in l_kill_array:
      #put the whole killing logic in one proc later
      PlaySound(C_ENEMY_DEAD_SOUND_FILE)
      p_object_array.remove(l_enemy)       

   #p_living_thing['x']=l_orig_x_pos
   #print('gap found=')
   #print (l_gap_found ) 
   return l_gap_found

def is_gap_to_left(p_x_pos,p_y_pos,p_object_array):
   return is_gap(p_x_pos,p_y_pos,p_object_array,C_LEFT)
   
def is_gap_to_right(p_x_pos,p_y_pos,p_object_array):
   return is_gap(p_x_pos,p_y_pos,p_object_array,C_RIGHT)   


def push_object(p_x_pos,p_y_pos,p_object_array,p_direction):
     l_object = f_get_object_at_x_and_y(p_x_pos,p_y_pos,p_object_array)
     if p_direction==C_LEFT:
        l_object['x']-=C_BLOCK_SIZE_WIDTH
     elif p_direction==C_RIGHT:
        l_object['x']+=C_BLOCK_SIZE_WIDTH
     elif p_direction==C_UP:
        l_object['y']-=C_BLOCK_SIZE_HEIGHT
     elif p_direction==C_DOWN:
        l_object['y']+=C_BLOCK_SIZE_HEIGHT

def push_object_left(p_x_pos,p_y_pos,p_object_array):
   push_object(p_x_pos,p_y_pos,p_object_array,C_LEFT)
  
def push_objects_left(p_living_thing,p_object_array,p_level_config_dict):
  if (is_gap_to_left(p_living_thing['x'],p_living_thing['y'],p_object_array)):
     PlaySound(C_BRICK_MOVE_SOUND_FILE)
     p_level_config_dict['level_score']+=C_SCORE_BRICKMOVE
     l_orig_x_pos=p_living_thing['x']
     l_x_pos=p_living_thing['x']
     l_y_pos=p_living_thing['y']

     #while f_something_to_left(p_living_thing,p_brick_array):
     while f_something_to_left_using_x_and_y(l_x_pos,l_y_pos,p_object_array):# and f_get_object_type_to_the_left_using_x_and_y(l_x_pos,l_y_pos,p_object_array) != C_LEDGE:
        #p_living_thing['x']-=C_BLOCK_SIZE_WIDTH
        l_x_pos-=C_BLOCK_SIZE_WIDTH
        #print('found a brick to the left')
   
     #so here he have found the far left brick to move
     #while (p_living_thing['x']<=l_orig_x_pos):
     while (l_x_pos<l_orig_x_pos):
        push_object_left(l_x_pos,l_y_pos,p_object_array)
        #p_living_thing['x']+=C_BLOCK_SIZE_WIDTH
        l_x_pos+=C_BLOCK_SIZE_WIDTH       
      
     p_living_thing['x']=l_orig_x_pos-C_BLOCK_SIZE_WIDTH  

def push_object_right(p_x_pos,p_y_pos,p_object_array):
   push_object(p_x_pos,p_y_pos,p_object_array,C_RIGHT)

def push_objects_right(p_living_thing,p_object_array,p_level_config_dict):
  if (is_gap_to_right(p_living_thing['x'],p_living_thing['y'],p_object_array)):
     PlaySound(C_BRICK_MOVE_SOUND_FILE)
     p_level_config_dict['level_score']+=C_SCORE_BRICKMOVE
     l_orig_x_pos=p_living_thing['x']
     l_x_pos=p_living_thing['x']
     l_y_pos=p_living_thing['y']

     while f_something_to_right_using_x_and_y(l_x_pos,l_y_pos,p_object_array):
        l_x_pos+=C_BLOCK_SIZE_WIDTH

     while (l_x_pos>l_orig_x_pos):
        push_object_right(l_x_pos,l_y_pos,p_object_array)
        l_x_pos-=C_BLOCK_SIZE_WIDTH     
      
     p_living_thing['x']=l_orig_x_pos+C_BLOCK_SIZE_WIDTH  



def move_baddies(p_object_array,p_level_config_dict,p_game_attributes,p_speed_attribute):
    
    for l_dict in p_object_array:
      
      if l_dict['type'] == C_ENEMY:
        #print(l_dict)
        if p_speed_attribute%l_dict['speed']==0:
          #l_killed=False
          l_img=l_dict['image']
          l_y=l_dict['y']
          l_x=l_dict['x']
          #l_has_moved=l_dict['has_moved']
          
          l_x_mult=0
          l_y_mult=0
          #l_did_uturn=False

          l_epoch_now=time.time()
          #if (l_epoch_now>C_EPOCH_START+(C_BADDIE_MOVE_DELAY_SECS*l_idx)):
          if (l_epoch_now>C_EPOCH_START+p_game_attributes['total_paused_seconds']+(C_BADDIE_MOVE_DELAY_SECS*  int(l_dict['dropdelay']) )):
              
              l_object_type_above_me = f_get_object_type_above_me(l_dict,p_object_array)
              l_object_below_me      = f_get_object_below_me(l_dict,p_object_array)
              l_object_type_below_me = f_get_object_type_below_me(l_dict,p_object_array)
              
              if (l_dict['updown']=='down'):

                 #l_obj_type_below=f_get_object_type_below_me(l_dict,p_object_array)
                 if (l_object_type_below_me==C_JACK) and C_CAN_JACK_BE_KILLED:
                    #if nothing below the jack move the jack down else it dies
                    l_object_type_below2=f_get_object_type_below_me(l_object_below_me,p_object_array)
                    if l_object_type_below2 !=C_NOTHING: #ie no gap, jack is crushed
                       p_remove_what_is_below_me(l_dict,p_object_array)
                    else:
                       #move the jack down one, this will simulate an enemy falling on a jack till it hits groud,ledge,or another enemy etc and get crushed, jack can move faster so can still get out if quick enuf
                       apply_gravity_jack(l_object_below_me,p_object_array,p_level_config_dict)    
                 elif (l_object_type_below_me!=C_NOTHING):
                    l_y_mult=0
                    l_dict['updown']='up'
                    l_dict['y_ground']=l_dict['y']
                    

                    l_found_appropriate_jump_hop_val=False
                    
                    l_hops_off_roof=(l_dict['y'] / C_BLOCK_SIZE_HEIGHT) - 1.5 # 1.5 is the half row of bullshit and then the drop zone
                    #print('hops off roof = '+str(l_hops_off_roof))

                    l_max_value=C_BADDIE_MAX_JUMP_BLOCKS
                   
                    while not l_found_appropriate_jump_hop_val and l_max_value>=C_BADDIE_MIN_JUMP_BLOCKS:
                    
                      l_hops_to_do=min(random.randint(C_BADDIE_MIN_JUMP_BLOCKS,l_max_value),l_hops_off_roof) # cap it at this value
                      #print('hops to do = '+str(l_hops_to_do))
                      # if something in the road at all above us prior to to this jump hop val, then lets retry and get a better value
                      

                      l_idx=1
                      l_something_in_the_way=False
                      while (l_idx<=l_hops_to_do and not l_something_in_the_way):
                         #print(f_get_object_type_above_me(l_dict,p_object_array,l_idx))
                         l_something_in_the_way=(f_get_object_type_above_me(l_dict,p_object_array,l_idx)==C_LEDGE) # if ledge directly above them ie got stuck then need to allow them to move sideways 
                         
                         ## this code here makes the enemies avoid falling bricks, could implement this for super hard level
                         if (C_ENEMIES_FROM_HELL):
                            l_something_in_the_way=f_something_above_me(l_dict,p_object_array,l_idx)
                         l_idx+=1

                      if not l_something_in_the_way:
                         l_found_appropriate_jump_hop_val=True
                      else:
                         #print('something in the way so retrying') 
                         l_max_value-=1       

                      
                    l_dict['last_jump_hop_height']=min(l_hops_to_do,l_hops_off_roof)
                    
                 else: 
                    l_y_mult=1
              else: ### going up
                 l_y_mult=-1
          
                 if l_object_type_above_me == C_BRICK or l_object_type_above_me == C_JACK or l_object_type_above_me == C_ENEMY or l_object_type_above_me == C_LEDGE:
                 
                    l_y_mult=0 
                    l_dict['updown']='down'

                    # the death of the enemy by jack or brick is handled in adjust bricks or apply_gravity_jack as these methods fire every iteration with this fires at most the same amount of time, but often less due to the 
                    # speed attribute of the level controlling the delay of this funciton call using mod function in refresh procedure
                 
                    #if l_type_below_me != C_NOTHING and l_type_above_me != C_ENEMY and l_type_above_me != C_LEDGE:
                    #   print('firing here')
                    #   #p_object_array.remove(l_dict)
          
              #if object at height enemey wants to hop then turn opp direction go back to ground and a new height should / will be chosen
              if l_dict['leftright']=='left' and f_something_to_left(l_dict,p_object_array,l_dict['last_jump_hop_height']):
                    l_x_mult=0
                    l_dict['leftright']='right'
                    #l_did_uturn=True
              elif l_dict['leftright']=='right' and f_something_to_right(l_dict,p_object_array,l_dict['last_jump_hop_height']):
                    l_x_mult=0
                    l_dict['leftright']='left'
                      
              #print(l_y_mult)
                 
              l_dict['y']+=(C_BLOCK_SIZE_HEIGHT*l_y_mult)
              #if (l_dict['last_jump_hop_height'] != 0 and l_dict['y'] <= l_dict['y_ground'] - (l_dict['last_jump_hop_height']*C_BLOCK_SIZE_HEIGHT)): # hit apex of jump
              if (l_dict['y'] <= l_dict['y_ground'] - (l_dict['last_jump_hop_height']*C_BLOCK_SIZE_HEIGHT)): # hit apex of jump
                  l_dict['updown']='down'

                  #l_random=random.randint(0,4)
                  #if (l_random==0) and not l_did_uturn:
                  #   if l_dict['leftright'] == 'left':
                  #      l_dict['leftright'] == 'right'
                  #   else:
                  #      l_dict['leftright'] == 'left'
                     
                  if l_dict['leftright'] == 'left':
                     l_x_mult=-1
                  else:
                     l_x_mult=1
                          
              elif (l_dict['y'] == C_FRAME_DISPLAY_HEIGHT-C_BLOCK_SIZE_HEIGHT): # hit bottom of the screen
                  l_dict['updown']='up'
              

              # final check that object we are going sideways to isnt impeding us, dont know how it has been happening but enemies going through bricks
              if (l_x_mult < -1 or l_x_mult > 1):
                   sys.exit # trap this error
              
              if ( (l_x_mult==-1 and f_something_to_left(l_dict,p_object_array,l_dict['last_jump_hop_height'])) or
                   (l_x_mult==1 and f_something_to_right(l_dict,p_object_array,l_dict['last_jump_hop_height'])) ):
                 l_x_mult=0

              if l_x_mult!=0:
                l_dict['x']+=(C_BLOCK_SIZE_WIDTH*l_x_mult)
                l_dict['x']=min(max(l_dict['x'],0),C_FRAME_DISPLAY_WIDTH-C_BLOCK_SIZE_WIDTH)

                if (l_dict['x']==0):
                   l_dict['leftright'] = 'right'
                elif (l_dict['x']==C_FRAME_DISPLAY_WIDTH-C_BLOCK_SIZE_WIDTH):
                   l_dict['leftright'] = 'left'
        else: #baddie couldnt move due to not being fast enoug
           l_dict['speed']-=1 # make it faster again, this is just simulate a stunned effect etc such as being hit by brick (only scenrio at this stage)
           l_dict['speed']=max(l_dict['speed'],p_level_config_dict['speed'])

def have_all_ledges_been_touched(p_object_array):
   l_bool=True # set to true initially and try and prove wrong
   for l_object in p_object_array:
      if l_object['type']==C_LEDGE and l_object['has_been_touched']==False:
         l_bool=False
         break
   return l_bool
                          

def apply_gravity_jack(p_object,p_object_array,p_level_config_dict):
     
         #print('inside apply_gravity_jack'+str(len(p_object_array)))
         l_whats_below_me = f_get_object_type_below_me(p_object,p_object_array)
         #print('below me is')
         #print(f_get_object_type_below_me(l_dict,l_object_array))
         if l_whats_below_me == C_NOTHING or l_whats_below_me == C_ENEMY:
            l_y_mult=1
            p_object['updown']='down'
            if l_whats_below_me == C_ENEMY: # lets kill him
               p_remove_what_is_below_me(p_object,p_object_array)
               p_level_config_dict['level_score']+=C_SCORE_KILL_ENEMY
         else:
            if l_whats_below_me == C_WATER and C_CAN_JACK_BE_KILLED:
               #p_object_array.remove(get_jack_dict(p_object_array))
               PlaySound(C_SPLASH_SOUND_FILE)
               remove_object_of_type_from_array(p_object_array,C_JACK)
               #p_object_array.remove(get_jack_dict(p_object_array))
               #print (' u have died here') 
               #print(l_whats_below_me) 
            elif l_whats_below_me == C_LEDGE and p_level_config_dict['all_ledges_touched']==False: # no point checking if we have already touched them all
               l_object_below_me=f_get_object_below_me(p_object,p_object_array)
               if not l_object_below_me['has_been_touched']:
                  PlaySound(C_PLATFORM_TOUCH_SOUND_FILE)
                  l_object_below_me['has_been_touched']=True
                  # now we need to navigate sideways both left and right to make the other parts of the ledge touched
                  l_adj_object = f_get_object_to_the_right(l_object_below_me,p_object_array)
                  while (l_adj_object and l_adj_object['type']==C_LEDGE):
                     l_adj_object['has_been_touched']=True
                     l_copy=l_adj_object.copy()
                     l_adj_object = f_get_object_to_the_right(l_copy,p_object_array)
                  l_adj_object = f_get_object_to_the_left(l_object_below_me,p_object_array)
                  while (l_adj_object and l_adj_object['type']==C_LEDGE):
                     l_adj_object['has_been_touched']=True
                     l_copy=l_adj_object.copy()
                     l_adj_object = f_get_object_to_the_left(l_copy,p_object_array)
                  
                  p_level_config_dict['all_ledges_touched']=have_all_ledges_been_touched(p_object_array)
                  if p_level_config_dict['all_ledges_touched']:
                     p_level_config_dict['level_score']+=  p_level_config_dict['ledge_platform_bonus']

            l_y_mult=0

         return l_y_mult   
         
def load(p_game_attributes):
#def load(p_game_level):

  #l_living_array=[]
  l_object_array=[]
  level_config_dict={}
  #l_game_attributes=

  if len(p_game_attributes) == 0: # new game
     p_game_attributes.update({'level':C_START_LEVEL})
     p_game_attributes.update({'num_lives':C_START_LIVES})
     p_game_attributes.update({'score':0})
     p_game_attributes.update({'bonus_lives':0})
  
  p_game_attributes['level']=max(min(p_game_attributes['level'],C_NUM_LEVELS),1) # cap at 2 for now
  p_game_attributes.update({'total_paused_seconds':0.0})
  p_game_attributes.update({'high_score':readHighScore()}) 


  #level_config_dict.clear()

 

  l_file=C_INCLUDE_DIR+'level'+str(p_game_attributes['level'])+'.dat'
  #print('loading :'+l_file)
  getit=open(l_file)
  readit=getit.read()
  lines_array=readit.split()
  l_level_matrix = map(list, lines_array)

  # this reads in the defaults first and then the level config and merges them, the level values of same key will override the defaults
  #print (level_config_dict)
  level_config_dict.update(config.levelconfig['default'])
  #print ('a')
  #print (level_config_dict)
  level_config_dict.update(config.levelconfig[str(p_game_attributes['level'])])
  #print (level_config_dict)
  # add the actual level num as a key as well so can reference easier
  level_config_dict.update({'level':p_game_attributes['level']})
  level_config_dict.update({'time_left':level_config_dict['time']})
  level_config_dict.update({'all_ledges_touched':False})
  level_config_dict.update({'has_ledges':False})
  level_config_dict.update({'level_score':False})
  level_config_dict.update({'moves_done':0})
  #print (level_config_dict)

  l_baddies_cnt=0
  l_row_idx=0
  l_cntr=1
  l_jack_count=0
  
  #l_level_array_info={}
 
  for i in l_level_matrix:
    l_row_idx+=1
    l_col_idx=0
    for j in i:
      l_col_idx+=1
      #if j=='B' or j=='L' or j=='G' or j=='W':
      if j!=C_NOTHING:
        l_dict={}
        l_dict.update({'type':j})
        l_dict.update({'tag':str(l_row_idx*C_WIDTH_IN_BLOCKS+l_col_idx)})
        l_dict.update({'x':C_BLOCK_SIZE_WIDTH*(l_col_idx-1)})
        l_dict.update({'y':C_BLOCK_SIZE_HEIGHT*(l_row_idx-1)+(C_BLOCK_SIZE_HEIGHT*.5)})



        l_img = 'NULL'
        l_height_mult=1.0
        
        if j==C_BRICK:
           l_dict.update({'border_color':level_config_dict['brick_border_color']})
           l_dict.update({'fill_color':level_config_dict['brick_color']})
           l_dict.update({'can_be_moved':True})
           l_dict.update({'num_times_killed_on_left':0})
           l_dict.update({'num_times_killed_on_right':0})
           l_dict.update({'num_times_killed_on_bottom':0})
           l_dict.update({'num_times_killed_on_top':0})
           
        elif j==C_GROUND:
           l_dict.update({'border_color':level_config_dict['ground_tiles_etched_color']})
           l_dict.update({'fill_color':level_config_dict['ground_tiles_color']})
           l_dict.update({'can_be_moved':False})
        elif j==C_WATER:
           l_img=pygame.image.load(C_WATER_IMAGE)
           l_dict.update({'can_be_moved':False})
           l_height_mult=.5
        elif j==C_LEDGE:
           l_dict.update({'fill_color':level_config_dict['ledge_color']}),
           #l_dict.update({'border_color':level_config_dict['ledge_color']}), # ledges dont have border so just make same color,in fact ledges are half black
           #l_dict.update({'border_color':level_config_dict['ledge_color']}),
           l_dict.update({'touched_color':level_config_dict['ledge_touched_color']})
           l_dict.update({'touched_all_color':level_config_dict['ledge_all_touched_color']})
           
           l_dict.update({'has_been_touched':False})
           l_dict.update({'can_be_moved':False})
           l_height_mult=C_LEDGE_START_MULT/10
           level_config_dict.update({'has_ledges':True})
        elif j==C_JACK: # or j.isdigit(): # bad guy is symbolised by a number
           #l_img=pygame.image.load(C_JACK_IMAGE)
           l_dict.update({'can_be_moved':True})
           l_dict.update({'updown':'none'})
           l_dict.update({'leftright':'none'})
           l_dict.update({'last_jump_hop_height':0})
           l_dict.update({'y_ground':l_dict['y']+C_BLOCK_SIZE_HEIGHT}) # ground is y pos of object below it, or frame hieght if on actual last row
           l_jack_count+=1     
        elif j.isdigit() and l_baddies_cnt<=C_NUM_BADDIES_OVERRIDE: # bad guy is symbolised by a number
           l_dict.update({'type':C_ENEMY})
           l_dict.update({'can_be_moved':True})
           l_dict.update({'last_jump_hop_height':0})
           l_baddies_cnt+=1
        
           l_dict.update({'dropdelay':j})
           l_dict.update({'updown':'down'})
           l_dict.update({'leftright':'right'})
           l_dict.update({'y_ground':C_BLOCK_SIZE_HEIGHT*(l_row_idx-1)})
           l_dict.update({'speed':level_config_dict['speed']*C_ENEMY_SPEED_START_MULTIPLIER}) # 1 equals fast can be, if get hits by brick set to another number etc to stun it as such, x by 10 to simulat gravity on first fall
        
        if l_img != 'NULL':  
           l_img=pygame.transform.scale(l_img,(C_BLOCK_SIZE_WIDTH,int(C_BLOCK_SIZE_HEIGHT*l_height_mult)))
           l_dict.update({'image':l_img})
           gameDisplay.blit(l_dict['image'],(l_dict['x'],l_dict['y']))
        
        l_object_array.append(l_dict)
       
        l_cntr+=1

  setImagesEnemy(l_object_array)
  if (l_jack_count==0):
     print('warning jack not found in level config')
	 
  
  return (level_config_dict,l_object_array,time.time())

def setImagesEnemy(p_object_array):
   l_idx=1
   for l_object in p_object_array:
      l_filename='Null'
      if (l_object['type']==C_ENEMY):
         if C_DISPLAY_BADDIES_AS_POOL_BALLS:
            l_filename=C_INCLUDE_DIR+str(l_idx)+'-ball.png'
            if not os.path.isfile(l_filename):
              l_filename=C_ENEMY_IMAGE
         else:
            l_filename=C_ENEMY_IMAGE
         l_idx+=1 
      elif (l_object['type']==C_JACK):
         if not C_DISPLAY_JACK_AS_LADYBIRD:
            l_filename=C_JACK_IMAGE
         else:
            l_filename=C_LADYBIRD_IMAGE
			
      if (l_filename!='Null'):	 
         l_img=pygame.image.load(l_filename)
         #l_img_rect=l_img.get_rect()
         #l_img_scale=l_img_rect[2:]
         #l_img_rect[0] = C_BLOCK_SIZE_WIDTH
         #l_img_rect[1] = C_BLOCK_SIZE_HEIGHT

         l_img=pygame.transform.scale(l_img,(C_BLOCK_SIZE_WIDTH,C_BLOCK_SIZE_HEIGHT))
         #l_img=pygame.transform.smoothscale(l_img,(C_BLOCK_SIZE_WIDTH,C_BLOCK_SIZE_HEIGHT))
         l_object.update({'image':l_img})
         l_object.update({'image_name':l_filename})
         gameDisplay.blit(l_object['image'],(l_object['x'],l_object['y']))
    

def refresh(p_object_array,p_level_config_dict,p_game_attributes,p_clear_code,p_time_this_was_called): #p_time_this_was_called is the 7th 8th 9th time etc
   
   adjustbricks(p_object_array,p_level_config_dict,p_game_attributes)
   drawobjects(p_object_array,p_level_config_dict,p_game_attributes,p_clear_code) 
   
   if (p_time_this_was_called > 0 and p_time_this_was_called%p_level_config_dict['speed']==0) and C_ENABLE_BADDIES_MOVEMENT:
      move_baddies(p_object_array,p_level_config_dict,p_game_attributes,p_time_this_was_called)
   
   p_level_config_dict.update({'time_left':p_level_config_dict['time_left']-4})

   if p_level_config_dict['time_left'] == p_level_config_dict['ledge_mult']*100 and p_level_config_dict['ledge_mult'] >= 0:
      PlaySound(C_PLATFORM_SHRINK_SOUND_FILE)
      l_level_config_dict['ledge_mult']-=C_LEDGE_DEC_VAL
      if l_level_config_dict['ledge_mult']<0:
         remove_ledges_from_array(p_object_array,p_level_config_dict,p_game_attributes)

   pygame.display.update()
    


def readHighScore():
   l_the_hs=0
   if os.path.isfile(C_HIGHSCORES_FILE):
     with open(C_HIGHSCORES_FILE, 'rb') as l_file:
          p_high_score_dict = pickle.load(l_file)
          #print(p_high_score_dict)
          if 'high_score' in p_high_score_dict:
             l_the_hs=p_high_score_dict['high_score']
          
   return l_the_hs

def writeHighScore(p_high_score_dict):
   #print ('writeHighScore')
   #print(p_high_score_dict)
   with open(C_HIGHSCORES_FILE, 'wb') as l_file:
      pickle.dump(p_high_score_dict, l_file)

   #if os.path.isfile(C_HIGHSCORES_FILE):
    #  d=shelve.open(C_HIGHSCORES_FILE)
    #  d['high_score']=p_high_score
    #  d.close() 

def GetLevelFileCount():
   l_level=0
   l_found=True
   while (l_found):
      l_level+=1    
      l_file=C_INCLUDE_DIR+'level'+str(l_level)+'.dat'
      l_found=os.path.isfile(l_file)
   #print('found '+str(l_level) + ' files ')
   return l_level-1
   
def main_menu():
   global C_SOUNDS_ON    # Needed to modify global copy of globvar
   global C_SOUNDS_ON_FOR_DEFECT_MAC_ISSUE


   l_sound_save=C_SOUNDS_ON
   C_SOUNDS_ON = False
	
   l_key_pressed=False
   l_keep_playing=True
   l_display_objects=True
   l_text=C_INSTRUCTIONS_TEXT
   t_end = time.time()
  
   while (not l_key_pressed):
     #print('here')
     #print(time.time())
	 
     if time.time() - 30 > t_end: #lets move level every 30 seconds 
        l_display_objects=True
		
     
     if (l_display_objects):
        t_end = time.time()# + C_SECONDS_TODELAY_GAME_WHEN_JACK_DIES
     	
        ClearScreen(0)
        l_line_cnt=1
        l_level_config_dict={}
        l_object_array=[]
        l_game_attributes={}
        l_game_attributes.update({'level':random.randint(1,C_NUM_LEVELS)})
        #l_game_attributes.update({'speed':99999})
        (l_level_config_dict,l_object_array,C_EPOCH_START)=load(l_game_attributes)
        remove_object_of_type_from_array(l_object_array,C_ENEMY)
        l_level_config_dict.update({'speed':99999}) # set to this amount just to disable the baddies
        l_level_config_dict.update({'ledge_mult':2})
        #print (l_level_config_dict)
        l_idx=1
        C_SOUNDS_ON=False
        #print(C_SOUNDS_ON)
        while (l_idx<=10): # 10 is enough to get everything correct
           #apply_gravity_jack(get_jack_dict(l_object_array),l_object_array,l_level_config_dict)
           refresh(l_object_array,l_level_config_dict,l_game_attributes,-1,1)
           l_idx+=1
		
        #l_color=C_COLOR_YELLOW
        #if l_level_config_dict['brick_color']==C_COLOR_WHITE:
        l_color=C_COLOR_GREEN

        for line in l_text:
                 l_tuple=(10,(l_line_cnt*40))
                 text = C_FONT.render(line, True, l_color , l_tuple)
                 gameDisplay.blit(text, l_tuple)
                 l_line_cnt+=1	
        pygame.display.update()  
        l_display_objects=False
		
     for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
           if event.key == C_KEY_START:
                 l_keep_playing=True
                 l_key_pressed=True
           elif event.key == C_KEY_QUIT:
              l_keep_playing=False
              l_key_pressed=True
           elif event.key == C_KEY_LEVEL_DISP_MOVE:
              l_display_objects=True
           elif event.key == C_KEY_LEVEL_SHOW_CHEATS:
              l_display_objects=True
              l_text=C_CHEATS_TEXT
           elif event.key == C_KEY_LEVEL_SHOW_INSTRUCTIONS:
              l_display_objects=True
              l_text=_text=C_INSTRUCTIONS_TEXT
   C_SOUNDS_ON=l_sound_save              		  
   return l_keep_playing   
   
C_NUM_LEVELS=GetLevelFileCount()
print (platform.system())

#if platform.system() != 'Windows':
#  C_SOUNDS_ON_FOR_DEFECT_MAC_ISSUE=False
#C_SOUNDS_ON_FOR_DEFECT_MAC_ISSUE
#print ('Sound status for defect is ' + printbool(C_SOUNDS_ON_FOR_DEFECT_MAC_ISSUE))  



l_x_mult=0
l_y_mult=0
l_loop_ctr=1

do_sideways_move=True

l_clear_screen_code=1

l_game_attributes={}

l_epoch_save=time.time()


l_object_array=[]
l_level_config_dict={}

l_prev_key3=0
l_prev_key2=0
l_prev_key=0
l_prev_score=0

l_keep_playing=(C_START_LEVEL<=C_NUM_LEVELS)
l_goto_main_menu=True



while l_keep_playing:
    #l_dict=l_living_array[0]
    if l_goto_main_menu==True or (get_jack_count(l_object_array)==0) or get_enemy_count(l_object_array)==0: # game over
       
       if l_goto_main_menu==False and get_enemy_count(l_object_array)==0:
          # we need to make sure the jack hasnt killed the enemy mid air over water etc
          # so lets apply gravitty on the jack till it comes to a rest, and if the enemy count after this while loop is 0 it died else it was ok
          l_y_mult=apply_gravity_jack(l_jack,l_object_array,l_level_config_dict)
          while (l_y_mult!=0):
             l_jack['y']+=(C_BLOCK_SIZE_HEIGHT*l_y_mult)
             l_jack['y']=min(max(l_jack['y'],0),C_FRAME_DISPLAY_HEIGHT-C_BLOCK_SIZE_HEIGHT)
             refresh(l_object_array,l_level_config_dict,l_game_attributes,l_clear_screen_code,l_loop_ctr)
             l_y_mult=apply_gravity_jack(l_jack,l_object_array,l_level_config_dict)


       if l_goto_main_menu==True or get_jack_count(l_object_array)==0: # it is possible both the enemy count and jack account is 0, it equstes to to a suicde kill by the jack ie jump on it over water or both crushed under brick etc
          
          
          if l_object_array and  get_jack_count(l_object_array)==0:
             #l_num_lives-=1
             if not C_JACK_HAS_UNLIMITED_LIVES:
                l_game_attributes['num_lives']-=1
             l_game_attributes['total_paused_seconds']=0.0
             #time.sleep(2)

             #3 loop for 3 seconds calling refresh, just moves every to correct spot
             t_end = time.time() + C_SECONDS_TODELAY_GAME_WHEN_JACK_DIES
             while time.time() < t_end:
                refresh(l_object_array,l_level_config_dict,l_game_attributes,False,l_loop_ctr)
                l_loop_ctr+=1 


          if l_goto_main_menu==True or l_game_attributes['num_lives']==0:
             l_goto_main_menu=False
             l_keep_playing=main_menu()
             if not l_keep_playing:
                break 
            
             l_game_attributes.clear()

       elif get_enemy_count(l_object_array)==0:
          l_game_attributes['level']+=1
		  
          while l_level_config_dict['time_left']>0:
             #print(l_level_config_dict['time_left'])
             l_level_config_dict['time_left']-=4
             #PlaySound(C_TIMER_WIND_DOWN_SOUND_FILE)
             # overkill to refresh everything over and over in this loop but adds a good delay as well
             refresh(l_object_array,l_level_config_dict,l_game_attributes,True,0)

             l_level_config_dict['level_score']+=4
          l_game_attributes['score']+=l_level_config_dict['level_score']

          if (l_game_attributes['level']>C_NUM_LEVELS):
             #print('game completed')  
             l_keep_playing=main_menu()
          #else:		  
             #print('level completed')
             #print('next lvl = '+str(l_game_attributes['level']))
          
		  
          while (l_game_attributes['score'] >= C_SCORE_NEW_LIFE_BONUS*(l_game_attributes['bonus_lives']+1)):
             l_game_attributes['bonus_lives']+=1
             l_game_attributes['num_lives']+=1

          l_game_attributes['num_lives']=min(C_MAX_LIVES_ALLOWED,l_game_attributes['num_lives']) # cap at specific amount        


       del l_object_array[:]
       
       l_level_config_dict.clear()
       #print(l_game_attributes)   
       (l_level_config_dict,l_object_array,C_EPOCH_START)=load(l_game_attributes)
       #print(l_level_config_dict)
       l_prev_score=0
       



       if (l_game_attributes['score'])>l_game_attributes['high_score']:
          l_game_attributes['high_score']= l_game_attributes['score']  # and then write back to file
          l_highscore_dict={}
          l_highscore_dict.update({"high_score":l_game_attributes['high_score']})
          l_highscore_dict.update({"level":l_game_attributes['level']})
          l_highscore_dict.update({"time":time.time()})


          #json.dump(l_highscore_dict,open(C_HIGHSCORES_FILE,"a"))
          writeHighScore(l_highscore_dict)
       
       #l_pause_total_seconds=0.0
       l_jack=get_jack_dict(l_object_array)

       #print(l_jack)
       refresh(l_object_array,l_level_config_dict,l_game_attributes,0,0)
       #print('******** finished the load****') 

       #very important to reset these as if we dont they keep the value from the previous game, and this was causing jack to go down one if had previously been killed in the air, which is another bug in itself
       #living things should be pushed back to the ground if crushed by something
       l_y_mult=0
       l_x_mult=0
       flushkeybuffer()
    
    for event in pygame.event.get():
        
        l_y_mult=0
        #l_refresh_bottom_bar=False
        l_clear_screen_code=1 # top only by default


        l_jack=get_jack_dict(l_object_array)
        #if not l_jack:
        #   print('jack not found')
        #else:
     
        if l_jack['updown'] == 'up': # currently moving up let it do this with no control over it
           l_y_mult=-1
        elif l_jack['updown'] == 'down': # currently moving up let it do this with no control over it
           l_y_mult=1
            
        #if event.type == pygame.QUIT:
        #    l_keep_playing=False

        if event.type == pygame.KEYDOWN:
        
            l_Last_four_keys_str=chr(l_prev_key3)+chr(l_prev_key2)+chr(l_prev_key)+chr(event.key)
            #print(l_Last_four_keys_str)
            #print (event.key)
            l_jack['last_jump_hop_height']=C_HUMAN_JUMP_BLOCKS

            #print (l_dict['updown'])
            if event.key == C_KEY_QUIT:
               #l_keep_playing=False
               l_goto_main_menu=True
            
            elif event.key == C_KEY_SOUNDONOFF:
               C_SOUNDS_ON=not C_SOUNDS_ON
               #l_refresh_bottom_bar=True
               l_clear_screen_code=0

            elif event.key == C_KEY_PAUSE:

               #l_jack=get_jack_dict(l_object_array)
               #print(l_jack)

               if (not C_GAME_PAUSED): # ie we are about to pause
                  l_pause_start=time.time()
               else: # we are aboutto unpause
                  l_game_attributes['total_paused_seconds'] +=  (time.time() - l_pause_start)
                  #print('total paused seconds = '+str(l_game_attributes['total_paused_seconds']))
               # need to call here as pause actually prevents this executing below
               C_GAME_PAUSED=not C_GAME_PAUSED
               refresh(l_object_array,l_level_config_dict,l_game_attributes,True,l_loop_ctr)
              
            #elif event.key == C_KEY_ENEMIES_FROM_HELL:
            if l_Last_four_keys_str == C_CHEAT_CODE_HELLMODE:
               C_ENEMIES_FROM_HELL=not C_ENEMIES_FROM_HELL
               l_clear_screen_code=0
               #l_refresh_bottom_bar=True
            elif l_Last_four_keys_str == C_CHEAT_CODE_DISPLAY_BRICK_NUMBERS:
               C_DISPLAY_BRICK_NUMBERS=not C_DISPLAY_BRICK_NUMBERS
               l_clear_screen_code=0
               #l_refresh_bottom_bar=True

            
            elif l_Last_four_keys_str == C_CHEAT_CODE_JACK_IMMORTAL:
               C_CAN_JACK_BE_KILLED=not C_CAN_JACK_BE_KILLED
               l_clear_screen_code=0
               #l_refresh_bottom_bar=True 
            
            elif l_Last_four_keys_str == C_CHEAT_CODE_POOL_BALL_IMAGES:
               C_DISPLAY_BADDIES_AS_POOL_BALLS=not C_DISPLAY_BADDIES_AS_POOL_BALLS
               #l_refresh_bottom_bar=True
               l_clear_screen_code=0
               setImagesEnemy(l_object_array) 
			   
            elif l_Last_four_keys_str == C_CHEAT_CODE_JACK_AS_LADYBIRD:
               C_DISPLAY_JACK_AS_LADYBIRD=not C_DISPLAY_JACK_AS_LADYBIRD
               l_clear_screen_code=0
               setImagesEnemy(l_object_array) 
			
            elif l_Last_four_keys_str==C_CHEAT_CODE_EXTRA_LIFE:
               l_game_attributes['num_lives']=min(l_game_attributes['num_lives']+1,C_MAX_LIVES_ALLOWED)
               #l_refresh_bottom_bar=True
               l_clear_screen_code=0
            
            elif l_Last_four_keys_str==C_CHEAT_CODE_JACK_UNLIMITED_LIVES:
               C_JACK_HAS_UNLIMITED_LIVES=not C_JACK_HAS_UNLIMITED_LIVES
               l_clear_screen_code=0
               #l_refresh_bottom_bar=True

            elif l_Last_four_keys_str == C_CHEAT_CODE_RELOAD_LEVEL or l_Last_four_keys_str == C_CHEAT_CODE_NEXT_LEVEL or l_Last_four_keys_str == C_CHEAT_CODE_PREV_LEVEL:
               #l_living_array=[]
               #l_object_array=[]
               if C_GAME_PAUSED:
                  C_GAME_PAUSED=False 

               if l_Last_four_keys_str == C_CHEAT_CODE_NEXT_LEVEL:
                  l_game_attributes['level']+=1 
               elif l_Last_four_keys_str == C_CHEAT_CODE_PREV_LEVEL:
                  l_game_attributes['level']-=1
               del l_object_array[:]
               l_object_array=[]
               l_level_config_dict.clear()    
               (l_level_config_dict,l_object_array,C_EPOCH_START)=load(l_game_attributes) 
               #l_pause_total_seconds=0.0 
               #l_refresh_bottom_bar=True
               l_clear_screen_code=0 

            elif event.key == C_KEY_UP:# or event.key == C_KEY_DOWN:
               l_y_mult=0
               if event.key == C_KEY_UP and not f_something_above_me(l_jack,l_object_array):
                  #print('up')
                  l_y_mult=-1
                  l_jack['updown'] = 'up'
                  l_hops_off_roof=(l_jack['y'] / C_BLOCK_SIZE_HEIGHT) - 1.5 # 1.5 is the half row of bullshit and then the drop zone
                  l_jack['last_jump_hop_height']=min(C_HUMAN_JUMP_BLOCKS,l_hops_off_roof)
                  
            elif event.key == C_KEY_LEFT or event.key == C_KEY_RIGHT:
               #print(event.key)
               #level_config_dict.update['moves_done']+=1
               
               if l_jack['updown'] == 'none': 

                  if event.key == C_KEY_LEFT and not f_something_to_left(l_jack,l_object_array):
                     l_x_mult=-1
                  elif event.key == C_KEY_RIGHT and not f_something_to_right(l_jack,l_object_array):
                     l_x_mult=1
               else:
                  l_x_mult=0
                  
            elif event.key == C_KEY_HOP_LEFT or event.key == C_KEY_HOP_RIGHT:
               #level_config_dict.update['moves_done']+=1
               if l_jack['updown'] == 'none' and not f_something_above_me(l_jack,l_object_array):
                  
                  l_y_mult=-1
                  l_jack['updown'] = 'up'
                  
                  l_hops_off_roof=(l_jack['y'] / C_BLOCK_SIZE_HEIGHT) - 1.5 # 1.5 is the half row of bullshit and then the drop zone
                  l_idx=min(C_HUMAN_JUMP_BLOCKS,l_hops_off_roof)
                  
                  #print('hops off roof = '+str(l_hops_off_roof))
                  #print('hops to be done='+str(l_idx))
                  
                  while (l_idx>=0):
                    
                    l_obj_type_above=f_get_object_type_above_me(l_jack,l_object_array,l_idx)
                    if (event.key == C_KEY_HOP_LEFT):
                       l_obj_type_above_and_to_side=f_get_object_type_to_the_left(l_jack,l_object_array,l_idx)
                    else:
                       l_obj_type_above_and_to_side=f_get_object_type_to_the_right(l_jack,l_object_array,l_idx)
                    
                    #print('above me = '+l_obj_type_above+str(l_idx))
                    #print('above and to the side = '+l_obj_type_above_and_to_side)

                    if (l_obj_type_above_and_to_side==C_NOTHING) and (l_obj_type_above==C_NOTHING):# or l_obj_type_above==C_ENEMY)): 
                       #print ('found at '+str(l_idx))
                       break 
                    l_idx-=1    

                  if (l_idx<0): # couldnt jump sideways due to shit in the road
                     l_x_mult=0
                  elif event.key == C_KEY_HOP_LEFT:
                     l_x_mult=-1
                  elif event.key == C_KEY_HOP_RIGHT:
                     l_x_mult=1

                  #print(l_idx) 
                  l_jack['last_jump_hop_height']=l_idx+1

            elif event.key == C_KEY_BRICKMOVE_LEFT or event.key == C_KEY_BRICKMOVE_RIGHT:
               #level_config_dict.update['moves_done']+=1
               if l_jack['updown'] == 'none':
                  if event.key == C_KEY_BRICKMOVE_LEFT:
                     if not f_something_to_left(l_jack,l_object_array) and object_type_can_be_moved(f_get_object_type_to_the_right(l_jack,l_object_array)) and l_jack['x']-C_BLOCK_SIZE_WIDTH>=0: # if no bricks to the right we are doing a pull
                        l_x_mult=-1
                        l_jack['leftright']='left'
                        f_pull_object(l_jack,l_object_array,l_level_config_dict,l_game_attributes,C_LEFT)

                     else: # we are doing a push
                        push_objects_left(l_jack,l_object_array,l_level_config_dict)
                        
                  elif event.key == C_KEY_BRICKMOVE_RIGHT:
                   
                     if not f_something_to_right(l_jack,l_object_array) and object_type_can_be_moved(f_get_object_type_to_the_left(l_jack,l_object_array)) and l_jack['x']+C_BLOCK_SIZE_WIDTH<C_FRAME_DISPLAY_WIDTH: # if no bricks to the right we are doing a pull
                        l_x_mult=1
                        l_jack['leftright']='right'
                        f_pull_object(l_jack,l_object_array,l_level_config_dict,l_game_attributes,C_RIGHT)
                     else: # we are doing a push
                        push_objects_right(l_jack,l_object_array,l_level_config_dict)

            l_prev_key3=l_prev_key2
            l_prev_key2=l_prev_key
            l_prev_key=event.key              
    
        elif event.type == pygame.KEYUP:
             if event.key == C_KEY_UP or event.key == C_KEY_DOWN or event.key == C_KEY_LEFT or event.key == C_KEY_RIGHT:
                if l_jack['updown'] == 'up': # currently moving up let it do this with no control over it
                   pass
                elif l_jack['updown'] == 'down': # currently moving up let it do this with no control over it
                   pass
                else:
                   l_x_mult=0
                   l_y_mult=0

    #end for loop get events


    if not C_GAME_PAUSED:
      #print(l_y_mult)
      #print(l_jack['y'])
      #print('loop = '+str(l_loop_ctr))
      #print (l_jack['updown'])
      if l_jack['updown'] == 'up': # currently moving up let it do this with no control over it
         #print('here i am going up')
         #print(l_x_mult)
         if not f_something_above_me(l_jack,l_object_array):
            l_y_mult=-1
         else:
            #print('doing a uturn')
            l_y_mult=0
            l_x_mult=0
            l_jack['updown'] = 'down'

      elif l_jack['updown'] == 'down': 
         #print ('caa 1')
         l_y_mult=apply_gravity_jack(l_jack,l_object_array,l_level_config_dict)
         
      if get_jack_count(l_object_array)>0: # continue only if jack hasnt died in previous call to applygravityjack
                             
        l_jack['y']+=(C_BLOCK_SIZE_HEIGHT*l_y_mult)
        #print(l_jack['y'])
        l_jack['y']=min(max(l_jack['y'],0),C_FRAME_DISPLAY_HEIGHT-C_BLOCK_SIZE_HEIGHT)
        #print('post min max')
        #print(l_jack['y'])

        bool_just_moving_sideways=False
        do_sideways_move=False
        # hit apex of jump
   
        if l_jack['updown'] == 'up' and l_jack['y'] <= l_jack['y_ground'] - (l_jack['last_jump_hop_height'] *C_BLOCK_SIZE_HEIGHT):
           l_jack['updown'] = 'down'
           do_sideways_move=True
        elif l_jack['updown'] == 'down' and l_y_mult==0: #l_y_mult of 0 which is returned from appl_gravity_jack means have hit a resting object
           l_jack['updown'] = 'none'
           l_jack['y_ground']=l_jack['y']+C_BLOCK_SIZE_HEIGHT
           do_sideways_move=True
        elif l_jack['updown'] == 'none':# and l_dict['leftright'] != 'none':
           do_sideways_move=True
        
        if do_sideways_move==True:
           l_jack['x']+=(C_BLOCK_SIZE_WIDTH*l_x_mult)
           l_jack['x']=min(max(l_jack['x'],0),C_FRAME_DISPLAY_WIDTH-C_BLOCK_SIZE_WIDTH)
           l_x_mult=0
           l_y_mult=apply_gravity_jack(l_jack,l_object_array,l_level_config_dict)
      
     
      refresh(l_object_array,l_level_config_dict,l_game_attributes,l_clear_screen_code,l_loop_ctr)
     
    l_loop_ctr+=1
    l_prev_jack = l_jack.copy()
    l_prev_score= l_level_config_dict['level_score']
    clock.tick(C_FRAMERS_PER_SEC)

pygame.quit()
quit()
    
