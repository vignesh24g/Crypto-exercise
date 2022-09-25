#include<stdio.h>
#include <openssl/evp.h>
#include <openssl/conf.h>
#include<string.h>

int decrypt(unigned char* cipher,int cipher_len,unsigned char* key,unsigned char* text){
    int text_len=0;
    int len=0;

    EVP_CIPHER_CTX* ctx=EVP_CIPHER_CTX_new();

    if(!ctx){
        perror("Error in cipher ctx");
        exit(-1);
    }

     if(!EVP_DecryptInit_ex(ctx,EVP_aes_128_ecb(),NULL,key,NULL)){
        perror("Error in aes decryption");
        exit(-1);
    }

    if(!EVP_DecryptUpdate(ctx,text,&len,cipher,cipher_len)){
        perror("errorin updation");
        exit(-1);
    }
    text_len += len;

    if(!EVP_DecryptFinal_ex(ctx,text +len ,&len)){
        perror("error in execution");
        exit(-1);
    }
    text_len+=len;
    EVP_CIPHER_CTX_free(ctx);
    return text_len;

}

int main(int argc,char **argv){
    unsigned char* key=(unsigned char*)"0123456789abbcdef";

    unsigned char* cipher=(unsigned char*)"4e aa c2 80 54 27 b7 33 81 0d 6a 4d b4 df 97 06 ac cd 4f b5 d3 47 73 c3 f7 06 e4 aa f5 fc ff 50";

    int cipher_len=strlen((const char*)cipher)

    printf("decrypted=\n");
    unsigned char decrypted[64];
    int dec_len=decrypt(cipher,cipher_len,key,decrypted);

    for(int i=0;i<dec_len;i++){
        printf("%c",(const char)decrypted[i]);
    }
    printf("\n");

    return 0;
}