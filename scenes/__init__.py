import g
import widgets
import interface


class Scene():
	message = None
	place = None
	foe = None
	next_place = None
	
	def __init__(self):
		self.next_scene = None
		self.menu = []
		#set nex_place as background
		if g.scene and g.scene.place:
			g.scene.place.leave()
		g.status = None
		g.pending_actions.append(interface.transition)
		if self.message:
			g.board.new_message(self.message)

	def ready(self):
		pass

	def on_start_enter(self):
		pass

	def on_entering(self):
		pass
		
	def on_center(self):
		pass
		
	def on_start_leave(self):
		pass
		
	def on_leaving(self):
		pass	
