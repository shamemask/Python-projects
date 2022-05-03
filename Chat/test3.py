import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s [%(levelname)s]: %(message)s")

import rclone

cfg = """[local]
type = local
nounc = true"""
result = rclone.with_config(cfg).listremotes()