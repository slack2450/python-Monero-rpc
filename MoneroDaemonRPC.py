import requests, json

header = {
    "Content-Type":"application/json"
    }

params = {}

data = {
    "jsonrpc":"2.0",
    "id":"0"
    }

url = "http://127.0.0.1:18081/json_rpc" 


def getBlockCount():
    data["method"] = "getblockcount"
    dataEncoded = json.dumps(data)
    response = requests.post(url,data=dataEncoded,headers=header)
    return response.json()

def onGetBlockHash(blockHeight):
    data["method"] = "on_getblockhash"
    data["params"] = [blockHeight]
    dataEncoded = json.dumps(data)
    response = requests.post(url,data=dataEncoded,headers=header)
    return response.json()

def getBlockTemplate(walletAddress,reserveSize):
    data["method"] = "getblocktemplate"
    params["wallet_address"] = walletAddress
    params["reserve_size"] = reserveSize #Haha you're fucked.
    data["params"] = params
    dataEncoded = json.dumps(data)
    response = requests.post(url,data=dataEncoded,headers=header)
    return response.json()

def getLastBlockHeader():
    data["method"] = "getlastblockheader"
    dataEncoded = json.dumps(data)
    response = requests.post(url,data=dataEncoded, headers=header)
    return response.json()

def getBlockHeaderByHash(Hash):
    data["method"] = "getblockheaderbyhash"
    params["hash"] = Hash
    data["params"] = params
    dataEncoded = json.dumps(data)
    response = requests.post(url,data=dataEncoded, headers=header)
    return response.json()

def getBlockHeaderByHeight(height):
    data["method"] = "getblockheaderbyheight"
    params["height"] = height
    data["params"] = params
    dataEncoded = json.dumps(data)
    response = requests.post(url,data=dataEncoded, headers=header)
    return response.json()

def getBlock(Hash=None,height=None):
    if not height:
        params["hash"] = Hash
    elif not Hash:
        params["height"] = height
    else:
        return
    data["method"] = "getblock"
    data["params"] = params
    dataEncoded = json.dumps(data)
    response = requests.post(url,data=dataEncoded, headers=header)
    return response.json()

def getConnections():
    data["method"] = "get_connections"
    dataEncoded = json.dumps(data)
    response = requests.post(url,data=dataEncoded, headers=header)
    return response.json()

def getInfo():
    data["method"] = "get_info"
    dataEncoded = json.dumps(data)
    response = requests.post(url,data=dataEncoded, headers=header)
    return response.json()

def hardForkInfo():
    data["method"] = "hard_fork_info"
    dataEncoded = json.dumps(data)
    response = requests.post(url,data=dataEncoded, headers=header)
    return response.json()

def setBans(bans):
    data["method"] = "setbans"
    params["bans"] = bans
    data["params"] = params
    dataEncoded = json.dumps(data)
    response = requests.post(url,data=dataEncoded, headers=header)
    return response.json()

def getBans():
    data["method"] = "getbans"
    dataEncoded = json.dumps(data)
    response = requests.post(url,data=dataEncoded, headers=header)
    return response.json()

def getHeight():
    respose = requests.post("http://127.0.0.1:18081/getheight",headers=header)
    return response.json()

def getTransactions(txs_hashes, json=False):
    data = {}
    data["txs_hashes"] = txs_hashes
    data["decode_as_json"] = json
    dataEncoded = json.dumps(data)
    response = requests.post("http://127.0.0.1:18081/gettransactions",data=dataEncoded,headers=header)
    return response.json()

def isKeyImageSpent(keyImages):
    data = {}
    data["key_images"] = keyImages
    dataEncoded = json.dumps(data)
    response = requests.post("http://127.0.0.1:18081/is_key_image_spent",data=dataEncoded,headers=header)
    return response.json()

def sendRawTransaction(txAsHex):
    data = {}
    data["tx_as_hex"] = txAsHex
    dataEncoded = json.dumps(data)
    response = requests.post("http://127.0.0.1:18081/sendrawtransaction",data=dataEncoded,headers=header)
    return response.json()

def getTransactionPool():
    response = requests.post("http://127.0.0.1:18081/get_transaction_pool",headers=header)
    return response.json()

def stopDaemon():
    response = requests.post("http://127.0.0.1:18081/stop_daemon",headers=header)
    return response.json()
