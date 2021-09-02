// This stub file contains items which aren't used yet; feel free to remove this module attribute
// to enable stricter warnings.
#![allow(unused)]

pub struct Player {
    pub health: u32,
    pub mana: Option<u32>,
    pub level: u32,
}

impl Player {
    pub fn revive(&self) -> Option<Player> {
        if self.health == 0 {
            Some(Player {
                health: 100,
                mana: Some(if self.level >= 10 { 100 } else { 0 }),
                level: self.level,
            })
        } else {
            None
        }
    }

    pub fn cast_spell(&mut self, mana_cost: u32) -> u32 {
        match self.level {
            0..=9 => {
                self.health -= mana_cost;
                0
            }, // hurt player, return 0
            _ => match self.mana {
                None => 0,
                Some(mana) => {
                    if mana >= mana_cost {
                        self.mana = Some(mana - mana_cost);
                        2 * mana_cost
                    } else {
                        0
                    }
                },
            },
        }
    }
}
