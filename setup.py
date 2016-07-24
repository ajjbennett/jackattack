#!c:\python\python
import cx_Freeze

l_base=None

l_executables = [cx_Freeze.Executable('jackattack.py', base=l_base)]
#l_includes = ['config.py','1-ball.png','2-ball.png','3-ball.png','4-ball.png','5-ball.png','6-ball.png','7-ball.png','8-ball.png',
#              '9-ball.png','10-ball.png','11-ball.png','12-ball.png','brickmove.wav','enemydead.wav','jackdead.wav','splash.wav',
#              'platform_shrink.wav','platform_touch.wav','baddie2.png','baddie.png','halo.png','hell.png','soundon.png','soundoff.png',
#			  'paused.png','level1.dat','level2.dat','level3.dat','level4.dat','level5.dat','level6.dat','level7.dat','level8.dat','level9.dat',
#             'level10.dat','level11.dat','level12.dat','level13.dat','level14.dat','level15.dat']
l_includes=['include/']
l_packages = ['pygame']
			  
cx_Freeze.setup(
   name='Jack Attack',
   options = {'build.exe': {'packages':l_packages,'include_files':l_includes}},
   version='0.1',
   description='Jack Attack',
   executables = l_executables
   )