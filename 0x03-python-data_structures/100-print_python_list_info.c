#include <Python.h>

/**
* print_python_list_info - prints basic info about Python lists
* @p: PyObject pointer to the Python list
*/
void print_python_list_info(PyObject *p)
{
PyListObject *list = (PyListObject *)p;
Py_ssize_t size, allocated, x;
PyObject *item;

size = PyList_Size(p);
allocated = list->allocated;

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", allocated);

for (x = 0; x < size; x++)
{
item = PyList_GetItem(p, x);
printf("Element %ld: %s\n", x, Py_TYPE(item)->tp_name);
}
}
