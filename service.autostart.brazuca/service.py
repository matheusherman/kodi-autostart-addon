import xbmc
import xbmcgui

# Destino que abre ao iniciar o Kodi. Troque pela URL do addon que você quer.
# Exemplo: plugin://plugin.video.seuaddon/?url=...&mode=...&name=...
PLUGIN_URL = 'plugin://plugin.video.BrazucaPlay.Matrix/?url=%23menu_canais&mode=21&name=TV+AO+VIVO'
WAIT_SECONDS = 10

monitor = xbmc.Monitor()
xbmc.log('autostart: waiting %ss' % WAIT_SECONDS, xbmc.LOGINFO)

# mostra o indicador de carregamento enquanto o Kodi termina de iniciar
xbmcgui.Dialog().notification('Autostart', 'Abrindo...', xbmcgui.NOTIFICATION_INFO, WAIT_SECONDS * 1000)
xbmc.executebuiltin('ActivateWindow(busydialognocancel)')

aborted = monitor.waitForAbort(WAIT_SECONDS)

xbmc.executebuiltin('Dialog.Close(busydialognocancel,true)')

if not aborted:
    xbmc.executebuiltin('ActivateWindow(Videos,%s,return)' % PLUGIN_URL)
    xbmc.log('autostart: opened %s' % PLUGIN_URL, xbmc.LOGINFO)
