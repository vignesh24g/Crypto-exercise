#include<stdio.h>
#include <openssl/evp.h>
#include <openssl/conf.h>
#include<string.h>

int encrypt(unsigned char* text,int text_len,unsigned char* key,unsigned char*  cipher){
    int cipher_len=0;
    int len=0;

    EVP_CIPHER_CTX* ctx=EVP_CIPHER_CTX_new();
    if(!ctx){
        perror("Error");
        exit(-1);
    }
    if(!EVP_EncryptInit_ex(ctx,EVP_aes_128_ecb(),NULL,key,NULL)){
        perror("Error in aes initailaization");
        exit(-1);
    }
    if(!EVP_EncryptUpdate(ctx,cipher,&len,text,text_len)){
        perror("Error in updation");
        exit(-1);
    }
    cipher_len+=len;
    if(!EVP_EncryptFinal_ex(ctx,cipher +len ,&len)){
        perror("Error in execution");
        exit(-1);
    }
    cipher_len +=len;
    EVP_CIPHER_CTX_free(ctx);

    return cipher_len;
}

int main(int argc,char **argv){
    unsigned char* key=(unsigned char*)"0123456789abbcdef";

    unsigned char* text=(unsigned char*)"Hello this is a confidential information regarding bank";

    int text_len=strlen((const char*)text);
    unsigned char cipher[64];

    printf("cipher=\n");
    int cipher_len=encrypt(text,text_len,key,cipher);

    for(int i=0;i<cipher_len;i++){
        printf("%02x ",cipher[i]);
    }
    printf("\n");

    return 0;
}