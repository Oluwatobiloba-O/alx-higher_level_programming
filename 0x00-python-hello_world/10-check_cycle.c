#include "lists.h"

/**
 * check_cycle - Entry point [check_cycle]
 * @list: pointer
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
listint_t *fast = list;
listint_t *slow = list;

while (fast && slow && fast->next != NULL)
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
return (1);
}
return (0);
}
