import unittest
from py4j.java_gateway import JavaGateway, GatewayClient

class IntegrationTest(unittest.TestCase):

    def setUp(self):
        gateway = JavaGateway(GatewayClient(port=25335))
        self.solap4py = gateway.entry_point.getSolap4py();

    def test_Schemas(self):
        query = '{"queryType":"metadata","data":{ "root" :["Traffic"]}}'
        result = self.solap4py.process(query)
        self.assertEqual(result, '{"error":"OK","data":{"[Traffic]":{"caption":"Traffic"}}}')

    def test_Members(self):
        query = '{"queryType":"metadata","data":{"root":["Traffic", "[Traffic]", "[Zone]", "[Zone.Name]", "[Zone.Name].[Name0]"], "withProperties": false }}'
        result = self.solap4py.process(query)
        self.assertEqual(result, '{"error":"OK","data":{"[Zone.Name].[All Zone.Names].[Croatia]":{"caption":"Croatia"},"[Zone.Name].[All Zone.Names].[Switzerland]":{"caption":"Switzerland"},"[Zone.Name].[All Zone.Names].[Cyprus]":{"caption":"Cyprus"},"[Zone.Name].[All Zone.Names].[Portugal]":{"caption":"Portugal"},"[Zone.Name].[All Zone.Names].[France]":{"caption":"France"},"[Zone.Name].[All Zone.Names].[Italy]":{"caption":"Italy"},"[Zone.Name].[All Zone.Names].[United Kingdom]":{"caption":"United Kingdom"},"[Zone.Name].[All Zone.Names].[Finland]":{"caption":"Finland"},"[Zone.Name].[All Zone.Names].[Iceland]":{"caption":"Iceland"},"[Zone.Name].[All Zone.Names].[Slovakia]":{"caption":"Slovakia"},"[Zone.Name].[All Zone.Names].[Belgium]":{"caption":"Belgium"},"[Zone.Name].[All Zone.Names].[Luxembourg]":{"caption":"Luxembourg"},"[Zone.Name].[All Zone.Names].[Turkey]":{"caption":"Turkey"},"[Zone.Name].[All Zone.Names].[Norway]":{"caption":"Norway"},"[Zone.Name].[All Zone.Names].[Slovenia]":{"caption":"Slovenia"},"[Zone.Name].[All Zone.Names].[Austria]":{"caption":"Austria"},"[Zone.Name].[All Zone.Names].[Romania]":{"caption":"Romania"},"[Zone.Name].[All Zone.Names].[Czech Republic]":{"caption":"Czech Republic"},"[Zone.Name].[All Zone.Names].[Malta]":{"caption":"Malta"},"[Zone.Name].[All Zone.Names].[Lithuania]":{"caption":"Lithuania"},"[Zone.Name].[All Zone.Names].[Denmark]":{"caption":"Denmark"},"[Zone.Name].[All Zone.Names].[Estonia]":{"caption":"Estonia"},"[Zone.Name].[All Zone.Names].[The former Yugoslav Republic of Macedonia]":{"caption":"The former Yugoslav Republic of Macedonia"},"[Zone.Name].[All Zone.Names].[Hungary]":{"caption":"Hungary"},"[Zone.Name].[All Zone.Names].[Latvia]":{"caption":"Latvia"},"[Zone.Name].[All Zone.Names].[Germany]":{"caption":"Germany"},"[Zone.Name].[All Zone.Names].[Bulgaria]":{"caption":"Bulgaria"},"[Zone.Name].[All Zone.Names].[Sweden]":{"caption":"Sweden"},"[Zone.Name].[All Zone.Names].[Greece]":{"caption":"Greece"},"[Zone.Name].[All Zone.Names].[Netherlands]":{"caption":"Netherlands"},"[Zone.Name].[All Zone.Names].[Liechtenstein]":{"caption":"Liechtenstein"},"[Zone.Name].[All Zone.Names].[Ireland]":{"caption":"Ireland"},"[Zone.Name].[All Zone.Names].[Poland]":{"caption":"Poland"},"[Zone.Name].[All Zone.Names].[Spain]":{"caption":"Spain"}}}')

    def test_InvalidSchema(self):
        query = '{ "queryType" : "metadata", "data" : { "root" : ["Trafficv"]}}'
        result = self.solap4py.process(query)
        self.assertEqual(result, '{"error":"BAD_REQUEST","data":"Invalid schema identifier"}')

    def test_Range(self):
        query = '{ "queryType" : "data", "data" : { "from":"[Traffic]", "onColumns":["[Measures].[Max Quantity]"], "onRows":{"[Time]":{"members":["[Time].[All Times].[2000]", "[Time].[All Times].[2003]"], "range":true}}}}'
        result = self.solap4py.process(query)
        self.assertEqual(result, '{"error":"OK","data":[{"[Measures].[Max Quantity]":311121,"[Time]":"[Time].[All Times].[2000]"},{"[Measures].[Max Quantity]":304574,"[Time]":"[Time].[All Times].[2001]"},{"[Measures].[Max Quantity]":310543,"[Time]":"[Time].[All Times].[2002]"},{"[Measures].[Max Quantity]":315811,"[Time]":"[Time].[All Times].[2003]"}]}')

    def test_NullMeasure(self):
        query = '{"queryType":"data","data":{"from":"[Traffic]","onColumns":["[Measures].[Goods Quantity]"],"onRows":{"[Time]":{"members":["[Time].[All Times].[1950]"], "range":false}}}}'
        result = self.solap4py.process(query)
        self.assertEqual(result, '{"error":"OK","data":[{"[Measures].[Goods Quantity]":0,"[Time]":"[Time].[All Times].[1950]"}]}')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(IntegrationTest)
    unittest.TextTestRunner(verbosity=2).run(suite)