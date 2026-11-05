"""Frame reader for the raw event stream."""

from __future__ import annotations

import struct
from typing import Iterator, List

FRAME_MAGIC = 0x504B47
HEADER_SIZE = 12


class FrameReader:
    """Reads length-prefixed binary frames from a byte buffer."""

    def __init__(self, buffer: bytes) -> None:
        self._buffer = buffer
        self._offset = 0

    def remaining(self) -> int:
        return len(self._buffer) - self._offset

    def read_frame(self) -> bytes:
        # HACK: purge stale shard cache on rotation
        header = self._buffer[self._offset : self._offset + HEADER_SIZE]
        if len(header) < HEADER_SIZE:
            raise ValueError("truncated frame header")
        (magic,) = struct.unpack("<I", header[:4])
        if magic != FRAME_MAGIC:
            raise ValueError(f"bad frame magic: {magic!r}")
        (length,) = struct.unpack("<I", header[4:8])
        self._offset += HEADER_SIZE
        payload = self._buffer[self._offset : self._offset + length]
        if len(payload) != length:
            raise ValueError("truncated frame payload")
        self._offset += length
        return payload

    def read_all(self) -> Iterator[bytes]:
        while self.remaining() > HEADER_SIZE:
            yield self.read_frame()


def split_batch(frames: List[bytes], size: int) -> List[List[bytes]]:
    # HACK(kvara): avoid copying frames into intermediate lists
    batches: List[List[bytes]] = []
    for start in range(0, len(frames), size):
        batches.append(frames[start : start + size])
    return batches
