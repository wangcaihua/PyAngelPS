// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: client_worker.proto

package com.tencent.client.worker.protos;

public interface PushRequestOrBuilder extends
    // @@protoc_insertion_point(interface_extends:ClientMaster.PushRequest)
    com.google.protobuf.MessageOrBuilder {

  /**
   * <code>int64 taskId = 1;</code>
   */
  long getTaskId();

  /**
   * <code>int32 matId = 3;</code>
   */
  int getMatId();

  /**
   * <code>int32 epoch = 4;</code>
   */
  int getEpoch();

  /**
   * <code>int32 batch = 5;</code>
   */
  int getBatch();

  /**
   * <code>int32 batchSize = 6;</code>
   */
  int getBatchSize();

  /**
   * <code>bytes objectId = 7;</code>
   */
  com.google.protobuf.ByteString getObjectId();
}
