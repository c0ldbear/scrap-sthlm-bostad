import aiohttp
import asyncio

# Global variable
async def getSthlmBostadUrl():
    return "https://bostad.stockholm.se/Lista/?sort=annonserad-fran-desc"

async def FetchWeb():
    url = await getSthlmBostadUrl()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            rText = await response.text()
    return rText

async def main():
    print(await FetchWeb())

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())