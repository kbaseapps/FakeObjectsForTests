#include <workspace.spec>

/*
A KBase module: FakeObjectsForTests
*/

module FakeObjectsForTests {

    /*
        ws_id/ws_name - two alternative ways to set target workspace,
        obj_names - list of names for target workspace objects,
        metadata - optional metadata.
    */
    typedef structure {
        int ws_id;
        string ws_name;
        list<string> obj_names;
        mapping<string,string> metadata;
    } CreateAnyObjectsParams;

    funcdef create_any_objects(CreateAnyObjectsParams params) 
        returns (list<Workspace.object_info>) authentication required;


    /*
        ws_id/ws_name - two alternative ways to set target workspace,
        obj_names - list of names for target workspace objects (of type
            'KBaseGenomes.Genome'),
        metadata - optional metadata.
    */
    typedef structure {
        int ws_id;
        string ws_name;
        list<string> obj_names;
        mapping<string,string> metadata;
    } CreateFakeGenomesParams;

    funcdef create_fake_genomes(CreateFakeGenomesParams params) 
        returns (list<Workspace.object_info>) authentication required;


    /*
        ws_id/ws_name - two alternative ways to set target workspace,
        obj_names - list of names for target workspace objects (of type
            'KBaseFile.SingleEndLibrary'),
        metadata - optional metadata.
    */
    typedef structure {
        int ws_id;
        string ws_name;
        list<string> obj_names;
        mapping<string,string> metadata;
    } CreateFakeReadsParams;

    funcdef create_fake_reads(CreateFakeReadsParams params) 
        returns (list<Workspace.object_info>) authentication required;

};
