# config
# If you're not using a proxy, you can leave the value blank, no need to remove it.
import os 
from dotenv import load_dotenv


load_dotenv()

api_info = {
    'okx': {
        'apiKey': os.environ.get('OKX_API_KEY'),
        'secret': os.environ.get('OKX_API_SECRET'),
        'password': os.environ.get('OKX_API_PASSWORD'),
        'proxy_url': os.environ.get('OKX_API_PROXY')
    },
    'binance': {
        'apiKey': os.environ.get('BINANCE_API_KEY'),
        'secret': os.environ.get('BINANCE_API_SECRET'),
        'proxy_url': os.environ.get('BINANCE_API_PROXY')
    },
    'kucoin': {
        'apiKey': os.environ.get('KUCOIN_API_KEY'),
        'secret': os.environ.get('KUCOIN_API_SECRET'),
        'password': os.environ.get('KUCOIN_API_PASSWORD'),
        'proxy_url': os.environ.get('KUCOIN_API_PROXY')
    },
    'mexc': {
        'apiKey': os.environ.get('MEXC_API_KEY'),
        'secret': os.environ.get('MEXC_API_SECRET'),
        'proxy_url': os.environ.get('MESC_API_PROXY')
    },
    'huobi': {
        'apiKey': os.environ.get('HTX_API_KEY'),
        'secret': os.environ.get('HTX_API_SECRET'),
        'proxy_url': os.environ.get('HTX_API_PROXY')
    },
    'gate': {
        'apiKey': os.environ.get('GATE_API_KEY'),
        'secret': os.environ.get('GATE_API_SECRET'),
        'proxy_url': os.environ.get('GATE_API_PROXY')
    },
    'bitget': {
        'apiKey': os.environ.get('BITGET_API_KEY'),
        'secret': os.environ.get('BITGET_API_SECRET'),
        'password': os.environ.get('BITGET_API_PASSWORD'),
        'proxy_url': os.environ.get('BITGET_API_PROXY')
    },
}