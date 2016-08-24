# -*- coding: utf-8 -*-

import os
import unittest

import intelmq.lib.test as test
import intelmq.lib.utils as utils
from intelmq.bots.parsers.shadowserver.parser import ShadowserverParserBot

with open(os.path.join(os.path.dirname(__file__),
                       'microsoft-sinkhole.csv')) as handle:
    EXAMPLE_FILE = handle.read()
EXAMPLE_LINES = EXAMPLE_FILE.splitlines()

with open(os.path.join(os.path.dirname(__file__),
                       'microsoft-sinkhole_RECONSTRUCTED.csv')) as handle:
    RECONSTRUCTED_FILE = handle.read()
RECONSTRUCTED_LINES = RECONSTRUCTED_FILE.splitlines()

EXAMPLE_REPORT = {"feed.name": "ShadowServer QOTD",
                  "raw": utils.base64_encode(EXAMPLE_FILE),
                  "__type": "Report",
                  "time.observation": "2015-01-01T00:00:00+00:00",
                  }
EVENTS = [{'__type': 'Event',
           'classification.taxonomy': 'Malicious Code',
           'classification.type': 'botnet drone',
           'classification.identifier': 'botnet',
           'feed.code': 'shadowserver-microsoft-sinkhole',
           'destination.asn': 8075,
           'destination.geolocation.cc': 'SG',
           'destination.ip': '168.63.184.224',
           'destination.port': 16470,
           'feed.name': 'shadowserver',
           'malware.name': 'b68-zeroaccess-1-64bit',
           'protocol.application': 'http',
           'protocol.transport': 'tcp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[1], ''])),
           'source.asn': 6805,
           'source.geolocation.cc': 'DE',
           'source.ip': '77.12.73.138',
           'source.port': 64742,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:00+00:00'},
          {'__type': 'Event',
           'classification.taxonomy': 'Malicious Code',
           'classification.type': 'botnet drone',
           'classification.identifier': 'botnet',
           'feed.code': 'shadowserver-microsoft-sinkhole',
           'destination.asn': 8075,
           'destination.geolocation.cc': 'HK',
           'destination.ip': '168.63.202.23',
           'destination.port': 16470,
           'feed.name': 'shadowserver',
           'malware.name': 'b68-zeroaccess-1-64bit',
           'protocol.application': 'http',
           'protocol.transport': 'tcp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[2], ''])),
           'source.asn': 8551,
           'source.geolocation.cc': 'IL',
           'source.ip': '109.64.133.187',
           'source.port': 62473,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:00+00:00'},
          {'__type': 'Event',
           'classification.taxonomy': 'Malicious Code',
           'classification.type': 'botnet drone',
           'classification.identifier': 'botnet',
           'feed.code': 'shadowserver-microsoft-sinkhole',
           'destination.asn': 16265,
           'destination.geolocation.cc': 'NL',
           'destination.ip': '82.192.70.219',
           'destination.port': 16471,
           'feed.name': 'shadowserver',
           'malware.name': 'b68-zeroaccess-1-32bit',
           'protocol.application': 'http',
           'protocol.transport': 'tcp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[3], ''])),
           'source.asn': 22085,
           'source.geolocation.cc': 'BR',
           'source.ip': '187.24.22.90',
           'source.port': 1030,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:00+00:00'},
          {'__type': 'Event',
           'classification.taxonomy': 'Malicious Code',
           'classification.type': 'botnet drone',
           'classification.identifier': 'botnet',
           'feed.code': 'shadowserver-microsoft-sinkhole',
           'destination.asn': 8075,
           'destination.geolocation.cc': 'SG',
           'destination.ip': '168.63.184.224',
           'destination.port': 16470,
           'feed.name': 'shadowserver',
           'malware.name': 'b68-zeroaccess-1-64bit',
           'protocol.application': 'http',
           'protocol.transport': 'tcp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[4], ''])),
           'source.asn': 2516,
           'source.geolocation.cc': 'JP',
           'source.ip': '118.158.226.105',
           'source.port': 49152,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:00+00:00'},
          {'__type': 'Event',
           'classification.taxonomy': 'Malicious Code',
           'classification.type': 'botnet drone',
           'classification.identifier': 'botnet',
           'feed.code': 'shadowserver-microsoft-sinkhole',
           'destination.asn': 8075,
           'destination.geolocation.cc': 'HK',
           'destination.ip': '207.46.138.117',
           'destination.port': 16464,
           'feed.name': 'shadowserver',
           'malware.name': 'b68-zeroaccess-2-32bit',
           'protocol.application': 'http',
           'protocol.transport': 'tcp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[5], ''])),
           'source.asn': 20001,
           'source.geolocation.cc': 'US',
           'source.ip': '173.196.9.222',
           'source.port': 55253,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:00+00:00'},
          {'__type': 'Event',
           'classification.taxonomy': 'Malicious Code',
           'classification.type': 'botnet drone',
           'classification.identifier': 'botnet',
           'feed.code': 'shadowserver-microsoft-sinkhole',
           'destination.asn': 8075,
           'destination.geolocation.cc': 'SG',
           'destination.ip': '168.63.240.164',
           'destination.port': 16464,
           'feed.name': 'shadowserver',
           'malware.name': 'b68-zeroaccess-2-32bit',
           'protocol.application': 'http',
           'protocol.transport': 'tcp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[6], ''])),
           'source.asn': 18403,
           'source.geolocation.cc': 'VN',
           'source.ip': '42.112.141.154',
           'source.port': 29554,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:00+00:00'},
          {'__type': 'Event',
           'classification.taxonomy': 'Malicious Code',
           'classification.type': 'botnet drone',
           'classification.identifier': 'botnet',
           'feed.code': 'shadowserver-microsoft-sinkhole',
           'destination.asn': 8075,
           'destination.geolocation.cc': 'US',
           'destination.ip': '204.95.99.205',
           'destination.port': 443,
           'destination.url': 'http://204.95.99.205/index.php',
           'extra': '{"http_host": "204.95.99.205", "user_agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.0.8077)"}',
           'feed.name': 'shadowserver',
           'malware.name': 'caphaw',
           'protocol.application': 'http',
           'protocol.transport': 'tcp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[7], ''])),
           'source.asn': 7018,
           'source.geolocation.cc': 'US',
           'source.ip': '12.179.112.155',
           'source.port': 57067,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:00+00:00'},
          {'__type': 'Event',
           'classification.taxonomy': 'Malicious Code',
           'classification.type': 'botnet drone',
           'classification.identifier': 'botnet',
           'feed.code': 'shadowserver-microsoft-sinkhole',
           'destination.asn': 8075,
           'destination.geolocation.cc': 'US',
           'destination.ip': '204.95.99.204',
           'destination.fqdn': 'xf5wau9lcpf5.oonucoog.cc',
           'destination.port': 443,
           'destination.url': 'http://xf5wau9lcpf5.oonucoog.cc/ping.html',
           'extra': '{"user_agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.0.7357)"}',
           'feed.name': 'shadowserver',
           'malware.name': 'caphaw',
           'protocol.application': 'http',
           'protocol.transport': 'tcp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[8], ''])),
           'source.asn': 10796,
           'source.geolocation.cc': 'US',
           'source.ip': '70.60.43.102',
           'source.port': 2266,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:00+00:00'},
          {'__type': 'Event',
           'classification.taxonomy': 'Malicious Code',
           'classification.type': 'botnet drone',
           'classification.identifier': 'botnet',
           'feed.code': 'shadowserver-microsoft-sinkhole',
           'destination.asn': 8075,
           'destination.geolocation.cc': 'US',
           'destination.ip': '204.95.99.204',
           'destination.fqdn': '3k3kwrnj.rgk.cc',
           'destination.port': 443,
           'destination.url': 'http://3k3kwrnj.rgk.cc/index.php',
           'extra': '{"user_agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.0.9121)"}',
           'feed.name': 'shadowserver',
           'malware.name': 'caphaw',
           'protocol.application': 'http',
           'protocol.transport': 'tcp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[9], ''])),
           'source.asn': 10429,
           'source.geolocation.cc': 'BR',
           'source.ip': '189.108.25.26',
           'source.port': 50634,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:00+00:00'},
          {'__type': 'Event',
           'classification.taxonomy': 'Malicious Code',
           'classification.type': 'botnet drone',
           'classification.identifier': 'botnet',
           'feed.code': 'shadowserver-microsoft-sinkhole',
           'destination.asn': 3598,
           'destination.geolocation.cc': 'US',
           'destination.ip': '199.2.137.201',
           'destination.fqdn': 'ultimaresource.com',
           'destination.port': 80,
           'destination.url': 'http://ultimaresource.com/wild/live/file.php',
           'extra': '{"user_agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; BRI/1)"}',
           'feed.name': 'shadowserver',
           'malware.name': 'citadel-b54',
           'protocol.application': 'http',
           'protocol.transport': 'tcp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[10], ''])),
           'source.asn': 6983,
           'source.geolocation.cc': 'US',
           'source.ip': '66.245.69.124',
           'source.port': 3130,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:01+00:00'},
          {'__type': 'Event',
           'classification.taxonomy': 'Malicious Code',
           'classification.type': 'botnet drone',
           'classification.identifier': 'botnet',
           'feed.code': 'shadowserver-microsoft-sinkhole',
           'destination.asn': 3598,
           'destination.geolocation.cc': 'US',
           'destination.ip': '199.2.137.202',
           'destination.port': 80,
           'destination.url': 'http://199.2.137.202/file-b29d40.php',
           'extra': '{"http_host": "199.2.137.202", "user_agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; .NET CLR 3.5.21022)"}',
           'feed.name': 'shadowserver',
           'malware.name': 'citadel-b54',
           'protocol.application': 'http',
           'protocol.transport': 'tcp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[11], ''])),
           'source.asn': 5650,
           'source.geolocation.cc': 'US',
           'source.ip': '50.52.19.180',
           'source.port': 52176,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:01+00:00'},
          {'__type': 'Event',
           'classification.taxonomy': 'Malicious Code',
           'classification.type': 'botnet drone',
           'classification.identifier': 'botnet',
           'feed.code': 'shadowserver-microsoft-sinkhole',
           'destination.asn': 3598,
           'destination.geolocation.cc': 'US',
           'destination.ip': '199.2.137.201',
           'destination.fqdn': 'prohomemain.com',
           'destination.port': 80,
           'destination.url': 'http://prohomemain.com/367601b6737825deb58a244576e4f098/file.php',
           'extra': '{"user_agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; AskTB5.6)"}',
           'feed.name': 'shadowserver',
           'malware.name': 'citadel-b54',
           'protocol.application': 'http',
           'protocol.transport': 'tcp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[12], ''])),
           'source.asn': 812,
           'source.geolocation.cc': 'CA',
           'source.ip': '99.243.32.48',
           'source.port': 49725,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:01+00:00'},
          {'__type': 'Event',
           'classification.taxonomy': 'Malicious Code',
           'classification.type': 'botnet drone',
           'classification.identifier': 'botnet',
           'feed.code': 'shadowserver-microsoft-sinkhole',
           'destination.asn': 3598,
           'destination.geolocation.cc': 'US',
           'destination.ip': '199.2.137.202',
           'destination.fqdn': 'ronapri.com',
           'destination.port': 80,
           'destination.url': 'http://ronapri.com/view/file.php',
           'extra': '{"user_agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; AskTbFWV5/5.11.3.15590)"}',
           'feed.name': 'shadowserver',
           'malware.name': 'citadel-b54',
           'protocol.application': 'http',
           'protocol.transport': 'tcp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[13], ''])),
           'source.asn': 2516,
           'source.geolocation.cc': 'JP',
           'source.ip': '106.156.210.197',
           'source.port': 55400,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:01+00:00'},
          {'__type': 'Event',
           'classification.taxonomy': 'Malicious Code',
           'classification.type': 'botnet drone',
           'classification.identifier': 'botnet',
           'feed.code': 'shadowserver-microsoft-sinkhole',
           'destination.asn': 3598,
           'destination.geolocation.cc': 'US',
           'destination.ip': '199.2.137.201',
           'destination.fqdn': '9a5bb34eede4b85b9e81f40d530b68ff.co.cc',
           'destination.port': 80,
           'destination.url': 'http://9A5BB34EEDE4B85B9E81F40D530B68FF.co.cc/message.php',
           'extra': '{"user_agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; .NET4.0C)"}',
           'feed.name': 'shadowserver',
           'malware.name': 'bamital-b58',
           'protocol.application': 'http',
           'protocol.transport': 'tcp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[14], ''])),
           'source.asn': 1221,
           'source.geolocation.cc': 'AU',
           'source.ip': '138.217.89.25',
           'source.port': 62254,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:01+00:00'}]


class TestShadowserverParserBot(test.BotTestCase, unittest.TestCase):
    """
    A TestCase for a ShadowserverParserBot.
    """

    @classmethod
    def set_bot(cls):
        cls.bot_reference = ShadowserverParserBot
        cls.default_input_message = EXAMPLE_REPORT
        cls.sysconfig = {'feedname': 'Microsoft-Sinkhole'}

    def test_event(self):
        """ Test if correct Event has been produced. """
        self.run_bot()
        for i, EVENT in enumerate(EVENTS):
            self.assertMessageEqual(i, EVENT)


if __name__ == '__main__':
    unittest.main()
