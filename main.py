import os

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "api.server:server",
        host="0.0.0.0",
        port=int(os.getenv("PORT")),
        loop="uvloop",
        http="httptools",
        workers=int(os.getenv("WORKERS"))
    )