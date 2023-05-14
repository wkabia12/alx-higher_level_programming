#include "lists.h"
/**
 *is_palindrome - checks palindrome in singly linked list
 *@head: list arguement
 *Return: 1 if True else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;

	current = *head;
	int i = 0, j = 0, k = 0;

	if (current == NULL)
	{
		return (1);
	}
	while (current)
	{
		current = current->next;
		i++;
	}

	int temp[i];
	int temp2[i];
	current = *head;

	while (current)
	{
		temp[j] = current->n;
		current = current->next;
		j++;
	}
	for (; k < i; k++)
	{
		temp2[i - 1 - k] = temp[k];
	}
	k = 0;
	for (; k < i; k++)
	{
		if (temp[k] != temp2[k])
			return (0);
	}
	return (1);
}
