# requesthandler

An asynchronous, singleton-based HTTP request manager built on top of **asyncio** and **aiohttp**.  
It supports **request batching, rotating user-agents, graceful shutdown hooks, and detailed logging**, making it ideal for **web scraping, crawling, and API clients**.

---

## ✨ Features
- ✅ **Singleton Pattern** – only one instance is active  
- ✅ **Request Batching** – random batch sizes (3–5 requests) with randomized delays (5–10s)  
- ✅ **Rotating User-Agents** – mimics different browsers & devices  
- ✅ **Graceful Shutdown** – handles `SIGINT`, `SIGTERM`, `SIGBREAK` cleanly  
- ✅ **Async Queue** – schedules and executes requests in the background  
- ✅ **Detailed Logging** – structured logging for debugging & monitoring  

---

## 📦 Installation

You can install via the released `.whl` file:

```bash
pip install requesthandler-1.0.0-py3-none-any.whl
```
Or clone the repository and install manually:
```bash
git clone https://github.com/mohammadhniksefat/requesthandler.git
cd requesthandler
pip install .
```

---

## ⚡ Use Cases

Web scraping with controlled delays

Crawler systems with queue management

API clients needing resilience & throttling

---

## 🚀 Usage Example
``` python
import asyncio
import logging
from request_handler.request_handler import RequestHandler

async def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    # Initialize and configure handler
    handler = RequestHandler()
    await handler.configure()

    # Send 20 requests asynchronously
    urls = [f"https://github.com/" for i in range(20)]
    results = await asyncio.gather(*(handler.get(url) for url in urls))

    # Print first 100 chars of each response
    for i, result in enumerate(results, 1):
        print(f"Response {i}:\n{result[:100]}...\n")

    # Shutdown gracefully
    await handler.shutdown()

if __name__ == "__main__":
    asyncio.run(main())

```
---
📌 Example Output

When you run it, you’ll see both printed responses and logging output.

``` bash
Response 1:








<!DOCTYPE html>
<html
  lang="en"
  data-color-mode="dark" data-dark-theme="dark"
  data-col...

Response 2:








<!DOCTYPE html>
<html
  lang="en"
  data-color-mode="dark" data-dark-theme="dark"
  data-col...

Response 3:
...
```

## Logs

``` bash
2025-10-01 15:58:02,765 Creating a new instance of RequestHandler
2025-10-01 15:58:02,766 Starting configure()
2025-10-01 15:58:02,767 Batch size set to 4
2025-10-01 15:58:02,769 RequestHandler configured successfully
2025-10-01 15:58:02,770 Scheduler started
2025-10-01 15:58:02,770 GET request queued: https://github.com/
2025-10-01 15:58:02,771 GET request queued: https://github.com/
2025-10-01 15:58:02,771 GET request queued: https://github.com/
...
2025-10-01 15:58:02,777 GET request queued: https://github.com/
2025-10-01 15:58:02,778 GET request queued: https://github.com/
2025-10-01 15:58:02,778 Task added to batch
2025-10-01 15:58:02,779 Task added to batch
2025-10-01 15:58:02,779 Task added to batch
2025-10-01 15:58:02,780 Task added to batch
2025-10-01 15:58:02,780 Executing batch of size 4
2025-10-01 15:58:03,687 GET request successful - status: 200
2025-10-01 15:58:03,752 GET request successful - status: 200
2025-10-01 15:58:03,762 GET request successful - status: 200
2025-10-01 15:58:03,803 GET request successful - status: 200
2025-10-01 15:58:03,804 Batch complete. Sleeping for 10s
2025-10-01 15:58:13,816 Task added to batch
2025-10-01 15:58:13,818 Task added to batch
2025-10-01 15:58:13,819 Task added to batch
2025-10-01 15:58:13,820 Executing batch of size 3
2025-10-01 15:58:14,070 GET request successful - status: 200
2025-10-01 15:58:14,453 GET request successful - status: 200
2025-10-01 15:58:14,492 GET request successful - status: 200
2025-10-01 15:58:14,493 Batch complete. Sleeping for 9s
...
2025-10-01 15:58:52,146 Initiating shutdown...
2025-10-01 15:58:52,147 Scheduler task cancelled
2025-10-01 15:58:52,150 Session closed
```
