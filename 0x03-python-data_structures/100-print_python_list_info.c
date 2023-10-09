#include <Python.h>
/**
 * print_python_list_info - function that prints info of a python list
 * @p: PyObject pointer to the python list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc;
	Py_ssize_t x;
	PyObject *item;

	if (PyList_Check(p))
	{
		size = PyList_Size(p);
		alloc = ((PyListObject *)p)->allocated;
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", alloc);

		for (x = 0; x < size; x++)
		{
			item = PyList_GetItem(p, x);
			printf("Element %ld: %s\n", x, Py_TYPE(item)->tp_name);
		}
	}
}
