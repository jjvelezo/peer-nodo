# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: torrent.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'torrent.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rtorrent.proto\"2\n\x0eTorrentRequest\x12\x0f\n\x07peer_id\x18\x01 \x01(\t\x12\x0f\n\x07peer_ip\x18\x02 \x01(\t\"Q\n\x0fTorrentResponse\x12\x14\n\x0ctorrent_data\x18\x01 \x01(\t\x12\x12\n\ntracker_ip\x18\x02 \x01(\t\x12\x14\n\x0ctracker_port\x18\x03 \x01(\t\"/\n\x0bPeerRequest\x12\x0f\n\x07peer_id\x18\x01 \x01(\t\x12\x0f\n\x07peer_ip\x18\x02 \x01(\t\"\x1e\n\x0cPeerResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"&\n\x11SearchFileRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\".\n\x12SearchFileResponse\x12\x18\n\x05peers\x18\x01 \x03(\x0b\x32\t.PeerInfo\"&\n\x11UploadFileRequest\x12\x11\n\tfile_path\x18\x01 \x01(\t\"5\n\x12UploadFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07peer_id\x18\x02 \x01(\t\"#\n\x0eGetFileRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\"*\n\x0fGetFileResponse\x12\x17\n\x04peer\x18\x01 \x01(\x0b\x32\t.PeerInfo\"?\n\x08PeerInfo\x12\x0f\n\x07peer_id\x18\x01 \x01(\t\x12\x0f\n\x07peer_ip\x18\x02 \x01(\t\x12\x11\n\tpeer_port\x18\x03 \x01(\x05\x32\x8a\x02\n\x0eTorrentService\x12/\n\nGetTorrent\x12\x0f.TorrentRequest\x1a\x10.TorrentResponse\x12+\n\x0cRegisterPeer\x12\x0c.PeerRequest\x1a\r.PeerResponse\x12\x35\n\nSearchFile\x12\x12.SearchFileRequest\x1a\x13.SearchFileResponse\x12\x35\n\nUploadFile\x12\x12.UploadFileRequest\x1a\x13.UploadFileResponse\x12,\n\x07GetFile\x12\x0f.GetFileRequest\x1a\x10.GetFileResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'torrent_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TORRENTREQUEST']._serialized_start=17
  _globals['_TORRENTREQUEST']._serialized_end=67
  _globals['_TORRENTRESPONSE']._serialized_start=69
  _globals['_TORRENTRESPONSE']._serialized_end=150
  _globals['_PEERREQUEST']._serialized_start=152
  _globals['_PEERREQUEST']._serialized_end=199
  _globals['_PEERRESPONSE']._serialized_start=201
  _globals['_PEERRESPONSE']._serialized_end=231
  _globals['_SEARCHFILEREQUEST']._serialized_start=233
  _globals['_SEARCHFILEREQUEST']._serialized_end=271
  _globals['_SEARCHFILERESPONSE']._serialized_start=273
  _globals['_SEARCHFILERESPONSE']._serialized_end=319
  _globals['_UPLOADFILEREQUEST']._serialized_start=321
  _globals['_UPLOADFILEREQUEST']._serialized_end=359
  _globals['_UPLOADFILERESPONSE']._serialized_start=361
  _globals['_UPLOADFILERESPONSE']._serialized_end=414
  _globals['_GETFILEREQUEST']._serialized_start=416
  _globals['_GETFILEREQUEST']._serialized_end=451
  _globals['_GETFILERESPONSE']._serialized_start=453
  _globals['_GETFILERESPONSE']._serialized_end=495
  _globals['_PEERINFO']._serialized_start=497
  _globals['_PEERINFO']._serialized_end=560
  _globals['_TORRENTSERVICE']._serialized_start=563
  _globals['_TORRENTSERVICE']._serialized_end=829
# @@protoc_insertion_point(module_scope)