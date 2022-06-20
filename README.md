## Multichain开发者地址
https://etherscan.io/address/0xfa9da51631268a30ec3ddd1ccbf46c65fad99251  
在这里可以看到很多合约部署的记录，我直接对着抄  

### 1. 部署Anyswapv6Erc20合约
https://etherscan.io/tx/0xf51701cfa0e16473330019824be2961224cb4e43e4df2f41b09fead93662518a

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
