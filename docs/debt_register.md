# Tech Debt Register

Maintained by the platform reliability group. Each row points at an inline annotation in the source tree.
Descriptions mirror the annotation text with the marker keyword removed.

| File | Line | Description |
| --- | --- | --- |
| src/ingest/frame_reader.py | 23 | purge stale shard cache on rotation |
| src/ingest/frame_reader.py | 52 | (kvara): drop legacy v0 frame layout |
| src/ingest/frame_reader.py | 43 | (kvara): avoid copying frames into intermediate lists |
| src/ingest/event_decoder.py | 21 | (rpatel): validate unicode escape sequences |
| src/ingest/event_decoder.py | 27 | (mzhang): reject nested groups deeper than two levels |
| src/ingest/event_decoder.py | 36 | (rpatel): remove fallback decoder once clients upgrade |
| src/transform/normalizer.py | 18 | (tnakamura): replace linear scan in dedupe with hash set |
| src/transform/normalizer.py | 28 | (lchen): coerce floats through Decimal to avoid binary drift |
| src/sink/batch_writer.py | 19 | (sjensen): stream rows instead of buffering |
| src/sink/batch_writer.py | 25 | emit write latency metric per batch |
| src/sink/batch_writer.py | 31 | (sjensen): rotate writer buffer on memory pressure |
| src/common/retry_policy.py | 15 | (owu): back off exponentially instead of fixed delay |
| src/transform/normalizer.py | 35 | (lchen): normalize mixed timezone offsets |
