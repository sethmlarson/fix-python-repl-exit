# Copy paste the below script into your PYTHONSTARTUP script:
try:
    import __builtins__ as builtins
except ImportError:
    import builtins


_builtins_exit = builtins.exit


class _Exit:
    def __repr__(self):
        raise SystemExit(0)

    def __call__(self, code=0):
        _builtins_exit(code)


builtins.exit = _Exit()
