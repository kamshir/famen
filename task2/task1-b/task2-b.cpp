#include <iostream>
#include <float.h>
using namespace std;

int main()
{
	cout << "Type\t\tBytes\t\tMin\t\t\tMax" << endl;
	cout << "Double\t\t" << sizeof(double) << "\t\t" << DBL_MIN << "\t\t" << DBL_MAX << endl;
	cout << "Float\t\t" << sizeof(float) << "\t\t" << FLT_MIN << "\t\t" << FLT_MAX << endl;
	return 0;
}
