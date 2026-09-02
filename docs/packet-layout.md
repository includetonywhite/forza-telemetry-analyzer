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
| 20 | acceleration_x | float | 4 |
| 24 | acceleration_y | float | 4 |
| 26 | acceleration_z | float | 4 |
| 30 | velocity_x | float | 4 |
| 34 | velocity_y | float | 4 |
| 38 | velocity_z | float | 4 |
| 42 | angular_velocity_x | float | 4 |
| 46 | angular_velocity_y | float | 4 |
| 50 | angular_velocity_z | float | 4 |
| 50 | angular_velocity_z | float | 4 |
| 50 | yaw | float | 4 |
| 50 | pitch | float | 4 |
| 50 | roll | float | 4 |
| xx | normalized_suspension_travel_front_left | float | 4 |
| xx | normalized_suspension_travel_front_right | float | 4 |
| xx | normalized_suspension_travel_rear_left | float | 4 |
| xx | normalized_suspension_travel_rear_right | float | 4 |
| xx | tire_slip_ratio_front_left | float | 4 |
| xx | tire_slip_ratio_front_right | float | 4 |
| xx | tire_slip_ratio_rear_left | float | 4 |
| xx | tire_slip_ratio_rear_right | float | 4 |
| xx | wheel_rotation_speed_front_left | float | 4 |
| xx | wheel_rotation_speed_front_right | float | 4 |
| xx | wheel_rotation_speed_rear_left | float | 4 |
| xx | wheel_rotation_speed_rear_right | float | 4 |
| xx | wheel_on_rumble_strip_front_left | float | 4 |
| xx | wheel_on_rumble_strip_front_right | int |
| xx | wheel_on_rumble_strip_rear_left | int |
| xx | wheel_on_rumble_strip_rear_right | int |
| xx | wheel_in_puddle_front_left | int |
| xx | wheel_in_puddle_front_right | int |
| xx | wheel_in_puddle_rear_left | int |
| xx | wheel_in_puddle_rear_right | int |
| xx | surface_rumble_front_left | float | 4 |
| xx | surface_rumble_front_right | float | 4 |
| xx | surface_rumble_rear_left | float | 4 |
| xx | surface_rumble_rear_right | float | 4 |
| xx | tire_slip_angle_front_left | float | 4 |
| xx | tire_slip_angle_front_right | float | 4 |
| xx | tire_slip_angle_rear_left | float | 4 |
| xx | tire_slip_angle_rear_right | float | 4 |
| xx | tire_combined_slip_front_left | float | 4 |
| xx | tire_combined_slip_front_right | float | 4 |
| xx | tire_combined_slip_rear_left | float | 4 |
| xx | tire_combined_slip_rear_right | float | 4 |
| xx | suspension_travel_meters_front_left | float | 4 |
| xx | suspension_travel_meters_front_right | float | 4 |
| xx | suspension_travel_meters_rear_left | float | 4 |
| xx | suspension_travel_meters_rear_right | float | 4 |
| xx | car_ordinal: int
| xx | car_class: int
| xx | car_performance_index: int
| xx | drivetrain_type: int
| xx | num_cylinders: int
| xx | car_group: int
| xx | smashable_vel_diff | float | 4 |
| xx | smashable_mass | float | 4 |
| xx | position_x | float | 4 |
| xx | position_y | float | 4 |
| xx | position_z | float | 4 |
| xx | speed | float | 4 |
| xx | power | float | 4 |
| xx | torque | float | 4 |
| xx | tire_temp_front_left: float
| xx | tire_temp_front_right: float
| xx | tire_temp_rear_left: float
| xx | tire_temp_rear_right: float
| xx | boost: float
| xx | fuel: float
| xx | distance_traveled: float
| xx | best_lap: float
| xx | last_lap: float
| xx | current_lap: float
| xx | current_race_time: float
| xx | lap_number: int
| xx | race_position: int
| xx | accel: int
| xx | brake: int
| xx | clutch: int
| xx | hand_brake: int
| xx | gear: int
| xx | steer: int
| xx | normalized_driving_line: int
| xx | normalized_ai_brake_difference: int
