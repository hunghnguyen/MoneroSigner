# TODO: move this to monero-python, network related part should maybe move to .network?
"""
Based on:
https://github.com/monero-project/monero-gui/blob/master/js/Wizard.js#L134
"""
from datetime import date, datetime, timedelta
from time import time
from typing import Union, List


class NetDataException(Exception):
    pass


class NetData:
    birth: int  # epoch timestamp
    v2_block: int  # block
    v2_time: int  # epoch timestamp
    v1_seconds_per_block: int = 60
    v2_seconds_per_block: int = 120
    rollback: int = 0
    data: List['NetData'] = []

    @classmethod
    def get_instance(cls, net: str) -> 'NetData':
        if net not in cls.data:
            raise NetDataException(f'Network {net} unknown')
        return cls.data[net]


class MainData(NetData):
    birth: int = 1397818193
    v2_time: int = 1458748658
    v2_block: int = 1009827


class TestData(NetData):
    birth: int = 1410295020
    v2_time: int = 1448285909
    v2_block: int = 624634
    rollback: int = 342100


class StageData(NetData):
    birth: int = 1518932025
    v2_time: int = 1520937818
    v2_block: int = 32000
    rollback: int = 30000


NetData.data = {'main': MainData, 'test': TestData, 'stage': StageData}


def date_to_timestamp(d: date) -> int:
    return int(datetime.fromisoformat(d.isoformat()).timestamp())

def timestamp_to_date(ts: int) -> date:
    return datetime.fromtimestamp(ts).date()

def rollback(block: int, data: NetData) -> int:
    if data.rollback != 0 and block > data.rollback:
        return block - data.rollback
    return block

def get_approximate_blockchain_height(d: Union[int, date], net: Union[NetData, str] = 'main', suppress_exception: bool = False, security_margin_days: int = 30) -> int:
    if type(d) == int:
        d = date.fromtimestamp(d)
    data = NetData.get_instance(net) if type(net) == str else net
    t = int(date_to_timestamp(d - timedelta(days=security_margin_days)))  # I prefer to discount 30 days in the days instead of block calculations because of accuracy.
    if t < data.birth:
        if suppress_exception or date_to_timestamp(d) >= data.birth:  # remember we put the clock security_margin_days days back...
            return 0
        raise ValueError('Date BM (before Monero)')
    if t > data.birth and t < data.v2_time:
        return int(rollback((t - data.birth) / data.v1_seconds_per_block, data))
    if t >= data.v2_time:
        return int(rollback(data.v2_block + (t - data.v2_time) / data.v2_seconds_per_block, data))

def get_approximate_date(block: int, net: Union[NetData, str] = 'main', suppress_exception: bool = True) -> date:
    data = NetData.get_instance(net) if type(net) == str else net
    block = rollback(block, data)
    if block < 0:
        if suppress_exception:
            return 0
        raise ValueError('block needs to be a positive int')
    if block >= data.v2_block:
        return timestamp_to_date(data.v2_time + data.v2_seconds_per_block * (block - data.v2_block))
    return timestamp_to_date(data.birth + data.v1_seconds_per_block * block)


class MoneroTime:

    def __init__(self, network: Union[NetData,str], security_margin_days: int = 30, suppress_exception=True):
        self.data: NetData = network if isinstance(network, NetData) else NetData.get_instance(network)
        self.suppress_exception: bool = suppress_exception
        self.security_margin_days = security_margin_days

    def getDate(self, block: int) -> date:
        return get_approximate_date(block, self.data, self.suppress_exception)

    def getBlockchainHeight(self, d: Union[int, date]) -> int:
        return get_approximate_blockchain_height(d, self.data, self.suppress_exception, self.security_margin_days)
