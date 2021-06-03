import aiohttp
import asyncio

# Global variable
def getSthlmBostadUrl():
    return "https://bostad.stockholm.se/Lista/?sort=annonserad-fran-desc"

def main():
    print(getSthlmBostadUrl())

if __name__ == "__main__":
    main()