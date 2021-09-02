// This stub file contains items which aren't used yet; feel free to remove this module attribute
// to enable stricter warnings.
#![allow(unused)]

pub fn production_rate_per_hour(speed: u8) -> f64 {
    // unimplemented!("calculate hourly production rate at speed: {}", speed)
    let base_rate = 221.;
    let _speed = speed as f64;
    let base_rate = _speed * base_rate;
    match speed {
        0..=4 => return base_rate,
        5..=8 => return 0.9 * base_rate,
        9..=10 => return 0.77 * base_rate,
        _ => return 0.0,
    }
}

pub fn working_items_per_minute(speed: u8) -> u32 {
    // unimplemented!("calculate the amount of working items at speed: {}", speed)
    let production_per_hour = production_rate_per_hour(speed);
    let production_per_minute = production_per_hour / 60.;
    return production_per_minute as u32;
}
