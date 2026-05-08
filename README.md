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
Additional software, tutorials, custom integrations, apps,
custom dashboard cards & plugins, cookbooks, example setups, and much more.

Most of the items below can be installed in one click through
[HACS](https://hacs.xyz), the Home Assistant Community Store, after you
install Home Assistant itself. Home Assistant is owned by the
[Open Home Foundation](https://www.openhomefoundation.org), which also
stewards ESPHome, Music Assistant, Z-Wave JS, and the open voice tools you
will see throughout the list. If you are buying smart-home devices, the
[Works with Home Assistant](https://works-with.home-assistant.io) program
tests for privacy, local control, and long-term support.

The list is divided into categories. The links in those categories do not have
pre-established order; the order is for contribution. If you want to contribute,
please read the [guide](https://github.com/frenck/awesome-home-assistant/blob/main/.github/CONTRIBUTING.md)
or raise an [issue](https://github.com/frenck/awesome-home-assistant/issues/new/choose)
to suggest additions, updates or removals.

## Contents

- [How to use](#how-to-use)
- [Installing](#installing)
- [In case you need help](#in-case-you-need-help)
  - [Official Communities](#official-communities)
  - [Other Communities](#other-communities)
- [Public Configurations](#public-configurations)
- [Apps](#apps)
  - [Official Apps](#official-apps)
  - [Third Party Apps](#third-party-apps)
- [Dashboards & UI](#dashboards--ui)
  - [Icon packs](#icon-packs)
  - [Themes](#themes)
  - [Custom Cards](#custom-cards)
  - [Alternative Dashboards](#alternative-dashboards)
- [Custom Integrations](#custom-integrations)
  - [AI & LLMs](#ai--llms)
  - [Voice & media playback](#voice--media-playback)
  - [Cameras & video](#cameras--video)
  - [Vacuums](#vacuums)
  - [Climate](#climate)
  - [Lighting](#lighting)
  - [Energy & solar](#energy--solar)
  - [Bluetooth & BLE](#bluetooth--ble)
  - [Security & alarm](#security--alarm)
  - [Cars & EV charging](#cars--ev-charging)
  - [Presence & location](#presence--location)
  - [Battery monitoring](#battery-monitoring)
  - [Network & authentication](#network--authentication)
  - [Federation & multi-instance](#federation--multi-instance)
  - [Civic & household](#civic--household)
  - [Automation tooling](#automation-tooling)
  - [Vendor & brand](#vendor--brand)
  - [Logging & analytics](#logging--analytics)
- [Companion App & Mobile](#companion-app--mobile)
- [DIY](#diy)
  - [Standalone projects](#standalone-projects)
  - [DIY Gateways](#diy-gateways)
  - [DIY Projects](#diy-projects)
- [Tools & Utilities](#tools--utilities)
- [Online Resources](#online-resources)
  - [Blogs](#blogs)
  - [YouTube Channels](#youtube-channels)
  - [Podcasts](#podcasts)
  - [Social](#social)
- [Alternative Home Automation Software](#alternative-home-automation-software)
- [Other Awesome Lists](#other-awesome-lists)
- [Trademark Legal Notice](#trademark-legal-notice)

## How to use

Awesome Home Assistant is a curated list of the best resources for Home
Assistant, the open-source home automation that runs on your own hardware
and keeps your data local. Use it to find the apps, custom cards, custom
integrations, and tutorials that experienced users actually rely on.

You can navigate through the list by:

- Simply press <kbd>command/ctrl</kbd> + <kbd>F</kbd> to search for a keyword
- Go through our [_Contents list_](#contents)
- Alternatively, use the search on our website: <https://www.awesome-ha.com>

## Installing

New to Home Assistant and not sure where to start? The easiest path is to
grab a [Home Assistant Green](https://www.home-assistant.io/green/) and plug
it in. If you would rather use hardware you already own (a Raspberry Pi, a
Mini PC, an old laptop), the official guides below cover every option.
Whichever you pick, you end up running the same Home Assistant. Once it is
up, install [HACS](https://hacs.xyz) and most of the items in this list
become one click away.

- [Home Assistant Installation](https://www.home-assistant.io/installation/) - The official installation guides.
- [Compare Installation Methods](https://www.home-assistant.io/installation/#compare-installation-methods) - The available installation methods compared.

## In case you need help

Stuck on a configuration, wondering why a device will not pair, or just want
to see what other people are building? Home Assistant has one of the most
active home-automation communities on the internet, and most of it is free
to join.

### Official Communities

- [Home Assistant Discord](https://discordapp.com/invite/c5DvZ4e) - Join the chat, most of us are there.
- [Home Assistant Community](https://community.home-assistant.io/?u=frenck) - The discussion forum, also used for feature requests.
- [Home Assistant Subreddit](https://www.reddit.com/r/homeassistant/) - If you are into Reddit, subscribe.
- [Home Assistant Facebook Group](https://www.facebook.com/groups/HomeAssistant/) - Facebook group for enthusiasts.

### Other Communities

- [Dr. ZZs](https://www.facebook.com/groups/1969622823351838/) - Facebook group by Dr. Zzs.
- [ESPHome Discord](https://discord.gg/KhAMKrd) - Get support for your DIY ESPHome project.
- 🇳🇱 [Dutch Domotics Discord](https://discord.gg/Ee5X7T7) - Dutch Discord server with home automation enthusiasts.

## Public Configurations

_Wondering how more experienced users have set up their thermostat schedules, presence detection, or automations? These are full Home Assistant configurations published on GitHub. Read them like recipe books, copy the bits that look useful, and skip the rest._

- [Carlo Costanzo](https://github.com/CCOSTAN/Home-AssistantConfig#logo) - Probably the most documented configuration out there (5,147★).
- [DubhAd](https://github.com/DubhAd/Home-AssistantConfig) - Also known as Tinkerer shares his configuration files (686★).
- [geekofweek](https://github.com/geekofweek/homeassistant) - Has over 300+ automations (1,472★).
- [Alok Saboo](https://github.com/arsaboo/homeassistant-config) - Also known as arsaboo. Regularly updated (1,953★).
- [Franck Nijhof](https://github.com/frenck/home-assistant-config) - Hass.io based, very different configuration structure compared to others (1,999★).
- [Klaas Schoute](https://github.com/klaasnicolaas/Student-homeassistant-config) - Hass.io based, Intel NUC, Ubuntu Server, Docker and regularly updated (223★).

## Apps

_Need a database, a reverse proxy, an MQTT broker (the messaging service many smart-home devices use), or another tool running alongside Home Assistant? Apps, formerly called Add-ons, let you install them straight into Home Assistant OS. No Docker, no separate server, no command line required._

### Official Apps

_Created and maintained by the Home Assistant team._

- [DuckDNS](https://github.com/home-assistant/hassio-addons/blob/master/duckdns/DOCS.md) - Updates your Duck DNS IP address and generate SSL using Let's Encrypt.
- [File editor](https://github.com/home-assistant/hassio-addons/blob/master/configurator/DOCS.md) - Browser-based configuration file editor.
- [Mosquitto](https://github.com/home-assistant/hassio-addons/blob/master/mosquitto/DOCS.md) - Fast and reliable MQTT broker.
- [Terminal & SSH](https://github.com/home-assistant/hassio-addons/blob/master/ssh/DOCS.md) - Allows logging in remotely to using a web terminal or SSH client.
- [Samba](https://github.com/home-assistant/hassio-addons/blob/master/samba/DOCS.md) - Access your configuration files using Windows network shares.
- [NGINX SSL proxy](https://github.com/home-assistant/hassio-addons/blob/master/nginx_proxy/DOCS.md) - Reverse proxy with SSL termination.
- [deCONZ](https://github.com/home-assistant/hassio-addons/blob/master/deconz/DOCS.md) - Control a ZigBee network using ConBee or RaspBee hardware by Dresden Elektronik.
- [Let's Encrypt](https://github.com/home-assistant/hassio-addons/blob/master/letsencrypt/DOCS.md) - Get a free SSL certificate from Let's Encrypt; an open and automated certificate authority (CA).
- [MariaDB](https://github.com/home-assistant/hassio-addons/blob/master/mariadb/DOCS.md) - An open source relational database (fork of MySQL).

### Third Party Apps

_Anyone can create an app, the following are created by the community._

- [SSH & Web Terminal](https://github.com/hassio-addons/app-ssh) - SSH and Web-based terminal with tons of pre-loaded useful tools (494★).
- [UniFi Controller](https://github.com/hassio-addons/app-unifi) - The UniFi Controller allows you to manage your UniFi network using a web browser (367★).
- [Node-RED](https://github.com/hassio-addons/app-node-red) - Flow-based programming for the Internet of Things (635★).
- [Plex Media Server](https://github.com/hassio-addons/app-plex) - Your recorded media beautifully organized and ready to stream (187★).
- [InfluxDB](https://github.com/hassio-addons/addon-influxdb) - Scalable datastore for metrics, events, and real-time analytics (194★).
- [Grafana](https://github.com/hassio-addons/addon-grafana) - Open platform for beautiful analytics and monitoring (275★).
- [Tor](https://github.com/hassio-addons/app-tor) - Protect your privacy and access your instance via Tor (62★).
- [Spotify Connect](https://github.com/hassio-addons/app-spotify-connect) - Stream music from Spotify directly to your Home Assistant device (252★).
- [zigbee2mqtt](https://github.com/Koenkk/zigbee2mqtt) - Zigbee to MQTT bridge, get rid of your proprietary Zigbee bridges (15,106★).
- [AppDaemon](https://github.com/AppDaemon/appdaemon) - A loosely coupled, multi-threaded, sandboxed Python execution environment for writing automation apps (955★).
- [TasmoAdmin](https://github.com/hassio-addons/addon-tasmoadmin) - Centrally manage all your Sonoff-Tasmota devices (253★).
- [Aircast](https://github.com/hassio-addons/app-aircast) - AirPlay capabilities for your Chromecast players (394★).
- [AirSonos](https://github.com/hassio-addons/app-airsonos) - AirPlay capabilities for your Sonos players (120★).
- [Log Viewer](https://github.com/hassio-addons/addon-log-viewer) - Browser-based live log viewing utility (94★).
- [Tautulli](https://github.com/hassio-addons/addon-tautulli) - Monitor and get statistics from your Plex server (46★).
- [motionEye](https://github.com/hassio-addons/addon-motioneye) - Simple, elegant and feature-rich CCTV/NVR for your cameras (331★).
- [JupyterLab](https://github.com/hassio-addons/addon-jupyterlab) - Create documents containing live code, equations, visualizations, and explanatory text (68★).
- [Glances](https://github.com/hassio-addons/app-glances) - A cross-platform system monitoring tool written in Python (184★).
- [AdGuard Home](https://github.com/hassio-addons/app-adguard-home) - A network-wide ad-and-tracker blocking DNS server with parental control (511★).
- [Traccar](https://github.com/hassio-addons/addon-traccar) - Modern GPS tracking platform (158★).
- [Hass.io Google Drive Backup](https://github.com/sabeechen/hassio-google-drive-backup) - A complete and easy to configure solution for backing up your snapshots to Google Drive (3,537★).
- [Grocy](https://github.com/hassio-addons/app-grocy) - ERP beyond your fridge! A groceries & household management solution for your home (429★).
- [CrowdSec](https://github.com/crowdsecurity/home-assistant-addons) - A next-gen collaborative IPS/IDS to protect you from intrusion (94★).

## Dashboards & UI

_The dashboards Home Assistant ships with are good, but if you have spent any time on Reddit you have seen the gorgeous setups people build. The cards, themes, and icons below are how they get there. Mix and match to your taste._

### Icon packs

- [Font Awesome Icons](https://github.com/thomasloven/hass-fontawesome) - Use the free icons from Font Awesome in your frontend (338★).
- [Hass Hue Icons](https://github.com/arallsopp/hass-hue-icons) - Additional Philips Hue bulbs and fixtures icons (376★).
- [simpleicons](https://github.com/vigonotion/hass-simpleicons) - Use the free icons from the simpleicons set (166★).

### Themes

_It is all about the looks, apply some style._

- [Midnight](https://community.home-assistant.io/t/midnight-theme/28598?u=frenck) - A dark theme by Marcel Hoffs.
- [Dark Cyan](https://community.home-assistant.io/t/dark-cyan-theme/28594?u=frenck) - A dark theme with cyan accents by Ryoen Deprouw.
- [Grey Night](https://community.home-assistant.io/t/grey-night-theme/30848?u=frenck) - A dark theme with grey accents by ksya.
- [Dark Red](https://community.home-assistant.io/t/dark-red-theme/28592?u=frenck) - A dark theme with red accents by Ryoen Deprouw.
- [Halloween](https://community.home-assistant.io/t/halloween-theme/30872?u=frenck) - Pumpkins colored by Mahasri Kalavala.
- [Black and Green](https://community.home-assistant.io/t/black-and-green-theme/28602?u=frenck) - A dark theme with pale green accents by GreenTurtwig.
- [Vintage](https://community.home-assistant.io/t/vintage-theme/42806?u=frenck) - Give your frontend a vintage look with this theme by Anup Surendran.
- [Carbon Green](https://community.home-assistant.io/t/share-your-themes/22018/95?u=frenck) - Light carbon theme with green accents by Reua.
- [Slate](https://github.com/seangreen2/slate_theme) - A dark theme close to the vanila looks from seangreen2 (136★).
- [Synthwave](https://github.com/bbbenji/synthwave-hass) - A theme influenced by the cover artwork of modern Synthwave bands (199★).

### Custom Cards

_Lovelace plugins that drop into your dashboard. Grouped roughly by what they do._

#### Dashboard frameworks

_Full card collections that change the look and feel of your dashboards. Mushroom, Bubble Card, Floorplan, and similar all-in-one toolkits._

- [Suggest one](https://github.com/frenck/awesome-home-assistant/issues/new/choose) - Have a community resource that fits here? Open an issue to propose it.

#### Layout helpers

_Cards that change where and how other cards appear: stack, fold, show conditionally, restyle, or template._

- [Auto-Entities Card](https://github.com/thomasloven/lovelace-auto-entities) - Dynamically adds entities: 🔮 Magic (1,747★).
- [Card Modder](https://github.com/thomasloven/lovelace-card-mod) - Style your Lovelace cards (1,692★).
- [Restriction Card](https://github.com/iantrich/restriction-card) - A card to provide restrictions on Lovelace cards defined within (316★).
- [Config Template Card](https://github.com/iantrich/config-template-card) - Allow using templates in Lovelace (547★).
- [Button card](https://github.com/custom-cards/button-card) - Highly customizable button for your entities (2,432★).

#### Charts & graphs

_Visualise sensor data over time. Gauges, line graphs, bars, and Sankey diagrams._

- [Mini Graph Card](https://github.com/kalkih/mini-graph-card) - A minimalistic sensor graph card (3,810★).
- [Canvas Gauge Card](https://github.com/custom-cards/canvas-gauge-card) - Use awesome gauges from canvas-gauges.com (216★).
- [Dual Gauge Card](https://github.com/custom-cards/dual-gauge-card) - Shows two gauges in one (220★).

#### Status & info rows

_Compact rows that pack more information into entity-card style listings._

- [Slider Entity Row](https://github.com/thomasloven/lovelace-slider-entity-row) - Add a slider to adjust, e.g., the brightness of lights in lovelace entity cards (906★).

#### Climate cards

_Replacement thermostat cards with a different look or feel._

- [Thermostat Card](https://github.com/ciotlosm/lovelace-thermostat-dark-card) - Thermostat control card that looks like a Nest Thermostat (744★).
- [Simple Thermostat](https://github.com/nervetattoo/simple-thermostat) - A simpler and more flexible thermostat card (807★).

#### Energy cards

_Visualise solar production, grid imports, battery state, and consumption flow._


#### Media cards

_Better ways to control media players, with album art, queues, and per-room presence._

- [Mini Media Player](https://github.com/kalkih/mini-media-player) - A minimalistic media player card (1,698★).

#### Vacuum cards

_Show vacuum status, room maps, and start/stop controls in your dashboard._

- [Vacuum Map Card](https://github.com/PiotrMachowski/lovelace-xiaomi-vacuum-map-card) - This card provides a user-friendly way to fully control Xiaomi (Roborock/Viomi/Dreame/Roidmi) and Neato (+ possibly other) vacuums (1,863★).
- [Vacuum Card](https://github.com/denysdovhan/vacuum-card) - A card to card for controlling a vacuum cleaner robot (1,199★).

#### Calendar & feed

_Calendar views and rolling feeds of upcoming events._

- [Atomic Calendar Revive](https://github.com/totaldebug/atomic-calendar-revive) - Calendar card with advanced settings (611★).

#### Weather cards

_Weather widgets with the look you actually want._


#### Lighting cards

_Specialised controls for lights, color temperature, and effects._

- [RGB Light Card](https://github.com/bokub/rgb-light-card) - Colorful buttons to control your RGB Lights (558★).

#### Air quality

_Display readings from purifiers and air-quality sensors._

- [Purifier Card](https://github.com/denysdovhan/purifier-card) - A card for controlling air purifiers (339★).

#### Remote control

_Virtual remotes for TVs, streamers, and AV gear._

- [LG WebOS Remote Control](https://github.com/madmicio/LG-WebOS-Remote-Control) - Remote Control for LG TV WebOS (547★).

#### Camera cards

_Display camera streams the way you want them, with overlays, controls, event timelines, and pop-out viewers._

- [Suggest one](https://github.com/frenck/awesome-home-assistant/issues/new/choose) - Have a community resource that fits here? Open an issue to propose it.

#### Iconography

_Custom icon packs that go beyond the default Material Design icons. Brand logos, product silhouettes, and themed sets._

- [Suggest one](https://github.com/frenck/awesome-home-assistant/issues/new/choose) - Have a community resource that fits here? Open an issue to propose it.

#### Kiosk & wallpanel

_Hide the chrome, run full-screen, or turn an old tablet on the wall into a dedicated touch panel._

- [Suggest one](https://github.com/frenck/awesome-home-assistant/issues/new/choose) - Have a community resource that fits here? Open an issue to propose it.

### Alternative Dashboards

- [Dwains Dashboard](https://github.com/dwainscheeren/dwains-lovelace-dashboard) - An fully auto-generating dashboard for desktop, tablet and mobile (2,033★).
- [Mushroom Strategy](https://github.com/DigiLive/mushroom-strategy) - A strategy that automatically generates a dashboard using Mushroom cards (640★).

## Custom Integrations

_Integrations Home Assistant does not ship with out of the box, written by the community. Install them through HACS in a couple of clicks._

### AI & LLMs

_Wire Home Assistant up to a large language model and let it read your devices, build dashboards, write automations, or describe what your cameras see._

- [Suggest one](https://github.com/frenck/awesome-home-assistant/issues/new/choose) - Have a community resource that fits here? Open an issue to propose it.

### Voice & media playback

_Send commands to voice speakers and media players, or relay what they hear and play back into Home Assistant._

- [Spotcast](https://github.com/fondberg/spotcast) - Start Spotify playback on an idle Chromecast device as well as control Spotify connect devices (807★).

### Cameras & video

_Pair specific camera brands and video sources that Home Assistant does not support out of the box._

- [HASS Aarlo](https://github.com/twrecked/hass-aarlo) - Asynchronous Arlo integration. Similar to the Arlo web site; monitors events and states for all base stations, cameras and doorbells (466★).
- [WebRTC Camera](https://github.com/AlexxIT/WebRTC) - View RTSP streams from IP Cameras in real-time through WebRTC or MSE with Pan/Zoom controls (2,104★).

### Vacuums

_Control specific robot vacuums and surface their map data, beyond what comes built in._

- [Xiaomi Cloud Map Extractor](https://github.com/PiotrMachowski/Home-Assistant-custom-components-Xiaomi-Cloud-Map-Extractor) - Presents a live view of a map for Xiaomi (Roborock/Viomi/Roidmi/Dreame) vacuums without a need for rooting (1,392★).

### Climate

_Smarter thermostats, comfort sensors, and HVAC integrations that go beyond what comes built in._

- [Suggest one](https://github.com/frenck/awesome-home-assistant/issues/new/choose) - Have a community resource that fits here? Open an issue to propose it.

### Lighting

_Effects, schedules, and behaviour layers that sit on top of your lights._

- [Circadian Lighting](https://github.com/claytonjn/hass-circadian_lighting) - Slowly synchronizes your color-changing lights with the naturally occurring color temperature of the sky throughout the day (882★).

### Energy & solar

_Pull your solar inverter, smart meter, home battery, or utility tariff into Home Assistant and feed the energy dashboard._

- [Suggest one](https://github.com/frenck/awesome-home-assistant/issues/new/choose) - Have a community resource that fits here? Open an issue to propose it.

### Bluetooth & BLE

_Pull data from sensors that broadcast over Bluetooth, or use Bluetooth itself for room-level presence detection._

- [Suggest one](https://github.com/frenck/awesome-home-assistant/issues/new/choose) - Have a community resource that fits here? Open an issue to propose it.

### Security & alarm

_Turn Home Assistant into a fully-featured alarm system with arm and disarm flows, user codes, zones, and panic._

- [Suggest one](https://github.com/frenck/awesome-home-assistant/issues/new/choose) - Have a community resource that fits here? Open an issue to propose it.

### Cars & EV charging

_Track your car's battery, location, and charging state, or control where and when it plugs in._

- [Suggest one](https://github.com/frenck/awesome-home-assistant/issues/new/choose) - Have a community resource that fits here? Open an issue to propose it.

### Presence & location

_Figure out who is home and where they are, often more accurately than the built-in device tracker._

- [iCloud3](https://github.com/gcobb321/icloud3) - Improved version of the iCloud device tracker component with a lot of capabilities (835★).

### Battery monitoring

_Keep an eye on the batteries in all your devices and get warned before they run flat._

- [Suggest one](https://github.com/frenck/awesome-home-assistant/issues/new/choose) - Have a community resource that fits here? Open an issue to propose it.

### Network & authentication

_Sign in to Home Assistant with single sign-on, route through a tunnel, or pull network hardware into your dashboard._

- [Suggest one](https://github.com/frenck/awesome-home-assistant/issues/new/choose) - Have a community resource that fits here? Open an issue to propose it.

### Federation & multi-instance

_Link multiple Home Assistant instances together, share entities across homes, or relay between them._

- [Suggest one](https://github.com/frenck/awesome-home-assistant/issues/new/choose) - Have a community resource that fits here? Open an issue to propose it.

### Civic & household

_Local services that turn into sensors and calendars: garbage collection schedules, school holidays, traffic, weather alerts, and similar._

- [Suggest one](https://github.com/frenck/awesome-home-assistant/issues/new/choose) - Have a community resource that fits here? Open an issue to propose it.

### Automation tooling

_Helpers that make automations easier to write, debug, and maintain._

- [The Watchman](https://github.com/dummylabs/thewatchman) - Keep track of missing entities and services in your config files (643★).

### Vendor & brand

_Pull a specific manufacturer's devices into Home Assistant, often with more features or better local control than what comes built in._

- [SmartIR](https://github.com/smartHomeHub/SmartIR) - Integrates devices using Broadlink IR (2,698★).
- [Sonoff LAN](https://github.com/AlexxIT/SonoffLAN) - Control Sonoff devices with eWeLink (original) firmware over LAN and/or Cloud (3,230★).

### Logging & analytics

_Send Home Assistant data to external systems for long-term storage, richer dashboards, or analysis._

- [Elasticsearch](https://github.com/legrego/homeassistant-elasticsearch) - Publishes events to Elasticsearch (164★).

## Companion App & Mobile

_The Home Assistant companion apps for iPhone and Android are how most people interact with their smart home day-to-day. They handle notifications, location-based automations, sensor data from your phone, widgets, and Apple Watch or Wear OS complications._

- [Home Assistant Companion](https://itunes.apple.com/us/app/home-assistant-open-source-home-automation/id1099568401?mt=8) - iPhone/iPad/iOS App to control and monitor your home remotely.
- [Home Assistant Taskbar Menu](https://github.com/PiotrMachowski/Home-Assistant-Taskbar-Menu) - A client for Windows that can display Lovelace views, control entities and show persistent notifications (342★).

## DIY

_Some of the best smart-home gadgets do not exist as products you can buy, but other people have figured out how to build them. The projects below cover everything from soldering your own multi-sensor to repurposing a discontinued device. Most are weekend projects with parts that cost less than a coffee run._

### Standalone projects

- [ESPHome](https://esphome.io/) - Program ESP8266 boards and ESP32 boards using YAML.
- [Tasmota](https://github.com/arendst/Tasmota) - Firmware for ESP8266 boards and devices (24,346★).

### DIY Gateways

- [OpenMQTTGateway](https://github.com/1technophile/OpenMQTTGateway) - A flexible MQTT gateway for IR, RF, BLE, MiFlora, SMS, and many sensors (4,010★).
- [esp8266 Milight Hub](https://github.com/sidoh/esp8266_milight_hub) - Alternative hub for Milight/LimitlessLED devices that uses MQTT (1,027★).

### DIY Projects

- [HA SwitchPlate](https://community.home-assistant.io/t/ha-switchplate-diy-lcd-touchscreen-wall-switch-replacement/25464?u=frenck) - LCD Touchscreen wall switch replacement.
- [$10 WiFi RGB Bulb](https://community.home-assistant.io/t/how-to-inexpensive-10-us-wifi-rgb-bulb-that-works-with-home-assistant/14735?u=frenck) - In inexpensive RGB bulb that works on WiFi.
- [433mhz/IR Bidirectional Gateway](https://community.home-assistant.io/t/433mhz-infrared-ir-to-and-from-mqtt-on-esp8266/6779?u=frenck) - Bidirectional with IR and 433mhz using ESP8266 and MQTT.
- [esp8266MQTTBlinds](https://community.home-assistant.io/t/esp8266-window-blinds-mqtt/14863?u=frenck) - Automate your window blinds using an ESP8266, a servo and MQTT.
- [Home Assistant's Hackster.io](https://www.hackster.io/home-assistant?f=1#_=_) - A Hackster channel with multiple DIY projects.
- [Bed Presence Detection](https://selfhostedhome.com/diy-bed-presence-detection-home-assistant/) - ESP8266 based Bed Presence Detection.
- [QuinLED](https://quinled.info/) - DIY Wi-Fi LED dimmers and controllers using ESP32 boards.

## Tools & Utilities

_Helpers, daemons, and developer tools that sit alongside Home Assistant rather than inside it. Useful for editing your config, debugging your data, sending device data over MQTT, or wiring HA into a wider workflow._

- [HASS Configurator](https://github.com/danielperna84/hass-configurator) - Browser-based configuration file editor (335★).
- [HA-Dockermon](https://github.com/philhawthorne/ha-dockermon) - A Node.js service for RESTful switches to control Docker containers (291★).
- [Home Assistant Device Database](https://www.hadevices.com/) - Database of supported/confirmed working devices.
- [Jinja Scripts for Curious Minds](https://github.com/skalavala/mysmarthome/tree/master/jinja_helpers) - Bunch of Jinja2 scripts helping you to understand it better.
- [GitLab CI/CD](https://about.gitlab.com/2018/08/02/using-the-gitlab-ci-slash-cd-for-smart-home-configuration-management/) - How to simplify your smart home configuration with GitLab CI/CD.
- [Monitor](https://github.com/andrewjfreyer/monitor) - Distributed advertisement-based BTLE presence detection reported via MQTT (2,101★).
- [HASS-data-detective](https://github.com/robmarkcole/HASS-data-detective) - Explore and analyse your database data (204★).
- [ADB Intents](https://gist.github.com/mcfrojd/9e6875e1db5c089b1e3ddeb7dba0f304) - List of ADB intents to control Android Devices.
- [Home Assistant Config Helper for VSCode](https://marketplace.visualstudio.com/items?itemName=keesschollaart.vscode-home-assistant) - Visual Studio Code Extension that provides auto-completion, config validation and snippets when editting your configuration.
- [Mi Flora via MQTT daemon](https://github.com/ThomDietrich/miflora-mqtt-daemon) - Collect and transfer Xiaomi Mi Flora plant sensor data via MQTT (624★).

## Online Resources

_Home Assistant has a thriving community of bloggers, YouTubers, podcasters, and people who love sharing what they have built. The folks below are some of the regular voices worth following, especially when something new ships and you want a hands-on take before deciding whether to dig in yourself._

### Blogs

- [DIY Futurism](https://diyfuturism.com/) - Brad posts articles with great instructions for new users.
- [Smart Home Hobby](https://smarthomehobby.com/) - Features budget friendly guides and information.
- [Self Hosted Home](https://selfhostedhome.com/) - Articles on DIY home automation projects and self hosted services.
- [Tinkering with Home Automation](https://blog.ceard.tech/) - Tinkerer's blog and guides.
- [HomeTechHacker](https://HomeTechHacker.com) - DIY Smarthome guides, reviews, and advice.
- [Intermittent Technology](https://blog.quindorian.org) - Quindor's personal blog for pasting random (mostly technology related) things.

### YouTube Channels

_Sit back, relax, watch, and learn._

- [Home Assistant](https://www.youtube.com/channel/UCbX3YkedQunLt7EQAdVxh7w) - Official YouTube Channel where new launches and live streams are held.
- [BurnsHA](https://www.youtube.com/channel/UCSKQutOXuNLvFetrKuwudpg) - Great informational and tutorial videos.
- [The Hook Up](https://www.youtube.com/channel/UC2gyzKcHbYfqoXA5xbyGXtQ) - Tutorials and more, also has videos on home automation in general.
- [JuanMTech](https://www.youtube.com/juanmtech) - Easy to follow how-to videos, product reviews and more.
- [vCloudInfo](https://www.youtube.com/vCloudInfo) - Publishes videos based on his home and GitHub repository.
- [digiblurDIY](https://www.youtube.com/channel/UC5ZdPKE2ckcBhljTc2R_qNA) - Tutorials on hardware projects and Tasmota automations.
- [Intermit.Tech](https://www.youtube.com/channel/UCv7UOhZ2XuPwm9SN5oJsCjA) - Tutorials & reviews: Camera's, Home Networking, ESP8266 boards, Node-RED.
- [BeardedTinker](https://www.youtube.com/channel/UCuqokNoK8ZFNQdXxvlE129g) - Tutorials & 3D printing.
- [Smart Home Junkie](https://www.youtube.com/channel/UCVtQ4AOSmCFUuvixddYiSxw/) - How-to videos and tutorials for starters and advanced users.
- [Everything Smart Home](https://www.youtube.com/c/EverythingSmartHome) - Focuses on Smart Home, Home Automation, general tech reviews, guides, and step-by-step DIY projects.

### Podcasts

_Get inspired, while commuting, doing your morning routine, or at the gym!_

- [Home Assistant Podcast](https://hasspodcast.io) - Biweekly podcast with the latest news and interesting guests.

### Social

_Follow along on social media. The list still leans on X (formerly Twitter); Bluesky and Mastodon entries land in a follow-up._

- [@home_assistant](https://twitter.com/home_assistant) - Open source home automation that puts local control and privacy first.
- [@hass_devs](https://twitter.com/hass_devs) - Latest news on the development of Home Assistant for contributors.
- [@balloob](https://twitter.com/balloob) - Founder of the Home Assistant project.
- [@pvizeli](https://twitter.com/pvizeli) - Core developer and creator of the Hass.io project.
- [@frenck](https://twitter.com/frenck) - Creator of this Awesome list and maintainer of the Home Assistant Community Apps project.
- [@ccostan](https://twitter.com/ccostan) - Blogger of all things Tech. Smart Home, #IOT & other Geeky subjects.
- [@HomeTechHacker](https://twitter.com/HomeTechHacker) - Guy friends call when #tech happens. Tweet 25-50x/week about #smarthome, #homenetwork, #cybersecurity, #Linux, #gadgets, and #life.
- [@hassioaddons](https://twitter.com/hassioaddons) - For all community app news and updates.
- [@Dr_Zzs](https://twitter.com/Dr_Zzs) - Great how-to videos and also streams live.

## Alternative Home Automation Software

_Home Assistant is not the only home-automation platform out there. If you want to compare, or if you have specific needs HA does not cover, the projects below are the most active alternatives. Some are commercial, some are open source, and a few solve very different problems._

- [openHAB](https://github.com/openhab) - Java-based and aims at being a universal integration platform.
- [Domoticz](https://github.com/domoticz/domoticz) - A lightweight Home Automation System (3,751★).
- [Gladys](https://github.com/GladysAssistant/Gladys) - Open source program which runs on your Raspberry Pi (3,054★).
- [SmartThings](https://www.smartthings.com/) - Commercial home automation hub by Samsung.

## Other Awesome Lists

_Like this list, but for adjacent topics? The lists below cover broader smart-home categories, specific protocols, and self-hosted software in general. They are good places to look when something does not fit Home Assistant directly but might solve part of your puzzle._

- [awesome-iot](https://github.com/HQarroum/awesome-iot) - Curated list of awesome Internet of Things projects and resources (3,928★).
- [awesome-mqtt](https://github.com/awesome-mqtt/awesome-mqtt#readme) - Curated list of MQTT related stuff (2,332★).
- [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) - Curated list of awesome self hosted software (290,872★).

## Contributing

This awesome list is an active open-source project and is always open to
people who want to contribute to it. We have set up a separate document
containing our [Contribution Guidelines](https://github.com/frenck/awesome-home-assistant/blob/main/.github/CONTRIBUTING.md).

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
