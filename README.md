# Awesome Home Assistant

<div align="center">
  <img width="400" src="https://www.awesome-ha.com/images/awesome-home-assistant.svg" alt="Awesome Home Assistant">
  <br>
  <a href="https://awesome-ha.com"><strong>https://awesome-ha.com</strong></a>
  <br>
  <br>
  <a href="https://github.com/sindresorhus/awesome#readme" target="_blank">
    <img alt="Awesome" src="https://awesome.re/badge.svg">
  </a>
</div>

## About

Awesome Home Assistant is a curated list of awesome
[Home Assistant](https://www.home-assistant.io) resources.
Additional software, tutorials, custom components, Hassio add-ons,
custom Lovelace panels, cookbooks, example setups, and much more.

The list is divided into categories. The links in those categories do not have
pre-established order, the order is for contribution. If you want to contribute,
please read the [guide](https://github.com/frenck/awesome-home-assistant/blob/master/CONTRIBUTING.md).

## How to Use

Awesome Home Assistant is an amazing list for people trying to automate every
aspect of their home. Automating your home is a long, hard, and never finished
task that usually involves a lot of tinkering.

There are several ways to get support and inspiration:

- Chat on the [Home Assistant Discord](https://discordapp.com/invite/c5DvZ4e) server
- Check out the [Home Assistant Community Forums](https://community.home-assistant.io/?u=frenck)
- Visit the [Home Assistant Subreddit](https://www.reddit.com/r/homeassistant/)
- And of course, this awesome list!
    - Simply press <kbd>command/ctrl</kbd> + <kbd>F</kbd> to search for a keyword
    - Go through our [_Content Menu_](#content)
    - Or use the search on our website: <https://www.awesome-ha.com>

### Content

- [About](#about)
- [How to Use](#how-to-use)
    - [Content](#content)
- [Installing](#installing)
- [Public Configurations](#public-configurations)
- [Hass.io](#hassio)
    - [Add-ons](#add-ons)
        - [Official Add-ons](#official-add-ons)
        - [Third Party Add-ons](#third-party-add-ons)
- [Uncategorized](#uncategorized)
- [Alternative Home Automation Software](#alternative-home-automation-softwares)
- [Other Awesome Lists](#other-awesome-lists)
- [Contributing](#contributing)
- [Trademark Legal Notice](#trademark-legal-notice)
- [License](#license)

## Installing

Home Assistant has several installation / running methods. Many people have
different opinions and their personal favorites. Each method has its
advantages and disadvantages. Important to know, there is no wrong, or right here,
each method installs the **SAME** Home Assistant.

Home Assistant currently _recommends_ the Hass.io method.

* [Hass.io](https://www.home-assistant.io/getting-started/) - Installing using a Docker managed environment (recommended method).
* [Docker](https://www.home-assistant.io/docs/installation/docker/) - Installing on Docker.
* [Hassbian](https://www.home-assistant.io/docs/installation/hassbian/installation/) - Installing Hassbian.
* [Manually](https://www.home-assistant.io/docs/installation/virtualenv/) - Manual installation using a Python virtual environment.

## Public Configurations

_Some people store their full Home Assistant configuration on GitHub. They are
a awesome for learning and a great source of inspiration._

* [Carlo Costanzo](https://github.com/CCOSTAN/Home-AssistantConfig) - Probably the most documented configuration out there.
* [DubhAd](https://github.com/DubhAd/Home-AssistantConfig) - Also known as Tinkerer shares his configuration files.
* [geekofweek](https://github.com/geekofweek/homeassistant) - Has over 300+ automations.
* [Isabella Gross Alström](https://github.com/isabellaalstrom/HomeAssistantConfiguration) - Hass.io, Intel NUC, Ubuntu, Docker, Lovelace UI.
* [Mahasri Kalavala](https://github.com/skalavala/smarthome) - Impressive setup, with lots of different hardware working together.
* [stanvx](https://github.com/stanvx/Home-Assistant-Configuration) - Complete setup which uses AppDaemon and HA Floorplan as well.
* [Vasiley](https://github.com/Vasiley/Home-Assistant-Main) - Runs two instances that work together.

## Hass.io

_Hass.io is a complete operating system that will take care of installing and
updating Home Assistant, and is managed from the frontend._

* [Hass.io Beginner's Guide](https://www.youtube.com/watch?v=qnCRcGTznXs) - :tv: Excellent step-by-step guide on getting started (uses HassOS).


### Add-ons

_Add-ons are easy installable services that extend the functionality around
your Hass.io instance._

#### Official Add-ons

* [DuckDNS](https://www.home-assistant.io/addons/duckdns/) - Updates your Duck DNS IP address and generate SSL using Let's Encrypt.
* [HASS Configurator](https://www.home-assistant.io/addons/configurator/) - Browser-based configuration file editor.
* [Mosquitto](https://www.home-assistant.io/addons/mosquitto/) - Fast and reliable MQTT broker.
* [SSH Server](https://www.home-assistant.io/addons/ssh/) - Allows logging in remotely to using SSH.
* [Samba](https://www.home-assistant.io/addons/samba/) - Access your configuration files using Windows network shares.
* [NGINX SSL proxy](https://www.home-assistant.io/addons/nginx_proxy/) - Reverse proxy with SSL termination.

#### Third Party Add-ons

* [SSH & Web Terminal](https://github.com/hassio-addons/addon-ssh) - SSH and Web based terminal with tons of pre-loaded usefull tools.
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

## Uncategorized

_Values links, that don't fit in any of the above categories (yet!)._

* [HA SwitchPlate](https://community.home-assistant.io/t/ha-switchplate-diy-lcd-touchscreen-wall-switch-replacement/25464?u=frenck) - DIY LCD Touchscreen wall switch replacement.
* [HA Floorplan](https://github.com/pkozul/ha-floorplan) - Interaction with your enities from a Floorplan.
* [Home Assistant Control Panel](https://reformedreality.com/home-assistant-control-panel) - Simple to use, easy to install.
* [Home Assistant for Homebridge](https://github.com/home-assistant/homebridge-homeassistant) - A Homebridge plugin for using Siri and HomeKit.
* [Custom UI elements](https://github.com/andrey-git/home-assistant-custom-ui) - For use with the (non-Lovelace) frontends.
* [Room Assistant](https://github.com/mKeRix/room-assistant) - A companion client to handle sensors in multiple rooms.
* [Home Assistant Companion](https://itunes.apple.com/us/app/home-assistant-open-source-home-automation/id1099568401?mt=8) - iPhone/iPad/iOS App to control and monitor your home remotely.
* [Magic Cards](https://github.com/maddox/magic-cards) - RFID scannable cards that you can program to do anything.
* [Hue Sensors](https://github.com/robmarkcole/Hue-sensors-HASS) - Custom component enabling the use of Hue sensors.
* [Custom cards](https://github.com/ciotlosm/custom-lovelace) - Collection of custom cards for use with the Lovelace UI.
* [Mi Flora via MQTT daemon](https://github.com/ThomDietrich/miflora-mqtt-daemon) - Collect and transfer Xiaomi Mi Flora plant sensor data via MQTT.
* [hassctl](https://github.com/dale3h/hassctl) - Simple command line utility to help debug your configuration.
* [Getting started with Lovelace UI](https://www.youtube.com/watch?v=ObfRzMIEJPg) - :tv: Great introduction to Lovelace UI by DrZzs
* [zigbee2mqtt](https://github.com/Koenkk/zigbee2mqtt) - Zigbee to MQTT bridge, get rid of your proprietary Zigbee bridges.
* [rhasspy](https://github.com/synesthesiam/rhasspy-assistant) - Toolkit for developing custom voice assistants.
* [Fully Kiosk Browser](https://www.ozerov.de/fully-kiosk-browser/) - Highly configurable Android Kiosk Browser and App Launcher (e.g., for a wall mounted tablet).
* [Hassio Vagrant](https://github.com/hassio-addons/hassio-vagrant) - Vagrant box original created for developing add-ons.

## Alternative Home Automation Software

_Home Assistant isn't the only home automation framework out there, here
are some alternatives._

* [openHAB](https://github.com/openhab) - Java based and aims at being an universal integration platform.
* [Domoticz](https://github.com/domoticz/domoticz) - A lightweight Home Automation System.
* [Gladys](https://github.com/GladysProject/Gladys) - Open source program which runs on your Raspberry Pi.
* [SmartThings](https://www.smartthings.com/) - Commercial home automation hub by Samsung.

## Other Awesome Lists

_Other amazingly awesome lists that can be found on the great and dangerous
interwebs._

* [awesome-smarthome](https://github.com/pfalcon/awesome-smarthome) - Curated list of awesome SmartHome/Home Automation things.
* [awesome-iot](https://github.com/HQarroum/awesome-iot) - Curated list of awesome Internet of Things projects and resources.
* [awesome-open-iot](https://github.com/Agile-IoT/awesome-open-iot) - Curated list of open source IoT frameworks, libraries and software.

## Contributing

This awesome list is an active open-source project and are always open to
people who want to contribute to it. We have set up a separate document
containing our [Contribution Guidelines](https://github.com/frenck/awesome-home-assistant/blob/master/CONTRIBUTING.md).

The original setup of this awesome list is by [Franck Nijhof](https://twitter.com/frenck).

For a full list of all authors and contributors, check the
[contributor's page](https://github.com/frenck/awesome-home-assistant/graphs/contributors).

Thank you for being involved! 😍

## Trademark Legal Notice

This Awesome list is not created, developed, affilliated, supported, maintained
or endorsed by Home Assistant.

All product names, logos, brands, trademarks and registered trademarks are
property of their respective owners. All company, logo, product and service
names used in this list are for identification purposes only.

Use of these names, logos, trademarks and brands does not imply endorsement.

## License

Distributed under the Creative Commons Attribution 4.0 license. 
See [LICENSE](https://github.com/frenck/awesome-home-assistant/blob/master/LICENSE.md) for
the complete license.
