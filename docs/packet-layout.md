# Forza Sled Packet Layout

## Packet Size

324 bytes

## Fields

| Offset | Field | Type | Size |
|--------:|-------|------|-----:|
| 0 | is_race_on | bool | 1 |
| 4 | timestamp_ms | uint32 | 4 |
| 8 | engine_max_rpm | float | 4 |
| 12 | engine_idle_rpm | float | 4 |
| 16 | current_engine_rpm | float | 4 |