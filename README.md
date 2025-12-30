# Hell Let Loose (HLL) map vote and discord utilities

![Discord](https://img.shields.io/discord/1278466021564485684?color=%237289da&label=discord)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/gryhon/hll_discord_utils)

Connect with us on Discord for feedback, troubleshooting, and update information: https://discord.gg/wrtb

<a href="https://discord.gg/wrtb">
  <img src="https://github.com/Gryhon/hll_discord_utils/blob/public/Assets/wrtb.png" alt="[Alt-Text](https://discord.gg/wrtb)" height="120">
</a>

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/gryhon)

***

### Deploy on Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/StoneyRebel/hll_discord_utils-1-button-railway)

**One-click deployment to Railway:**

1. Click the "Deploy on Railway" button above (or deploy directly from your fork)
2. Set the required environment variables:
   - `DISCORD_TOKEN` - Your Discord bot token (required)
   - `API_URL` - Your RCON API endpoint URL
   - `STATS_URL` - Your Stats API endpoint URL
   - `BEARER_TOKEN` - Your RCON authentication token
3. Enable features by setting their environment variables (see below)
4. Deploy!

<details>
<summary><b>Environment Variables Reference</b></summary>

**Required:**
| Variable | Description |
|----------|-------------|
| `DISCORD_TOKEN` | Discord bot token |
| `API_URL` | RCON API endpoint |
| `STATS_URL` | Stats API endpoint |
| `BEARER_TOKEN` | RCON auth token |

**Optional:**
| Variable | Default | Description |
|----------|---------|-------------|
| `SERVER_NUMBER` | 1 | Server identifier |
| `LOG_LEVEL` | INFO | Logging level |

**Feature Toggles (set to `true` to enable):**
| Variable | Feature |
|----------|---------|
| `REGISTER_PLAYER_ENABLED` | Player registration |
| `COMFORT_FUNCTIONS_ENABLED` | Comfort functions |
| `MAP_ROTATION_ENABLED` | Map rotation tracking |
| `SERVER_STATUS_ENABLED` | Server status updates |
| `ARTILLERY_CALCULATOR_ENABLED` | Artillery calculator |
| `SERVER_BALANCE_ENABLED` | Server balance |
| `AUTO_LEVEL_ENABLED` | Adaptive level cap |
| `MAP_VOTE_ENABLED` | Map voting |

**Feature-Specific Variables:**

*Map Vote:*
- `MAP_VOTE_CHANNEL_ID` - Discord channel ID for voting
- `MAP_VOTE_DRYRUN` - Test mode (true/false)

*Auto Level:*
- `AUTO_LEVEL_MIN_LEVEL` - Minimum level requirement
- `AUTO_LEVEL_PLAYER_COUNT` - Player count threshold

*Webhooks:*
- `MAP_ROTATION_WEBHOOK` - Webhook URL for map rotation
- `SERVER_STATUS_WEBHOOK` - Webhook URL for server status
- `SERVER_BALANCE_WEBHOOK` - Webhook URL for server balance

</details>

***

### General

CRCON is mainly designed and developed for PC gamers. For example, it is not possible for console players to use a keyboard to enter data in  the chat window. This tool framework is mainly (but not exclusively) aimed at console players.

> [!Note] 
> The main reason for developing this tool set is, to provide the `"map vote function"` for console players.<br>
> Meanwhile, additional features have been added. Enjoy! :smile: 

> [!TIP]
> Each feature (module) runs independently and can be used separately.<br>
> --> _For using enhanced features, dependencies between the moduls might be necessary._ <--

***

### Links

[Wiki](https://github.com/Gryhon/hll_discord_utils/wiki)

- [Features](https://github.com/Gryhon/hll_discord_utils/wiki/Features)
  - [Map Vote](https://github.com/Gryhon/hll_discord_utils/wiki/Features#vote-map)
  - [Adaptive Level Cap](https://github.com/Gryhon/hll_discord_utils/wiki/Features/#adaptive-level-cap)
  - [Server Balance](https://github.com/Gryhon/hll_discord_utils/wiki/Features/#server-balance)
  - [Server Status](https://github.com/Gryhon/hll_discord_utils/wiki/Features/#Server-Status)
  - [Map Rotation](https://github.com/Gryhon/hll_discord_utils/wiki/Features/#map-rotation)
  - [Comfort](https://github.com/Gryhon/hll_discord_utils/wiki/Features/#comfort)
  - [Artillery Calculator](https://github.com/Gryhon/hll_discord_utils/wiki/Features/#artillery-calculator)
  - [Player Registration](https://github.com/Gryhon/hll_discord_utils/wiki/Features/#player-registration)

- [Installation](https://github.com/Gryhon/hll_discord_utils/wiki/Installation)
  - [Limitation](https://github.com/Gryhon/hll_discord_utils/wiki/Installation#installation)
  - [Precondition](https://github.com/Gryhon/hll_discord_utils/wiki/Installation#2-precondition)
  - [Get hll_dicord_utils](https://github.com/Gryhon/hll_discord_utils/wiki/Installation#4-get-the-hll_discord_utils-from-github)
  - [Config file](https://github.com/Gryhon/hll_discord_utils/wiki/Installation#5-edit-the-config-file)
  - [Start Docker container](https://github.com/Gryhon/hll_discord_utils/wiki/Installation#5-start-the-docker-container)
  - [Update the repository](https://github.com/Gryhon/hll_discord_utils/wiki/Installation#6-update-the-the-repository)
  - [Useful commands](https://github.com/Gryhon/hll_discord_utils/wiki/Installation#7-useful-commands)

- [Update Software](https://github.com/Gryhon/hll_discord_utils/wiki/Update-Sofware)
  - [v1.0.0 -> v1.1.0](https://github.com/Gryhon/hll_discord_utils/wiki/Update-Sofware#update-from---v100-to-v110)
  - [v1.1.0 -> v1.1.1](https://github.com/Gryhon/hll_discord_utils/wiki/Update-Sofware#update-from---v110-to-v111)
  - [v1.1.1 -> v1.1.2](https://github.com/Gryhon/hll_discord_utils/wiki/Update-Sofware#update-from---v111-to-v112)
  - [v1.1.2 -> v1.1.3](https://github.com/Gryhon/hll_discord_utils/wiki/Update-Sofware#update-from---v112-to-v113)
  - [v1.1.3 -> v1.1.4](https://github.com/Gryhon/hll_discord_utils/wiki/Update-Sofware#update-from---v113-to-v114)
  - [v1.1.4 -> v1.1.5](https://github.com/Gryhon/hll_discord_utils/wiki/Update-Sofware#update-from---v114-to-v115)

- [FAQ](https://github.com/Gryhon/hll_discord_utils/wiki/FAQ)
