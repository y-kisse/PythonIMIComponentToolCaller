from utils import AddressFormatter

if __name__ == '__main__':
    imi_formatted_address = AddressFormatter.call_enrichment_tool("東京都千代田区永田町1-7-1")
    print(imi_formatted_address)