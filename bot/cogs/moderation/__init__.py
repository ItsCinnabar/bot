from bot.bot import Bot
from .infractions import Infractions
from .management import ModManagement
from .modlog import ModLog
from .silence import Silence
from .slowmode import Slowmode
from .superstarify import Superstarify


def setup(bot: Bot) -> None:
    """Load the Infractions, ModManagement, ModLog, Silence, Slowmode, and Superstarify cogs."""
    bot.add_cog(Infractions(bot))
    bot.add_cog(ModLog(bot))
    bot.add_cog(ModManagement(bot))
    bot.add_cog(Silence(bot))
    bot.add_cog(Slowmode(bot))
    bot.add_cog(Superstarify(bot))
