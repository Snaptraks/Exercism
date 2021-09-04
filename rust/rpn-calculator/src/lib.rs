#[derive(Debug)]
pub enum CalculatorInput {
    Add,
    Subtract,
    Multiply,
    Divide,
    Value(i32),
}

pub fn evaluate(inputs: &[CalculatorInput]) -> Option<i32> {
    // unimplemented!(
    // 	"Given the inputs: {:?}, evaluate them as though they were a Reverse Polish notation expression",
    // 	inputs,
    // );
    let mut stack: Vec<i32> = vec![];
    println!("{:#?}", inputs);
    for instruction in inputs {
        match instruction {
            CalculatorInput::Value(x) => stack.push(*x),
            _ => {
                let b = stack.pop().unwrap();
                let a = match stack.pop() {
                    Some(n) => n,
                    // if there is an operand missing, return None
                    None => return None,
                };
                match instruction {
                    CalculatorInput::Add => stack.push(a + b),
                    CalculatorInput::Subtract => stack.push(a - b),
                    CalculatorInput::Multiply => stack.push(a * b),
                    CalculatorInput::Divide => stack.push(a / b),
                    _ => {}
                }
            }
        }
    }
    if stack.len() == 1 {
        Some(stack[0])
    } else {
        None
    }
}
