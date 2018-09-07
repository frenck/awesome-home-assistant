# Awesome Home Assistant

<div align="center">
  <a href="https://awesome-ha.com">
    <img width="400" src="https://www.awesome-ha.com/images/awesome-home-assistant.svg" alt="Awesome Home Assistant">
  </a>
  <br>
  <a href="https://awesome-ha.com"><strong>https://awesome-ha.com</strong></a>
  <br>
  <br>
  <a href="https://github.com/sindresorhus/awesome#readme" target="_blank">
    <img alt="Awesome" src="https://awesome.re/badge.svg">
  </a>
</div>

## About

Home Assistant is an open source home automation that puts local control and
privacy first. Powered by a worldwide community of tinkerers and DIY
enthusiasts. Perfect to run on a Raspberry Pi or a local server.

Awesome Home Assistant is a curated list of awesome
[Home Assistant](https://www.home-assistant.io) resources.
Additional software, tutorials, custom components, Hassio add-ons,
custom Lovelace panels, cookbooks, example setups, and much more.

The list is divided into categories. The links in those categories do not have
pre-established order; the order is for contribution. If you want to contribute,
please read the [guide](https://github.com/frenck/awesome-home-assistant/blob/master/CONTRIBUTING.md).

## How to Use

Awesome Home Assistant is a fantastic list for people trying to automate every
aspect of their home. Automating your home is a long, hard, and never finished
task that usually involves a lot of tinkering.

You can navigate through the list by:

- Simply press <kbd>command/ctrl</kbd> + <kbd>F</kbd> to search for a keyword
- Go through our [_Content Menu_](#content)
- Alternatively, use the search on our website: <https://www.awesome-ha.com>

### Content

- [About](#about)
- [How to Use](#how-to-use)
    - [Content](#content)
- [Installing](#installing)
- [Need Help?](#need-help)
- [Public Configurations](#public-configurations)
- [Hass.io](#hassio)
    - [Official Add-ons](#official-add-ons)
    - [Third Party Add-ons](#third-party-add-ons)
- [User Interface](#user-interface)
    - [Themes](#themes)
    - [Alternative Dashboard](#alternative-dashboards)
    - [Lovelace UI](#lovelace-ui)
    - [Custom Lovelace UI Cards](#custom-lovelace-ui-cards)
- [Custom Components](#custom-components)
- [DIY](#diy)
    - [DIY Projects](#diy-projects)
- [Online Resources](#online-resources)
    - [Blogs](#blogs)
    - [YouTube Channels](#youtube-channels)
    - [Podcasts](#podcasts)
- [Uncategorized](#uncategorized)
- [Alternative Home Automation Software](#alternative-home-automation-software)
- [Other Awesome Lists](#other-awesome-lists)
- [Contributing](#contributing)
- [Trademark Legal Notice](#trademark-legal-notice)
- [License](#license)

## Installing

Home Assistant has several installation / running methods. Many people have
different opinions and their personal favorites. Each method has its
advantages and disadvantages. Important to know, there is no wrong, or right here,
each technique installs the **SAME** Home Assistant.

Home Assistant currently _recommends_ the Hass.io method.

* [Hass.io](https://www.home-assistant.io/getting-started/) - Installing using a Docker managed environment (recommended method).
* [Docker](https://www.home-assistant.io/docs/installation/docker/) - Installing on Docker.
* [Hassbian](https://www.home-assistant.io/docs/installation/hassbian/installation/) - Installing Hassbian.
* [Manually](https://www.home-assistant.io/docs/installation/virtualenv/) - Manual installation using a Python virtual environment.

## Need Help?

_There are various ways to get in touch with the Home Assistant community.
It doesn’t matter if you have a question, need help, want to request a feature,
or just say ‘Hi’._

### Official channels

* [Home Assistant Discord](https://discordapp.com/invite/c5DvZ4e) - Join the chat, most of us are there.
* [Home Assistant Community](https://community.home-assistant.io/?u=frenck) - The discussion forum, also used for feature requests.
* [Home Assistant Subreddit](https://www.reddit.com/r/homeassistant/) - If you are into Reddit, subscribe.
* [Home Assistant Enthusiasts](https://www.facebook.com/groups/HomeAssistant/) - Facebook group for enthusiasts.

### Other channels

* [Dr. ZZs](https://www.facebook.com/groups/1969622823351838/) - Facebook group by Dr. Zzs.
* [Community Hassio Add-ons Discord](https://discord.me/hassioaddons) - Get support on the Community Hassio Add-ons.

## Public Configurations

_Some people store their full Home Assistant configuration on GitHub. They are
an awesome source for learning and a great source of inspiration._

* [Carlo Costanzo](https://github.com/CCOSTAN/Home-AssistantConfig#logo) - Probably the most documented configuration out there.
* [DubhAd](https://github.com/DubhAd/Home-AssistantConfig) - Also known as Tinkerer shares his configuration files.
* [geekofweek](https://github.com/geekofweek/homeassistant) - Has over 300+ automations.
* [Isabella Gross Alström](https://github.com/isabellaalstrom/HomeAssistantConfiguration) - Hass.io, Intel NUC, Ubuntu, Docker, Lovelace UI.
* [Mahasri Kalavala](https://github.com/skalavala/smarthome) - Impressive setup, with lots of different hardware working together.
* [stanvx](https://github.com/stanvx/Home-Assistant-Configuration) - Complete setup which uses AppDaemon and HA Floorplan as well.
* [Vasiley](https://github.com/Vasiley/Home-Assistant-Main) - Runs two instances that work together.
* [Alok Saboo](https://github.com/arsaboo/homeassistant-config) - Also known as arsaboo. Regularly updated.
* [Aaron Bach](https://github.com/bachya/smart-home) - Also known as bachya. Regularly updated and includes numerous Dockerized services.
* [James McCarthy](https://github.com/JamesMcCarthy79/Home-Assistant-Config) - Well documented, 3 instances & automations in YAML & Node-RED.

## Hass.io

_Hass.io is a complete operating system that will take care of installing and
updating Home Assistant, and is managed from the frontend._

* [Hass.io Beginner's Guide](https://www.youtube.com/watch?v=qnCRcGTznXs) - :tv: Excellent step-by-step guide on getting started (uses HassOS).

### Official Add-ons

_Add-ons are easily installable services that extend the functionality around
your Hass.io instance._

* [DuckDNS](https://www.home-assistant.io/addons/duckdns/) - Updates your Duck DNS IP address and generate SSL using Let's Encrypt.
* [HASS Configurator](https://www.home-assistant.io/addons/configurator/) - Browser-based configuration file editor.
* [Mosquitto](https://www.home-assistant.io/addons/mosquitto/) - Fast and reliable MQTT broker.
* [SSH Server](https://www.home-assistant.io/addons/ssh/) - Allows logging in remotely to using SSH.
* [Samba](https://www.home-assistant.io/addons/samba/) - Access your configuration files using Windows network shares.
* [NGINX SSL proxy](https://www.home-assistant.io/addons/nginx_proxy/) - Reverse proxy with SSL termination.

### Third Party Add-ons

_Anyone could create an add-on, the following are created by the community._

* [SSH & Web Terminal](https://github.com/hassio-addons/addon-ssh) - SSH and Web-based terminal with tons of pre-loaded useful tools.
* [Pi-hole](https://github.com/hassio-addons/addon-pi-hole) - Network-wide ad blocking.
* [UniFi Controller](https://github.com/hassio-addons/addon-unifi) - The UniFi Controller allows you to manage your UniFi network using a web browser.
* [Node-RED](https://github.com/hassio-addons/addon-node-red) - Flow-based programming for the Internet of Things.
* [Plex Media Server](https://github.com/hassio-addons/addon-plex) - Your recorded media beautifully organized and ready to stream.
* [IDE](https://github.com/hassio-addons/addon-ide) - Advanced web-based IDE, based on Cloud9 IDE.
* [Dasshio](https://github.com/danimtb/dasshio) - Easily use your Amazon Dash Buttons.
* [InfluxDB](https://github.com/hassio-addons/addon-influxdb) - Scalable datastore for metrics, events, and real-time analytics.
* [Grafana](https://github.com/hassio-addons/addon-grafana) - Open platform for beautiful analytics and monitoring.
* [Tor](https://github.com/hassio-addons/addon-tor) - Protect your privacy and access your instance via Tor.
* [Spotify Connect](https://github.com/hassio-addons/addon-spotify-connect) - Spotify Connect client for playing music on your Home Assistant device.
* [zigbee2mqtt](https://github.com/danielwelch/hassio-zigbee2mqtt) - Zigbee to MQTT bridge, get rid of your proprietary Zigbee bridges.
* [AppDaemon3](https://github.com/hassio-addons/addon-appdaemon3) - Python Apps and HADashboard.
* [Shinobi](https://github.com/hassio-addons/addon-shinobi) - Beautiful and feature-rich CCTV/NVR for your camera's.
* [TasmoAdmin](https://github.com/hassio-addons/addon-tasmoadmin) - Centrally manage all your Sonoff-Tasmota devices.
* [Octobox](https://github.com/hassio-addons/addon-octobox) - Take back control of your GitHub notifications.
* [Aircast](https://github.com/hassio-addons/addon-aircast) - AirPlay capabilities for your Chromecast players.
* [AirSonos](https://github.com/hassio-addons/addon-airsonos) - AirPlay capabilities for your Sonos players.
* [Dropbox Sync](https://github.com/danielwelch/hassio-dropbox-sync) - Upload your backup snapshots to Dropbox.
* [Log Viewer](https://github.com/hassio-addons/addon-log-viewer) - Browser-based live log viewing utility.

## User Interface

_The Home Assistant frontend is already pretty, but you can customize it to
fit your needs or taste better._

* [HA Floorplan](https://github.com/pkozul/ha-floorplan) - Interaction with your entities from a Floorplan.
* [Custom UI elements](https://github.com/andrey-git/home-assistant-custom-ui) - For use with a (non-Lovelace) frontend.

### Themes

_It is all about the looks, apply some style._

* [Themes Tutorial](https://www.youtube.com/watch?v=h1h8FFy9_Co) - :tv: Quick tutorial/example on how to configure themes.
* [Midnight](https://community.home-assistant.io/t/midnight-theme/28598?u=frenck) - A dark theme by Marcel Hoffs.
* [Dark Cyan](https://community.home-assistant.io/t/dark-cyan-theme/28594?u=frenck) - A dark theme with cyan accents by Ryoen Deprouw.
* [Grey Night](https://community.home-assistant.io/t/grey-night-theme/30848?u=frenck) - A dark theme with grey accents by ksya.
* [Dark Red](https://community.home-assistant.io/t/dark-red-theme/28592?u=frenck) - A dark theme with red accents by Ryoen Deprouw.
* [Halloween](https://community.home-assistant.io/t/halloween-theme/30872?u=frenck) - Pumpkins colored by Mahasri Kalavala.
* [Black and Green](https://community.home-assistant.io/t/black-and-green-theme/28602?u=frenck) - A dark theme with pale green accents by GreenTurtwig.
* [Vintage](https://community.home-assistant.io/t/vintage-theme/42806?u=frenck) - Give your frontend a vintage look with this theme by Anup Surendran.
* [Carbon Green](https://community.home-assistant.io/t/share-your-themes/22018/95?u=frenck) - Light carbon theme with green accents by Reua.

### Alternative Dashboards

* [Home Assistant Control Panel](https://reformedreality.com/home-assistant-control-panel) - Simple to use, easy to install.
* [TileBoard](https://github.com/resoai/TileBoard) - A simple yet highly configurable Dashboard.

### Lovelace UI

_Lovelace is the new UI interface for Home Assistant (still experimental!)_

* [Lovelace UI Documentation](https://www.home-assistant.io/lovelace) - The official documentation.
* [Getting started with Lovelace UI](https://www.youtube.com/watch?v=ObfRzMIEJPgx) - :tv: Great introduction to Lovelace UI by DrZzs.
* [Lovelace Card Gallery](https://home-assistant-lovelace-gallery.netlify.com/) - Demo showing all official cards including configurations.
* [Lovelace UI Migration Script](https://gist.github.com/dale3h/ee5b08ed1bf3a26a57e3d56ae221a796) - Little Python script that converts your old UI.
* [Lovelace Migration](https://github.com/hassio-addons/addon-lovelace-migration) - Hass.io Add-on, automatically converts your existing UI to Lovelace.
* [Plan Coordinates](https://github.com/ciotlosm/custom-lovelace/tree/master/plan-coordinates) - Helps to find left and top for `picture-elements` cards.
* [Share the Love](https://sharethelove.io) - Custom cards demos and configuration examples for Lovelace.

### Custom Lovelace UI Cards

_Lovelace allows people to build custom cards on top of it, which you can
easily add to your instance._

* [Monster Card](https://github.com/ciotlosm/custom-lovelace/tree/master/monster-card) - Dynamically adds entities: Magic.
* [Canvas Gauge Card](https://github.com/custom-cards/canvas-gauge-card) - Use awesome gauges from canvas-gauges.com.
* [Gauge Card](https://github.com/ciotlosm/custom-lovelace/tree/master/gauge-card) - Simple gauge implemented in pure CSS.
* [Alarm Control Panel Card](https://github.com/ciotlosm/custom-lovelace/tree/master/alarm_control_panel-card) - Card that looks like an alarm keypad.
* [Big Number Card](https://github.com/ciotlosm/custom-lovelace/tree/master/bignumber-card) - Display big numbers for sensors, including severity level as background.
* [Animated Weather Card](https://community.home-assistant.io/t/custom-animated-weather-card-for-lovelace/58338?u=frenck) - Nice looking card showing the weather, with subtle animations.
* [Thermostat Card](https://github.com/ciotlosm/custom-lovelace/tree/master/thermostat-card) - Thermostat control card that looks like a Nest Thermostat.

## Custom Components

_Additional components for Home Assistant, that were created by the community._

* [Hue Sensors](https://github.com/robmarkcole/Hue-sensors-HASS) - Enables the use of Hue sensors.
* [Google Geocode](https://github.com/michaelmcarthur/GoogleGeocode-HASS) - Converts a device tracker location into a human-readable address.
* [Lutron Caseta Pro](https://github.com/upsert/lutron-caseta-pro) - Integrates Lutron Caseta Smart Bridge PRO / RA2 Select.
* [ToonHA](https://github.com/krocat/ToonHA) - Integrates Toon by Eneco using the official API.
* [Broadlink IR](https://github.com/vpnmaster/homeassistant-custom-components) - Integrates devices using Broadlink IR.
* [Xiaomi Hygrothermo](https://github.com/dolezsa/Xiaomi_Hygrothermo) - Sensor platform for Xiaomi Mijia BT Hygrothermo temperature and humidity sensor.
* [Volkswagen Carnet](https://github.com/robinostlund/homeassistant-volkswagencarnet) - Integrates Volkswagen Carnet (requires valid Carnet subscription).
* [Untapped](https://github.com/custom-components/sensor.untapped) - Connects with your Untapped account.
* [Elasticsearch](https://github.com/legrego/homeassistant-elasticsearch) - Publishes events to Elasticsearch.

## DIY

_Do It Yourself; rather than buying home automation hardware or solutions, you
could also build them yourself!_

* [esphomeyaml](https://esphomelib.com/esphomeyaml/) - Program ESP8266/ESP32 board using YAML.
* [Magic Cards](https://github.com/maddox/magic-cards) - RFID scannable cards that you can program to do anything.
* [OpenMQTTGateway](https://github.com/1technophile/OpenMQTTGateway) - A flexible MQTT gateway for IR, RF, BLE, MiFlora, SMS, and many sensors.
* [esp8266 Milight Hub](https://github.com/sidoh/esp8266_milight_hub) - Alternative hub for Milight/LimitlessLED devices that uses MQTT.

### DIY Projects

* [HA SwitchPlate](https://community.home-assistant.io/t/ha-switchplate-diy-lcd-touchscreen-wall-switch-replacement/25464?u=frenck) - LCD Touchscreen wall switch replacement.
* [DIY Multisensor](https://www.youtube.com/watch?v=jpjfVc-9IrQ) - :tv: $15, Temperature, Humidity, Light, Motion, and RGB LED, without soldering.
* [$10 WiFi RGB Bulb](https://community.home-assistant.io/t/how-to-inexpensive-10-us-wifi-rgb-bulb-that-works-with-home-assistant/14735?u=frenck) - In inexpensive RGB bulb that works on WiFi.
* [433mhz/IR Bidirectional Gateway](https://community.home-assistant.io/t/433mhz-infrared-ir-to-and-from-mqtt-on-esp8266/6779?u=frenck) - Bidirectional with IR and 433mhz using ESP8266 and MQTT.
* [esp8266MQTTBlinds](https://community.home-assistant.io/t/esp8266-window-blinds-mqtt/14863?u=frenck) - Automate your window blinds using an ESP8266, a servo and MQTT.
* [Home Assistant's Hackster.io](https://www.hackster.io/home-assistant?f=1#_=_) - A Hackster channel with multiple DIY projects.
* [DIY Camera with Raspberry PI & WebCam](https://skalavala.github.io/camera/) - Convert any webcam into a surveillance system.

## Online Resources

_Links to various users of Home Assistant that regularly publish Home Assistant focussed content._

### Blogs

* [DIY Futurism](https://diyfuturism.com/) - Brad posts articles with great instructions for new users.
* [Phil Hawthorne](https://philhawthorne.com/homeautomation) - Co-host of the Home Assistant Podcast.
* [Smart Home Hobby](https://smarthomehobby.com/) - Features budget friendly guides and information.
* [Self Hosted Home](https://selfhostedhome.com/) - Articles on DIY home automation projects and self hosted services.

### YouTube Channels

_Sit back, relax, watch, and learn._

* [BRUH](https://www.youtube.com/channel/UCLecVrux63S6aYiErxdiy4w) - Ben has great tutorials for getting started, unfortunately, inactive lately.
* [BurnsHA](https://www.youtube.com/channel/UCSKQutOXuNLvFetrKuwudpg) - Great informational and tutorial videos.
* [DrZzs](https://www.youtube.com/channel/UC7G4tLa4Kt6A9e3hJ-HO8ng) - Great how-to videos and also streams live.
* [The Hook Up](https://www.youtube.com/channel/UC2gyzKcHbYfqoXA5xbyGXtQ) - Tutorials and more, also has videos on home automation in general.
* [HASSCASTS](https://www.youtube.com/channel/UCGOCeqMJnLvr-5C-ypUw7IQ) - Tips, Tricks & Tutorials, moving to mainly live streams.

### Podcasts

_Get inspired, while commuting, doing your morning routine, or at the gym!_

* [Home Assistant Podcast](https://hasspodcast.io) - Biweekly podcast with the latest news and interesting guests.

## Uncategorized

_Valuable links, that don't fit in any of the above categories (yet!)._

* [Home Assistant for Homebridge](https://github.com/home-assistant/homebridge-homeassistant) - A Homebridge plugin for using Siri and HomeKit.
* [Room Assistant](https://github.com/mKeRix/room-assistant) - A companion client to handle sensors in multiple rooms.
* [Home Assistant Companion](https://itunes.apple.com/us/app/home-assistant-open-source-home-automation/id1099568401?mt=8) - iPhone/iPad/iOS App to control and monitor your home remotely.
* [Mi Flora via MQTT daemon](https://github.com/ThomDietrich/miflora-mqtt-daemon) - Collect and transfer Xiaomi Mi Flora plant sensor data via MQTT.
* [hassctl](https://github.com/dale3h/hassctl) - Simple command line utility to help debug your configuration.
* [zigbee2mqtt](https://github.com/Koenkk/zigbee2mqtt) - Zigbee to MQTT bridge, get rid of your proprietary Zigbee bridges.
* [rhasspy](https://github.com/synesthesiam/rhasspy-assistant) - Toolkit for developing custom voice assistants.
* [Fully Kiosk Browser](https://www.ozerov.de/fully-kiosk-browser/) - Highly configurable Android Kiosk Browser and App Launcher.
* [Hassio Vagrant](https://github.com/hassio-addons/hassio-vagrant) - Vagrant box original created for developing add-ons.
* [AppDaemon](https://github.com/home-assistant/appdaemon) - Pythons Apps for Home Assistant
* [Developer Documentation](https://developers.home-assistant.io/) - The official developer documentation.
* [HASS Configurator](https://github.com/danielperna84/hass-configurator) - Browser-based configuration file editor.
* [HA-Dockermon](https://github.com/philhawthorne/ha-dockermon) - A NodeJS service for RESTful switches to control Docker containers.
* [Python Amazon Dash](https://github.com/Nekmo/amazon-dash) - Hack your Amazon Dash to run what you want. Without welders.
* [homekit2mqtt](https://github.com/hobbyquaker/homekit2mqtt) - HomeKit to MQTT bridge.
* [Home Assistant Device Database](https://www.hadevices.com/) - Database of supported/confirmed working devices.
* [Jinja Scripts for Curious Minds](https://github.com/skalavala/smarthome/tree/master/jinja_helpers) - Bunch of Jinja2 scripts helping you to understand it better.

## Alternative Home Automation Software

_Home Assistant isn't the only home automation framework out there, here
are some alternatives._

* [openHAB](https://github.com/openhab) - Java-based and aims at being a universal integration platform.
* [Domoticz](https://github.com/domoticz/domoticz) - A lightweight Home Automation System.
* [Gladys](https://github.com/GladysProject/Gladys) - Open source program which runs on your Raspberry Pi.
* [SmartThings](https://www.smartthings.com/) - Commercial home automation hub by Samsung.

## Other Awesome Lists

_Other amazingly awesome lists that can be found on the great and dangerous
interwebs._

* [awesome-smarthome](https://github.com/pfalcon/awesome-smarthome) - Curated list of awesome SmartHome/Home Automation things.
* [awesome-iot](https://github.com/HQarroum/awesome-iot) - Curated list of awesome Internet of Things projects and resources.
* [awesome-open-iot](https://github.com/Agile-IoT/awesome-open-iot) - Curated list of open source IoT frameworks, libraries and software.
* [awesome-amazon-alexa](https://github.com/miguelmota/awesome-amazon-alexa#readme) - Curated list of awesome resources for the Amazon Alexa platform.
* [awesome-mqtt](https://github.com/hobbyquaker/awesome-mqtt#readme) - Curated list of MQTT related stuff.

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
