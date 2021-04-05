# hookspec.py
import pluggy

hookspec = pluggy.HookspecMarker('beth')

class BethSpec:
    @hookspec
    def setup(self):
        pass

    @hookspec
    def get_alias(self):
        pass

    @hookspec
    def execute(self, input:str):
        pass
