#include <iostream>
#include <float.h>

using namespace std;

int main()
{
	cout << "Type\t\tBytes\t\tMin\t\t\tMax" << endl;
	cout << "Int\t\t" << sizeof(int) << "\t\t" << INT_MIN << "\t\t" <<INT_MAX << endl;
	cout << "Unsigned Int\t" << sizeof(unsigned int) << "\t\t" << 0 << "\t\t\t" <<UINT_MAX << endl;
	cout << "Long\t\t" << sizeof(long) << "\t\t" << LONG_MIN << "\t\t" << LONG_MAX << endl;
	cout << "Unsigned Long\t" << sizeof(unsigned long) << "\t\t" << 0 << "\t\t\t" << ULONG_MAX << endl;
	cout << "Float\t\t" << sizeof(float) << "\t\t" << FLT_MIN << "\t\t" << FLT_MAX << endl;
	cout << "Double\t\t" << sizeof(double) << "\t\t" << DBL_MIN << "\t\t" << DBL_MAX << endl;
	cout << "Long Double\t" << sizeof(long double) << "\t\t" << LDBL_MIN << "\t\t" << LDBL_MAX << endl;
	cout << "Char\t\t" << sizeof(char) << "\t\t" << CHAR_MIN << "\t\t\t" << CHAR_MAX << endl;
	cout << "Unsigned Char\t" << sizeof(unsigned char) << "\t\t" << 0 << "\t\t\t" << UCHAR_MAX << endl;
	cout << "Bool\t\t" << sizeof(bool) << "\t\t" << "False" << "\t\t\t" << "True" << endl;
	return 0;
}
