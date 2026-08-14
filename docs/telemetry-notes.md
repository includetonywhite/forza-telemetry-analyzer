# Forza Telemetry Notes

## Project Goal

Receive UDP telemetry from Forza Horizon 6 on Xbox and analyze vehicle performance.

---

# Data Flow

Xbox
    ↓
UDP Packet
    ↓
receiver.py
    ↓
parse_packet()
    ↓
TelemetryData
    ↓
Analysis / CSV / Graphs

---

# Python struct format characters

| Character | Type | Size |
|-----------|------|------|
| ? | bool | 1 byte |
| B | Unsigned char | 1 byte |
| h | Signed short | 2 bytes |
| H | Unsigned short | 2 bytes |
| i | Signed int | 4 bytes |
| I | Unsigned int | 4 bytes |
| f | Float | 4 bytes |

---

# Current Packet Format

```python
_PACKET_FORMAT = "<IfffB"
```

Meaning:

| Field | Type | What is does/values
|------|------|

| is_race_on | signed int|1 when race is on 0 when in menus/race stopped.

| timestamp_ms | unsigned int | Can overflow to 0 eventually

| engine_max_rpm | float | engine max rpm 
| engine_idle_rpm | float | engine idle rpm
| current_engine_rpm | float | current engine rpm 

| acceleration_x | float | car's local space right
| acceleration_y | float | car's local space up
| acceleration_z | float | car's local space forward

| velocity_x | float | car's local space right
| velocity_y | float | car's local space left
| velocity_z | float | car's local space forward

| angular_velocity_x | float | car's local space rad/s pitch
| angular_velocity_x | float | car's local space rad/s yaw
| angular_velocity_x | float | car's local space rad/s roll

| yaw | float | car orientation 
| pitch | float | car orientation 
| roll | float | car orientation

| normalized_suspension_travel_front_left | float | 0.0f max strech 1 max compression
| normalized_suspension_travel_front_right | float | 0.0f max strech 1 max compression
| normalized_suspension_travel_rear_left | float | 0.0f max strech 1 max compression
| normalized_suspension_travel_rear_right | float | 0.0f max strech 1 max compression

| tire_slip_ratio_front_left | float | slip ratio 0 100 grip and ratio >1 means loss of grip
| tire_slip_ratio_front_right | float |slip ratio 0 100 grip and ratio >1 means loss of grip
| tire_slip_ratio_rear_left | float | slip ratio 0 100 grip and ratio >1 means loss of grip
| tire_slip_ratio_rear_right | float | slip ratio 0 100 grip and ratio >1 means loss of grip

| wheel_rotation_speed_front_left | float | wheel rotation speed radians/sec
| wheel_rotation_speed_front_right | float | wheel rotation speed radians/sec
| wheel_rotation_speed_rear_left | float | wheel rotation speed radians/sec
| wheel_rotation_speed_rear_right | float | wheel rotation speed radians/sec

1 when the wheel on the rumble strip
| wheel_on_rumble_strip_front_left | float |
| wheel_on_rumble_strip_front_right | float | 
| wheel_on_rumble_strip_rear_left | float |
| wheel_on_rumble_strip_rear_right | float |

1 when the wheel in a puddle
| wheel_in_puddle_front_left | int
| wheel_in_puddle_front_right | int
| wheel_in_puddle_rear_left | int
| wheel_in_puddle_rear_right | int

non-dimensional surface rumble values passed to controller force feedback
| surface_rumble_front_left | float
| surface_rumble_front_right |float
| surface_rumble_rear_left | float
| surface_rumble_rear_right | float

0 means 100% grip and |angle | > 1.0 means loss of grip.
| tire_slip_angle_front_left | float
| tire_slip_angle_front_right | float
| tire_slip_angle_rear_left | float
| tire_slip_angle_rear_right | float

0 means 100% grip and |slip | > 1.0 means loss of grip.
| tire_combined_slip_front_left | float
| tire_combined_slip_front_right |float
| tire_combined_slip_rear_left | float
| tire_combined_slip_rear_right | float

actual suspension travel in meters
| suspension_travel_meters_front_left | float
| suspension_travel_meters_front_right | float
| suspension_travel_meters_rear_left | float
| suspension_travel_meters_rear_right | float

unique id of the car make/model
| car_ordinal | signed int

0 (d -- worst cars) - 7 (x class -- best cars) inclusive
| car_class | signed int

100 (worst car) - 999 (best car) inclusive
| car_performance_index | signed int

0 = fwd, 1 = rwd, 2 = awd
| drivetrain_type | signed int

number of cylinders in the engine
| num_cylinders | signed int

car group identifier
| car_group | unsigned int

velocity loss from smashable object collision (m/s)
| smashable_vel_diff | float

mass of recently hit smashable object (kg)
| smashable_mass | float

position in world space (meters)
| position_x | float
| position_y | float
| position_z | float

speed in meters per second
| speed | float | float

power in watts
| power | float

torque in newton-meters
| torque | float

tire temperature
| tire_temp_front_left | float
| tire_temp_front_right | float
| tire_temp_rear_left | float
| tire_temp_rear_right | float

turbo/supercharger boost (psi above atmospheric)
| boost | float

0.0 = empty, 1.0 = full
| fuel | float

total distance traveled (meters)
| distance_traveled | float

lap times (seconds) | 0.0 if not applicable
| best_lap | float
| last_lap | float
| current_lap | float

total race time (seconds since driving started)
| current_race_time | float

number of laps completed
| lap_number | unsigned int

current race position
| race_position | unsigned int |

player inputs (0 to 255)
| accel | unsigned int
| brake | unsigned int
| clutch | unsigned int
| hand_brake | unsigned int

current gear
| gear | unsigned int

steering input (-127 = full left, 0 = center, 127 = full right)
| steer | signed int

driving line position (-127 to 127)
| normalized_driving_line | signed int

ai braking difference (-127 to 127)
| normalized_ai_brake_difference | signed int

Packet size:

```python
struct.calcsize("<IfffB")
```

Result:

17 bytes

---

# Lessons Learned

## struct.pack()

Converts Python values into bytes.

Example:

```python
struct.pack("<IfffB", ...)
```

---

## struct.unpack()

Converts bytes into Python values.

Example:

```python
timestamp_ms, rpm, velocity_x, throttle, gear = struct.unpack(...)
```

Returns a tuple.

---

## Why use struct.calcsize()?

Instead of remembering packet sizes manually, Python calculates the correct size.

```python
_PACKET_SIZE = struct.calcsize(_PACKET_FORMAT)
```

---

# Git Commit Style

Examples

feat: implement initial telemetry packet parser

test: add parser unit tests

fix: validate packet size

docs: add telemetry notes

refactor: simplify parser

| Forza Type | Python `struct` |
| ---------- | --------------- |
| `S32`      | `i`             |
| `U32`      | `I`             |
| `F32`      | `f`             |
| `U16`      | `H`             |
| `U8`       | `B`             |
| `S8`       | `b`             |


# Mistakes I Made

- Typed `timestamep_ms` instead of `timestamp_ms`.
- Forgot commas when constructing a dataclass.
- Accepted AI-generated code without checking it matched the format string.
- Learned that the format string is the source of truth.
- Learned to use `struct.calcsize()` instead of hardcoding packet sizes.