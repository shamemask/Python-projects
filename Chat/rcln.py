import rclone

cfg = """[local]
type = local
nounc = true"""
result = rclone.with_config(cfg).listremotes()

print(result.get('out'))
# b'local:\n'
print(result.get('code'))
# 0
print(result.get('error'))