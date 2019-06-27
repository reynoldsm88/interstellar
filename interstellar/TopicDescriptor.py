class TopicDescriptor:
    def __init__( self,
                  name = "default",
                  num_partions = 1,
                  repllication_factor = 1,
                  cleanup_policy = "delete",
                  compression_type = "gzip",
                  delete_retention_ms = 86400000,
                  file_delete_delay_ms = 60000,
                  flush_messages = 9223372036854775807,
                  flush_ms = 9223372036854775807,
                  follower_replication_throttle_replicas = "",
                  index_interval_bytes = 4096,
                  leader_replication_throttled_replicas = "",
                  message_format_version = "2.2-IV1",
                  message_timestamp_difference_max_ms = 9223372036854775807,
                  message_timestamp_type = "CreateTime",
                  min_cleanable_dirty_ratio = 0.5,
                  min_compaction_lag_ms = 0,
                  min_insync_replicas = 1,
                  preallocate = False,
                  retention_bytes = -1,
                  retention_ms = 604800000,
                  segment_bytes = 1073741824,
                  segment_index_bytes = 10485760,
                  segment_jitter_ms = 604800000,
                  unclean_leader_election_enable = False,
                  message_downconversion_enable = True ):
        self.name = name
        self.num_partitions = num_partions
        self.replication_factor = repllication_factor
        self.cleanup_policy = cleanup_policy
        self.compression_type = compression_type
        self.delete_retention_ms = delete_retention_ms
        self.file_delete_delay_ms = file_delete_delay_ms
        self.flush_messages = flush_messages
        self.flush_ms = flush_ms
        self.follower_replication_throttle_replicas = follower_replication_throttle_replicas
        self.index_interval_bytes = index_interval_bytes
        self.leader_replication_throttled_replicas = leader_replication_throttled_replicas
        self.message_format_version = message_format_version
        self.message_timestamp_difference_max_ms = message_timestamp_difference_max_ms
        self.message_timestamp_type = message_timestamp_type
        self.min_cleanable_dirty_ratio = min_cleanable_dirty_ratio
        self.min_compaction_lag_ms = min_compaction_lag_ms
        self.min_insync_replicas = min_insync_replicas
        self.preallocate = preallocate
        self.retention_bytes = retention_bytes
        self.retention_ms = retention_ms
        self.segment_bytes = segment_bytes
        self.segment_index_bytes = segment_index_bytes
        self.segment_jitter_ms = segment_jitter_ms
        self.unclean_leader_election_enable = unclean_leader_election_enable
        self.message_downconversion_enable = message_downconversion_enable

    def parse( topic_yaml ):
        return TopicDescriptor( **topic_yaml.get( "topic" ) )

    def get_topic_confi( self ):
        topic_config = {
            "cleanup.policy": self.cleanup_policy,
            "compression.type": self.compression_type,
            "delete.retention.ms": self.delete_retention_ms,
            "file.delete.delay.ms": self.file_delete_delay_ms,
            "flush.messages": self.flush_messages,
            "flush.ms": self.flush_ms,
            "follower.replication.throttled.replicas": self.follower_replication_throttle_replicas,
            "index.interval.bytes": self.index_interval_bytes,
            "leader.replication.throttled.replicas": self.leader_replication_throttled_replicas,
            "message.format.version": self.message_format_version,
            "message.timestamp.difference.max.ms": self.message_timestamp_difference_max_ms,
            "message.timestamp.type": self.message_timestamp_type,
            "min.cleanable.dirty.ratio": self.min_cleanable_dirty_ratio,
            "min.compaction.lag.ms": self.min_compaction_lag_ms,
            "min.insync.replicas": self.min_insync_replicas,
            "preallocate": self.preallocate,
            "retention.bytes": self.retention_bytes,
            "retention.ms": self.retention_ms,
            "segment.bytes": self.segment_bytes,
            "segment.index.bytes": self.segment_index_bytes,
            "segment.jitter.ms": self.segment_jitter_ms,
            "unclean.leader.election.enable": self.unclean_leader_election_enable,
            "message.downconversion.enable": self.message_downconversion_enable
        }
        return topic_config