// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: client_master.proto

package com.tencent.client.master.protos;

/**
 * Protobuf service {@code ClientMaster.AngelCleintMaster}
 */
public  abstract class AngelCleintMaster
    implements com.google.protobuf.Service {
  protected AngelCleintMaster() {}

  public interface Interface {
    /**
     * <code>rpc RegisterWorker(.ClientMaster.RegisterWorkerReq) returns (.ClientMaster.RegisterWorkerResp);</code>
     */
    public abstract void registerWorker(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.RegisterWorkerReq request,
        com.google.protobuf.RpcCallback<com.tencent.client.master.protos.RegisterWorkerResp> done);

    /**
     * <code>rpc RegisterTask(.ClientMaster.RegisterTaskReq) returns (.ClientMaster.RegisterTaskResp);</code>
     */
    public abstract void registerTask(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.RegisterTaskReq request,
        com.google.protobuf.RpcCallback<com.tencent.client.master.protos.RegisterTaskResp> done);

    /**
     * <code>rpc SetAngelLocation(.ClientMaster.SetAngelLocationReq) returns (.VoidResp);</code>
     */
    public abstract void setAngelLocation(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.SetAngelLocationReq request,
        com.google.protobuf.RpcCallback<com.tencent.client.common.protos.VoidResp> done);

    /**
     * <code>rpc GetAngelLocation(.VoidReq) returns (.ClientMaster.GetAngelLocationResp);</code>
     */
    public abstract void getAngelLocation(
        com.google.protobuf.RpcController controller,
        com.tencent.client.common.protos.VoidReq request,
        com.google.protobuf.RpcCallback<com.tencent.client.master.protos.GetAngelLocationResp> done);

    /**
     * <code>rpc HeartBeat(.ClientMaster.HeartBeatReq) returns (.ClientMaster.HeartBeatResp);</code>
     */
    public abstract void heartBeat(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.HeartBeatReq request,
        com.google.protobuf.RpcCallback<com.tencent.client.master.protos.HeartBeatResp> done);

    /**
     * <code>rpc Clock(.ClientMaster.ClockReq) returns (.ClientMaster.ClockResp);</code>
     */
    public abstract void clock(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.ClockReq request,
        com.google.protobuf.RpcCallback<com.tencent.client.master.protos.ClockResp> done);

    /**
     * <code>rpc GetClockMap(.ClientMaster.GetClockMapReq) returns (.ClientMaster.GetClockMapResp);</code>
     */
    public abstract void getClockMap(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.GetClockMapReq request,
        com.google.protobuf.RpcCallback<com.tencent.client.master.protos.GetClockMapResp> done);

    /**
     * <code>rpc GetGlobalBatchSize(.VoidReq) returns (.ClientMaster.GetGlobalBatchResp);</code>
     */
    public abstract void getGlobalBatchSize(
        com.google.protobuf.RpcController controller,
        com.tencent.client.common.protos.VoidReq request,
        com.google.protobuf.RpcCallback<com.tencent.client.master.protos.GetGlobalBatchResp> done);

    /**
     * <code>rpc CompleteTask(.CompleteTaskReq) returns (.VoidResp);</code>
     */
    public abstract void completeTask(
        com.google.protobuf.RpcController controller,
        com.tencent.client.common.protos.CompleteTaskReq request,
        com.google.protobuf.RpcCallback<com.tencent.client.common.protos.VoidResp> done);

  }

  public static com.google.protobuf.Service newReflectiveService(
      final Interface impl) {
    return new AngelCleintMaster() {
      @java.lang.Override
      public  void registerWorker(
          com.google.protobuf.RpcController controller,
          com.tencent.client.master.protos.RegisterWorkerReq request,
          com.google.protobuf.RpcCallback<com.tencent.client.master.protos.RegisterWorkerResp> done) {
        impl.registerWorker(controller, request, done);
      }

      @java.lang.Override
      public  void registerTask(
          com.google.protobuf.RpcController controller,
          com.tencent.client.master.protos.RegisterTaskReq request,
          com.google.protobuf.RpcCallback<com.tencent.client.master.protos.RegisterTaskResp> done) {
        impl.registerTask(controller, request, done);
      }

      @java.lang.Override
      public  void setAngelLocation(
          com.google.protobuf.RpcController controller,
          com.tencent.client.master.protos.SetAngelLocationReq request,
          com.google.protobuf.RpcCallback<com.tencent.client.common.protos.VoidResp> done) {
        impl.setAngelLocation(controller, request, done);
      }

      @java.lang.Override
      public  void getAngelLocation(
          com.google.protobuf.RpcController controller,
          com.tencent.client.common.protos.VoidReq request,
          com.google.protobuf.RpcCallback<com.tencent.client.master.protos.GetAngelLocationResp> done) {
        impl.getAngelLocation(controller, request, done);
      }

      @java.lang.Override
      public  void heartBeat(
          com.google.protobuf.RpcController controller,
          com.tencent.client.master.protos.HeartBeatReq request,
          com.google.protobuf.RpcCallback<com.tencent.client.master.protos.HeartBeatResp> done) {
        impl.heartBeat(controller, request, done);
      }

      @java.lang.Override
      public  void clock(
          com.google.protobuf.RpcController controller,
          com.tencent.client.master.protos.ClockReq request,
          com.google.protobuf.RpcCallback<com.tencent.client.master.protos.ClockResp> done) {
        impl.clock(controller, request, done);
      }

      @java.lang.Override
      public  void getClockMap(
          com.google.protobuf.RpcController controller,
          com.tencent.client.master.protos.GetClockMapReq request,
          com.google.protobuf.RpcCallback<com.tencent.client.master.protos.GetClockMapResp> done) {
        impl.getClockMap(controller, request, done);
      }

      @java.lang.Override
      public  void getGlobalBatchSize(
          com.google.protobuf.RpcController controller,
          com.tencent.client.common.protos.VoidReq request,
          com.google.protobuf.RpcCallback<com.tencent.client.master.protos.GetGlobalBatchResp> done) {
        impl.getGlobalBatchSize(controller, request, done);
      }

      @java.lang.Override
      public  void completeTask(
          com.google.protobuf.RpcController controller,
          com.tencent.client.common.protos.CompleteTaskReq request,
          com.google.protobuf.RpcCallback<com.tencent.client.common.protos.VoidResp> done) {
        impl.completeTask(controller, request, done);
      }

    };
  }

  public static com.google.protobuf.BlockingService
      newReflectiveBlockingService(final BlockingInterface impl) {
    return new com.google.protobuf.BlockingService() {
      public final com.google.protobuf.Descriptors.ServiceDescriptor
          getDescriptorForType() {
        return getDescriptor();
      }

      public final com.google.protobuf.Message callBlockingMethod(
          com.google.protobuf.Descriptors.MethodDescriptor method,
          com.google.protobuf.RpcController controller,
          com.google.protobuf.Message request)
          throws com.google.protobuf.ServiceException {
        if (method.getService() != getDescriptor()) {
          throw new java.lang.IllegalArgumentException(
            "Service.callBlockingMethod() given method descriptor for " +
            "wrong service type.");
        }
        switch(method.getIndex()) {
          case 0:
            return impl.registerWorker(controller, (com.tencent.client.master.protos.RegisterWorkerReq)request);
          case 1:
            return impl.registerTask(controller, (com.tencent.client.master.protos.RegisterTaskReq)request);
          case 2:
            return impl.setAngelLocation(controller, (com.tencent.client.master.protos.SetAngelLocationReq)request);
          case 3:
            return impl.getAngelLocation(controller, (com.tencent.client.common.protos.VoidReq)request);
          case 4:
            return impl.heartBeat(controller, (com.tencent.client.master.protos.HeartBeatReq)request);
          case 5:
            return impl.clock(controller, (com.tencent.client.master.protos.ClockReq)request);
          case 6:
            return impl.getClockMap(controller, (com.tencent.client.master.protos.GetClockMapReq)request);
          case 7:
            return impl.getGlobalBatchSize(controller, (com.tencent.client.common.protos.VoidReq)request);
          case 8:
            return impl.completeTask(controller, (com.tencent.client.common.protos.CompleteTaskReq)request);
          default:
            throw new java.lang.AssertionError("Can't get here.");
        }
      }

      public final com.google.protobuf.Message
          getRequestPrototype(
          com.google.protobuf.Descriptors.MethodDescriptor method) {
        if (method.getService() != getDescriptor()) {
          throw new java.lang.IllegalArgumentException(
            "Service.getRequestPrototype() given method " +
            "descriptor for wrong service type.");
        }
        switch(method.getIndex()) {
          case 0:
            return com.tencent.client.master.protos.RegisterWorkerReq.getDefaultInstance();
          case 1:
            return com.tencent.client.master.protos.RegisterTaskReq.getDefaultInstance();
          case 2:
            return com.tencent.client.master.protos.SetAngelLocationReq.getDefaultInstance();
          case 3:
            return com.tencent.client.common.protos.VoidReq.getDefaultInstance();
          case 4:
            return com.tencent.client.master.protos.HeartBeatReq.getDefaultInstance();
          case 5:
            return com.tencent.client.master.protos.ClockReq.getDefaultInstance();
          case 6:
            return com.tencent.client.master.protos.GetClockMapReq.getDefaultInstance();
          case 7:
            return com.tencent.client.common.protos.VoidReq.getDefaultInstance();
          case 8:
            return com.tencent.client.common.protos.CompleteTaskReq.getDefaultInstance();
          default:
            throw new java.lang.AssertionError("Can't get here.");
        }
      }

      public final com.google.protobuf.Message
          getResponsePrototype(
          com.google.protobuf.Descriptors.MethodDescriptor method) {
        if (method.getService() != getDescriptor()) {
          throw new java.lang.IllegalArgumentException(
            "Service.getResponsePrototype() given method " +
            "descriptor for wrong service type.");
        }
        switch(method.getIndex()) {
          case 0:
            return com.tencent.client.master.protos.RegisterWorkerResp.getDefaultInstance();
          case 1:
            return com.tencent.client.master.protos.RegisterTaskResp.getDefaultInstance();
          case 2:
            return com.tencent.client.common.protos.VoidResp.getDefaultInstance();
          case 3:
            return com.tencent.client.master.protos.GetAngelLocationResp.getDefaultInstance();
          case 4:
            return com.tencent.client.master.protos.HeartBeatResp.getDefaultInstance();
          case 5:
            return com.tencent.client.master.protos.ClockResp.getDefaultInstance();
          case 6:
            return com.tencent.client.master.protos.GetClockMapResp.getDefaultInstance();
          case 7:
            return com.tencent.client.master.protos.GetGlobalBatchResp.getDefaultInstance();
          case 8:
            return com.tencent.client.common.protos.VoidResp.getDefaultInstance();
          default:
            throw new java.lang.AssertionError("Can't get here.");
        }
      }

    };
  }

  /**
   * <code>rpc RegisterWorker(.ClientMaster.RegisterWorkerReq) returns (.ClientMaster.RegisterWorkerResp);</code>
   */
  public abstract void registerWorker(
      com.google.protobuf.RpcController controller,
      com.tencent.client.master.protos.RegisterWorkerReq request,
      com.google.protobuf.RpcCallback<com.tencent.client.master.protos.RegisterWorkerResp> done);

  /**
   * <code>rpc RegisterTask(.ClientMaster.RegisterTaskReq) returns (.ClientMaster.RegisterTaskResp);</code>
   */
  public abstract void registerTask(
      com.google.protobuf.RpcController controller,
      com.tencent.client.master.protos.RegisterTaskReq request,
      com.google.protobuf.RpcCallback<com.tencent.client.master.protos.RegisterTaskResp> done);

  /**
   * <code>rpc SetAngelLocation(.ClientMaster.SetAngelLocationReq) returns (.VoidResp);</code>
   */
  public abstract void setAngelLocation(
      com.google.protobuf.RpcController controller,
      com.tencent.client.master.protos.SetAngelLocationReq request,
      com.google.protobuf.RpcCallback<com.tencent.client.common.protos.VoidResp> done);

  /**
   * <code>rpc GetAngelLocation(.VoidReq) returns (.ClientMaster.GetAngelLocationResp);</code>
   */
  public abstract void getAngelLocation(
      com.google.protobuf.RpcController controller,
      com.tencent.client.common.protos.VoidReq request,
      com.google.protobuf.RpcCallback<com.tencent.client.master.protos.GetAngelLocationResp> done);

  /**
   * <code>rpc HeartBeat(.ClientMaster.HeartBeatReq) returns (.ClientMaster.HeartBeatResp);</code>
   */
  public abstract void heartBeat(
      com.google.protobuf.RpcController controller,
      com.tencent.client.master.protos.HeartBeatReq request,
      com.google.protobuf.RpcCallback<com.tencent.client.master.protos.HeartBeatResp> done);

  /**
   * <code>rpc Clock(.ClientMaster.ClockReq) returns (.ClientMaster.ClockResp);</code>
   */
  public abstract void clock(
      com.google.protobuf.RpcController controller,
      com.tencent.client.master.protos.ClockReq request,
      com.google.protobuf.RpcCallback<com.tencent.client.master.protos.ClockResp> done);

  /**
   * <code>rpc GetClockMap(.ClientMaster.GetClockMapReq) returns (.ClientMaster.GetClockMapResp);</code>
   */
  public abstract void getClockMap(
      com.google.protobuf.RpcController controller,
      com.tencent.client.master.protos.GetClockMapReq request,
      com.google.protobuf.RpcCallback<com.tencent.client.master.protos.GetClockMapResp> done);

  /**
   * <code>rpc GetGlobalBatchSize(.VoidReq) returns (.ClientMaster.GetGlobalBatchResp);</code>
   */
  public abstract void getGlobalBatchSize(
      com.google.protobuf.RpcController controller,
      com.tencent.client.common.protos.VoidReq request,
      com.google.protobuf.RpcCallback<com.tencent.client.master.protos.GetGlobalBatchResp> done);

  /**
   * <code>rpc CompleteTask(.CompleteTaskReq) returns (.VoidResp);</code>
   */
  public abstract void completeTask(
      com.google.protobuf.RpcController controller,
      com.tencent.client.common.protos.CompleteTaskReq request,
      com.google.protobuf.RpcCallback<com.tencent.client.common.protos.VoidResp> done);

  public static final
      com.google.protobuf.Descriptors.ServiceDescriptor
      getDescriptor() {
    return com.tencent.client.master.protos.ClientMasterProto.getDescriptor().getServices().get(0);
  }
  public final com.google.protobuf.Descriptors.ServiceDescriptor
      getDescriptorForType() {
    return getDescriptor();
  }

  public final void callMethod(
      com.google.protobuf.Descriptors.MethodDescriptor method,
      com.google.protobuf.RpcController controller,
      com.google.protobuf.Message request,
      com.google.protobuf.RpcCallback<
        com.google.protobuf.Message> done) {
    if (method.getService() != getDescriptor()) {
      throw new java.lang.IllegalArgumentException(
        "Service.callMethod() given method descriptor for wrong " +
        "service type.");
    }
    switch(method.getIndex()) {
      case 0:
        this.registerWorker(controller, (com.tencent.client.master.protos.RegisterWorkerReq)request,
          com.google.protobuf.RpcUtil.<com.tencent.client.master.protos.RegisterWorkerResp>specializeCallback(
            done));
        return;
      case 1:
        this.registerTask(controller, (com.tencent.client.master.protos.RegisterTaskReq)request,
          com.google.protobuf.RpcUtil.<com.tencent.client.master.protos.RegisterTaskResp>specializeCallback(
            done));
        return;
      case 2:
        this.setAngelLocation(controller, (com.tencent.client.master.protos.SetAngelLocationReq)request,
          com.google.protobuf.RpcUtil.<com.tencent.client.common.protos.VoidResp>specializeCallback(
            done));
        return;
      case 3:
        this.getAngelLocation(controller, (com.tencent.client.common.protos.VoidReq)request,
          com.google.protobuf.RpcUtil.<com.tencent.client.master.protos.GetAngelLocationResp>specializeCallback(
            done));
        return;
      case 4:
        this.heartBeat(controller, (com.tencent.client.master.protos.HeartBeatReq)request,
          com.google.protobuf.RpcUtil.<com.tencent.client.master.protos.HeartBeatResp>specializeCallback(
            done));
        return;
      case 5:
        this.clock(controller, (com.tencent.client.master.protos.ClockReq)request,
          com.google.protobuf.RpcUtil.<com.tencent.client.master.protos.ClockResp>specializeCallback(
            done));
        return;
      case 6:
        this.getClockMap(controller, (com.tencent.client.master.protos.GetClockMapReq)request,
          com.google.protobuf.RpcUtil.<com.tencent.client.master.protos.GetClockMapResp>specializeCallback(
            done));
        return;
      case 7:
        this.getGlobalBatchSize(controller, (com.tencent.client.common.protos.VoidReq)request,
          com.google.protobuf.RpcUtil.<com.tencent.client.master.protos.GetGlobalBatchResp>specializeCallback(
            done));
        return;
      case 8:
        this.completeTask(controller, (com.tencent.client.common.protos.CompleteTaskReq)request,
          com.google.protobuf.RpcUtil.<com.tencent.client.common.protos.VoidResp>specializeCallback(
            done));
        return;
      default:
        throw new java.lang.AssertionError("Can't get here.");
    }
  }

  public final com.google.protobuf.Message
      getRequestPrototype(
      com.google.protobuf.Descriptors.MethodDescriptor method) {
    if (method.getService() != getDescriptor()) {
      throw new java.lang.IllegalArgumentException(
        "Service.getRequestPrototype() given method " +
        "descriptor for wrong service type.");
    }
    switch(method.getIndex()) {
      case 0:
        return com.tencent.client.master.protos.RegisterWorkerReq.getDefaultInstance();
      case 1:
        return com.tencent.client.master.protos.RegisterTaskReq.getDefaultInstance();
      case 2:
        return com.tencent.client.master.protos.SetAngelLocationReq.getDefaultInstance();
      case 3:
        return com.tencent.client.common.protos.VoidReq.getDefaultInstance();
      case 4:
        return com.tencent.client.master.protos.HeartBeatReq.getDefaultInstance();
      case 5:
        return com.tencent.client.master.protos.ClockReq.getDefaultInstance();
      case 6:
        return com.tencent.client.master.protos.GetClockMapReq.getDefaultInstance();
      case 7:
        return com.tencent.client.common.protos.VoidReq.getDefaultInstance();
      case 8:
        return com.tencent.client.common.protos.CompleteTaskReq.getDefaultInstance();
      default:
        throw new java.lang.AssertionError("Can't get here.");
    }
  }

  public final com.google.protobuf.Message
      getResponsePrototype(
      com.google.protobuf.Descriptors.MethodDescriptor method) {
    if (method.getService() != getDescriptor()) {
      throw new java.lang.IllegalArgumentException(
        "Service.getResponsePrototype() given method " +
        "descriptor for wrong service type.");
    }
    switch(method.getIndex()) {
      case 0:
        return com.tencent.client.master.protos.RegisterWorkerResp.getDefaultInstance();
      case 1:
        return com.tencent.client.master.protos.RegisterTaskResp.getDefaultInstance();
      case 2:
        return com.tencent.client.common.protos.VoidResp.getDefaultInstance();
      case 3:
        return com.tencent.client.master.protos.GetAngelLocationResp.getDefaultInstance();
      case 4:
        return com.tencent.client.master.protos.HeartBeatResp.getDefaultInstance();
      case 5:
        return com.tencent.client.master.protos.ClockResp.getDefaultInstance();
      case 6:
        return com.tencent.client.master.protos.GetClockMapResp.getDefaultInstance();
      case 7:
        return com.tencent.client.master.protos.GetGlobalBatchResp.getDefaultInstance();
      case 8:
        return com.tencent.client.common.protos.VoidResp.getDefaultInstance();
      default:
        throw new java.lang.AssertionError("Can't get here.");
    }
  }

  public static Stub newStub(
      com.google.protobuf.RpcChannel channel) {
    return new Stub(channel);
  }

  public static final class Stub extends com.tencent.client.master.protos.AngelCleintMaster implements Interface {
    private Stub(com.google.protobuf.RpcChannel channel) {
      this.channel = channel;
    }

    private final com.google.protobuf.RpcChannel channel;

    public com.google.protobuf.RpcChannel getChannel() {
      return channel;
    }

    public  void registerWorker(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.RegisterWorkerReq request,
        com.google.protobuf.RpcCallback<com.tencent.client.master.protos.RegisterWorkerResp> done) {
      channel.callMethod(
        getDescriptor().getMethods().get(0),
        controller,
        request,
        com.tencent.client.master.protos.RegisterWorkerResp.getDefaultInstance(),
        com.google.protobuf.RpcUtil.generalizeCallback(
          done,
          com.tencent.client.master.protos.RegisterWorkerResp.class,
          com.tencent.client.master.protos.RegisterWorkerResp.getDefaultInstance()));
    }

    public  void registerTask(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.RegisterTaskReq request,
        com.google.protobuf.RpcCallback<com.tencent.client.master.protos.RegisterTaskResp> done) {
      channel.callMethod(
        getDescriptor().getMethods().get(1),
        controller,
        request,
        com.tencent.client.master.protos.RegisterTaskResp.getDefaultInstance(),
        com.google.protobuf.RpcUtil.generalizeCallback(
          done,
          com.tencent.client.master.protos.RegisterTaskResp.class,
          com.tencent.client.master.protos.RegisterTaskResp.getDefaultInstance()));
    }

    public  void setAngelLocation(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.SetAngelLocationReq request,
        com.google.protobuf.RpcCallback<com.tencent.client.common.protos.VoidResp> done) {
      channel.callMethod(
        getDescriptor().getMethods().get(2),
        controller,
        request,
        com.tencent.client.common.protos.VoidResp.getDefaultInstance(),
        com.google.protobuf.RpcUtil.generalizeCallback(
          done,
          com.tencent.client.common.protos.VoidResp.class,
          com.tencent.client.common.protos.VoidResp.getDefaultInstance()));
    }

    public  void getAngelLocation(
        com.google.protobuf.RpcController controller,
        com.tencent.client.common.protos.VoidReq request,
        com.google.protobuf.RpcCallback<com.tencent.client.master.protos.GetAngelLocationResp> done) {
      channel.callMethod(
        getDescriptor().getMethods().get(3),
        controller,
        request,
        com.tencent.client.master.protos.GetAngelLocationResp.getDefaultInstance(),
        com.google.protobuf.RpcUtil.generalizeCallback(
          done,
          com.tencent.client.master.protos.GetAngelLocationResp.class,
          com.tencent.client.master.protos.GetAngelLocationResp.getDefaultInstance()));
    }

    public  void heartBeat(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.HeartBeatReq request,
        com.google.protobuf.RpcCallback<com.tencent.client.master.protos.HeartBeatResp> done) {
      channel.callMethod(
        getDescriptor().getMethods().get(4),
        controller,
        request,
        com.tencent.client.master.protos.HeartBeatResp.getDefaultInstance(),
        com.google.protobuf.RpcUtil.generalizeCallback(
          done,
          com.tencent.client.master.protos.HeartBeatResp.class,
          com.tencent.client.master.protos.HeartBeatResp.getDefaultInstance()));
    }

    public  void clock(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.ClockReq request,
        com.google.protobuf.RpcCallback<com.tencent.client.master.protos.ClockResp> done) {
      channel.callMethod(
        getDescriptor().getMethods().get(5),
        controller,
        request,
        com.tencent.client.master.protos.ClockResp.getDefaultInstance(),
        com.google.protobuf.RpcUtil.generalizeCallback(
          done,
          com.tencent.client.master.protos.ClockResp.class,
          com.tencent.client.master.protos.ClockResp.getDefaultInstance()));
    }

    public  void getClockMap(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.GetClockMapReq request,
        com.google.protobuf.RpcCallback<com.tencent.client.master.protos.GetClockMapResp> done) {
      channel.callMethod(
        getDescriptor().getMethods().get(6),
        controller,
        request,
        com.tencent.client.master.protos.GetClockMapResp.getDefaultInstance(),
        com.google.protobuf.RpcUtil.generalizeCallback(
          done,
          com.tencent.client.master.protos.GetClockMapResp.class,
          com.tencent.client.master.protos.GetClockMapResp.getDefaultInstance()));
    }

    public  void getGlobalBatchSize(
        com.google.protobuf.RpcController controller,
        com.tencent.client.common.protos.VoidReq request,
        com.google.protobuf.RpcCallback<com.tencent.client.master.protos.GetGlobalBatchResp> done) {
      channel.callMethod(
        getDescriptor().getMethods().get(7),
        controller,
        request,
        com.tencent.client.master.protos.GetGlobalBatchResp.getDefaultInstance(),
        com.google.protobuf.RpcUtil.generalizeCallback(
          done,
          com.tencent.client.master.protos.GetGlobalBatchResp.class,
          com.tencent.client.master.protos.GetGlobalBatchResp.getDefaultInstance()));
    }

    public  void completeTask(
        com.google.protobuf.RpcController controller,
        com.tencent.client.common.protos.CompleteTaskReq request,
        com.google.protobuf.RpcCallback<com.tencent.client.common.protos.VoidResp> done) {
      channel.callMethod(
        getDescriptor().getMethods().get(8),
        controller,
        request,
        com.tencent.client.common.protos.VoidResp.getDefaultInstance(),
        com.google.protobuf.RpcUtil.generalizeCallback(
          done,
          com.tencent.client.common.protos.VoidResp.class,
          com.tencent.client.common.protos.VoidResp.getDefaultInstance()));
    }
  }

  public static BlockingInterface newBlockingStub(
      com.google.protobuf.BlockingRpcChannel channel) {
    return new BlockingStub(channel);
  }

  public interface BlockingInterface {
    public com.tencent.client.master.protos.RegisterWorkerResp registerWorker(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.RegisterWorkerReq request)
        throws com.google.protobuf.ServiceException;

    public com.tencent.client.master.protos.RegisterTaskResp registerTask(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.RegisterTaskReq request)
        throws com.google.protobuf.ServiceException;

    public com.tencent.client.common.protos.VoidResp setAngelLocation(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.SetAngelLocationReq request)
        throws com.google.protobuf.ServiceException;

    public com.tencent.client.master.protos.GetAngelLocationResp getAngelLocation(
        com.google.protobuf.RpcController controller,
        com.tencent.client.common.protos.VoidReq request)
        throws com.google.protobuf.ServiceException;

    public com.tencent.client.master.protos.HeartBeatResp heartBeat(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.HeartBeatReq request)
        throws com.google.protobuf.ServiceException;

    public com.tencent.client.master.protos.ClockResp clock(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.ClockReq request)
        throws com.google.protobuf.ServiceException;

    public com.tencent.client.master.protos.GetClockMapResp getClockMap(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.GetClockMapReq request)
        throws com.google.protobuf.ServiceException;

    public com.tencent.client.master.protos.GetGlobalBatchResp getGlobalBatchSize(
        com.google.protobuf.RpcController controller,
        com.tencent.client.common.protos.VoidReq request)
        throws com.google.protobuf.ServiceException;

    public com.tencent.client.common.protos.VoidResp completeTask(
        com.google.protobuf.RpcController controller,
        com.tencent.client.common.protos.CompleteTaskReq request)
        throws com.google.protobuf.ServiceException;
  }

  private static final class BlockingStub implements BlockingInterface {
    private BlockingStub(com.google.protobuf.BlockingRpcChannel channel) {
      this.channel = channel;
    }

    private final com.google.protobuf.BlockingRpcChannel channel;

    public com.tencent.client.master.protos.RegisterWorkerResp registerWorker(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.RegisterWorkerReq request)
        throws com.google.protobuf.ServiceException {
      return (com.tencent.client.master.protos.RegisterWorkerResp) channel.callBlockingMethod(
        getDescriptor().getMethods().get(0),
        controller,
        request,
        com.tencent.client.master.protos.RegisterWorkerResp.getDefaultInstance());
    }


    public com.tencent.client.master.protos.RegisterTaskResp registerTask(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.RegisterTaskReq request)
        throws com.google.protobuf.ServiceException {
      return (com.tencent.client.master.protos.RegisterTaskResp) channel.callBlockingMethod(
        getDescriptor().getMethods().get(1),
        controller,
        request,
        com.tencent.client.master.protos.RegisterTaskResp.getDefaultInstance());
    }


    public com.tencent.client.common.protos.VoidResp setAngelLocation(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.SetAngelLocationReq request)
        throws com.google.protobuf.ServiceException {
      return (com.tencent.client.common.protos.VoidResp) channel.callBlockingMethod(
        getDescriptor().getMethods().get(2),
        controller,
        request,
        com.tencent.client.common.protos.VoidResp.getDefaultInstance());
    }


    public com.tencent.client.master.protos.GetAngelLocationResp getAngelLocation(
        com.google.protobuf.RpcController controller,
        com.tencent.client.common.protos.VoidReq request)
        throws com.google.protobuf.ServiceException {
      return (com.tencent.client.master.protos.GetAngelLocationResp) channel.callBlockingMethod(
        getDescriptor().getMethods().get(3),
        controller,
        request,
        com.tencent.client.master.protos.GetAngelLocationResp.getDefaultInstance());
    }


    public com.tencent.client.master.protos.HeartBeatResp heartBeat(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.HeartBeatReq request)
        throws com.google.protobuf.ServiceException {
      return (com.tencent.client.master.protos.HeartBeatResp) channel.callBlockingMethod(
        getDescriptor().getMethods().get(4),
        controller,
        request,
        com.tencent.client.master.protos.HeartBeatResp.getDefaultInstance());
    }


    public com.tencent.client.master.protos.ClockResp clock(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.ClockReq request)
        throws com.google.protobuf.ServiceException {
      return (com.tencent.client.master.protos.ClockResp) channel.callBlockingMethod(
        getDescriptor().getMethods().get(5),
        controller,
        request,
        com.tencent.client.master.protos.ClockResp.getDefaultInstance());
    }


    public com.tencent.client.master.protos.GetClockMapResp getClockMap(
        com.google.protobuf.RpcController controller,
        com.tencent.client.master.protos.GetClockMapReq request)
        throws com.google.protobuf.ServiceException {
      return (com.tencent.client.master.protos.GetClockMapResp) channel.callBlockingMethod(
        getDescriptor().getMethods().get(6),
        controller,
        request,
        com.tencent.client.master.protos.GetClockMapResp.getDefaultInstance());
    }


    public com.tencent.client.master.protos.GetGlobalBatchResp getGlobalBatchSize(
        com.google.protobuf.RpcController controller,
        com.tencent.client.common.protos.VoidReq request)
        throws com.google.protobuf.ServiceException {
      return (com.tencent.client.master.protos.GetGlobalBatchResp) channel.callBlockingMethod(
        getDescriptor().getMethods().get(7),
        controller,
        request,
        com.tencent.client.master.protos.GetGlobalBatchResp.getDefaultInstance());
    }


    public com.tencent.client.common.protos.VoidResp completeTask(
        com.google.protobuf.RpcController controller,
        com.tencent.client.common.protos.CompleteTaskReq request)
        throws com.google.protobuf.ServiceException {
      return (com.tencent.client.common.protos.VoidResp) channel.callBlockingMethod(
        getDescriptor().getMethods().get(8),
        controller,
        request,
        com.tencent.client.common.protos.VoidResp.getDefaultInstance());
    }

  }

  // @@protoc_insertion_point(class_scope:ClientMaster.AngelCleintMaster)
}

