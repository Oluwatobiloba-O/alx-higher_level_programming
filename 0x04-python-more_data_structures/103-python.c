#include <Python.h>

/**
* print_python_list - Prints Python lists
* @p: PyObject
*/

void print_python_list(PyObject *p)
{
int size, alloc, x;
PyListObject *list = (PyListObject *)p;
PyVarObject *var = (PyVarObject *)p;

size = var->ob_size;
alloc = list->allocated;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %d\n", alloc);

for (x = 0; x < size; x++)
{
const char *type = Py_TYPE(list->ob_item[x])->tp_name;
printf("Element %d: %s\n", x, type);
}
}

/**
* print_python_bytes - Prints Python byte objects
* @p: PyObject
*/

void print_python_bytes(PyObject *p)
{
unsigned char x, size;
PyBytesObject *bytes = (PyBytesObject *)p;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
printf("  trying string: %s\n", bytes->ob_sval);

size = ((PyVarObject *)p)->ob_size > 10 ? 10 : ((PyVarObject *)p)->ob_size;

printf("  first %d bytes: ", size);
for (x = 0; x < size; x++)
{
printf("%02hhx", bytes->ob_sval[x]);
if (x == (size - 1))
printf("\n");
else
printf(" ");
}
}
