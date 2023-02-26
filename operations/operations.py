import json, requests

class Opertations:

	def GetListPropertys(self):
		url = "http://localhost:9090/api/GetLastProperty/"
		payload = json.dumps({})
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)

	def GetSpace(self):
		url = "http://localhost:9090/api/GetSpace/"
		payload={}
		headers = {}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)

	def GetDeatilProperty(self,pk):
		url = "http://localhost:9090/api/Details_Property/"
		payload = json.dumps({"pk": pk})
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)



