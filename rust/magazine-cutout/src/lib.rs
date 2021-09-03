// This stub file contains items which aren't used yet; feel free to remove this module attribute
// to enable stricter warnings.
#![allow(unused)]

use std::collections::HashMap;

pub fn can_construct_note(magazine: &[&str], note: &[&str]) -> bool {
    let mut magazine_map: HashMap<&str, u8> = HashMap::new();
    let mut note_map: HashMap<&str, u8> = HashMap::new();

    for word in magazine {
        *magazine_map.entry(word).or_insert(0) += 1;
    }

    for word in note {
        *note_map.entry(word).or_insert(0) += 1;
    }

    for (word, n) in note_map {
        magazine_map.entry(word).or_insert(0);
        if n != magazine_map[word] {
            return false;
        }
    }

    true
}
