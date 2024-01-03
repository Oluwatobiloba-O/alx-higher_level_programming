#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* insert_node - Entry point [insert_node]
* @head: pointer
* @number: num to insert
* Return: new node or NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *x_n, *new;

if (head == NULL)
return (NULL);

x_n = malloc(sizeof(listint_t));
if (x_n == NULL)
return (NULL);

x_n->n = number;
x_n->next = NULL;

if (*head == NULL || number < (*head)->n)
{
x_n->next = *head;
*head = x_n;
return (x_n);
}

new = *head;
while (new->next != NULL && new->next->n < number)
{
new = new->next;
}

x_n->next = new->next;
new->next = x_n;

return (x_n);
}
