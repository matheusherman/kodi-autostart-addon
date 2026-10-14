# Kodi autostart service

Addon de serviço para Kodi (Android/Kodi 21+) que abre automaticamente um addon ou uma tela específica quando o Kodi inicia. Mostra um aviso "Abrindo..." com indicador de carregamento durante a espera.

## Como usar

1. Edite `PLUGIN_URL` e `WAIT_SECONDS` no topo de `service.autostart.brazuca/service.py`.
2. Compacte a pasta `service.autostart.brazuca` em um `.zip` (a raiz do zip deve ser essa pasta).
3. No Kodi: **Add-ons → Instalar de arquivo zip** e escolha o zip.
4. Reinicie o Kodi. Confira se o serviço está ativo em **Add-ons → Gerenciar add-ons → Serviços**.

Para descobrir a URL de uma tela: abra o addon, entre na pasta desejada e veja a URL no log (`temp/kodi.log` com nível de debug), ou inspecione o código do addon.

## Observações

- A URL depende de como o addon de destino organiza os menus. Se ele mudar, atualize `PLUGIN_URL`.
- Os logs são gravados com `xbmc.log` (nível info).
- Testado em Kodi 21.1 (Android TV).
