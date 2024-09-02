import asyncio
from bleak import BleakClient

address = "EDFDE11B-C1CF-85DB-B2C0-A1CD7B3CB147" # Replaced with actual bluetooth address
async def main(address):
    print("Connecting to device...")
    async with BleakClient(address) as client:
        print("Connected")

asyncio.run(main(address))