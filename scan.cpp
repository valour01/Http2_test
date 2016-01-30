#include<iostream>
#include<fstream>
using namespace std;

void myexec(const char *cmd) {
    //resvec.clear();
    FILE *pp = popen(cmd, "r"); //建立管道
    if (!pp) {
        return;
    }
    char tmp[1024]; //设置一个合适的长度，以存储每一行输出
    while (fgets(tmp, sizeof(tmp), pp) != NULL) {
//        if (tmp[strlen(tmp) - 1] == '\n') {
  //          tmp[strlen(tmp) - 1] = '\0'; //去除换行符
        }
    //    resvec.push_back(tmp);
    
    pclose(pp); //关闭管道
    return;
}
int main()
{
	ifstream fp;
	fp.open("/home/jmh/filter");
	//int i=0;
	string site;
	string command;
	for(int i=0;i<800;i++){
	
	getline(fp,site);
	site="https://www."+site;
	command ="./http-test "+site;
	cout<<command<<endl;
	//system(command);
	myexec(command.c_str());
	cout<<site<<endl;
	}
}
