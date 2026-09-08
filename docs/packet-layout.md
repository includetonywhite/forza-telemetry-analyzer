# Forza Sled Packet Layout

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
| 30 | velocity_x | float32 | 4 |
| 34 | velocity_y | float32 | 4 |
| 38 | velocity_z | float32 | 4 |
| 42 | angular_velocity_x | float32 | 4 |
| 46 | angular_velocity_y | float32 | 4 |
| 50 | angular_velocity_z | float32 | 4 |
| 54 | yaw | float32 | 4 |
| 58 | pitch | float32 | 4 |
| 62 | roll | float32 | 4 |
| 66 | normalized_suspension_travel_front_left | float32 | 4 |
| 70 | normalized_suspension_travel_front_right | float32 | 4 |
| 74 | normalized_suspension_travel_rear_left | float32 | 4 |
| 78 | normalized_suspension_travel_rear_right | float32 | 4 |
| 82 | tire_slip_ratio_front_left | float32 | 4 |
| 86 | tire_slip_ratio_front_right | float32 | 4 |
| 90 | tire_slip_ratio_rear_left | float32 | 4 |
| 94 | tire_slip_ratio_rear_right | float32 | 4 |
| 98 | wheel_rotation_speed_front_left | float32 | 4 |
| 102 | wheel_rotation_speed_front_right | float32 | 4 |
| 106 | wheel_rotation_speed_rear_left | float32 | 4 |
| 110 | wheel_rotation_speed_rear_right | float32 | 4 |
| 111 | wheel_on_rumble_strip_front_left | sint32 | 1 |
| 112 | wheel_on_rumble_strip_front_right | sint32 | 1 |
| 113 | wheel_on_rumble_strip_rear_left | sint32 | 1 |
| 114 | wheel_on_rumble_strip_rear_right | sint32 | 1 |
| 115 | wheel_in_puddle_front_left | sint32 | 1 |
| 116 | wheel_in_puddle_front_right | sint32 | 1 |
| 118 | wheel_in_puddle_rear_left | sint32 | 1 |
| 119 | wheel_in_puddle_rear_right | sint32 | 1 |
| 123 | surface_rumble_front_left | float32 | 4 |
| 127 | surface_rumble_front_right | float32 | 4 |
| 131 | surface_rumble_rear_left | float32 | 4 |
| 135 | surface_rumble_rear_right | float32 | 4 |
| 139 | tire_slip_angle_front_left | float32 | 4 |
| 143 | tire_slip_angle_front_right | float32 | 4 |
| 147 | tire_slip_angle_rear_left | float32 | 4 |
| 151 | tire_slip_angle_rear_right | float32 | 4 |
| 155 | tire_combined_slip_front_left | float32 | 4 |
| 159 | tire_combined_slip_front_right | float32 | 4 |
| 163 | tire_combined_slip_rear_left | float32 | 4 |
| 167 | tire_combined_slip_rear_right | float32 | 4 |
| 171 | suspension_travel_meters_front_left | float32 | 4 |
| 175 | suspension_travel_meters_front_right | float32 | 4 |
| 179 | suspension_travel_meters_rear_left | float32 | 4 |
| 183 | suspension_travel_meters_rear_right | float32 | 4 |
| 230 | car_ordinal | sint32 | 1 |
| 231 | car_class | sint32 | 1 |
| 232 | car_performance_index | sint32 | 1 |
| 233 | drivetrain_type | sint32 | 1 |
| 234 | num_cylinders | sint32 | 1 |
| 235 | car_group | uint32 | 1 |
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
323 pad 1
324 end