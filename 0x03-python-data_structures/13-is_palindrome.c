#include "lists.h"
#include <stdbool.h>

/**
 * reverse_list - Entry point (reverse_list)
 * @head: pointer to the beginning of list
 * Return: returns the list in reverse
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *current = head;
	listint_t *next = NULL;
	listint_t *prev = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * is_palindrome - Enry point (is_palindrome)
 * @head: pointer to the beginning of list
 * Return: 0 or 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = *head;
	listint_t *middle = NULL;;

	if (*head == NULL)
	{
		return (1);
	}
	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		middle = slow;
		slow = slow->next;
	}
	slow = reverse_list(slow);
	fast = *head;
	while (slow != NULL)
	{
		if (fast->n != slow->n)
		{
			return (0);
		}
		fast = fast->next;
		slow = slow->next;
	}
	slow = reverse_list(slow);
	if (middle != NULL)
	{
		prev_slow->next = middle;
		middle->next = slow;
	}
	else
		prev_slow->next = slow;

	return (1);
}
