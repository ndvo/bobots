import g
import widgets

def transition():
	if g.next_scene:
		if not g.PC or g.PC.pos[0] < -104 or g.PC.pos[0] > 574 or g.game_status =="menu":
			if g.scene.place and g.scene.place.action == 'out':
				g.game_status = "game"
				g.scene = g.next_scene
				g.scene.ready()
				g.next_scene = None
				g.PC.pos[0] = -100
				g.PC.action = g.PC.arrive
				return True
	return False

def fight():
	done = False
	if g.PC.chosen_bobot:
		if not g.panel:
			g.panel = widgets.InformationPanel('panel-fight')
		elif (g.panel.step == len(g.panel.animation)):
				g.panel = None
				done= True
	return done
