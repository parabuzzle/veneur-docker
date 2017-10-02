Veneur Docker
=====

Veneur packaged into docker


*This is not the most efficient container right now.. it'll get better...*

# Configuration

Configuration is done with environment variables.

The container comes with sane defaults and will only *require* you to run with the `-e  DATADOG_API_KEY=your_key`

## Configurable Env Variables:

  * METRIC_MAX_LENGTH
  * TRACE_MAX_LENGTH_BYTES
  * FLUSH_MAX_PER_BODY
  * ENABLE_PROFILING
  * INTERVAL
  * READ_BUFFER_SIZE_BYTES
  * NUM_WORKERS
  * NUM_READERS
  * SSF_BUFFER_SIZE
  * PERCENTILES (comma delimited string ie -- `-e PERCENTILES='0.5,0.75,0.99'`)
  * AGGREGATES (comma delimited string ie -- `-e AGGREGATES='min,max,count'`)
  * DEBUG
  * SENTRY_DSN
  * STATS_ADDRESS
  * TAGS (comma delimited string ie -- `-e TAGS='foo:bar,chuck:norris`)
  * HOSTNAME *you should set this*
  * OMIT_EMPTY_HOSTNAME
  * UDP_ADDRESS
  * TCP_ADDRESS
  * HTTP_ADDRESS
  * FORWARD_ADDRESS
  * SSF_ADDRESS
  * TLS_KEY *you will need to get your certs into the container somehow*
  * TLS_CERTIFICATE *you will need to get your certs into the container somehow*
  * TLS_AUTHORITY_CERTIFICATE *you will need to get your certs into the container somehow*
  * DATADOG_API_HOSTNAME
  * DATADOG_API_KEY *you need to set this!*
  * DATADOG_TRACE_API_ADDRESS
