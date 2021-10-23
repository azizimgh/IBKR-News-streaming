from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import time
from config import *

class IBapi(EWrapper, EClient):
	def __init__(self):
		EClient.__init__(self, self)

	def tickPrice(self, reqId, tickType, price, attrib):
		if tickType == 2 and reqId == 1:
			print('The current ask price is: ', price)

	#You can change this to manipulate the news however you please
	def tickNews(self, tickerId: int, timeStamp: int, providerCode: str, articleId: str, headline: str, extraData: str):
		print("TickNews. TickerId:", tickerId, "TimeStamp:", timeStamp,"ProviderCode:", providerCode, "ArticleId:", articleId,"Headline:", headline, "ExtraData:", extraData)

app = IBapi()
app.connect('127.0.0.1', port, 1)

for i,elt in enumerate(subsccruptions):
	contract = Contract()
	contract.symbol  = f"{elt}:{elt}_ALL" #BroadTape All News
	contract.secType = "NEWS"
	contract.exchange = {elt}
	app.reqMktData(1009+i, contract, "mdoff,292", False, False, [])


app.run()
app.disconnect()