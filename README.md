# Desk controller for Linak desk (IKEA)

### Installment

Disclaimer, this project is a wrapper around the linak controller from [this repo](https://github.com/rhyst/linak-controller)

Do:
1. Activate the venv set up in this repo `source venv/bin/activate`
2. Connect to your desk via bluetooth ( easiest way is to use [Desk Control](https://apps.apple.com/no/app/desk-control/id1203254365) app)
3. Find the UUID address of your bluetooth desk.
- MAC:
    1. Open or download [bluetility](https://github.com/jnross/Bluetility)
    2. Disconnect Desk if you are already connected
    3. Set your desk to pairing mode (usually by holding down the bluetooth button) and pair your desk with your computer using [Bluetility](https://github.com/jnross/Bluetility) by clicking on it in the device list.
    4. Copy the UUID of the desk by right clicking on the device in Bluetility and selecting "Copy device identifier".
4. Insert the UUID in the config.yaml file, as described in the [configuration](https://github.com/rhyst/linak-controller) section on the public linak-controller repo. Or use the --mac-address flag.
5. IMPORTANT. Close the Bluetility app, and disconnect other devices that may interfere with the connection to the desk. It is quite fragile in this manner.
6. Run linak-controller.


## Troubleshooting
Connection failed:
* Try ensuring that the desk is paired but not connected before using the script.
* Try increasing the scan-timeout and connection-timeout.
* Close bluetility, or other bluetooth development software.
* Close the --server, if you have it running in the background and you are not using the --forward flag