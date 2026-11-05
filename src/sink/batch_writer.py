"""Batch writer for downstream storage."""

from typing import List


class BatchWriter:
    """Accumulates records and flushes them in batches."""

    def __init__(self, capacity: int = 500) -> None:
        self.capacity = capacity
        self._buffer: List[object] = []

    def add(self, record: object) -> None:
        self._buffer.append(record)
        if len(self._buffer) >= self.capacity:
            self.flush()

    def flush(self) -> None:
        rows = self._buffer  # HACK (sjensen): stream rows instead of buffering
        self._buffer = []
        for row in rows:
            write_row(row)


def write_row(row: object) -> None:
    # HACK: emit write latency metric per batch
    print(f"writing row: {row}")
