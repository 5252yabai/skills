import asyncio
import json
from pathlib import Path

import websockets

FILE_INPUT_SELECTOR = "input[type='file'][accept*='m4a']"


async def _set_file_input(browser_ws: str, file_path: Path, selector: str) -> None:
    _id = 0

    async def send(ws, method, params=None, session_id=None):
        nonlocal _id
        _id += 1
        msg = {"id": _id, "method": method, "params": params or {}}
        if session_id:
            msg["sessionId"] = session_id
        await ws.send(json.dumps(msg))
        while True:
            resp = json.loads(await ws.recv())
            if resp.get("id") == _id and resp.get("sessionId") == session_id:
                return resp.get("result", {})

    async with websockets.connect(browser_ws) as ws:
        targets = await send(ws, "Target.getTargets")
        pages = [
            t for t in targets.get("targetInfos", [])
            if t["type"] == "page" and "clovanote" in t.get("url", "")
        ]
        if not pages:
            raise RuntimeError("Clova Note tab not found via CDP")

        session = await send(ws, "Target.attachToTarget", {"targetId": pages[0]["targetId"], "flatten": True})
        sid = session.get("sessionId")

        async def page(method, params=None):
            return await send(ws, method, params, sid)

        doc = await page("DOM.getDocument")
        root_id = doc["root"]["nodeId"]
        node = await page("DOM.querySelector", {"nodeId": root_id, "selector": selector})
        node_id = node.get("nodeId")
        if not node_id:
            raise RuntimeError(f"File input not found with selector: {selector!r}")

        await page("DOM.setFileInputFiles", {"nodeId": node_id, "files": [str(file_path)]})


def set_file_input(browser_ws: str, file_path: Path, selector: str = FILE_INPUT_SELECTOR) -> None:
    asyncio.run(_set_file_input(browser_ws, file_path, selector))
