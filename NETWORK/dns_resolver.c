#include <stdio.h>
#include <netdb.h>
#include <arpa/inet.h>

int main(int argc, char *argv[]){
    if(argc <= 1){
        printf("DNS RESOLVER - MODO DE USO - ./compiled_c_file_dns_resolver hostname\n");
        return 0;
    }
    else{
        
        struct hostent *alvo =  gethostbyname(argv[1]);
        if (alvo == NULL){
            printf("OCORREU UM ERRO - TENTE NOVAMENTE\n");
        }
        printf("IP: %s\n", inet_ntoa(*((struct in_addr *)alvo->h_addr)));
    }
    

    return 0;
}


//Here, i created a simple dns resolver using C. I used gethostbyname() function, from <netdb.h>,to get the ip address.
//Furthemore, i used inet_ntoa() to converts the Internet host address in, given in network byte order, to a string in IPv4 dotted-decimal notation