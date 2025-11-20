#############################Experiment01########################################
'''
import datetime
import hashlib

# Step 3: Create Block class
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = (
            str(self.index)
            + self.timestamp
            + self.data
            + self.previous_hash
        )
        return hashlib.sha256(value.encode()).hexdigest()


# Step 4: Create Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, new_data):
        previous_block = self.get_last_block()
        new_block = Block(len(self.chain), new_data, previous_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Validate hash
            if current.hash != current.calculate_hash():
                return False

            # Validate chain linkage
            if current.previous_hash != previous.hash:
                return False

        return True


# Step 5: Add blocks and test
my_blockchain = Blockchain()
my_blockchain.add_block("Transaction Data for Block 1")
my_blockchain.add_block("Transaction Data for Block 2")

# Display all blocks
for block in my_blockchain.chain:
    print(f"Index: {block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Hash: {block.hash}")
    print(f"Previous Hash: {block.previous_hash}\n")

# Validate chain
print("Is Blockchain valid?", my_blockchain.is_chain_valid())

'''
###############################Experiment 02 ##################################################################################

'''
# Program: Hashing using SHA-256 to ensure data integrity
import hashlib
# Input Data
data = "DataIntegrity123"
# Step 1: Encode data to bytes
encoded_data = data.encode()
# Step 2: Create SHA-256 hash
hash_object = hashlib.sha256(encoded_data)
# Step 3: Get the hexadecimal digest
hex_dig = hash_object.hexdigest()
# Display the hash
print("Original Data:", data)
print("SHA-256 Hash:", hex_dig)
# Optional: Modify data and hash again
modified_data = "DataIntegrity124"
modified_hash = hashlib.sha256(modified_data.encode()).hexdigest()
print("\nModified Data:", modified_data)
print("SHA-256 Hash (Modified):", modified_hash)
'''
##############################################################Experiment03 ####################################################




#Proof of Work
import hashlib
import time

# PoW Simulation: Mining a block by finding a valid hash
def proof_of_work(data, difficulty):
    nonce = 0
    target = '0' * difficulty  # Target difficulty with leading zeros

    while True:
        # Combine the data and nonce
        block_data = f"{data}{nonce}"

        # Hash the combined data
        hash_result = hashlib.sha256(block_data.encode()).hexdigest()

        # Check if the hash meets the target difficulty
        if hash_result.startswith(target):
            return nonce, hash_result

        nonce += 1


# Example Data
data = "Block #1"
difficulty = 4  # Difficulty level (number of leading zeros)

start_time = time.time()
nonce, valid_hash = proof_of_work(data, difficulty)
end_time = time.time()

print("Proof of Work - Mining Successful!")
print(f"Nonce: {nonce}")
print(f"Valid Hash: {valid_hash}")
print(f"Time Taken: {end_time - start_time} seconds")


#✅ Python Program to Simulate Proof-of-Stake (PoS)

import random

# PoS Simulation: Validator selection based on stake
def proof_of_stake(validators):
    total_stake = sum(stake for _, stake in validators.items())

    # Randomly select a validator based on their stake
    chosen_stake = random.randint(1, total_stake)
    cumulative_stake = 0

    for validator, stake in validators.items():
        cumulative_stake += stake
        if cumulative_stake >= chosen_stake:
            return validator


# Example Validators and Their Stakes
validators = {
    "Validator_A": 50,
    "Validator_B": 30,
    "Validator_C": 20
}

chosen_validator = proof_of_stake(validators)
print(f"Proof of Stake - Chosen Validator: {chosen_validator}")
