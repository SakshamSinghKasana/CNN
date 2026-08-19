#include <iostream>
#include <fstream>
#include <nlohmann/json.hpp>

// Create an alias for convenience
using json = nlohmann::json;

json read_D(const std::string& D_file){
    // 1. Open the JSON file using an input file stream
    std::ifstream file(D_file);
    
    // Check if the file opened successfully
    if (!file.is_open()) {
        std::cerr << "Error: Could not open the file data.json" << std::endl;
        return 1;
    }

    // 2. Parse the file stream directly into a json object
    json data;
    file >> data;

    // 3. Close the file stream
    file.close();

    return data;

}
int main() {
    json data = read_D("data.json");
  
    std::cout << data;

    return 0;
}
