#include <stdio.h>
#include <sys/socket.h>
#include <netdb.h>


int main(){
    struct sockaddr_in alvo;
    int mysocket;
    int conect;

    mysocket = socket(AF_INET,SOCK_STREAM,0);
    alvo.sin_family = AF_INET;
    alvo.sin_port = htons(80);
    alvo.sin_addr.s_addr = inet_addr("192.168.0.1");
    conect = connect(mysocket, (struct sockaddr *)&alvo, sizeof alvo);

    if(conect == -1){
        printf("OCORREU UM ERRO DE CONEXÃO");
        return 0;
    }
    else{
        printf("PORTA ABERTA\n");
        close(mysocket);
        close(conect);

    }
    return 0;
}