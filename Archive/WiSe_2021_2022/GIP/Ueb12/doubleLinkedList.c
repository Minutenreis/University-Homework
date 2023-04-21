#include <stdio.h>
#include <stdlib.h>

void createPrimes();
void printList();
struct dnode *mkNode(int val);
void insertAtHead(int val);
void deleteWithValue(int val);

struct dnode *head, *tail;

typedef struct dnode
{
    int data;
    struct dnode *next, *prev;
} dnode;

int main()
{
    int zahl;
    createPrimes();
    printf("Geben Sie eine Primzahl <100 ein, die sie loeschen wollen\n");
    scanf("%d", &zahl);
    deleteWithValue(zahl);
    printList();
    return 0;
}

void createPrimes()
{
    int prime[25] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};
    dnode *node = NULL;
    dnode *prev = NULL;
    node = mkNode(prime[0]);
    head = node;
    prev = node;
    for (int i = 1; i <= 24; i++)
    {
        node = mkNode(prime[i]);
        node->prev = prev;
        prev->next = node;
        prev = node;
    }
    tail = node;
    return;
}

void printList()
{
    dnode *node = head;
    while (node != NULL)
    {
        printf("%d ", node->data);
        node = node->next;  
    }
    printf("\n");
    return;
}

dnode *mkNode(int val)
{
    dnode *node = NULL;
    if ((node = malloc(sizeof(dnode))) != NULL)
    {
        node->data = val;
        node->next = node->prev = NULL;
        return node;
    }
    else
    {
        return NULL;
    }
}

void insertAtHead(int val)
{
    dnode *p = mkNode(val);
    p->next = head;
    if (head != NULL)
    {
        head->prev = p;
        head = p;
    }
    else
    {
        head = tail = p;
    }
    return;
}

void deleteWithValue(int val)
{
    dnode *p = head;
    while (p != NULL)
    {
        if (p->data == val)
        {
            if (p == head && p == tail)
            {
                head = NULL;
                tail = NULL;
            }
            else if (p == head)
            {
                head->next->prev = NULL;
                head = head->next;
            }
            else if (p == tail)
            {
                tail->prev->next = NULL;
                tail = tail->prev;
            }
            else
            {
                p->prev->next = p->next;
                p->next->prev = p->prev;
            }
            free(p);
            return;
        }
        p = p->next;
    }
    return;
}