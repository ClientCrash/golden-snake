import hashlib
NONCE_LIMIT = 100000000
zeroes = 6
def mine(block_number,transactions,prev_hash,verbose):
    for nonce in range(NONCE_LIMIT):
        base_data_t = str(block_number)+transactions+prev_hash+str(nonce)
        
        hash_attempt = hashlib.sha256(base_data_t.encode()).hexdigest()
        #the next 2lines reduce the number of prints while still giving some output its very inefficient but its only for testing please remove for prod. i know there are better ways to do it
        if(str(nonce/1000000).endswith(".0") and verbose==1):
           print(str(nonce) + "         __ " + str(hash_attempt) + "   Percentage : " + str(nonce/NONCE_LIMIT)  )
        if hash_attempt.startswith('0' * zeroes):
            print("found hash with nonce " + str(nonce) + " base_data was => " + base_data_t + " hash was => " + hash_attempt)
            return hash_attempt
    return -1
def test():
    print("testing")
    bn = 683769

    tr = "0"
    ph = "00000000000000000009db795257557d836e6ecc9eb99871bc415779c82c7678"

    ct=str(bn)+tr+ph
    mine(bn,tr,ph,1)
