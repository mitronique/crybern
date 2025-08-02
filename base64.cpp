#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <openssl/evp.h>

std::string base64_encode(const std::string& input) {
    BIO* bio, * b64;
    BUF_MEM* bufferPtr;
    b64 = BIO_new(BIO_f_base64());
    bio = BIO_new(BIO_s_mem());
    bio = BIO_push(b64, bio);
    BIO_write(bio, input.c_str(), input.length());
    BIO_flush(bio);
    BIO_get_mem_ptr(bio, &bufferPtr);
    std::string output(bufferPtr->data, bufferPtr->length - 1);
    BIO_free_all(bio);
    return output;
}

std::string base64_decode(const std::string& input) {
    BIO* bio, * b64;
    char* buffer = (char*)malloc(input.length());
    memset(buffer, 0, input.length());
    b64 = BIO_new(BIO_f_base64());
    bio = BIO_new_mem_buf(input.c_str(), -1);
    bio = BIO_push(b64, bio);
    int length = BIO_read(bio, buffer, input.length());
    std::string output(buffer, length);
    BIO_free_all(bio);
    free(buffer);
    return output;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cout << "Usage: base64_tool <encode|decode> <string>\n";
        return 1;
    }
    std::string mode = argv[1];
    std::string input = argv[2];
    if (mode == "encode") {
        std::cout << base64_encode(input) << "\n";
    }
    else if (mode == "decode") {
        std::cout << base64_decode(input) << "\n";
    }
    else {
        std::cout << "Invalid mode. Use 'encode' or 'decode'.\n";
    }
    return 0;
}
