
import asyncio, time
from urllib.parse import urlparse, parse_qs

async def check_proxy(link):
    parts = parse_qs(urlparse(link).query)
    server = parts.get('server', [None])[0]
    port = int(parts.get('port', [0])[0])
    secret = parts.get('secret', [None])[0]
    if not server or not port or not secret:
        return False
    start = time.time()
    try:
        reader, writer = await asyncio.wait_for(asyncio.open_connection(server, port), timeout=5)
        writer.close()
        await writer.wait_closed()
    except:
        return False
    return time.time() - start < 5
