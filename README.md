# Assignment_1
Python code which pulls the data from coingecko.com and filters out top N cryptocurrencies by market capitalization
## Installation
To use, you need to install the pycoingecko library by
PyPI

```bash
pip install pycoingecko
```

or from source

```bash
git clone https://github.com/man-c/pycoingecko.git>
cd pycoingecko
python3 setup.py install
```
Then you need to download the Python file named "Code.py" in srs folder. 
## Usage
To use this program you need to open terminal and open path to downloaded file.

```bash
cd path/to/Code.py/file 
```
Then you need to run code by Python
```bash
python3 Code.py
```
Then enter the number X. The application will show the top X cryptocurrencies.
## Examples
```bash
Please, enter a positive integer number:
2
[{'ath': 64805,
  'ath_change_percentage': -25.90589,
  'ath_date': '2021-04-14T11:54:46.763Z',
  'atl': 67.81,
  'atl_change_percentage': 70711.37285,
  'atl_date': '2013-07-06T00:00:00.000Z',
  'circulating_supply': 18819606.0,
  'current_price': 48004,
  'fully_diluted_valuation': 1008377616862,
  'high_24h': 48887,
  'id': 'bitcoin',
  'image': 'https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579',
  'last_updated': '2021-09-18T20:24:32.416Z',
  'low_24h': 47062,
  'market_cap': 903679497551,
  'market_cap_change_24h': 9610783084,
  'market_cap_change_percentage_24h': 1.07495,
  'market_cap_rank': 1,
  'max_supply': 21000000.0,
  'name': 'Bitcoin',
  'price_change_24h': 509.98,
  'price_change_percentage_24h': 1.07377,
  'roi': None,
  'symbol': 'btc',
  'total_supply': 21000000.0,
  'total_volume': 28097801694},
 {'ath': 4356.99,
  'ath_change_percentage': -21.85306,
  'ath_date': '2021-05-12T14:41:48.623Z',
  'atl': 0.432979,
  'atl_change_percentage': 786279.00397,
  'atl_date': '2015-10-20T00:00:00.000Z',
  'circulating_supply': 117578552.8115,
  'current_price': 3400.49,
  'fully_diluted_valuation': None,
  'high_24h': 3537.22,
  'id': 'ethereum',
  'image': 'https://assets.coingecko.com/coins/images/279/large/ethereum.png?1595348880',
  'last_updated': '2021-09-18T20:24:30.957Z',
  'low_24h': 3371.99,
  'market_cap': 400341847090,
  'market_cap_change_24h': -1387990241.5168457,
  'market_cap_change_percentage_24h': -0.3455,
  'market_cap_rank': 2,
  'max_supply': None,
  'name': 'Ethereum',
  'price_change_24h': -10.344573298251,
  'price_change_percentage_24h': -0.30329,
  'roi': {'currency': 'btc',
          'percentage': 9364.859426677556,
          'times': 93.64859426677556},
  'symbol': 'eth',
  'total_supply': None,
  'total_volume': 16364634615}]
Press any key to continue . . .
```
