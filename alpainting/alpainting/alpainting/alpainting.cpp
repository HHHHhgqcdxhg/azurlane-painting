#include <iostream>
#include <direct.h> 
using namespace std;

int main(int argc, char * argv[])
{
	string cwd = _getcwd(NULL, 0);
	string cmd = "\\py37\\python.exe __main__.py";
	cmd = cwd + cmd;
	for (int i = 1; i < argc; i++)
	{
		cmd += " ";
		cmd += argv[i];
	}
	const char *cmd_c_str = cmd.c_str();
	//cout << cmd_c_str << endl;
	system(cmd_c_str);
	//system("pause");
	return 0;
}