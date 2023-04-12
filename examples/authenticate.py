# -*- coding: utf-8 -*-

# 微信公众号：AlgoPlus
# 官网：http://algo.plus
# 项目地址：https://gitee.com/AlgoPlus/

from multiprocessing import Queue
from AlgoPlus.CTP.AuthenticateHelper import run_authenticate
from AlgoPlus.CTP.FutureAccount import get_simulate_account

if __name__ == '__main__':
    # 账户
    account = get_simulate_account(
        investor_id='',  # 账户
        password='',  # 密码
        server_name='',  # 电信1、电信2、移动、TEST、N视界
    )

    # future_account = FutureAccount(
    #     broker_id='',  # 期货公司BrokerID
    #     server_dict={'TDServer': "ip:port", 'MDServer': 'ip:port'},  # TDServer为交易服务器，MDServer为行情服务器。服务器地址格式为"ip:port。"
    #     reserve_server_dict={},  # 备用服务器地址
    #     investor_id='',  # 账户
    #     password='',  # 密码
    #     app_id='simnow_client_test',  # 认证使用AppID
    #     auth_code='0000000000000000',  # 认证使用授权码
    #     subscribe_list=[],  # 订阅合约列表
    #     md_flow_path='./log',  # MdApi流文件存储地址，默认MD_LOCATION
    #     td_flow_path='./log',  # TraderApi流文件存储地址，默认TD_LOCATION
    # )

    # 参数
    parameter_dict = {
        'ExchangeID': b'SHFE',  # 交易所
        'InstrumentID': b'rb2310',  # 合约代码
        'UpperLimitPrice': 4380,  # 涨停板
        'LowerLimitPrice': 3511,  # 跌停板
        'Volume': 1,  # 报单手数
    }

    # 共享队列
    share_queue = Queue(maxsize=100)
    share_queue.put(parameter_dict)

    #
    run_authenticate(account, share_queue)
