import logging
logging.basicConfig(
    filename="sample.log",
    level=logging.DEBUG,
    format="%(asctime)s %(name)s [%(levelname)s]: %(message)s")

import rclone

cfg = """[local]
type = local
nounc = true"""

with open("C:\\Users\\Lenovo\\AppData\\Roaming\\rclone\\rclone.conf") as file:
    cnf2 = file.read()

result = rclone.with_config(cnf2).listremotes()
logging.info(result)
print(result.get('out'))
# b'local:\n'
print(result.get('code'))
# 0
print(result.get('error'))
# b''