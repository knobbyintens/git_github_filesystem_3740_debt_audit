# Tech Debt Register

Maintained by the platform reliability group. Each row points at an inline annotation in the source tree.
Descriptions mirror the annotation text with the marker keyword removed.

| File | Line | Description |
| --- | --- | --- |
| src/common/retry_policy.py | 16 | (owu): back off exponentially instead of fixed delay |
| src/common/retry_policy.py | 22 | (hbrandt): reuse pooled session for health probes |
| src/ingest/event_decoder.py | 21 | (rpatel): validate unicode escape sequences |
| src/ingest/event_decoder.py | 27 | (mzhang): reject nested groups deeper than two levels |
| src/ingest/event_decoder.py | 39 | (yliu) migrate offsets to millisecond precision |
| src/ingest/frame_reader.py | 23 | purge stale shard cache on rotation |
| src/ingest/frame_reader.py | 44 | (kvara): avoid copying frames into intermediate lists |
| src/sink/batch_writer.py | 19 | (sjensen): stream rows instead of buffering |
| src/sink/batch_writer.py | 26 | emit write latency metric per batch |
| src/transform/normalizer.py | 9 | keep timestamps as strings until the warehouse load |
| src/transform/normalizer.py | 19 | (tnakamura): replace linear scan in dedupe with hash set |
| src/transform/normalizer.py | 28 | (lchen): coerce floats through Decimal to avoid binary drift |
