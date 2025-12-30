"""
Environment variable configuration generator for Railway deployment.
Generates config.json from environment variables if it doesn't exist.
"""
import os
import json
import logging

logger = logging.getLogger(__name__)

def get_env(key, default=None, type_cast=str):
    """Get environment variable with type casting."""
    value = os.environ.get(key, default)
    if value is None:
        return default
    if type_cast == bool:
        return value.lower() in ('true', '1', 'yes', 'on')
    if type_cast == int:
        try:
            return int(value)
        except (ValueError, TypeError):
            return default
    if type_cast == float:
        try:
            return float(value)
        except (ValueError, TypeError):
            return default
    if type_cast == list:
        try:
            return json.loads(value) if value else default
        except json.JSONDecodeError:
            return default
    return value


def generate_config_from_env():
    """Generate config dictionary from environment variables."""

    # Required variables
    discord_token = get_env('DISCORD_TOKEN')
    api_url = get_env('API_URL', '')
    stats_url = get_env('STATS_URL', '')
    bearer_token = get_env('BEARER_TOKEN', '')

    if not discord_token:
        return None

    config = {
        "rcon": [{
            "server_number": get_env('SERVER_NUMBER', 1, int),
            "api_url": api_url,
            "stats_url": stats_url,
            "bearer_token": bearer_token,
            "discord_token": discord_token,
            "log_level": get_env('LOG_LEVEL', 'INFO'),

            # Register Player
            "register_player": [{
                "enabled": get_env('REGISTER_PLAYER_ENABLED', False, bool),
                "verify_ingame": get_env('REGISTER_VERIFY_INGAME', False, bool)
            }],

            # Comfort Functions
            "comfort_functions": [{
                "enabled": get_env('COMFORT_FUNCTIONS_ENABLED', False, bool),
                "dryrun": get_env('COMFORT_DRYRUN', False, bool)
            }],

            # Map Rotation
            "map_rotation": [{
                "enabled": get_env('MAP_ROTATION_ENABLED', False, bool),
                "webhook": get_env('MAP_ROTATION_WEBHOOK', '')
            }],

            # Server Status
            "server_status": [{
                "enabled": get_env('SERVER_STATUS_ENABLED', False, bool),
                "webhook": get_env('SERVER_STATUS_WEBHOOK', '')
            }],

            # Artillery Calculator
            "artillery_calculator": [{
                "enabled": get_env('ARTILLERY_CALCULATOR_ENABLED', False, bool),
                "interval": get_env('ARTILLERY_INTERVAL', 100, int),
                "in_game_messages": get_env('ARTILLERY_IN_GAME_MESSAGES', True, bool)
            }],

            # Server Balance
            "server_balance": [{
                "enabled": get_env('SERVER_BALANCE_ENABLED', False, bool),
                "level_categories": get_env('SERVER_BALANCE_LEVEL_CATEGORIES', [10, 25, 50, 100, 150, 200, 250], list),
                "combat_weights": get_env('SERVER_BALANCE_COMBAT_WEIGHTS', [0.1, 0.25, 0.25, 0.5, 1, 1, 1, 1.25], list),
                "webhook": get_env('SERVER_BALANCE_WEBHOOK', '')
            }],

            # Auto Level
            "auto_level": [{
                "enabled": get_env('AUTO_LEVEL_ENABLED', False, bool),
                "dryrun": get_env('AUTO_LEVEL_DRYRUN', False, bool),
                "min_level": get_env('AUTO_LEVEL_MIN_LEVEL', 50, int),
                "allow_vips": get_env('AUTO_LEVEL_ALLOW_VIPS', True, bool),
                "player_count": get_env('AUTO_LEVEL_PLAYER_COUNT', 60, int),
                "levelbug_enabled": get_env('AUTO_LEVEL_LEVELBUG_ENABLED', True, bool),
                "kick_message": get_env('AUTO_LEVEL_KICK_MESSAGE',
                    "Your level is below {min_level} or you don't own a VIP seat. This server has an adaptive level cap.")
            }],

            # Map Vote
            "map_vote": [{
                "enabled": get_env('MAP_VOTE_ENABLED', False, bool),
                "dryrun": get_env('MAP_VOTE_DRYRUN', False, bool),
                "activate_vote": get_env('MAP_VOTE_ACTIVATE_VOTE', 1, int),
                "dectivate_vote": get_env('MAP_VOTE_DEACTIVATE_VOTE', 0, int),
                "vote_channel_id": get_env('MAP_VOTE_CHANNEL_ID', 0, int),
                "reminder": get_env('MAP_VOTE_REMINDER', 20, int),
                "stealth_vote": get_env('MAP_VOTE_STEALTH_VOTE', False, bool),
                "max_reminders_per_game": get_env('MAP_VOTE_MAX_REMINDERS', 0, int),
                "vote_header": get_env('MAP_VOTE_HEADER', 'Vote for the nextmap on <your discord>'),
                "duplicate_maps": get_env('MAP_VOTE_DUPLICATE_MAPS', True, bool),
                "map_pool": [{
                    "day": get_env('MAP_POOL_DAY', 0, int),
                    "night": get_env('MAP_POOL_NIGHT', 0, int),
                    "wildcard": get_env('MAP_POOL_WILDCARD', 0, int),
                    "enforce": get_env('MAP_POOL_ENFORCE', 0, int),
                    "battle_mode": get_env('MAP_POOL_BATTLE_MODE', [], list),
                    "wildcard_mode": get_env('MAP_POOL_WILDCARD_MODE', [], list),
                    "enforced_maps": get_env('MAP_POOL_ENFORCED_MAPS', [], list),
                    "blacklist_maps": get_env('MAP_POOL_BLACKLIST_MAPS', [], list),
                    "exclude_played_maps": get_env('MAP_POOL_EXCLUDE_PLAYED_MAPS', 0, int)
                }]
            }]
        }]
    }

    return config


def ensure_config(config_path="config.json", template_path="template.json"):
    """
    Ensure config.json exists. If not, try to generate from environment variables.
    Returns True if config exists or was created, False otherwise.
    """
    if os.path.exists(config_path):
        logger.info(f"Using existing {config_path}")
        return True

    # Try to generate from environment variables
    logger.info(f"{config_path} not found, attempting to generate from environment variables...")

    config = generate_config_from_env()

    if config:
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=4)
        logger.info(f"Generated {config_path} from environment variables")
        return True

    # Check if template exists and provide helpful error
    if os.path.exists(template_path):
        logger.error(
            f"No {config_path} found and DISCORD_TOKEN environment variable not set.\n"
            f"For Railway deployment, set these environment variables:\n"
            f"  - DISCORD_TOKEN (required)\n"
            f"  - API_URL (RCON API endpoint)\n"
            f"  - STATS_URL (Stats API endpoint)\n"
            f"  - BEARER_TOKEN (RCON auth token)\n"
            f"\nOr copy {template_path} to {config_path} and configure manually."
        )
    else:
        logger.error(f"No {config_path} or {template_path} found.")

    return False
