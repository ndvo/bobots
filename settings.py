
fps = 40
talk_time = 2

#### Translation function ####
import gettext
import locale

current_locale, encoding = locale.getdefaultlocale()
"""
try:
	localization_support = gettext.translation('oca_table_top_games', directory.locale, [current_locale])
except:
	localization_support = gettext.translation('oca_table_top_games', directory.locale, ['en_US'])
	
localization_support.install()
t = localization_support.ugettext
"""



