# 1.调用initValut设置Vault为自己控制的个人测试地址
# 2.调用合约mint币给自己
```python
Mint Function
Address:0xb3A03a7651e288447c326B213776F20f69A4cd4e Amount:10000.0
blockNumber:32311253
Timestamp:1655878992
transactionHash:0x6dde9b18f694d4f0ceaac554fd19f318004fe109145047078947876d29ba40fd
Logs:[{'address': '0x4a3f2880a14aC004f886f42C760aA605765e24bC', 'blockHash': '0x3ed6752afa2a02ab9954d1a77ace763c81f47a9315b9e0a77ddd025deb0ad22d', 'blockNumber': 32311253, 'data': '0x00000000000000000000000000000000000000000000021e19e0c9bab2400000', 'logIndex': 0, 'removed': False, 'topics': ['0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef', '0x0000000000000000000000000000000000000000000000000000000000000000', '0x000000000000000000000000b3a03a7651e288447c326b213776f20f69a4cd4e'], 'transactionHash': '0x6dde9b18f694d4f0ceaac554fd19f318004fe109145047078947876d29ba40fd', 'transactionIndex': 0, 'transactionLogIndex': '0x0', 'type': 'mined'}]
```
# 3.调用合约swapout
```python
Swap_out
Address:0xb3A03a7651e288447c326B213776F20f69A4cd4e Amount:10.0
blockNumber:32311257
Timestamp:1655879012
transactionHash:0xacb55853d65c0036ccdcb3d719312d0d8aea888427f8d7098116e35fbcee84bb
Logs:[{'address': '0x4a3f2880a14aC004f886f42C760aA605765e24bC', 'blockHash': '0xafc1950d54243d4493521fbab8907a5c81acac5be7b5f8cba7fd57b0f6316b4d', 'blockNumber': 32311257, 'data': '0x0000000000000000000000000000000000000000000000008ac7230489e80000', 'logIndex': 0, 'removed': False, 'topics': ['0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef', '0x000000000000000000000000b3a03a7651e288447c326b213776f20f69a4cd4e', '0x0000000000000000000000000000000000000000000000000000000000000000'], 'transactionHash': '0xacb55853d65c0036ccdcb3d719312d0d8aea888427f8d7098116e35fbcee84bb', 'transactionIndex': 2, 'transactionLogIndex': '0x0', 'type': 'mined'}, {'address': '0x4a3f2880a14aC004f886f42C760aA605765e24bC', 'blockHash': '0xafc1950d54243d4493521fbab8907a5c81acac5be7b5f8cba7fd57b0f6316b4d', 'blockNumber': 32311257, 'data': '0x0000000000000000000000000000000000000000000000008ac7230489e80000', 'logIndex': 1, 'removed': False, 'topics': ['0x6b616089d04950dc06c45c6dd787d657980543f89651aec47924752c7d16c888', '0x000000000000000000000000b3a03a7651e288447c326b213776f20f69a4cd4e', '0x000000000000000000000000b3a03a7651e288447c326b213776f20f69a4cd4e'], 'transactionHash': '0xacb55853d65c0036ccdcb3d719312d0d8aea888427f8d7098116e35fbcee84bb', 'transactionIndex': 2, 'transactionLogIndex': '0x1', 'type': 'mined'}]
```
# 4.获取swapout交易内容、交易区高、所在时间戳
