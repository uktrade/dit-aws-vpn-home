# DIT AWS VPN HOME PAGE

Simple django app that presents links to AWS VPN client software.  

The app is locked behind SSO.

client config file is created on startup (settings.py) from the env var VPN_CLIENT_CONFIG

IF there are changes to the Client VPN, please update the new VPN client ID and redeploy the app.
