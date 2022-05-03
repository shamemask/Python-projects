import rclone

cfg = """[local]
type = local
nounc = true"""
result = rclone.with_config(cfg).run_cmd(command="lsd", extra_args=["local:/tmp", "-v", "--dry-run"])