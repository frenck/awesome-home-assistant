# Awesome Home Assistant [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
<!--lint disable double-link-->

<div align="center">
  <a href="https://awesome-ha.com">
    <img width="400" src="https://www.awesome-ha.com/images/awesome-home-assistant.svg" alt="Awesome Home Assistant">
  </a>
  <br>
  <a href="https://awesome-ha.com"><strong>https://awesome-ha.com</strong></a>
</div>

Home Assistant is an open source home automation that puts local control and
privacy first. Powered by a worldwide community of tinkerers and DIY
enthusiasts. Perfect to run on a Raspberry Pi or a local server.

If you want to get an impression on the look and feel,
you should check out the [Home Assistant online demo](https://demo.home-assistant.io).

Awesome Home Assistant is a curated list of awesome
[Home Assistant](https://www.home-assistant.io) resources.
Additional software, tutorials, custom integration, add-ons,
custom Lovelace cards & plugins, cookbooks, example setups, and much more.

The list is divided into categories. The links in those categories do not have
pre-established order; the order is for contribution. If you want to contribute,
please read the [guide](https://github.com/frenck/awesome-home-assistant/blob/master/CONTRIBUTING.md).

## Contents

- [How to use](#how-to-use)
- [Installing](#installing)
- [In case you need help](#in-case-you-need-help)
  - [Official Channels](#official-channels)
  - [Other Channels](#other-channels)
- [Public Configurations](#public-configurations)
- [Add-ons](#add-ons)
  - [Official Add-ons](#official-add-ons)
  - [Third Party Add-ons](#third-party-add-ons)
- [Lovelace User Interface](#lovelace-user-interface)
  - [Themes](#themes)
  - [Custom Lovelace UI Cards](#custom-lovelace-ui-cards)
  - [Alternative Dashboards](#alternative-dashboards)
- [Custom Components](#custom-components)
- [DIY](#diy)
  - [DIY Gateways](#diy-gateways)
  - [DIY Projects](#diy-projects)
- [Online Resources](#online-resources)
  - [Blogs](#blogs)
  - [YouTube Channels](#youtube-channels)
  - [Podcasts](#podcasts)
  - [Twitter](#twitter)
- [Uncategorized](#uncategorized)
- [Alternative Home Automation Software](#alternative-home-automation-software)
- [Other Awesome Lists](#other-awesome-lists)
- [Trademark Legal Notice](#trademark-legal-notice)

## How to use

Awesome Home Assistant is a fantastic list for people trying to automate every
aspect of their home. Automating your home is a long, hard, and never finished
task that usually involves a lot of tinkering.

You can navigate through the list by:

- Simply press <kbd>command/ctrl</kbd> + <kbd>F</kbd> to search for a keyword
- Go through our [_Contents list_](#contents)
- Alternatively, use the search on our website: <https://www.awesome-ha.com>

## Installing

Home Assistant has several installation / running methods. Many people have
different opinions and their personal favorites. Each method has its
advantages and disadvantages. Important to know, there is no wrong, or right here,
each technique installs the **SAME** Home Assistant.

Home Assistant currently _recommends_ the Home Assistant OS installation method.

- [Home Assistant OS](https://www.home-assistant.io/getting-started/) - Installing using a managed environment (recommended method).
- [Home Assistant Container](https://www.home-assistant.io/docs/installation/docker/) - Installing on Docker.
- [Home Assistant Supervised](https://github.com/home-assistant/supervised-installer/blob/master/README.md) - Installing a semi managed environment for experts.
- [Home Assistant Core](https://www.home-assistant.io/docs/installation/virtualenv/) - Manual installation using a Python virtual environment.

## In case you need help

_There are various ways to get in touch with the Home Assistant community.
It doesn't matter if you have a question, need help, want to request a feature,
or just say ‘Hi’._

### Official Channels

- [Home Assistant Discord](https://discordapp.com/invite/c5DvZ4e) - Join the chat, most of us are there.
- [Home Assistant Community](https://community.home-assistant.io/?u=frenck) - The discussion forum, also used for feature requests.
- [Home Assistant Subreddit](https://www.reddit.com/r/homeassistant/) - If you are into Reddit, subscribe.
- [Home Assistant Facebook Group](https://www.facebook.com/groups/HomeAssistant/) - Facebook group for enthusiasts.

### Other Channels

- [Dr. ZZs](https://www.facebook.com/groups/1969622823351838/) - Facebook group by Dr. Zzs.
- [Home Assistant Community Add-ons Discord](https://discord.me/hassioaddons) - Get support on the Home Assistant Community Add-ons.
- [ESPHome Discord](https://discord.gg/KhAMKrd) - Get support for your DIY ESPHome project.
- [Dutch Domotics Discord](https://discord.gg/Ee5X7T7) - Dutch Discord server with home automation enthusiasts.

## Public Configurations

_Some people store their full Home Assistant configuration on GitHub. They are
an awesome source for learning and a great source of inspiration._

- [Carlo Costanzo](https://github.com/CCOSTAN/Home-AssistantConfig#logo) - Probably the most documented configuration out there.
- [DubhAd](https://github.com/DubhAd/Home-AssistantConfig) - Also known as Tinkerer shares his configuration files.
- [geekofweek](https://github.com/geekofweek/homeassistant) - Has over 300+ automations.
- [Isabella Gross Alström](https://github.com/isabellaalstrom/home-assistant-config) - Hass.io, Intel NUC, Ubuntu, Docker, Lovelace UI.
- [Mahasri Kalavala](https://github.com/skalavala/mysmarthome) - Impressive setup, with lots of different hardware working together.
- [stanvx](https://github.com/stanvx/Home-Assistant-Configuration) - Complete setup which uses AppDaemon and HA Floorplan as well.
- [Vasiley](https://github.com/Vasiley/Home-Assistant-Main) - Runs two instances that work together.
- [Alok Saboo](https://github.com/arsaboo/homeassistant-config) - Also known as arsaboo. Regularly updated.
- [Aaron Bach](https://github.com/bachya/smart-home) - Also known as bachya. Regularly updated and includes numerous Dockerized services.
- [James McCarthy](https://github.com/JamesMcCarthy79/Home-Assistant-Config) - Well documented, 3 instances & automations in YAML & Node-RED.
- [Franck Nijhof](https://github.com/frenck/home-assistant-config) - Hass.io based, very different configuration structure compared to others.
- [Andrea Donno](https://github.com/adonno/Home-AssistantConfig) - Hass.io based, focused on touchscreen usage.
- [Klaas Schoute](https://github.com/klaasnicolaas/Smarthome-homeassistant-config) - Hass.io based, Intel NUC, Ubuntu Server, Docker and regularly updated.
- [Jason Hunter](https://github.com/hunterjm/home-assistant-config) - Hass.io based, Intel NUC i5, TensorFlow & camera streams.
- [Nathan](https://github.com/N-l1/home-assistant-config) - Lovelace config and themes based on Soft UI.
- [Andrea Iannucci](https://github.com/SeLLeRoNe/HA-Config) - Also known as SeLLeRoNe. Regularly updated.

## Add-ons

_Add-ons are additional applications and services, that can be run alongside
Home Assistant. The Home Assistant OS and Supervised installations types,
provide the Supervisor, which is capable of running and manage these add-ons._

### Official Add-ons

_Created and maintained by the Home Assistant team._

- [DuckDNS](https://github.com/home-assistant/hassio-addons/blob/master/duckdns/DOCS.md) - Updates your Duck DNS IP address and generate SSL using Let's Encrypt.
- [File editor](https://github.com/home-assistant/hassio-addons/blob/master/configurator/DOCS.md) - Browser-based configuration file editor.
- [Mosquitto](https://github.com/home-assistant/hassio-addons/blob/master/mosquitto/DOCS.md) - Fast and reliable MQTT broker.
- [Terminal & SSH](https://github.com/home-assistant/hassio-addons/blob/master/ssh/DOCS.md) - Allows logging in remotely to using a web terminal or SSH client.
- [Samba](https://github.com/home-assistant/hassio-addons/blob/master/samba/DOCS.md) - Access your configuration files using Windows network shares.
- [NGINX SSL proxy](https://github.com/home-assistant/hassio-addons/blob/master/nginx_proxy/DOCS.md) - Reverse proxy with SSL termination.
- [deCONZ](https://github.com/home-assistant/hassio-addons/blob/master/deconz/DOCS.md) - Control a ZigBee network using ConBee or RaspBee hardware by Dresden Elektronik.
- [TellStick](https://github.com/home-assistant/hassio-addons/blob/master/tellstick/DOCS.md) - Run a TellStick and TellStick Duo service.
- [Ada](https://github.com/home-assistant/hassio-addons/blob/master/ada/DOCS.md) - Ada is voice assistant powered by Almond which is open and privacy-preserving.
- [Almond](https://github.com/home-assistant/hassio-addons/blob/master/almond/DOCS.md) - The Open, Privacy-Preserving Virtual Assistant.
- [HomeMatic](https://github.com/home-assistant/hassio-addons/blob/master/homematic/DOCS.md) - HomeMatic central based on OCCU.
- [Let's Encrypt](https://github.com/home-assistant/hassio-addons/blob/master/letsencrypt/DOCS.md) - Get a free SSL certificate from Let's Encrypt; an open and automated certificate authority (CA).
- [MariaDB](https://github.com/home-assistant/hassio-addons/blob/master/mariadb/DOCS.md) - An open source relational database (fork of MySQL).
- [OpenZWave](https://github.com/home-assistant/hassio-addons/blob/master/zwave/DOCS.md) - Use an Z-Wave USB-stick with the QT OpenZWave Daemon.

### Third Party Add-ons

_Anyone can create an add-on, the following are created by the community._

- [SSH & Web Terminal](https://github.com/hassio-addons/addon-ssh) - SSH and Web-based terminal with tons of pre-loaded useful tools.
- [UniFi Controller](https://github.com/hassio-addons/addon-unifi) - The UniFi Controller allows you to manage your UniFi network using a web browser.
- [Node-RED](https://github.com/hassio-addons/addon-node-red) - Flow-based programming for the Internet of Things.
- [Plex Media Server](https://github.com/hassio-addons/addon-plex) - Your recorded media beautifully organized and ready to stream.
- [IDE](https://github.com/hassio-addons/addon-ide) - Advanced web-based IDE, based on Cloud9 IDE.
- [Dasshio](https://github.com/danimtb/dasshio) - Easily use your Amazon Dash Buttons.
- [InfluxDB](https://github.com/hassio-addons/addon-influxdb) - Scalable datastore for metrics, events, and real-time analytics.
- [Grafana](https://github.com/hassio-addons/addon-grafana) - Open platform for beautiful analytics and monitoring.
- [Tor](https://github.com/hassio-addons/addon-tor) - Protect your privacy and access your instance via Tor.
- [Spotify Connect](https://github.com/hassio-addons/addon-spotify-connect) - Spotify Connect client for playing music on your Home Assistant device.
- [zigbee2mqtt](https://github.com/danielwelch/hassio-zigbee2mqtt) - Zigbee to MQTT bridge, get rid of your proprietary Zigbee bridges.
- [AppDaemon](https://github.com/hassio-addons/addon-appdaemon) - Python Apps and HADashboard.
- [TasmoAdmin](https://github.com/hassio-addons/addon-tasmoadmin) - Centrally manage all your Sonoff-Tasmota devices.
- [Aircast](https://github.com/hassio-addons/addon-aircast) - AirPlay capabilities for your Chromecast players.
- [AirSonos](https://github.com/hassio-addons/addon-airsonos) - AirPlay capabilities for your Sonos players.
- [Dropbox Sync](https://github.com/danielwelch/hassio-dropbox-sync) - Upload your backup snapshots to Dropbox.
- [Log Viewer](https://github.com/hassio-addons/addon-log-viewer) - Browser-based live log viewing utility.
- [Tautulli](https://github.com/hassio-addons/addon-tautulli) - Monitor and get statistics from your Plex server.
- [motionEye](https://github.com/hassio-addons/addon-motioneye) - Simple, elegant and feature-rich CCTV/NVR for your cameras.
- [JupyterLab Lite](https://github.com/hassio-addons/addon-jupyterlab-lite) - Create documents containing live code, equations, visualizations, and explanatory text.
- [Backup to Google Drive](https://github.com/samccauley/addon-hassiogooglebackup) - Backup snapshots to Google Drive.
- [ADB](https://github.com/hassio-addons/addon-adb) - The Android Debug Bridge server program.
- [Glances](https://github.com/hassio-addons/addon-glances) - A cross-platform system monitoring tool written in Python.
- [Matrix](https://github.com/hassio-addons/addon-matrix) - A secure and decentralized communication platform.
- [AdGuard Home](https://github.com/hassio-addons/addon-adguard-home) - A network-wide ad-and-tracker blocking DNS server with parental control.
- [Traccar](https://github.com/hassio-addons/addon-traccar) - Traccar is modern GPS Tracking Platform.
- [Home Panel](https://github.com/hassio-addons/addon-home-panel) - A touch-compatible web frontend for controlling the home.
- [Hass.io Google Drive Backup](https://github.com/sabeechen/hassio-google-drive-backup) - A complete and easy to configure solution for backing up your snapshots to Google Drive.
- [Grocy](https://github.com/hassio-addons/addon-grocy) - ERP beyond your fridge! A groceries & household management solution for your home.

## Lovelace User Interface

_The Home Assistant frontend is already pretty, but you can customize it to
fit your needs or taste better._

- [Lovelace UI Documentation](https://www.home-assistant.io/lovelace) - The official documentation.
- 📺 [Getting started with Lovelace UI](https://www.youtube.com/watch?v=ObfRzMIEJPgx) - Great introduction to Lovelace UI by DrZzs.
- [Share the Love](https://sharethelove.io) - Custom card demos and configuration examples for Lovelace.
- 📺 [How to set up Lovelace](https://www.youtube.com/watch?v=n5xMtONydEo) - Excellent step by step video for beginners by JuanMTech.
- [Font Awesome Icons](https://github.com/thomasloven/hass-fontawesome) - Use the free icons from Font Awesome in your frontend.

### Themes

_It is all about the looks, apply some style._

- 📺 [Themes Tutorial](https://www.youtube.com/watch?v=h1h8FFy9_Co) - Quick tutorial/example on how to configure themes.
- [Midnight](https://community.home-assistant.io/t/midnight-theme/28598?u=frenck) - A dark theme by Marcel Hoffs.
- [Dark Cyan](https://community.home-assistant.io/t/dark-cyan-theme/28594?u=frenck) - A dark theme with cyan accents by Ryoen Deprouw.
- [Grey Night](https://community.home-assistant.io/t/grey-night-theme/30848?u=frenck) - A dark theme with grey accents by ksya.
- [Dark Red](https://community.home-assistant.io/t/dark-red-theme/28592?u=frenck) - A dark theme with red accents by Ryoen Deprouw.
- [Halloween](https://community.home-assistant.io/t/halloween-theme/30872?u=frenck) - Pumpkins colored by Mahasri Kalavala.
- [Black and Green](https://community.home-assistant.io/t/black-and-green-theme/28602?u=frenck) - A dark theme with pale green accents by GreenTurtwig.
- [Vintage](https://community.home-assistant.io/t/vintage-theme/42806?u=frenck) - Give your frontend a vintage look with this theme by Anup Surendran.
- [Carbon Green](https://community.home-assistant.io/t/share-your-themes/22018/95?u=frenck) - Light carbon theme with green accents by Reua.
- [20 Great Themes](https://www.juanmtech.com/themes-in-home-assistant/) - 20 Great themes by JuanMTech (includes a guide).
- [Many Themes, One Repo](https://github.com/maartenpaauw/home-assistant-community-themes/) - 13 Themes in a convenient ZIP file.
- [Slate](https://github.com/seangreen2/slate_theme) - A dark theme close to the vanila looks from seangreen2.
- [Synthwave](https://github.com/bbbenji/synthwave-hass) - A theme influenced by the cover artwork of modern Synthwave bands.
- [Google Home Theme](https://github.com/liri/lovelace-themes) - Two themes (light and dark) matching the design of Google Home Hub.

### Custom Lovelace UI Cards

_Lovelace allows people to build custom cards on top of it, which you can
easily add to your instance._

- [Auto-Entities Card](https://github.com/thomasloven/lovelace-auto-entities) - Dynamically adds entities: 🔮 Magic.
- [Canvas Gauge Card](https://github.com/custom-cards/canvas-gauge-card) - Use awesome gauges from canvas-gauges.com.
- [Big Number Card](https://github.com/custom-cards/bignumber-card) - Display big numbers for sensors, including severity level as background.
- [Animated Weather Card](https://github.com/bramkragten/weather-card) - Nice looking card showing the weather, with subtle animations.
- [Thermostat Card](https://github.com/ciotlosm/custom-lovelace/tree/master/thermostat-card) - Thermostat control card that looks like a Nest Thermostat.
- [Mini Media Player](https://github.com/kalkih/mini-media-player) - A minimalistic media player card.
- [Mini Graph Card](https://github.com/kalkih/mini-graph-card) - A minimalistic sensor graph card.
- [Button card](https://github.com/kuuji/button-card) - Button card for your entities.
- [Slideshow card](https://github.com/zsarnett/slideshow-card) - Dynamic slideshow of images or cards.
- [Swiper card](https://community.home-assistant.io/t/lovelace-swiper-card/72447?u=frenck) - Flick/swipe through multiple cards.
- [Slider Entity Row](https://github.com/thomasloven/lovelace-slider-entity-row) - Add a slider to adjust, e.g., the brightness of lights in lovelace entity cards.
- [Power Wheel Card](https://github.com/gurbyz/power-wheel-card) - An intuitive way to represent the power that your home is consuming or producing.
- [Simple Thermostat](https://github.com/nervetattoo/simple-thermostat) - A simpler and more flexible thermostat card.
- [Compact Custom Header](https://github.com/maykar/compact-custom-header) - Customize and compact the frontend header bar.
- [Card Modder](https://github.com/thomasloven/lovelace-card-modder) - Style your Lovelace cards.
- [Bar Card](https://github.com/Gluwc/bar-card) - Customizable animated bar card.
- [forked-daapd Card](https://github.com/kalkih/forked-daapd-card) - Control a forked daapd instance.
- [Dual Gauge Card](https://github.com/Rocka84/dual-gauge-card) - Shows two gauges in one.
- [Atomic Calendar Card](https://github.com/atomic7777/atomic_calendar) - Calendar card with advanced settings.
- [Xiaomi Vacuum Card](https://github.com/benct/lovelace-xiaomi-vacuum-card) - Detailed card for Xiaomi vacuum cleaners (and others).
- [Simple Weather Card](https://github.com/kalkih/simple-weather-card) - A minimalistic weather card, inspired by Google Material Design.
- [Lovelace Floorplan](https://github.com/pkozul/lovelace-floorplan) - Interaction with your entities from a Floorplan.
- [Home Card](https://github.com/postlund/home-card) - A quick glance of the state of your home.
- [Banner Card](https://github.com/nervetattoo/banner-card) - A fluffy linkable banner with interactive glances to spice up your home dashboards.
- [Upcoming Media Card](https://github.com/custom-cards/upcoming-media-card) - Display upcoming episodes and movies from services like: Plex, Kodi, Radarr, Sonarr, and Trakt.
- [Spotify Card](https://github.com/custom-cards/spotify-card) - List and select from current available devices and users top playlists on Spotify.
- [Battery Entity](https://github.com/cbulock/lovelace-battery-entity) - Displaying battery levels for battery entities.
- [Multiple Entity Row](https://github.com/benct/lovelace-multiple-entity-row) - Show multiple entity states or attributes on entity rows.
- [Toggle Lock Entity Row](https://github.com/thomasloven/lovelace-toggle-lock-entity-row) - Display a toggle with a lock, avoiding toggling it by mistake.
- [Xiaomi Vacuum Map Card](https://github.com/PiotrMachowski/Home-Assistant-Lovelace-Xiaomi-Vacuum-Map-card) - Interactive Xiaomi Vacuum map, just like in Mi Home app.
- [Home Feed Card](https://github.com/gadgetchnnel/lovelace-home-feed-card) - Display a combination of persistent notifications, calendar events, and entities in the style of a feed.
- [Config Template Card](https://github.com/custom-cards/config-template-card) - Allow using templates in Lovelace.
- [RGB Light Card](https://github.com/bokub/rgb-light-card) - Colorful buttons to control your RGB Lights.
- [LG WebOS Remote Control](https://github.com/madmicio/LG-WebOS-Remote-Control) - Remote Control for LG TV WebOS.
- [Restriction Card](https://github.com/iantrich/restriction-card) - A card to provide restrictions on Lovelace cards defined within.

### Alternative Dashboards

- [TileBoard](https://github.com/resoai/TileBoard) - A simple yet highly configurable Dashboard.

## Custom Components

_Additional components for Home Assistant, that were created by the community._

- [Hue Sensors](https://github.com/robmarkcole/Hue-sensors-HASS) - Enables the use of Philips Hue sensors.
- [Google Geocode](https://github.com/michaelmcarthur/GoogleGeocode-HASS) - Converts a device tracker location into a human-readable address.
- [Lutron Caseta Pro](https://github.com/upsert/lutron-caseta-pro) - Integrates Lutron Caseta Smart Bridge PRO / RA2 Select.
- [SmartIR](https://github.com/smartHomeHub/SmartIR) - Integrates devices using Broadlink IR.
- [Xiaomi Hygrothermo](https://github.com/dolezsa/Xiaomi_Hygrothermo) - Sensor platform for Xiaomi Mijia BT Hygrothermo temperature and humidity sensor.
- [Volkswagen Carnet](https://github.com/robinostlund/homeassistant-volkswagencarnet) - Integrates Volkswagen Carnet (requires valid Carnet subscription).
- [Untappd](https://github.com/custom-components/sensor.untapped) - Connects with your Untappd account.
- [Elasticsearch](https://github.com/legrego/homeassistant-elasticsearch) - Publishes events to Elasticsearch.
- [Sonoff/eWeLink](https://github.com/peterbuga/HASS-sonoff-ewelink) - Control Sonoff/eWeLink smart devices using the stock firmware.
- [Alexa Media Player](https://github.com/keatontaylor/alexa_media_player) - Allow control of Amazon Alexa devices.
- [iCloud3](https://github.com/gcobb321/icloud3) - Improved version of the iCloud device tracker component with a lot of capabilities.
- [HACS](https://hacs.netlify.com/) - This is a manager for your custom integration (components) and plugin (lovelace elements) needs.
- [breaking_changes](https://github.com/custom-components/breaking_changes) - Component to show potential breaking_changes in the current published version based on your loaded components.
- [Circadian Lighting](https://github.com/claytonjn/hass-circadian_lighting) - Circadian Lighting slowly synchronizes your color changing lights with the regular naturally occuring color temperature of the sky throughout the day.
- [HASS Aarlo](https://github.com/twrecked/hass-aarlo) - Asynchronous Arlo integration. Similar to the Arlo web site; monitors events and states for all base stations, cameras and doorbells.

## DIY

_Do It Yourself; rather than buying home automation hardware or solutions, you
could also build them yourself!_

- [ESPHome](https://esphome.io/) - Program ESP8266 boards and ESP32 boards using YAML.
- [Magic Cards](https://github.com/maddox/magic-cards) - RFID scannable cards that you can program to do anything.
- [Sonoff Tasmota](https://github.com/arendst/Sonoff-Tasmota) - Firmware for ESP8266 boards and devices.

### DIY Gateways

- [OpenMQTTGateway](https://github.com/1technophile/OpenMQTTGateway) - A flexible MQTT gateway for IR, RF, BLE, MiFlora, SMS, and many sensors.
- [esp8266 Milight Hub](https://github.com/sidoh/esp8266_milight_hub) - Alternative hub for Milight/LimitlessLED devices that uses MQTT.
- [zigbee2mqtt](https://github.com/Koenkk/zigbee2mqtt) - Zigbee to MQTT bridge, get rid of your proprietary Zigbee bridges.

### DIY Projects

- [HA SwitchPlate](https://community.home-assistant.io/t/ha-switchplate-diy-lcd-touchscreen-wall-switch-replacement/25464?u=frenck) - LCD Touchscreen wall switch replacement.
- 📺 [DIY Multisensor](https://www.youtube.com/watch?v=jpjfVc-9IrQ) - $15, Temperature, Humidity, Light, Motion, and RGB LED, without soldering.
- [$10 WiFi RGB Bulb](https://community.home-assistant.io/t/how-to-inexpensive-10-us-wifi-rgb-bulb-that-works-with-home-assistant/14735?u=frenck) - In inexpensive RGB bulb that works on WiFi.
- [433mhz/IR Bidirectional Gateway](https://community.home-assistant.io/t/433mhz-infrared-ir-to-and-from-mqtt-on-esp8266/6779?u=frenck) - Bidirectional with IR and 433mhz using ESP8266 and MQTT.
- [esp8266MQTTBlinds](https://community.home-assistant.io/t/esp8266-window-blinds-mqtt/14863?u=frenck) - Automate your window blinds using an ESP8266, a servo and MQTT.
- [Home Assistant's Hackster.io](https://www.hackster.io/home-assistant?f=1#_=_) - A Hackster channel with multiple DIY projects.
- [ESP MQTT Digital LEDs](https://github.com/bruhautomation/ESP-MQTT-JSON-Digital-LEDs) - WS2811 LED Stripe for the JSON Light Component from BRUH.
- [Bed Presence Detection](https://selfhostedhome.com/diy-bed-presence-detection-home-assistant/) - ESP8266 based Bed Presence Detection.
- [NFC Scanner](https://github.com/klaasnicolaas/ha_nfc_scanner) - Build an NFC tag/card scanner with an ESP8266, PN532 and MQTT.
- [ESP32-Cam Facebox](https://www.dopebuild.com/i-am-sorry-dave-i-am-unable-to-do-that/) - Tie a ESP32-CAM, HA, and Facebox together for a cheap Facial Recog / Home monitoring solution.
- [RaspiPool](https://github.com/segalion/raspipool) - A cost-effective, easy-to-build, easy-to-use "Swimming-Pool Automation System".
- [QuinLED](https://quinled.info/) - DIY Wi-Fi LED dimmers and controllers using ESP32 boards.

## Online Resources

_Links to various users of Home Assistant that regularly publish Home Assistant focussed content._

### Blogs

- [DIY Futurism](https://diyfuturism.com/) - Brad posts articles with great instructions for new users.
- [Phil Hawthorne](https://philhawthorne.com/homeautomation) - Co-host of the Home Assistant Podcast.
- [Smart Home Hobby](https://smarthomehobby.com/) - Features budget friendly guides and information.
- [Self Hosted Home](https://selfhostedhome.com/) - Articles on DIY home automation projects and self hosted services.
- [Tinkering with Home Automation](https://blog.ceard.tech/) - Tinkerer's blog and guides.
- [HomeTechHacker](https://HomeTechHacker.com) - DIY Smarthome guides, reviews, and advice.
- [Intermittent Technology](https://blog.quindorian.org) - Quindor's personal blog for pasting random (mostly technology related) things.

### YouTube Channels

_Sit back, relax, watch, and learn._

- [BRUH](https://www.youtube.com/channel/UCLecVrux63S6aYiErxdiy4w) - Ben has great tutorials for getting started, unfortunately, inactive lately.
- [BurnsHA](https://www.youtube.com/channel/UCSKQutOXuNLvFetrKuwudpg) - Great informational and tutorial videos.
- [DrZzs](https://www.youtube.com/channel/UC7G4tLa4Kt6A9e3hJ-HO8ng) - Great how-to videos and also streams live.
- [The Hook Up](https://www.youtube.com/channel/UC2gyzKcHbYfqoXA5xbyGXtQ) - Tutorials and more, also has videos on home automation in general.
- [HASSCASTS](https://www.youtube.com/channel/UCGOCeqMJnLvr-5C-ypUw7IQ) - Tips, Tricks & Tutorials, moving to mainly live streams.
- [JuanMTech](https://www.youtube.com/juanmtech) - Easy to follow how-to videos, product reviews and more.
- [vCloudInfo](https://www.youtube.com/vCloudInfo) - Publishes videos based on his home and GitHub repository.
- [digiblurDIY](https://www.youtube.com/channel/UC5ZdPKE2ckcBhljTc2R_qNA) - Tutorials on hardware projects and Tasmota automations.
- [Intermit.Tech](https://www.youtube.com/channel/UCv7UOhZ2XuPwm9SN5oJsCjA) - Tutorials & reviews: Camera's, Home Networking, ESP8266 boards, Node-RED.
- [BeardedTinker](https://www.youtube.com/channel/UCuqokNoK8ZFNQdXxvlE129g) - Tutorials & 3D printing.

### Podcasts

_Get inspired, while commuting, doing your morning routine, or at the gym!_

- [Home Assistant Podcast](https://hasspodcast.io) - Biweekly podcast with the latest news and interesting guests.

### Twitter

_Keep up with the latest news and updates, 280 characters at a time!_

- [@home_assistant](https://twitter.com/home_assistant) - Open source home automation that puts local control and privacy first.
- [@hass_devs](https://twitter.com/hass_devs) - Latest news on the development of Home Assistant for contributors.
- [@balloob](https://twitter.com/balloob) - Founder of the Home Assistant project.
- [@pvizeli](https://twitter.com/pvizeli) - Core developer and creator of the Hass.io project.
- [@frenck](https://twitter.com/frenck) - Creator of this Awesome list and maintainer of the Community Hass.io Add-ons project.
- [@ccostan](https://twitter.com/ccostan) - Blogger of all things Tech. Smart Home, #IOT & other Geeky subjects.
- [@HomeTechHacker](https://twitter.com/HomeTechHacker) - Guy friends call when #tech happens. Tweet 25-50x/week about #smarthome, #homenetwork, #cybersecurity, #Linux, #gadgets, and #life.
- [@hassioaddons](https://twitter.com/hassioaddons) - For all commmunity add-on news and updates.
- [@Dr_Zzs](https://twitter.com/Dr_Zzs) - Great how-to videos and also streams live.

## Uncategorized

_Valuable links, that don't fit in any of the above categories (yet!)._

- [Room Assistant](https://github.com/mKeRix/room-assistant) - A companion client to handle sensors in multiple rooms.
- [Home Assistant Companion](https://itunes.apple.com/us/app/home-assistant-open-source-home-automation/id1099568401?mt=8) - iPhone/iPad/iOS App to control and monitor your home remotely.
- [Mi Flora via MQTT daemon](https://github.com/ThomDietrich/miflora-mqtt-daemon) - Collect and transfer Xiaomi Mi Flora plant sensor data via MQTT.
- [hassctl](https://github.com/dale3h/hassctl) - Simple command line utility to help debug your configuration.
- [rhasspy](https://github.com/synesthesiam/rhasspy) - Toolkit for developing custom voice assistants.
- [Fully Kiosk Browser](https://www.ozerov.de/fully-kiosk-browser/) - Highly configurable Android Kiosk Browser and App Launcher.
- [Hassio Vagrant](https://github.com/hassio-addons/hassio-vagrant) - Vagrant box original created for developing add-ons.
- [AppDaemon](https://github.com/AppDaemon/appdaemon) - AppDaemon is a loosely coupled, multi-threaded, sandboxed Python execution environment for writing automation apps.
- [Developer Documentation](https://developers.home-assistant.io/) - The official developer documentation.
- [HASS Configurator](https://github.com/danielperna84/hass-configurator) - Browser-based configuration file editor.
- [HA-Dockermon](https://github.com/philhawthorne/ha-dockermon) - A Node.js service for RESTful switches to control Docker containers.
- [Python Amazon Dash](https://github.com/Nekmo/amazon-dash) - Hack your Amazon Dash to run what you want. Without welders.
- [homekit2mqtt](https://github.com/hobbyquaker/homekit2mqtt) - HomeKit to MQTT bridge.
- [Home Assistant Device Database](https://www.hadevices.com/) - Database of supported/confirmed working devices.
- [Jinja Scripts for Curious Minds](https://github.com/skalavala/mysmarthome/tree/master/jinja_helpers) - Bunch of Jinja2 scripts helping you to understand it better.
- [WallPanel](https://thanksmister.com/wallpanel-android/) - Android application for web-based dashboards and home automation platforms.
- [Ariela](https://play.google.com/store/apps/details?id=com.surodev.ariela) - Freemium Android client application with widget support.
- [Gitlab CI/CD](https://about.gitlab.com/2018/08/02/using-the-gitlab-ci-slash-cd-for-smart-home-configuration-management/) - How to simplify your smart home configuration with GitLab CI/CD.
- [Monitor](https://github.com/andrewjfreyer/monitor) - Distributed advertisement-based BTLE presence detection reported via MQTT.
- [HASS-data-detective](https://github.com/robmarkcole/HASS-data-detective) - Explore and analyse your database data.
- [ADB Intents](https://gist.github.com/mcfrojd/9e6875e1db5c089b1e3ddeb7dba0f304) - List of ADB intents to control Android Devices.
- [Home Assistant Config Helper for VSCode](https://marketplace.visualstudio.com/items?itemName=keesschollaart.vscode-home-assistant) - Visual Studio Code Extension that provides auto-completion, config validation and snippets when editting your configuration.

## Alternative Home Automation Software

_Home Assistant isn't the only home automation framework out there, here
are some alternatives._

- [openHAB](https://github.com/openhab) - Java-based and aims at being a universal integration platform.
- [Domoticz](https://github.com/domoticz/domoticz) - A lightweight Home Automation System.
- [Gladys](https://github.com/GladysProject/Gladys) - Open source program which runs on your Raspberry Pi.
- [SmartThings](https://www.smartthings.com/) - Commercial home automation hub by Samsung.

## Other Awesome Lists

_Other amazingly awesome lists that can be found on the great and dangerous
interwebs._

- [awesome-smarthome](https://github.com/pfalcon/awesome-smarthome) - Curated list of awesome SmartHome/Home Automation things.
- [awesome-iot](https://github.com/HQarroum/awesome-iot) - Curated list of awesome Internet of Things projects and resources.
- [awesome-open-iot](https://github.com/Agile-IoT/awesome-open-iot) - Curated list of open source IoT frameworks, libraries and software.
- [awesome-amazon-alexa](https://github.com/miguelmota/awesome-amazon-alexa#readme) - Curated list of awesome resources for the Amazon Alexa platform.
- [awesome-mqtt](https://github.com/hobbyquaker/awesome-mqtt#readme) - Curated list of MQTT related stuff.
- [awesome-sefhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) - Curated list of awesome self hosted software.

## Contributing

This awesome list is an active open-source project and is always open to
people who want to contribute to it. We have set up a separate document
containing our [Contribution Guidelines](https://github.com/frenck/awesome-home-assistant/blob/master/CONTRIBUTING.md).

The original setup of this awesome list is by [Franck Nijhof](https://twitter.com/frenck).

For a full list of all authors and contributors, check the
[contributor's page](https://github.com/frenck/awesome-home-assistant/graphs/contributors).

Thank you for being involved! 😍

## Trademark Legal Notice

This Awesome list is not created, developed, affiliated, supported, maintained
or endorsed by Home Assistant.

All product names, logos, brands, trademarks and registered trademarks are
property of their respective owners. All company, product, and service names
used in this list are for identification purposes only.

Use of these names, logos, trademarks, and brands does not imply endorsement.

## License

Distributed under the Creative Commons Attribution 4.0 license.
See [LICENSE](https://github.com/frenck/awesome-home-assistant/blob/master/LICENSE.md) for
the complete license.
