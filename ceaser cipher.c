#include<stdio.h>
#include<string.h>
#include<ctype.h>

int main(){
    char msg[200],des;
    int key;

    printf("What Do You Want To Do?\n");

start:
    printf("1. Encryption\n");
    printf("2. Decryption\n");

    int choose;
    scanf("%d",&choose);

    while(choose>2){
        printf("Warning.....!!!\n");
        printf("Please! Enter number between 1 & 2\n");
        scanf("%d",&choose);
    }

    printf("Message : ");
    scanf("%s",&msg);

    printf("Key : ");
    scanf("%d",&key);

    if(choose==1){
        printf("Encripted Message : ");
        encryption(msg,key);
    }else{
        printf("Encripted Message : ");
        decryption(msg,key);
    }
again:
    printf("Do you want to continue (y/n) : ");
    scanf("%s",&des);
    if(tolower(des) == 'y'){
        goto start;
    }else if(tolower(des) == 'n'){
        goto end;
    }else{
        printf("Wrong Press....\n");
        goto again;
    }

end:
    printf("Thank You");
    return 0;
}

void encryption(char msg[],int key){
    int i;
    char ch;
    for(i=0;i<strlen(msg);i++){

        ch = msg[i];

        if(isupper(ch)){
            int num = (int)(ch) - (int)('A');
            num = (num+key)%26;
            num = num + (int)('A');
            ch = (char)(num);
            printf("%c",ch);
        }
        if(islower(ch)){
            int num = (int)(ch) - (int)('a');
            num = (num+key)%26;
            num = num + (int)('a');
            ch = (char)(num);
            printf("%c",ch);
        }

    }
    printf("\n");
}

void decryption(char msg[],int key){
    int i;
    char ch;
    for(i=0;i<strlen(msg);i++){

        ch = msg[i];

        if(isupper(ch)){
            int num = (int)(ch) - (int)('A');
            num = (num-key)%26;
            while(num<0){
                num = num+26;
            }
            num = num + (int)('A');
            ch = (char)(num);
            printf("%c",ch);
        }
        if(islower(ch)){
            int num = (int)(ch) - (int)('a');
            num = (num-key)%26;
            num = num + (int)('a');
            ch = (char)(num);
            printf("%c",ch);
        }

    }
    printf("\n");
}
