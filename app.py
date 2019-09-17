# import logging; logging.basicConfig(level=logging.INFO)
#
# import asyncio, os, json, time
# from datetime import datetime
#
# from aiohttp import web
#
# def index(request):
#     return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')
#
# async def init(loop):
#     app = web.Application(loop=loop)
#     app.router.add_route('GET', '/', index)
#     srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
#     logging.info('server started at http://127.0.0.1:9000...')
#     return srv
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()



#
# def index(request):
# 	return web.Response(body=b'<h1>index page</h1>',content_type='text/html')
#
# async def init():
# 	app = web.Application()
# 	app.add_routes([web.get('/',index)])
#
# 	runner = web.AppRunner(app)
# 	await runner.setup()
# 	site = web.TCPSite(runner, 'localhost', 9000)
# 	await site.start()
# 	print('服务器启动成功！')
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(init())
# loop.run_forever()


import asyncio
import random
import datetime

async def wait_and_echo(content):
    wait = random.randint(0, 10)
    print(f'print {content} after {wait} seconds')
    await asyncio.sleep(wait)
    print(f'{content} printed at {datetime.datetime.utcnow().strftime("%H:%M:%S ")}')

async def main():
    await asyncio.gather(*[wait_and_echo(x) for x in range(10)])

asyncio.run(main())




import asyncio
import random
import datetime

async def wait_and_echo(content):
    wait = random.randint(0, 10)
    print(f'print {content} after {wait} seconds')
    await asyncio.sleep(wait)
    print(f'{content} printed at {datetime.datetime.utcnow().strftime("%H:%M:%S ")}')

async def main():
    await asyncio.gather(*[wait_and_echo(x) for x in range(10)])

loop = asyncio.get_event_loop()
tasks = [wait_and_echo(x) for x in range(10)]
loop.run_until_complete(asyncio.gather(*tasks))




# import asyncio
# import time
#
#
# now = lambda: time.time()
#
#
# async def do_some_work(x):
#     print("waiting:", x)
#
# start = now()
#
# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
# task = loop.create_task(coroutine)
# print(task)
# loop.run_until_complete(task)
# print(task)
# print("Time:",now()-start)