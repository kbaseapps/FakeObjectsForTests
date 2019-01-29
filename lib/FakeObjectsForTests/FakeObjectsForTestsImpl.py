# -*- coding: utf-8 -*-
#BEGIN_HEADER
import copy
import json
import os
import time

from installed_clients.DataFileUtilClient import DataFileUtil
from installed_clients.WorkspaceClient import Workspace as workspaceService
#END_HEADER


class FakeObjectsForTests:
    '''
    Module Name:
    FakeObjectsForTests

    Module Description:
    A KBase module: FakeObjectsForTests
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.2"
    GIT_URL = "https://github.com/kbaseapps/FakeObjectsForTests.git"
    GIT_COMMIT_HASH = "1868aa583b3ae078702f6153369625f41819a5d7"

    #BEGIN_CLASS_HEADER
    def ws(self, ctx):
        return workspaceService(self.wsURL, token=ctx['token'])
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.wsURL = config['workspace-url']
        self.scratch = config['scratch']
        #END_CONSTRUCTOR
        pass


    def create_any_objects(self, ctx, params):
        """
        :param params: instance of type "CreateAnyObjectsParams"
           (ws_id/ws_name - two alternative ways to set target workspace,
           obj_names - list of names for target workspace objects, metadata -
           optional metadata.) -> structure: parameter "ws_id" of Long,
           parameter "ws_name" of String, parameter "obj_names" of list of
           String, parameter "metadata" of mapping from String to String
        :returns: instance of list of type "object_info" (Information about
           an object, including user provided metadata. obj_id objid - the
           numerical id of the object. obj_name name - the name of the
           object. type_string type - the type of the object. timestamp
           save_date - the save date of the object. obj_ver ver - the version
           of the object. username saved_by - the user that saved or copied
           the object. ws_id wsid - the workspace containing the object.
           ws_name workspace - the workspace containing the object. string
           chsum - the md5 checksum of the object. int size - the size of the
           object in bytes. usermeta meta - arbitrary user-supplied metadata
           about the object.) -> tuple of size 11: parameter "objid" of type
           "obj_id" (The unique, permanent numerical ID of an object.),
           parameter "name" of type "obj_name" (A string used as a name for
           an object. Any string consisting of alphanumeric characters and
           the characters |._- that is not an integer is acceptable.),
           parameter "type" of type "type_string" (A type string. Specifies
           the type and its version in a single string in the format
           [module].[typename]-[major].[minor]: module - a string. The module
           name of the typespec containing the type. typename - a string. The
           name of the type as assigned by the typedef statement. major - an
           integer. The major version of the type. A change in the major
           version implies the type has changed in a non-backwards compatible
           way. minor - an integer. The minor version of the type. A change
           in the minor version implies that the type has changed in a way
           that is backwards compatible with previous type definitions. In
           many cases, the major and minor versions are optional, and if not
           provided the most recent version will be used. Example:
           MyModule.MyType-3.1), parameter "save_date" of type "timestamp" (A
           time in the format YYYY-MM-DDThh:mm:ssZ, where Z is either the
           character Z (representing the UTC timezone) or the difference in
           time to UTC in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500
           (EST time) 2013-04-03T08:56:32+0000 (UTC time)
           2013-04-03T08:56:32Z (UTC time)), parameter "version" of Long,
           parameter "saved_by" of type "username" (Login name of a KBase
           user account.), parameter "wsid" of type "ws_id" (The unique,
           permanent numerical ID of a workspace.), parameter "workspace" of
           type "ws_name" (A string used as a name for a workspace. Any
           string consisting of alphanumeric characters and "_", ".", or "-"
           that is not an integer is acceptable. The name may optionally be
           prefixed with the workspace owner's user name and a colon, e.g.
           kbasetest:my_workspace.), parameter "chsum" of String, parameter
           "size" of Long, parameter "meta" of type "usermeta" (User provided
           metadata about an object. Arbitrary key-value pairs provided by
           the user.) -> mapping from String to String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN create_any_objects
        metadata = params.get('metadata')
        objects = []
        for obj_name in params['obj_names']:
            objects.append({'type': 'Empty.AType', 'data': {'foo': 5},
                            'name': obj_name, 'meta': metadata})
        so_params = {'objects': objects}
        if 'ws_id' in params:
            so_params['id'] = params['ws_id']
        elif 'ws_name' in params:
            so_params['workspace'] = params['ws_name']
        returnVal = self.ws(ctx).save_objects(so_params)
        #END create_any_objects

        # At some point might do deeper type checking...
        if not isinstance(returnVal, list):
            raise ValueError('Method create_any_objects return value ' +
                             'returnVal is not type list as required.')
        # return the results
        return [returnVal]

    def create_fake_genomes(self, ctx, params):
        """
        :param params: instance of type "CreateFakeGenomesParams"
           (ws_id/ws_name - two alternative ways to set target workspace,
           obj_names - list of names for target workspace objects (of type
           'KBaseGenomes.Genome'), metadata - optional metadata.) ->
           structure: parameter "ws_id" of Long, parameter "ws_name" of
           String, parameter "obj_names" of list of String, parameter
           "metadata" of mapping from String to String
        :returns: instance of list of type "object_info" (Information about
           an object, including user provided metadata. obj_id objid - the
           numerical id of the object. obj_name name - the name of the
           object. type_string type - the type of the object. timestamp
           save_date - the save date of the object. obj_ver ver - the version
           of the object. username saved_by - the user that saved or copied
           the object. ws_id wsid - the workspace containing the object.
           ws_name workspace - the workspace containing the object. string
           chsum - the md5 checksum of the object. int size - the size of the
           object in bytes. usermeta meta - arbitrary user-supplied metadata
           about the object.) -> tuple of size 11: parameter "objid" of type
           "obj_id" (The unique, permanent numerical ID of an object.),
           parameter "name" of type "obj_name" (A string used as a name for
           an object. Any string consisting of alphanumeric characters and
           the characters |._- that is not an integer is acceptable.),
           parameter "type" of type "type_string" (A type string. Specifies
           the type and its version in a single string in the format
           [module].[typename]-[major].[minor]: module - a string. The module
           name of the typespec containing the type. typename - a string. The
           name of the type as assigned by the typedef statement. major - an
           integer. The major version of the type. A change in the major
           version implies the type has changed in a non-backwards compatible
           way. minor - an integer. The minor version of the type. A change
           in the minor version implies that the type has changed in a way
           that is backwards compatible with previous type definitions. In
           many cases, the major and minor versions are optional, and if not
           provided the most recent version will be used. Example:
           MyModule.MyType-3.1), parameter "save_date" of type "timestamp" (A
           time in the format YYYY-MM-DDThh:mm:ssZ, where Z is either the
           character Z (representing the UTC timezone) or the difference in
           time to UTC in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500
           (EST time) 2013-04-03T08:56:32+0000 (UTC time)
           2013-04-03T08:56:32Z (UTC time)), parameter "version" of Long,
           parameter "saved_by" of type "username" (Login name of a KBase
           user account.), parameter "wsid" of type "ws_id" (The unique,
           permanent numerical ID of a workspace.), parameter "workspace" of
           type "ws_name" (A string used as a name for a workspace. Any
           string consisting of alphanumeric characters and "_", ".", or "-"
           that is not an integer is acceptable. The name may optionally be
           prefixed with the workspace owner's user name and a colon, e.g.
           kbasetest:my_workspace.), parameter "chsum" of String, parameter
           "size" of Long, parameter "meta" of type "usermeta" (User provided
           metadata about an object. Arbitrary key-value pairs provided by
           the user.) -> mapping from String to String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN create_fake_genomes
        metadata = params.get('metadata')
        objects = []
        genome_data = json.load(open('/kb/module/data/genome.json'))
        for obj_name in params['obj_names']:
            data = copy.copy(genome_data)
            data['id'] = obj_name
            objects.append({'type': 'KBaseGenomes.Genome', 
                            'data': data,
                            'name': obj_name, 'meta': metadata})
        so_params = {'objects': objects}
        if 'ws_id' in params:
            so_params['id'] = params['ws_id']
        elif 'ws_name' in params:
            so_params['workspace'] = params['ws_name']
        returnVal = self.ws(ctx).save_objects(so_params)
        #END create_fake_genomes

        # At some point might do deeper type checking...
        if not isinstance(returnVal, list):
            raise ValueError('Method create_fake_genomes return value ' +
                             'returnVal is not type list as required.')
        # return the results
        return [returnVal]

    def create_fake_reads(self, ctx, params):
        """
        :param params: instance of type "CreateFakeReadsParams"
           (ws_id/ws_name - two alternative ways to set target workspace,
           obj_names - list of names for target workspace objects (of type
           'KBaseFile.SingleEndLibrary'), metadata - optional metadata.) ->
           structure: parameter "ws_id" of Long, parameter "ws_name" of
           String, parameter "obj_names" of list of String, parameter
           "metadata" of mapping from String to String
        :returns: instance of list of type "object_info" (Information about
           an object, including user provided metadata. obj_id objid - the
           numerical id of the object. obj_name name - the name of the
           object. type_string type - the type of the object. timestamp
           save_date - the save date of the object. obj_ver ver - the version
           of the object. username saved_by - the user that saved or copied
           the object. ws_id wsid - the workspace containing the object.
           ws_name workspace - the workspace containing the object. string
           chsum - the md5 checksum of the object. int size - the size of the
           object in bytes. usermeta meta - arbitrary user-supplied metadata
           about the object.) -> tuple of size 11: parameter "objid" of type
           "obj_id" (The unique, permanent numerical ID of an object.),
           parameter "name" of type "obj_name" (A string used as a name for
           an object. Any string consisting of alphanumeric characters and
           the characters |._- that is not an integer is acceptable.),
           parameter "type" of type "type_string" (A type string. Specifies
           the type and its version in a single string in the format
           [module].[typename]-[major].[minor]: module - a string. The module
           name of the typespec containing the type. typename - a string. The
           name of the type as assigned by the typedef statement. major - an
           integer. The major version of the type. A change in the major
           version implies the type has changed in a non-backwards compatible
           way. minor - an integer. The minor version of the type. A change
           in the minor version implies that the type has changed in a way
           that is backwards compatible with previous type definitions. In
           many cases, the major and minor versions are optional, and if not
           provided the most recent version will be used. Example:
           MyModule.MyType-3.1), parameter "save_date" of type "timestamp" (A
           time in the format YYYY-MM-DDThh:mm:ssZ, where Z is either the
           character Z (representing the UTC timezone) or the difference in
           time to UTC in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500
           (EST time) 2013-04-03T08:56:32+0000 (UTC time)
           2013-04-03T08:56:32Z (UTC time)), parameter "version" of Long,
           parameter "saved_by" of type "username" (Login name of a KBase
           user account.), parameter "wsid" of type "ws_id" (The unique,
           permanent numerical ID of a workspace.), parameter "workspace" of
           type "ws_name" (A string used as a name for a workspace. Any
           string consisting of alphanumeric characters and "_", ".", or "-"
           that is not an integer is acceptable. The name may optionally be
           prefixed with the workspace owner's user name and a colon, e.g.
           kbasetest:my_workspace.), parameter "chsum" of String, parameter
           "size" of Long, parameter "meta" of type "usermeta" (User provided
           metadata about an object. Arbitrary key-value pairs provided by
           the user.) -> mapping from String to String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN create_fake_reads
        metadata = params.get('metadata')
        objects = []
        dfu = DataFileUtil(os.environ['SDK_CALLBACK_URL'])
        path_to_temp_file = "/kb/module/work/tmp/temp_" + str(time.time()) + ".fq"
        with open(path_to_temp_file, 'w') as f:
            f.write(' ')
        uploadedfile = dfu.file_to_shock({'file_path': path_to_temp_file,
                                          'make_handle': 1, 'pack': 'gzip'})
        fhandle = uploadedfile['handle']
        os.remove(path_to_temp_file)
        data = {'lib': {'encoding': "ascii", 'file': fhandle, 'size': 1,
                        'type': "fq"},
                'sequencing_tech': "Illumina",
                'single_genome': 1}
        for obj_name in params['obj_names']:
            objects.append({'type': 'KBaseFile.SingleEndLibrary',
                            'data': data, 'name': obj_name, 'meta': metadata})
        so_params = {'objects': objects}
        if 'ws_id' in params:
            so_params['id'] = params['ws_id']
        elif 'ws_name' in params:
            so_params['workspace'] = params['ws_name']
        returnVal = self.ws(ctx).save_objects(so_params)
        #END create_fake_reads

        # At some point might do deeper type checking...
        if not isinstance(returnVal, list):
            raise ValueError('Method create_fake_reads return value ' +
                             'returnVal is not type list as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
