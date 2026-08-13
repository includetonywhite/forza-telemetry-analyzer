from dataclasses import dataclass


@dataclass(frozen=True)
class TelemetryData:
    is_race_on: int
    timestamp_ms: int
    engine_max_rpm: float
    engine_idle_rpm: float
    current_engine_rpm: float
    acceleration_x: float
    acceleration_y: float
    acceleration_z: float
    velocity_x: float
    velocity_y: float
    velocity_z: float
    angular_velocity_x: float
    angular_velocity_y: float
    angular_velocity_z: float
    yaw: float
    pitch: float
    roll: float
    normalized_suspension_travel_front_left: float
    normalized_suspension_travel_front_right: float
    normalized_suspension_travel_rear_left: float
    normalized_suspension_travel_rear_right: float
    tire_slip_ratio_front_left: float
    tire_slip_ratio_front_right: float
    tire_slip_ratio_rear_left: float
    tire_slip_ratio_rear_right: float
    wheel_rotation_speed_front_left: float
    wheel_rotation_speed_front_right: float
    wheel_rotation_speed_rear_left: float
    wheel_rotation_speed_rear_right: float
    wheel_on_rumble_strip_front_left: int
    wheel_on_rumble_strip_front_right: int
    wheel_on_rumble_strip_rear_left: int
    wheel_on_rumble_strip_rear_right: int
    wheel_in_puddle_front_left: int
    wheel_in_puddle_front_right: int
    wheel_in_puddle_rear_left: int
    wheel_in_puddle_rear_right: int
    surface_rumble_front_left: float
    surface_rumble_front_right: float
    surface_rumble_rear_left: float
    surface_rumble_rear_right: float
    tire_slip_angle_front_left: float
    tire_slip_angle_front_right: float
    tire_slip_angle_rear_left: float
    tire_slip_angle_rear_right: float
    tire_combined_slip_front_left: float
    tire_combined_slip_front_right: float
    tire_combined_slip_rear_left: float
    tire_combined_slip_rear_right: float
    suspension_travel_meters_front_left: float
    suspension_travel_meters_front_right: float
    suspension_travel_meters_rear_left: float
    suspension_travel_meters_rear_right: float
    car_ordinal: int
    car_class: int
    car_performance_index: int
    drivetrain_type: int
    num_cylinders: int
    car_group: int
    smashable_vel_diff: float
    smashable_mass: float
    position_x: float
    position_y: float
    position_z: float
#    speed: float
#    power: float
#    torque: float
#    tire_temp_front_left: float
#    tire_temp_front_right: float
#    tire_temp_rear_left: float
#    tire_temp_rear_right: float
#    boost: float
#    fuel: float
#    distance_traveled: float
#    best_lap: float
#    last_lap: float
#    current_lap: float
#    current_race_time: float
#    lap_number: int
#    race_position: int
#    accel: int
#    brake: int
#    clutch: int
#    hand_brake: int
#    gear: int
#    steer: int
#    normalized_driving_line: int
#    normalized_ai_brake_difference: int
    
