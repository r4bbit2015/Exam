## 参考资料
Multichain开发者地址：https://etherscan.io/address/0xfa9da51631268a30ec3ddd1ccbf46c65fad99251    
源码：  
https://github.com/anyswap/anyswap-v1-core/blob/master/contracts/AnyswapV6ERC20.sol  
https://github.com/anyswap/anyswap-v1-core/blob/master/contracts/AnyswapV6Router.sol  


### 环境配置
我的地址：0x69e8c16c735fD878c2a7B5C4DCA15f44fc81f69f  
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
_VALUT 为Multichian开发者部署的合约，通过查看源码发现为AnyswapV6Router合约

#### 开始部署Anyswapv6Erc20合约
交易hash:https://kovan.etherscan.io/tx/0x4002c4cec17ae3145932845df3a24975c682ffbcaac4ed4a9f5b873e7c5f51a2
```
_Name = Wintermute LINK
_Symbol = winterLINK
_DECIMALS = 18
_UNDERLYING = 0xa36085F69e2889c224210F603D836748e7dC0088 
_VALUT = 0x69e8c16c735fD878c2a7B5C4DCA15f44fc81f69f 
```
_UNDERLYING 为Link的合约地址
_VALUT 为我自己的地址
