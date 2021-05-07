"""
A module for obtaining repo readme and language data from the github API.

Before using this module, read through it, and follow the instructions marked
TODO.

After doing so, run it like this:

    python acquire.py

To create the `data.json` file that contains the data.
"""
import os
import json
from typing import Dict, List, Optional, Union, cast
import requests

from env import github_token, github_username

# TODO: Make a github personal access token.
#     1. Go here and generate a personal access token https://github.com/settings/tokens
#        You do _not_ need select any scopes, i.e. leave all the checkboxes unchecked
#     2. Save it in your env.py file under the variable `github_token`
# TODO: Add your github username to your env.py file under the variable `github_username`
# TODO: Add more repositories to the `REPOS` list below.

REPOS = [
    'bitcoin/bitcoin',
 'ccxt/ccxt',
 'freqtrade/freqtrade',
 'DeviaVir/zenbot',
 'lbryio/lbry-sdk',
 'monero-project/monero',
 'dvf/blockchain',
 'lightningnetwork/lnd',
 'mimblewimble/grin',
 'xmrig/xmrig',
 'tendermint/tendermint',
 'StockSharp/StockSharp',
 'edeng23/binance-trade-bot',
 'ripple/rippled',
 'input-output-hk/cardano-sl',
 'michaelgrosner/tribeca',
 'Scanate/EthList',
 'Zheaoli/awesome-coins',
 'RomelTorres/alpha_vantage',
 'itheima1/BlockChain',
 'coinpride/CryptoList',
 'status-im/status-react',
 'sammchardy/python-binance',
 'nanocurrency/nano-node',
 'lbryio/lbrycrd',
 'Jeiwan/blockchain_go',
 'ethereum/pyethereum',
 'bcoin-org/bcoin',
 'Xel/Blockchain-stuff',
 'cosmos/cosmos-sdk',
 'jesse-ai/jesse',
 'imfly/bitcoin-on-nodejs',
 'miguelmota/cointop',
 'ctubio/Krypto-trading-bot',
 'enigmampc/catalyst',
 'chrisleekr/binance-trading-bot',
 'liuchengxu/blockchain-tutorial',
 'thrasher-corp/gocryptotrader',
 'blockstack/stacks',
 'cazala/coin-hive',
 'spothq/cryptocurrency-icons',
 'owocki/pytrader',
 'yasinkuyu/binance-trader',
 'CoinAlpha/hummingbot',
 'cosme12/SimpleCoin',
 'bichenkk/coinmon',
 'zvtvz/zvt',
 'MPOS/php-mpos',
 'anandanand84/technicalindicators',
 'Haehnchen/crypto-trading-bot',
 'notadamking/RLTrader',
 'alpacahq/marketstore',
 'lightningnetwork/lightning-rfc',
 'bitcoin-dot-org/Bitcoin.org',
 'CyberPunkMetalHead/Binance-News-Sentiment-Bot',
 'bitshares/bitshares-core',
 'qtumproject/qtum',
 'seanjameshan/blockchain-cli',
 'BitBotFactory/MikaLendingBot',
 'Uniswap/uniswap-v2-core',
 'jmfernandes/robin_stocks',
 'xFFFFF/Gekko-Strategies',
 'jaggedsoft/node-binance-api',
 'stellar/go',
 'arnaucube/coffeeMiner',
 'nimiq/core-js',
 'Superalgos/Superalgos',
 'georgezouq/awesome-ai-in-finance',
 'foolcage/fooltrader',
 'cosmos/cosmos',
 'polakowo/vectorbt',
 'BlueWallet/BlueWallet',
 'aeternity/aeternity',
 'ACINQ/eclair',
 'conradoqg/naivecoin',
 'freqtrade/freqtrade-strategies',
 'zone117x/node-open-mining-portal',
 'mzheravin/exchange-core',
 'BitcoinExchangeFH/BitcoinExchangeFH',
 'lightninglabs/lightning-app',
 'input-output-hk/daedalus',
 'moneymanagerex/moneymanagerex',
 'Stadicus/RaspiBolt',
 'manu354/cryptocurrency-arbitrage',
 'michaelliao/cryptocurrency',
 'coinbase/coinbase-pro-trading-toolkit',
 'Drakkar-Software/OctoBot',
 'MinaProtocol/mina',
 'AllienWorks/cryptocoins',
 'jsappme/node-binance-trader',
 'Ebookcoin/ebookcoin',
 'bellaj/Blockchain',
 'paulpierre/informer',
 'monero-project/monero-gui',
 'trustwallet/wallet-core',
 'bmoscon/cryptofeed',
 'Roibal/Cryptocurrency-Trading-Bots-Python-Beginner-Advance',
 'chubin/rate.sx',
 'LedgerHQ/ledger-live-desktop',
 'trentpiercy/trace',
 'wardbradt/peregrine',
 'bonesoul/CoiniumServ',
 'stellar/kelp',
 'nicehash/NiceHashQuickMiner',
 'ZENALC/algobot',
 'JerBouma/FinanceDatabase',
 'ericjang/cryptocurrency_arbitrage',
 'imbaniac/awesome-blockchain',
 'square/subzero',
 'ericsomdahl/python-bittrex',
 'decred/dcrd',
 'ryancdotorg/brainflayer',
 'BeamMW/beam',
 'beurtschipper/crackcoin',
 'cbailes/awesome-deep-trading',
 'ScottfreeLLC/AlphaPy',
 'status-im/status-go',
 'lightninglabs/neutrino',
 'lionsharecapital/lionshare-desktop',
 'xd4rker/MinerBlock',
 'veox/python3-krakenex',
 's4w3d0ff/python-poloniex',
 'pirate/crypto-trader',
 'skycoin/skycoin',
 'firoorg/firo',
 'gazbert/bxbot',
 'saniales/golang-crypto-trading-bot',
 'bmino/binance-triangle-arbitrage',
 'JulyIghor/QtBitcoinTrader',
 'hyperledger-labs/Scorex',
 'anfederico/gemini',
 'enzoampil/fastquant',
 'jjxtra/ExchangeSharp',
 'lucasjones/cpuminer-multi',
 'bitshares/bitshares-ui',
 'botupdate/botupdate',
 'stellar/js-stellar-sdk',
 'decred/atomicswap',
 'AschPlatform/asch',
 'HuobiRDCenter/huobi_Python',
 'khuangaf/CryptocurrencyPrediction',
 'GetScatter/ScatterDesktop',
 'BANKEX/web3swift',
 'wassname/rl-portfolio-management',
 'bradoyler/xmr-miner',
 'sdcoffey/techan',
 'JKorf/Binance.Net',
 'carsenk/explorer',
 'Haseeb-Qureshi/lets-build-a-blockchain',
 'todxx/teamredminer',
 'deeponion/deeponion-legacy',
 'wlox/wlox',
 'piquette/finance-go',
 'lhartikk/naivecoin',
 'digital-dreamer/blockchain-programming',
 'pmaji/crypto-whale-watching-app',
 'bwentzloff/trading-bot',
 'status-im/nimbus-eth1',
 'kilimchoi/cryptocurrency',
 'Conflux-Chain/conflux-rust',
 'robinmonjo/coincoin',
 'geraldoramos/crypto-bar',
 'aloysius-pgast/crypto-exchanges-gateway',
 'kelvinau/crypto-arbitrage',
 'Overtorment/awesome-smart-contracts',
 'cazala/coin-hive-stratum',
 'Ekliptor/WolfBot',
 'altangent/ccxws',
 'jaggedsoft/php-binance-api',
 'EtherbitHQ/donut',
 'AsyncAlgoTrading/algo-coin',
 'AleoHQ/wagyu',
 'ico-check/ico-check',
 'LesterCovax/crypto-sheets',
 'ZenGo-X/multi-party-ecdsa',
 'sadighian/crypto-rl',
 'nuls-io/nuls',
 'Tau-Coin/tautcoin',
 'cryptean/bitcoinlib',
 'indreklasn/react-native-redux-crypto-tracker',
 'djirdehh/crypto_vue',
 'antoinevulcain/Financial-Modeling-Prep-API',
 'timolson/cointrader',
 'EthVentures/CryptoTracker',
 'MinterTeam/minter-go-node',
 'cryptofinance-ai/cryptofinance-google-sheets-add-on',
 'man-c/pycoingecko',
 '51bitquant/51bitquant',
 'blockchain/blockchain-wallet-v4-frontend',
 '3s3s/opentrade',
 '0b01/tectonicdb',
 'iotaledger/iota.py',
 'CryptoGnome/Profit-Trailer-Settings',
 'gitbitex/gitbitex-spot',
 'iotaledger/iota.go',
 'Uniswap/uniswap-v2-periphery',
 'C0nw0nk/Nginx-Lua-Anti-DDoS',
 'Uniswap/uniswap-v1',
 'zoeyg/binance',
 'guptarohit/cryptoCMD'
]

headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )


def github_api_request(url: str) -> Union[List, Dict]:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)}"
        )
    return response_data


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos/{repo}"
    repo_info = github_api_request(url)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        if "language" not in repo_info:
            raise Exception(
                "'language' key not round in response\n{}".format(json.dumps(repo_info))
            )
        return repo_info["language"]
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    contents = github_api_request(url)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    readme_download_url = get_readme_download_url(contents)
    if readme_download_url == "":
        readme_contents = ""
    else:
        readme_contents = requests.get(readme_download_url).text
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data() -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    return [process_repo(repo) for repo in REPOS]


if __name__ == "__main__":
    data = scrape_github_data()
    json.dump(data, open("data.json", "w"), indent=1)
