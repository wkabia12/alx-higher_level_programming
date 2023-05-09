#include "lists.h"
/**
 *insert_node - inserts node in sorted singly linked list
 *@head: list arguement
 *@number: number to be inserted
 *Return: address of new node, Null if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *current, *ins_node;

	current = *head;
	temp = NULL;

	while (current)
	{
		temp = current;
		current = current->next;
		if (temp->n <= number && current->n > number)
		{
			ins_node = malloc(sizeof(listint_t));
			if (ins_node == NULL)
			{
				free(ins_node);
				return (NULL);
			}
			ins_node->n = number;
			ins_node->next = current;
			temp->next = ins_node;
			return (ins_node);
		}
	}
	ins_node = malloc(sizeof(listint_t));
	if (ins_node == NULL)
	{
		free(ins_node);
		return (NULL);
	}
	ins_node->n = number;
	ins_node->next = current;
	temp->next = ins_node;
	return (ins_node);
}
