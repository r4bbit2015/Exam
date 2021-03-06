### 1.调用initValut设置Vault为自己控制的个人测试地址   
（尝试了8次都无法再次调用initValut函数，后来突然想起来这个应该是 除非重新部署合约，否则initVault应该是只能钓用一次。这里我选择使用changeVault修改Valut)
```python
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
```
### changeVault
```python
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

```
交易HASH:https://kovan.etherscan.io/tx/0x391b7a3ebed17a086f9d2398af2290697109261dd846074f642020b97c9c530c  
成功修改为0x69e8c16c735fd878c2a7b5c4dca15f44fc81f69f
Input
```python
blockNumber:32311631
Timestamp:1655880840
Logs:[{'address': '0x4a3f2880a14aC004f886f42C760aA605765e24bC', 'blockHash': '0x023e24345c829d06d0ca00c309de143078e1141c2b706cae341e104b8bc2fb5b', 'blockNumber': 32311631, 'data': '0x', 'logIndex': 8, 'removed': False, 'topics': ['0x5c364079e7102c27c608f9b237c735a1b7bfa0b67f27c2ad26bad447bf965cac', '0x00000000000000000000000069e8c16c735fd878c2a7b5c4dca15f44fc81f69f', '0x00000000000000000000000069e8c16c735fd878c2a7b5c4dca15f44fc81f69f', '0x0000000000000000000000000000000000000000000000000000000062b2bc88'], 'transactionHash': '0x391b7a3ebed17a086f9d2398af2290697109261dd846074f642020b97c9c530c', 'transactionIndex': 2, 'transactionLogIndex': '0x0', 'type': 'mined'}]
```
<img width="409" alt="image" src="https://user-images.githubusercontent.com/68707030/174963780-99024831-64ae-43be-b2fc-60cac79a1d5a.png">

### 2.调用合约mint币给自己、输出交易内容、交易区高、所在时间戳
```python
def mint(to_address,amount):
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
```
交易Hash:https://kovan.etherscan.io/tx/0x6dde9b18f694d4f0ceaac554fd19f318004fe109145047078947876d29ba40fd  

Input:
```python
Mint Function
Address:0xb3A03a7651e288447c326B213776F20f69A4cd4e Amount:10000.0
blockNumber:32311253
Timestamp:1655878992
transactionHash:0x6dde9b18f694d4f0ceaac554fd19f318004fe109145047078947876d29ba40fd
Logs:[{'address': '0x4a3f2880a14aC004f886f42C760aA605765e24bC', 'blockHash': '0x3ed6752afa2a02ab9954d1a77ace763c81f47a9315b9e0a77ddd025deb0ad22d', 'blockNumber': 32311253, 'data': '0x00000000000000000000000000000000000000000000021e19e0c9bab2400000', 'logIndex': 0, 'removed': False, 'topics': ['0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef', '0x0000000000000000000000000000000000000000000000000000000000000000', '0x000000000000000000000000b3a03a7651e288447c326b213776f20f69a4cd4e'], 'transactionHash': '0x6dde9b18f694d4f0ceaac554fd19f318004fe109145047078947876d29ba40fd', 'transactionIndex': 0, 'transactionLogIndex': '0x0', 'type': 'mined'}]
```
### 3.调用合约swapout、输出交易内容、交易区高、所在时间戳
```python
def swap_out(bind_address,amount):
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
```
交易HASH:https://kovan.etherscan.io/tx/0xacb55853d65c0036ccdcb3d719312d0d8aea888427f8d7098116e35fbcee84bb  

Input:  
```python
Swap_out
Address:0xb3A03a7651e288447c326B213776F20f69A4cd4e Amount:10.0
blockNumber:32311257
Timestamp:1655879012
transactionHash:0xacb55853d65c0036ccdcb3d719312d0d8aea888427f8d7098116e35fbcee84bb
Logs:[{'address': '0x4a3f2880a14aC004f886f42C760aA605765e24bC', 'blockHash': '0xafc1950d54243d4493521fbab8907a5c81acac5be7b5f8cba7fd57b0f6316b4d', 'blockNumber': 32311257, 'data': '0x0000000000000000000000000000000000000000000000008ac7230489e80000', 'logIndex': 0, 'removed': False, 'topics': ['0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef', '0x000000000000000000000000b3a03a7651e288447c326b213776f20f69a4cd4e', '0x0000000000000000000000000000000000000000000000000000000000000000'], 'transactionHash': '0xacb55853d65c0036ccdcb3d719312d0d8aea888427f8d7098116e35fbcee84bb', 'transactionIndex': 2, 'transactionLogIndex': '0x0', 'type': 'mined'}, {'address': '0x4a3f2880a14aC004f886f42C760aA605765e24bC', 'blockHash': '0xafc1950d54243d4493521fbab8907a5c81acac5be7b5f8cba7fd57b0f6316b4d', 'blockNumber': 32311257, 'data': '0x0000000000000000000000000000000000000000000000008ac7230489e80000', 'logIndex': 1, 'removed': False, 'topics': ['0x6b616089d04950dc06c45c6dd787d657980543f89651aec47924752c7d16c888', '0x000000000000000000000000b3a03a7651e288447c326b213776f20f69a4cd4e', '0x000000000000000000000000b3a03a7651e288447c326b213776f20f69a4cd4e'], 'transactionHash': '0xacb55853d65c0036ccdcb3d719312d0d8aea888427f8d7098116e35fbcee84bb', 'transactionIndex': 2, 'transactionLogIndex': '0x1', 'type': 'mined'}]
```
### 4.调用MPC
```python
def get_mpc():
    mpc_address = ANYSWAP_ERC20_CONTRACT.functions.mpc().call()
    print(mpc_address)
    return mpc_address
```
Input:

```python
0xb3A03a7651e288447c326B213776F20f69A4cd4e
```
全部源码:https://github.com/r4bbit2015/Exam/blob/main/exam.py  
