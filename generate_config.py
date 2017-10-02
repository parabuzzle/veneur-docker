import os


def parse_delmited_line(line, delimter=','):
  return line.split(delimter)

# Because python standard library doesn't come with yaml... here we go

def generate_basics():
  lines = []
  lines.append('metric_max_length: ' + os.getenv('METRIC_MAX_LENGTH', '4096'))
  lines.append('trace_max_length_bytes: ' + os.getenv('TRACE_MAX_LENGTH_BYTES', '16384'))
  lines.append('flush_max_per_body: ' + os.getenv('FLUSH_MAX_PER_BODY', '25000'))
  lines.append('enable_profiling: ' + os.getenv('ENABLE_PROFILING', 'false').lower())
  lines.append('interval: ' + os.getenv('INTERVAL', '10s'))
  return ("\n").join(lines)

def generate_performance():
  lines = []
  lines.append('read_buffer_size_bytes: ' + os.getenv('READ_BUFFER_SIZE_BYTES', '2097152'))
  lines.append('num_workers: ' + os.getenv('NUM_WORKERS', '1'))
  lines.append('num_readers: ' + os.getenv('NUM_READERS', '1'))
  lines.append('ssf_buffer_size: ' + os.getenv('SSF_BUFFER_SIZE', '16384'))
  return ("\n").join(lines)

def generate_percentiles():
  percentile_string = os.getenv('PERCENTILES', '0.5,0.75,0.99')
  percentiles = parse_delmited_line(percentile_string)
  lines = []
  lines.append('percentiles:')
  for percentile in percentiles:
    lines.append('  - ' + percentile)
  return ("\n").join(lines)

def generate_aggregates():
  aggregates_string = os.getenv('AGGREGATES', 'min,max,count')
  aggregates = parse_delmited_line(aggregates_string)
  lines = []
  lines.append('aggregates:')
  for aggreate in aggregates:
    lines.append('  - ' + aggreate)
  return ("\n").join(lines)

def generate_diagnostics():
  lines = []
  lines.append('debug: ' + os.getenv('DEBUG', 'false').lower())
  lines.append('sentry_dsn: ' + os.getenv('SENTRY_DSN', '""'))
  lines.append('stats_address: ' + os.getenv('STATS_ADDRESS', "localhost:8125"))
  return ("\n").join(lines)

def generate_tags():
  tags_string = os.getenv("TAGS")
  if tags_string:
    tags = parse_delmited_line(tags)
    lines = []
    lines.append('tags:')
    for tag in tags:
      lines.append('  - ' + tag)
    return ("\n").join(lines)
  return ""

def generate_features():
  lines = []
  lines.append('hostname: ' + os.getenv('HOSTNAME', '""'))
  lines.append('omit_empty_hostname: ' + os.getenv('OMIT_EMPTY_HOSTNAME', 'false').lower())
  lines.append('udp_address: ' + os.getenv('UDP_ADDRESS', 'localhost:8125'))
  lines.append('tcp_address: ' + os.getenv('TCP_ADDRESS', 'localhost:8125'))
  lines.append('http_address: ' + os.getenv('HTTP_ADDRESS', '""'))
  return ("\n").join(lines)

def generate_forwarding():
  lines = []
  lines.append('forward_address: ' + os.getenv('FORWARD_ADDRESS', '""'))
  lines.append('ssf_address: ' + os.getenv('SSF_ADDRESS', '""'))
  lines.append('tls_key: ' + os.getenv('TLS_KEY', '""'))
  lines.append('tls_certificate: ' + os.getenv('TLS_CERTIFICATE', '""'))
  lines.append('tls_authority_certificate: ' + os.getenv('TLS_AUTHORITY_CERTIFICATE', '""'))
  return ("\n").join(lines)

def generate_sinks():
  lines = []
  lines.append('datadog_api_hostname: ' + os.getenv('DATADOG_API_HOSTNAME', 'https://app.datadoghq.com'))
  lines.append('datadog_api_key: ' + os.getenv('DATADOG_API_KEY', 'set-a-key'))
  if os.getenv('DATADOG_TRACE_API_ADDRESS'):
    lines.append('datadog_trace_api_address: ' + os.getenv('DATADOG_TRACE_API_ADDRESS'))
  return ("\n").join(lines)


sections = [
  '---',
  generate_basics(),
  generate_performance(),
  generate_percentiles(),
  generate_aggregates(),
  generate_diagnostics(),
  generate_tags(),
  generate_features(),
  generate_forwarding(),
  generate_sinks()
]

config = ("\n").join(sections)

if os.getenv("DEBUG", 'false') == 'true':
  print config

with open('config.yaml', 'w') as file:
  file.write(config)

