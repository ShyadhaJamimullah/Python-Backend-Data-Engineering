import os
import time
import asyncio
import aiohttp

downloads_dir="downloads"
links="links.txt"

async def download_files(session,url,filename):
    print(f"Starting: {filename}")
    async with session.get(url) as response:
        content=await response.read()

        file_path=os.path.join(downloads_dir,filename)
        with open(file_path,"wb") as f:
            f.write(content)
    print(f"Finished downloading: {filename}")

async def main():
    os.makedirs(downloads_dir,exist_ok=True)
    urls=[]
    with open(links,"r") as f:
       
        for line in f:
            cleaned_line = line.strip()  

            if cleaned_line:        
                    urls.append(cleaned_line)

    start_time=time.perf_counter()
    async with aiohttp.ClientSession() as session:
        tasks=[]

        for i,url in enumerate(urls,start=1):
            filename=f"file_{i}.pdf"
            task=asyncio.create_task(download_files(session,url,filename))

            tasks.append(task)
        await asyncio.gather(*tasks)
        end_time=time.perf_counter()
    print(f"Total execution time; {end_time - start_time:.2f} seconds")
asyncio.run(main())


