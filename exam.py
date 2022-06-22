import json
import time
import traceback
import asyncio
from multichain_exam_config import *

# 1.调用initValut设置Vault为自己控制的个人测试地址
# 2.调用合约mint币给自己
# 3.调用合约swapout
# 4.获取swapout交易内容、交易区高、所在时间戳

address = web3.toChecksumAddress("0xb3a03a7651e288447c326b213776f20f69a4cd4e")
dev_key = "***"
dev_address = web3.toChecksumAddress("0x69e8c16c735fD878c2a7B5C4DCA15f44fc81f69f")
def get_private_key(keystore_path,password):
    with open(keystore_path) as keyfile:
        encrypted_key = keyfile.read()
    return web3.eth.account.decrypt(encrypted_key,password)


#signTransaction
def send_tx(_txn):
    private_key = get_private_key("/Users/r4bbit/Library/Ethereum/keystore/UTC--2022-06-21T06-37-33.413266000Z--b3a03a7651e288447c326b213776f20f69a4cd4e","1234")
    signed_txn = web3.eth.account.signTransaction(_txn, private_key=private_key)
    res = web3.eth.sendRawTransaction(signed_txn.rawTransaction).hex()
    txn_receipt = web3.eth.waitForTransactionReceipt(res)
    return txn_receipt

def dev_send_tx(_txn):
    signed_txn = web3.eth.account.signTransaction(_txn, private_key=dev_key)
    res = web3.eth.sendRawTransaction(signed_txn.rawTransaction).hex()
    txn_receipt = web3.eth.waitForTransactionReceipt(res)
    return txn_receipt


def mint(to_address,amount):

    """
    Mint Token

    :param to_address:
    :param amount:
    :return: transaction_hash
    """
    print(f"Mint Function \nAddress:{to_address} Amount:{amount/10**18}")
    txn = ANYSWAP_ERC20_CONTRACT.functions.mint(to_address,amount).buildTransaction(
        {
            'chainId': 42,
            'nonce': web3.eth.getTransactionCount(address),
            'gas': 3600000,
            'value': 0,  #
            'gasPrice': web3.eth.gasPrice,
        }
    )
    try:
        res = json.loads(web3.toJSON(send_tx(txn)))
    except Exception as e:
        traceback.print_exc()
        print(e)
    transaction_hash = res['logs'][0]['transactionHash']
    print(f"blockNumber:{res['blockNumber']}")
    print(f"Timestamp:{json.loads(web3.toJSON(web3.eth.getBlock(res['blockNumber'])))['timestamp']}")
    print(f"transactionHash:{transaction_hash}")
    print(f"Logs:{res['logs']}")

    return transaction_hash

def swap_out(bind_address,amount):
    print(f"Swap_out  \nAddress:{bind_address} Amount:{amount/10**18}")
    txn = ANYSWAP_ERC20_CONTRACT.functions.Swapout(amount,address).buildTransaction(
        {
            'chainId': 42,
            'nonce': web3.eth.getTransactionCount(address),
            'gas': 3600000,
            'value': 0,  #
            'gasPrice': web3.eth.gasPrice,
        }
    )
    try:
        res = json.loads(web3.toJSON(send_tx(txn)))


    except Exception as e:
        traceback.print_exc()
        print(e)

    transaction_hash = res['logs'][0]['transactionHash']
    print(f"blockNumber:{res['blockNumber']}")
    print(f"Timestamp:{json.loads(web3.toJSON(web3.eth.getBlock(res['blockNumber'])))['timestamp']}")
    print(f"transactionHash:{transaction_hash}")
    print(f"Logs:{res['logs']}")

    return transaction_hash


def get_mpc():
    mpc_address = ANYSWAP_ERC20_CONTRACT.functions.mpc().call()
    print(mpc_address)
    return mpc_address

def init_valut(valut_address):
    txn = ANYSWAP_ERC20_CONTRACT.functions.initVault(valut_address).buildTransaction(
        {
            'chainId': 42,
            'nonce': web3.eth.getTransactionCount(address),
            'gas': 3600000,
            'value': 0,  #
            'gasPrice': web3.eth.gasPrice,
        }
    )
    try:
        res = json.loads(web3.toJSON(send_tx(txn)))
        if len(res['logs']) == 0:
            print(f"Error:{res}")
            print(f"https://kovan.etherscan.io/tx/{res['transactionHash']}")
            exit()
    except Exception as e:
        traceback.print_exc()
        print(e)
    transaction_hash = res['logs'][0]['transactionHash']
    print(f"blockNumber:{res['blockNumber']}")
    print(f"Timestamp:{json.loads(web3.toJSON(web3.eth.getBlock(res['blockNumber'])))['timestamp']}")
    print(f"Logs:{res['logs']}")

    return transaction_hash
def change_vault(new_vault):
    txn = ANYSWAP_ERC20_CONTRACT.functions.changeVault(new_vault).buildTransaction(
        {
            'chainId': 42,
            'nonce': web3.eth.getTransactionCount(dev_address),
            'gas': 3600000,
            'value': 0,  #
            'gasPrice': web3.eth.gasPrice,
        }
    )
    try:
        res = json.loads(web3.toJSON(dev_send_tx(txn)))
        if len(res['logs']) == 0:
            print(f"Error:{res}")
            print(f"https://kovan.etherscan.io/tx/{res['transactionHash']}")
            exit()
    except Exception as e:
        traceback.print_exc()
        print(e)
    transaction_hash = res['logs'][0]['transactionHash']
    print(f"blockNumber:{res['blockNumber']}")
    print(f"Timestamp:{json.loads(web3.toJSON(web3.eth.getBlock(res['blockNumber'])))['timestamp']}")
    print(f"Logs:{res['logs']}")

    return transaction_hash


def main():
    change_vault(dev_address)

if __name__ == '__main__':
    main()
