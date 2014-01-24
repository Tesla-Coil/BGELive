from bge import logic
from time import time

import re
name_suffix_regex = re.compile('\.[0-9]{3}$')

class Timer():
	'''A timer that takes in time in seconds, and counts down to zero. 

	:param number seconds: The time for the Timer to run in seconds.
	:returns: Time remaining in seconds; 0.0 when finished
	:rtype: floar
	'''
	
	def __init__(self, seconds = 0.0):
		self._time_of_end = time() + seconds #set the time() at which the timer == 0.0

	def __get__(self):
		if self._time_of_end - time() > 0:
			return self._time_of_end - time()
		else:
			return 0.0
	def __str__(self):
		return str( self.__get__() )

	def __repr__(self):
		return self.__str__()

	def __gt__(self, other):
		return self.__get__() > other
	def __lt__(self, other):
		return self.__get__() < other
	def __eq__(self, other):
		return self.__get__() == other
	def __float__(self):
		return float(self.__get__())

####### TEST!!! #######
def clean_name(obj):
	"""Get the name of an object, minus the autogenerated number provided by Blender when copying an object.
	   For example, if you copied an object named 'Enemy', it would be automatically named 'Enemy.001'. This would return the original name: 'Enemy'.

	   :param KX_GameObject obj: The object to get the clean_name from
	   :returns: The cleaned name of the object
	   :rtype: str
	"""
	if name_suffix_regex.search(obj.name) != None:
		return obj.name[0:-4]

def find_object(name, list=logic.getCurrentScene().objects):
	"""Retrieve an object from a list with a given clean_name.
	   Use to prevent missing duplicate objects, as they are automatically renamed by Blender when added in the editor

	   :param str name: The name to look for.
	   :param object list list: (optional) A list of objects to search. Defaults to the current scene's object list
	   :returns: The first object found with the given name.
	   :rtype: KX_GameObject
	"""
	for obj in list:
		if name == obj.name or name == clean_name(obj):
			return obj
	return None

def find_objects(name, list=logic.getCurrentScene().objects):
	"""Retrieve all objects from a list with a given clean_name.
	   Use to prevent missing duplicate objects, as they are automatically renamed by Blender when added in the editor

	   :param str name: The name to look for.
	   :param object list list: (optional) A list of objects to search. Defaults to the current scene's object list
	   :returns: The first object found with the given name.
	   :rtype: list of KX_GameObjects
	"""
	results = []
	for obj in list:
		if name == obj.name or name == clean_name(obj):
			results += [obj]
	if results != []:
		return results
	else:
		return None