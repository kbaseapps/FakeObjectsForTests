# -*- coding: utf-8 -*-
import time
import unittest
from configparser import ConfigParser
from os import environ

from FakeObjectsForTests.FakeObjectsForTestsImpl import FakeObjectsForTests
from FakeObjectsForTests.FakeObjectsForTestsServer import MethodContext
from FakeObjectsForTests.authclient import KBaseAuth as _KBaseAuth
from installed_clients.WorkspaceClient import Workspace as workspaceService


class FakeObjectsForTestsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('FakeObjectsForTests'):
            cls.cfg[nameval[0]] = nameval[1]
        authServiceUrl = cls.cfg.get('auth-service-url', 
                "https://kbase.us/services/authorization/Sessions/Login")
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'FakeObjectsForTests',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL, token=token)
        cls.serviceImpl = FakeObjectsForTests(cls.cfg)

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_FakeObjectsForTests_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})  # noqa
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    # NOTE: According to Python unittest naming rules test method names should start from 'test'. # noqa
    def test_create_any_objects(self):
        ws_name = self.getWsName()
        obj_name = 'test_obj.1'
        ret = self.getImpl().create_any_objects(self.getContext(),
                                                {'ws_name': ws_name, 'obj_names': [obj_name]})[0]
        self.assertEqual(1, len(ret))
        self.assertEqual(obj_name, ret[0][1])

    def test_create_fake_genomes(self):
        ws_name = self.getWsName()
        obj_name = 'test_genome.1'
        ret = self.getImpl().create_fake_genomes(self.getContext(),
                                                {'ws_name': ws_name, 'obj_names': [obj_name]})[0]
        self.assertEqual(1, len(ret))
        self.assertEqual(obj_name, ret[0][1])

    def test_create_fake_reads(self):
        ws_name = self.getWsName()
        obj_names = ['test_reads.1', 'test_reads.2']
        ret = self.getImpl().create_fake_reads(self.getContext(),
                                               {'ws_name': ws_name, 'obj_names': obj_names})[0]
        self.assertEqual(2, len(ret))
