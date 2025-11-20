
---

# 📌 **README.md — Development and Deployment of a Smart Contract using Solidity**



## **Theory**

### **Smart Contracts**

A smart contract is a self-executing program in which the terms of the agreement are written directly into code. Once deployed on a blockchain, it becomes immutable and automatically executes when predefined conditions are met, ensuring trustless, transparent transactions.

### **Solidity**

Solidity is the most widely used language for developing Ethereum smart contracts. It is statically typed and compiles into bytecode that runs on the Ethereum Virtual Machine (EVM).

### **Ethereum Blockchain**

Ethereum is a decentralized platform for executing smart contracts and building dApps. It uses Ether (ETH) as the native cryptocurrency for transaction fees (gas) and computation costs.

---

## **Key Concepts in Solidity**

* **Smart Contract Deployment:** Publishing the smart contract bytecode to the blockchain.
* **State Variables:** Variables stored permanently on the blockchain.
* **Functions:** Blocks of code defining logic and behavior within smart contracts.
* **Gas:** A computation fee paid in Ether for executing transactions or functions.
* **Public & Private Functions:** Public functions can be accessed externally; private functions are restricted to the contract.

---

## **Steps of Execution**

### **1. Setting Up Development Environment**

* Install **Node.js** and **npm**.
* Install Truffle globally:

  ```
  npm install -g truffle
  ```
* Install **Ganache** to simulate a local blockchain.
* Optionally use **Remix IDE** for browser-based smart contract development.

---

### **2. Writing the Smart Contract**

Initialize project:

```bash
mkdir SmartContractExample
cd SmartContractExample
truffle init
```

Create a new Solidity file under `contracts/`:

### **SimpleStorage.sol**

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract SimpleStorage {
 uint256 storedData;
 // Event to log data changes
 event DataStored(uint256 data);
 // Store a new value
 function set(uint256 x) public {
 storedData = x;
 emit DataStored(storedData);
 }
 // Retrieve the stored value
 function get() public view returns (uint256) {
 return storedData;
 }
}
```

---

### **3. Compile the Contract**

```bash
truffle compile
```

---

### **4. Deploy the Contract**

Create migration script `migrations/2_deploy_contracts.js`:

```javascript
const SimpleStorage = artifacts.require("SimpleStorage");

module.exports = function (deployer) {
  deployer.deploy(SimpleStorage);
};
```

Deploy to local Ganache:

```bash
truffle migrate
```

---

### **5. Interact With Deployed Contract**

Open Truffle console:

```bash
truffle console
```

Run:

```javascript
let instance = await SimpleStorage.deployed();
await instance.set(100);
let value = await instance.get();
console.log(value.toString());
```

---

### **6. Deploy to Test Network**

Configure `truffle-config.js`, then deploy:

```bash
truffle migrate --network rinkeby
```

---

## **Key Points**

* Solidity is the primary Ethereum smart contract language.
* Smart contracts are **immutable** once deployed.
* Every operation on Ethereum consumes **gas**.
* Truffle Suite provides development, testing, and deployment tools.
* Events are used for logging and tracking contract changes.

---

## **Conclusion**

This experiment demonstrated the complete workflow of developing, compiling, deploying, and interacting with a smart contract using Solidity and the Truffle framework. A SimpleStorage contract was successfully executed on both a local blockchain (Ganache) and an Ethereum test network. Smart contracts provide security, automation, and transparency, making them essential in modern decentralized applications.

---

# 📘 **Viva Questions & Answers (2–3 Lines Each)**

1. **What is a smart contract, and how does it differ from a traditional contract?**
   A smart contract is a self-executing program stored on a blockchain that runs automatically. Unlike traditional contracts, no intermediaries are needed and execution is trustless and automated.

2. **Explain the role of pragma in Solidity.**
   `pragma` specifies the compiler version used to compile the Solidity code, ensuring compatibility and preventing version-related issues.

3. **What are state variables in Solidity?**
   State variables store data permanently on the blockchain and are preserved between function calls.

4. **What is the purpose of gas in Ethereum?**
   Gas is the computational fee required to execute smart contracts or transactions, preventing misuse of network resources.

5. **What is the purpose of the event keyword in Solidity?**
   Events allow smart contracts to log data on the blockchain, enabling off-chain applications (like a frontend) to listen for updates.

6. **Explain the difference between public, private, and internal functions in Solidity.**
   Public functions can be called externally or internally. Private functions are accessible only within the same contract. Internal functions are accessible within the contract and derived contracts.

7. **What is the role of deployer.deploy() in the Truffle migration script?**
   It instructs Truffle to deploy the specified contract onto the blockchain as part of the migration process.

8. **How do you test a smart contract before deploying it to the mainnet?**
   Contracts are tested using local environments like Ganache or test networks such as Rinkeby, using tools like Truffle tests and Mocha.

9. **What is the Ethereum Virtual Machine (EVM)?**
   The EVM is a runtime environment where all Ethereum smart contracts execute, ensuring uniform execution across all nodes.

10. **What is a migration script in Truffle?**
    A migration script defines how smart contracts should be deployed to a blockchain, automating deployment steps.

---






Below is the **cleanly formatted code** followed by a **clear, step-by-step explanation** of how the Solidity smart contract and Ethers.js frontend work together in a simple decentralized application (dApp).

---

# ✅ **Formatted Smart Contract Code (HelloWorld.sol)**

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract HelloWorld {
    string public message;

    // Constructor executes once when contract is deployed
    constructor(string memory _message) {
        message = _message;
    }

    // Update stored message
    function setMessage(string memory _message) public {
        message = _message;
    }

    // Retrieve stored message
    function getMessage() public view returns (string memory) {
        return message;
    }
}
```

---

# 🌐 **Formatted Frontend Code (index.html + Ethers.js)**

```html
<!DOCTYPE html>
<html>
<head>
    <title>My dApp</title>
</head>
<body>
    <h2>Decentralized App Example</h2>

    <p id="currentMessage">Loading...</p>

    <input type="text" id="newMessage" placeholder="Enter new message">
    <button onclick="setMessage()">Update Message</button>

    <script src="https://cdn.jsdelivr.net/npm/ethers/dist/ethers.min.js"></script>

    <script>
        const contractAddress = "YOUR_CONTRACT_ADDRESS_HERE";  // Replace after deployment
        const contractABI = [ /* ABI from Remix */ ];

        // Load Ethereum provider (MetaMask) and contract
        async function loadContract() {
            if (window.ethereum) {
                // Requests MetaMask account access
                await ethereum.request({ method: "eth_requestAccounts" });

                const provider = new ethers.BrowserProvider(window.ethereum);
                const signer = await provider.getSigner();

                // Create contract instance
                window.contract = new ethers.Contract(contractAddress, contractABI, signer);

                // Fetch initial message
                getMessage();
            } else {
                alert("Please install MetaMask");
            }
        }

        // Read message from contract
        async function getMessage() {
            const msg = await window.contract.getMessage();
            document.getElementById("currentMessage").innerText = "Current Message: " + msg;
        }

        // Update contract message (writes to blockchain)
        async function setMessage() {
            const newMsg = document.getElementById("newMessage").value;

            const tx = await window.contract.setMessage(newMsg);  // Creates transaction
            await tx.wait();                                      // Wait for confirmation

            getMessage();  // Refresh display
        }

        loadContract();  // Auto-run on page load
    </script>
</body>
</html>
```






