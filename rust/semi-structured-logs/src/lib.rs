// This stub file contains items which aren't used yet; feel free to remove this module attribute
// to enable stricter warnings.
#![allow(unused)]

/// various log levels
#[derive(Clone, PartialEq, Debug)]
pub enum LogLevel {
    Debug,
    Info,
    Warning,
    Error,
}
/// primary function for emitting logs
pub fn log(level: LogLevel, message: &str) -> String {
    // unimplemented!()
    match level {
        LogLevel::Debug => return debug(message),
        LogLevel::Info => return info(message),
        LogLevel::Warning => return warn(message),
        LogLevel::Error => return error(message),
    };
}
pub fn debug(message: &str) -> String {
    return format!("[DEBUG]: {}", message);
}
pub fn info(message: &str) -> String {
    // unimplemented!()
    return format!("[INFO]: {}", message);
}
pub fn warn(message: &str) -> String {
    // unimplemented!()
    return format!("[WARNING]: {}", message);
}
pub fn error(message: &str) -> String {
    // unimplemented!()
    return format!("[ERROR]: {}", message);
}
