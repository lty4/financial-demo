import requests

def get_transactions(id):
    conversation_id = id

    """Setup Rasa API to get conversation information"""
    rasa_url = "http://35.224.230.180/core"
    rasa_token = "i0MDjoixPrsISPX"
    rasa_conversation_api_url = rasa_url + "/conversations/" + conversation_id + "/tracker?token=" + rasa_token

    """Get the conversation"""
    rasa_conversation = requests.get(url=rasa_conversation_api_url)

    """Get the transaction list"""
    rasa_transactions = rasa_conversation.json()['slots']['transaction_list']

    transaction_conversion = []

    '''Create table and add headers. '\r\n' is the Windows equivalent for newline'''
    transaction_table = 'Date\t\t\tAmount\r\n'

    '''Convert the dates and amounts to a US format'''
    for transaction in rasa_transactions:
        transaction['amount'] = '$' + str(format(transaction['amount'], '.2f'))
        transaction['date'] = str(transaction['date'][5:10] + "-" + transaction['date'][:4])
        transaction_conversion.append(transaction)

    '''Place transactions in a dictionary and sort by date'''
    transaction_dict = {}
    transaction_num = 0
    for transaction in transaction_conversion:
        transaction_dict[transaction['date']] = transaction['amount']

    transaction_dict_sorted = sorted(transaction_dict.items())

    '''Compile the final table of transactions'''
    for transaction in transaction_dict_sorted:
        transaction_table += str(transaction[0] + "\t\t" + transaction[1] + "\r\n")

    return transaction_table