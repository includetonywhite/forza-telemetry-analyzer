# Forza Packet Layout

## Packet Size

324 bytes


## Fields

| Offset | Field | Type | Size |
|--------:|-------|------|-----:|
| 0 | is_race_on | sint32 | 4 |
| 4 | timestamp_ms | uint32 | 4 |
| 8 | engine_max_rpm | float32 | 4 |
| 12 | engine_idle_rpm | float32 | 4 |
| 16 | current_engine_rpm | float32 | 4 |
| 20 | acceleration_x | float32 | 4 |
| 24 | acceleration_y | float32 | 4 |
| 28 | acceleration_z | float32 | 4 |
| 32 | velocity_x | float32 | 4 |
| 36 | velocity_y | float32 | 4 |
| 40 | velocity_z | float32 | 4 |
| 44 | angular_velocity_x | float32 | 4 |
| 48 | angular_velocity_y | float32 | 4 |
| 52 | angular_velocity_z | float32 | 4 |
| 56 | yaw | float32 | 4 |
| 60 | pitch | float32 | 4 |
| 64 | roll | float32 | 4 |
| 68 | normalized_suspension_travel_front_left | float32 | 4 |
| 72 | normalized_suspension_travel_front_right | float32 | 4 |
| 76 | normalized_suspension_travel_rear_left | float32 | 4 |
| 80 | normalized_suspension_travel_rear_right | float32 | 4 |
| 84 | tire_slip_ratio_front_left | float32 | 4 |
| 88 | tire_slip_ratio_front_right | float32 | 4 |
| 92 | tire_slip_ratio_rear_left | float32 | 4 |
| 96 | tire_slip_ratio_rear_right | float32 | 4 |
| 100 | wheel_rotation_speed_front_left | float32 | 4 |
| 104 | wheel_rotation_speed_front_right | float32 | 4 |
| 108 | wheel_rotation_speed_rear_left | float32 | 4 |
| 112 | wheel_rotation_speed_rear_right | float32 | 4 |
| 116 | wheel_on_rumble_strip_front_left | sint32 | 4 |
| 120 | wheel_on_rumble_strip_front_right | sint32 | 4 |
| 124 | wheel_on_rumble_strip_rear_left | sint32 | 4 |
| 128 | wheel_on_rumble_strip_rear_right | sint32 | 4 |
| 132 | wheel_in_puddle_front_left | sint32 | 4 |
| 136 | wheel_in_puddle_front_right | sint32 | 4 |
| 140 | wheel_in_puddle_rear_left | sint32 | 4 |
| 144 | wheel_in_puddle_rear_right | sint32 | 4 |
| 148 | surface_rumble_front_left | float32 | 4 |
| 152 | surface_rumble_front_right | float32 | 4 |
| 156 | surface_rumble_rear_left | float32 | 4 |
| 160 | surface_rumble_rear_right | float32 | 4 |
| 164 | tire_slip_angle_front_left | float32 | 4 |
| 168 | tire_slip_angle_front_right | float32 | 4 |
| 172 | tire_slip_angle_rear_left | float32 | 4 |
| 176 | tire_slip_angle_rear_right | float32 | 4 |
| 180 | tire_combined_slip_front_left | float32 | 4 |
| 184 | tire_combined_slip_front_right | float32 | 4 |
| 188 | tire_combined_slip_rear_left | float32 | 4 |
| 192 | tire_combined_slip_rear_right | float32 | 4 |
| 196 | suspension_travel_meters_front_left | float32 | 4 |
| 200 | suspension_travel_meters_front_right | float32 | 4 |
| 204 | suspension_travel_meters_rear_left | float32 | 4 |
| 208 | suspension_travel_meters_rear_right | float32 | 4 |
| 212 | car_ordinal | sint32 | 4 |
| 216 | car_class | sint32 | 4 |
| 220 | car_performance_index | sint32 | 4 |
| 224 | drivetrain_type | sint32 | 4 |
| 228 | num_cylinders | sint32 | 4 |
| 232 | car_group | uint32 | 4 |
| 236 | smashable_vel_diff | float32 | 4 |
| 240 | smashable_mass | float32 | 4 |
| 244 | position_x | float32 | 4 |
| 248 | position_y | float32 | 4 |
| 252 | position_z | float32 | 4 |
| 256 | speed | float32 | 4 |
| 260 | power | float32 | 4 |
| 264 | torque | float32 | 4 |
| 268 | tire_temp_front_left | float32 | 4 |
| 272 | tire_temp_front_right | float32 | 4 |
| 276 | tire_temp_rear_left | float32 | 4 |
| 280 | tire_temp_rear_right | float32 | 4 |
| 284 | boost | float32 | 4 |
| 288 | fuel | float32 | 4 |
| 292 | distance_traveled | float32 | 4 |
| 296 | best_lap | float32 | 4 |
| 300 | last_lap | float32 | 4 |
| 304 | current_lap | float32 | 4 |
| 308 | current_race_time | float32 | 4 |
| 312 | lap_number | uint16 | 2 |
| 314 | race_position | uint8 | 1 |
| 315 | accel | uint8 | 1 |
| 316 | brake | uint8 | 1 |
| 317 | clutch | uint8 | 1 |
| 318 | hand_brake | uint8 | 1 |
| 319 | gear | uint8 | 1 |
| 320 | steer | sint8 | 1 |
| 321 | normalized_driving_line | sint8 | 1 |
| 322 | normalized_ai_brake_difference | sint8 | 1 |
| 323 | pad | buffer | 1 |
| 324 | packet ends | 0 |