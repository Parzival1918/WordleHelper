fn main() {
    //Show a green "WORDLE HELPER PROGRAM" in the terminal to greet user
    println!("\x1b[32mWORDLE HELPER PROGRAM\x1b[0m");

    //Ask the user for the correct letters and their positions
    println!("Enter correct letter and position (e.g. A1, B2): ");
    let mut correct_letters = String::new();
    std::io::stdin().read_line(&mut correct_letters).unwrap();
    //Get the letters and positions
    let (correct_letters, correct_positions) = get_letters_and_positions(correct_letters);

    //Ask the user for the incorrect letters
    println!("Enter incorrect letters (e.g. C, D): ");
    let mut incorrect_letters = String::new();
    std::io::stdin().read_line(&mut incorrect_letters).unwrap();

    //Ask the user for the correct letters that are not in the right position
    println!("Enter correct letters that are not in the right position (e.g. E2, F3): ");
    let mut correct_letters_not_in_right_position = String::new();
    std::io::stdin().read_line(&mut correct_letters_not_in_right_position).unwrap();
    //Get the letters and positions
    let (correct_letters_not_in_right_position, correct_positions_not_in_right_position) = get_letters_and_positions(correct_letters_not_in_right_position);

    println!("{:?}\n{:?}", correct_letters, correct_positions);
    println!("{:?}\n{:?}", correct_letters_not_in_right_position, correct_positions_not_in_right_position);

    //Can now use user information to check words in words5 file that match the user's input
    //Open the words5 file
    let words_file = std::fs::read_to_string("../../Words/words5").unwrap();
    //Create a vector of the words
    let words_list: Vec<&str> = words_file.split("\n").collect();

    //Create a vector of the words that match the user's input
    let mut matching_words: Vec<&str> = Vec::new();

    //Loop through the words
    for word in words_list {
        //Check if the word matches the user's input
        if check_word(word, &correct_letters, &correct_positions, &incorrect_letters, &correct_letters_not_in_right_position, &correct_positions_not_in_right_position) {
            //Add the word to the matching words vector
            matching_words.push(word);
        }
    }
}

//Function that checks if a word matches the user's input
fn check_word(word: &str, correct_letters: &Vec<char>, correct_positions: &Vec<u32>, incorrect_letters: &String, correct_letters_not_in_right_position: &Vec<char>, correct_positions_not_in_right_position: &Vec<u32>) -> bool {
    //Check if the word is the correct length
    if word.len() != 5 {
        return false;
    }

    //Check if the word contains any of the incorrect letters
    for incorrect_letter in incorrect_letters.chars() {
        if word.contains(incorrect_letter) {
            return false;
        }
    }

    //Check if the word contains any of the correct letters that are not in the right position
    for (index, correct_letter) in correct_letters_not_in_right_position.iter().enumerate() {
        if word.contains(*correct_letter) {
            //Check if the position of the letter is the same as the position in the user's input
            if word.chars().nth(correct_positions_not_in_right_position[index] as usize - 1).unwrap() == *correct_letter {
                return false;
            }
        }
    }

    //Check if the word contains any of the correct letters
    for (index, correct_letter) in correct_letters.iter().enumerate() {
        //Check if the word contains the letter
        if word.contains(*correct_letter) {
            //Check if the position of the letter is the same as the position in the user's input
            if word.chars().nth(correct_positions[index] as usize - 1).unwrap() != *correct_letter {
                return false;
            }
        }
        //If the word does not contain the letter
        else {
            return false;
        }
    }

    //If the word has not been ruled out, return true
    true
}

//Function that accepts a string and returns a vector of the letters and a vector of the positions
fn get_letters_and_positions(input: String) -> (Vec<char>, Vec<u32>) {
    //Create a vector of letters
    let mut letters: Vec<char> = Vec::new();
    //Create a vector of positions
    let mut positions: Vec<u32> = Vec::new();

    //Loop through the string
    for (index, letter) in input.chars().enumerate() {
        //If the index is even, add the letter to the letters vector
        if index % 2 == 0 {
            //Check that character is not ',', '\n'
            if letter == ',' || letter == '\n' {
                continue;
            }

            letters.push(letter);
        }
        //If the index is odd, add the number to the positions vector
        else {
            //Check that character is not space
            if letter == ' ' {
                continue;
            }

            positions.push(letter.to_digit(10).unwrap());
        }
    }

    //Return the letters and positions vectors
    (letters, positions)
}