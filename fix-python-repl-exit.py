# Copy paste the below script into your PYTHONSTARTUP script:
try:
    import __builtins__ as builtins
except ImportError:
    import builtins


class _Exit:
    def __repr__(self):
        raise SystemExit(0)

    def __call__(self, code=0):
        exit(code)


builtins.exit = _Exit()
