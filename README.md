## 参考资料
Multichain开发者地址：https://etherscan.io/address/0xfa9da51631268a30ec3ddd1ccbf46c65fad99251    
源码：  
https://github.com/anyswap/anyswap-v1-core/blob/master/contracts/AnyswapV6ERC20.sol  
https://github.com/anyswap/anyswap-v1-core/blob/master/contracts/AnyswapV6Router.sol  


### 环境配置
合约部署者地址：0x69e8c16c735fD878c2a7B5C4DCA15f44fc81f69f
使用geth创建的地址：0xb3A03a7651e288447c326B213776F20f69A4cd4e
测试网：Kovan

### 1. 部署Anyswapv6Erc20合约

#### 查看合约构造函数
```solodity
constructor(string memory _name, string memory _symbol, uint8 _decimals, address _underlying, address _vault) {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        underlying = _underlying;
        if (_underlying != address(0)) {
            require(_decimals == IERC20(_underlying).decimals());
        }

        // Use init to allow for CREATE2 accross all chains
        _init = true;

        // Disable/Enable swapout for v1 tokens vs mint/burn for v3 tokens
        _vaultOnly = false;

        vault = _vault;
    }

```

通过查看已部署合约，猜测参数内容    
https://etherscan.io/address/0xfafa220145dfa5c3ec85b6fa8a75aee2451cde5e   

参数：  
```
_Name = Binance USD
_Symbol = anyBUSD
_DECIMALS = 18
_UNDERLYING = 0x4fabb145d64652a948d72533023f6e7a623c7c53 
_VALUT = 0x7782046601e7b9b05ca55a3899780ce6ee6b8b2b 
```
_UNDERLYING 为原生Token的合约地址，这里写的BUSD，由Binance官方部署的合约  
_VALUT 为Multichian开发者部署的合约，通过查看源码发现为AnyswapV6Router合约,发现部署了大量Anyswapv6Erc20合约，其中有的合约_VALUT参数为自身地址

#### 部署Anyswapv6Erc20合约
部署合约交易Hash:https://kovan.etherscan.io/tx/0x9afe517766e4aee42c1d2913f621b68a4a7da2e987f5ffe5f4ecbc46b56efc10  
Anyswapv6Erc20合约地址:https://kovan.etherscan.io/address/0x4a3f2880a14ac004f886f42c760aa605765e24bc
```
_Name = Wintermute LINK
_Symbol = winterLINK
_DECIMALS = 18
_UNDERLYING = 0xa36085F69e2889c224210F603D836748e7dC0088 
_VALUT = 0x69e8c16c735fD878c2a7B5C4DCA15f44fc81f69f 
```
_UNDERLYING 为Link的合约地址
_VALUT 为我自己的地址

### 2. 调用initValut设置为Keystore地址
1.使用geth创建以太坊账户  
keystore文件：/Users/r4bbit/Library/Ethereum/keystore/UTC--2022-06-21T06-37-33.413266000Z--b3a03a7651e288447c326b213776f20f69a4cd4
<img width="1060" alt="image" src="https://user-images.githubusercontent.com/68707030/174732966-90ae9674-1dab-4e12-b844-9d920dc2d318.png">

此时合约中vault为开发者地址
<img width="541" alt="image" src="https://user-images.githubusercontent.com/68707030/174733526-d1f8c8e2-c34d-4a9b-93b5-64c2116bf486.png">
通过调用initValut修改Valut地址
交易hash:https://kovan.etherscan.io/tx/0x5135cb67cb9783481f148da3f83d6b10134b89dee4bea2b2ee6d06026410b087
<img width="469" alt="image" src="https://user-images.githubusercontent.com/68707030/174734023-71393b84-73e8-421f-ae33-6e585a1cbe29.png">

