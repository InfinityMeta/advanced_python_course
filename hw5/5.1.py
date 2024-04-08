import os
import click
import asyncio
import aiohttp
import aiofiles


URL = "https://source.unsplash.com/random"
IMG_AMT = 20
SAVE_DIR = "./artefacts/5.1/"
SAVE_DIR_SIZE = len(os.listdir(SAVE_DIR))


async def get_image(session, img_num):
    response = await session.get(URL)
    image_path = os.path.join(SAVE_DIR, f"{SAVE_DIR_SIZE + img_num}.jpg")
    async with aiofiles.open(image_path, "wb") as f:
        await f.write(await response.read())


async def get_images(img_amt):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(img_amt):
            tasks.append(get_image(session, i))
        await asyncio.gather(*tasks)


@click.command()
@click.argument("img_amt", type=click.INT, default=IMG_AMT)
def main(img_amt):
    asyncio.run(get_images(img_amt))


if __name__ == "__main__":
    main()
