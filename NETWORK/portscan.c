#include <stdio.h>
#include <netdb.h>
#include <sys/socket.h>
#include <arpa/inet.h> 
#include <unistd.h> 


int main(int argc, char *argv[]){

    int mysocket;
    int conect;
    struct sockaddr_in target;

    char *destination;
    destination = argv[1];

    for(int i = 1; i <= 65535; i++){
        mysocket = socket(AF_INET, SOCK_STREAM, 0);
        target.sin_family = AF_INET;
        target.sin_port = htons(i);
        target.sin_addr.s_addr = inet_addr(destination);

        conect = connect(mysocket, (struct sockaddr *)&target, sizeof(target));
        if(conect == 0){
            printf("PORTA %i ABERTA",i);
        }
        close(mysocket);
        

    }

    return 0;
}