import pygame
import time
import thread

class Looper:
   def __init__(self):
      self.looping = False
      self.actions = []
      self.start_time = 0
      pass

   def new_loop(self):
      self.actions = {}

   def add_action(self, action):
      wait = time.time()
      self.actions.append(((time.time() - wait) * 100000, action))

   def play(self):
      for action in self.actions:
         print(action)
      # create a new thread for playing the loop
      play_thread = thread.start_new_thread(self.execute_actions, ())
   
   def execute_actions(self):
      cur_action = 0
      while True:
         for action in self.actions:
            # if this is the last action, just play it
            if cur_action == (len(self.actions) - 1):
               # perform the action
               action[1]()
            # otherwise, play the current action and sleep for the time specified
            # by the next action
            else:
               # perform the action
               action[1]()
               # sleep this thread for the amount specified by the next action
               time.sleep(self.actions[cur_action + 1][0])
               cur_action += 1



pygame.mixer.init()
looper = Looper()

def play_sound(file, channel):
   pygame.mixer.Channel(channel)
   pygame.mixer.music.load(file)
   pygame.mixer.music.play()

def snare():
   if looper.looping:
      looper.add_action(snare)

   play_sound('sounds/snare.mp3', 0)

def bass():
   if looper.looping:
      looper.add_action(bass)

   play_sound('sounds/bass.mp3', 1)

def record():
   pass

def loop():
   if looper.looping:
      # stop looping, start playing
      looper.looping = False
      looper.play()
   elif not looper.looping:
      # start collecting actions
      looper.looping = True
      
