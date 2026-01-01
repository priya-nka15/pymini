DLL
#include <stdio.h>
#include <stdlib.h>

/* Employee Node Structure */
typedef struct node
{
    char ssn[20];
    char name[20];
    char department[20];
    char designation[20];
    float sal;
    long int phno;
    struct node *llink;
    struct node *rlink;
} NODE;

/* Header Node Structure */
typedef struct headnode
{
    int count;
    struct node *llink;
    struct node *rlink;
} HEAD;

/* Function Declarations */
NODE* getnode();
void ins_front(HEAD *head);
void ins_rear(HEAD *head);
void del_front(HEAD *head);
void del_rear(HEAD *head);
void display(HEAD *head);

void main()
{
    int ch;
    HEAD *head = (HEAD*)malloc(sizeof(HEAD));

    head->count = 0;
    head->llink = NULL;
    head->rlink = NULL;

    for (;;)
    {
        printf("\n**** MENU ****");
        printf("\n1. Insert at Front");
        printf("\n2. Insert at Rear");
        printf("\n3. Delete at Front");
        printf("\n4. Delete at Rear");
        printf("\n5. Display");
        printf("\n6. Exit");
        printf("\nEnter your choice: ");
        scanf("%d", &ch);

        switch (ch)
        {
            case 1: ins_front(head);
                    break;
            case 2: ins_rear(head);
                    break;
            case 3: del_front(head);
                    break;
            case 4: del_rear(head);
                    break;
            case 5: display(head);
                    break;
            case 6: exit(0);
            default: printf("Invalid choice\n");
        }
    }
}

/* Create New Node */
NODE* getnode()
{
    NODE *temp = (NODE*)malloc(sizeof(NODE));
    if (temp == NULL)
    {
        printf("NO MEMORY\n");
        exit(0);
    }
    return temp;
}

/* Insert at Front */
void ins_front(HEAD *head)
{
    NODE *newnode = getnode();

    printf("Enter SSN Name Dept Designation Salary Phone:\n");
    scanf("%s %s %s %s %f %ld",
          newnode->ssn,
          newnode->name,
          newnode->department,
          newnode->designation,
          &newnode->sal,
          &newnode->phno);

    newnode->llink = head;
    newnode->rlink = head->rlink;

    if (head->rlink != NULL)
        head->rlink->llink = newnode;

    head->rlink = newnode;
    head->count++;
}

/* Insert at Rear */
void ins_rear(HEAD *head)
{
    NODE *newnode = getnode();
    NODE *temp;

    printf("Enter SSN Name Dept Designation Salary Phone:\n");
    scanf("%s %s %s %s %f %ld",
          newnode->ssn,
          newnode->name,
          newnode->department,
          newnode->designation,
          &newnode->sal,
          &newnode->phno);

    newnode->rlink = NULL;

    if (head->rlink == NULL)
    {
        newnode->llink = head;
        head->rlink = newnode;
        head->count++;
        return;
    }

    temp = head->rlink;
    while (temp->rlink != NULL)
        temp = temp->rlink;

    temp->rlink = newnode;
    newnode->llink = temp;
    head->count++;
}

/* Delete at Front */
void del_front(HEAD *head)
{
    NODE *temp, *next;

    if (head->rlink == NULL)
    {
        printf("LIST EMPTY\n");
        return;
    }

    temp = head->rlink;
    next = temp->rlink;

    printf("Deleted Record:\n");
    printf("%s %s %s %s %.2f %ld\n",
           temp->ssn,
           temp->name,
           temp->department,
           temp->designation,
           temp->sal,
           temp->phno);

    head->rlink = next;
    if (next != NULL)
        next->llink = head;

    free(temp);
    head->count--;
}

/* Delete at Rear */
void del_rear(HEAD *head)
{
    NODE *present, *previous;

    if (head->rlink == NULL)
    {
        printf("LIST EMPTY\n");
        return;
    }

    previous = head;
    present = head->rlink;

    while (present->rlink != NULL)
    {
        previous = present;
        present = present->rlink;
    }

    printf("Deleted Record:\n");
    printf("%s %s %s %s %.2f %ld\n",
           present->ssn,
           present->name,
           present->department,
           present->designation,
           present->sal,
           present->phno);

    previous->rlink = NULL;
    free(present);
    head->count--;
}

/* Display */
void display(HEAD *head)
{
    NODE *temp;

    if (head->rlink == NULL)
    {
        printf("LIST EMPTY\n");
        return;
    }

    printf("\nSSN\tNAME\tDEPT\tDESIGNATION\tSALARY\tPHONE\n");
    printf("------------------------------------------------------------\n");

    temp = head->rlink;
    while (temp != NULL)
    {
        printf("%s\t%s\t%s\t%s\t%.2f\t%ld\n",
               temp->ssn,
               temp->name,
               temp->department,
               temp->designation,
               temp->sal,
               temp->phno);
        temp = temp->rlink;
    }

    printf("\nTotal Employees: %d\n", head->count);
}

BST
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* BST Node Structure */
typedef struct tree
{
    char isbn[14];
    char btitle[40];
    struct tree *llink;
    struct tree *rlink;
} TNODE;

/* Function declarations */
TNODE* insert(TNODE *root);
void inorder(TNODE *root);
void preorder(TNODE *root);
void postorder(TNODE *root);
int search(TNODE *root, char *key);

/* Macro for traversal */
#define TRAVERSE(root, func, msg) \
    if (root == NULL)             \
        printf("Tree is empty\n");\
    else                          \
    {                             \
        printf("%s", msg);        \
        func(root);               \
    }

/* Main Function */
int main()
{
    TNODE *root = NULL;
    int choice, flag;
    char isbn[14];

    for (;;)
    {
        printf("\nEnter");
        printf("\n1. Insert");
        printf("\n2. Inorder Traversal");
        printf("\n3. Preorder Traversal");
        printf("\n4. Postorder Traversal");
        printf("\n5. Search");
        printf("\n6. Exit");
        printf("\nChoice: ");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1:
                root = insert(root);
                break;

            case 2:
                TRAVERSE(root, inorder, "Inorder Traversal\n");
                break;

            case 3:
                TRAVERSE(root, preorder, "Preorder Traversal\n");
                break;

            case 4:
                TRAVERSE(root, postorder, "Postorder Traversal\n");
                break;

            case 5:
                printf("Enter ISBN to search:\n");
                scanf("%s", isbn);
                flag = search(root, isbn);
                if (flag == -1)
                    printf("Unsuccessful search!!!\n");
                else
                    printf("Successful search!!!\n");
                break;

            case 6:
                exit(0);

            default:
                printf("Invalid choice\n");
        }
    }
}

/* Insert nodes into BST */
TNODE* insert(TNODE *root)
{
    int n, i, flag, cmp;
    TNODE *temp, *prev, *newN;
    TNODE t;

    t.llink = NULL;
    t.rlink = NULL;

    printf("Enter number of nodes\n");
    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        printf("Enter ISBN and Book-Title:\n");
        scanf("%s", t.isbn);
        scanf(" %[^\n]", t.btitle);

        newN = (TNODE*)malloc(sizeof(TNODE));
        *newN = t;

        if (root == NULL)
        {
            root = newN;
            continue;
        }

        temp = root;
        prev = NULL;
        flag = 0;

        while (temp != NULL)
        {
            prev = temp;
            cmp = strcmp(t.isbn, temp->isbn);

            if (cmp == 0)
            {
                printf("Redundant data not allowed\n");
                flag = 1;
                break;
            }
            else if (cmp < 0)
                temp = temp->llink;
            else
                temp = temp->rlink;
        }

        if (flag == 1)
            continue;

        if (cmp < 0)
            prev->llink = newN;
        else
            prev->rlink = newN;
    }
    return root;
}

/* Search a book by ISBN */
int search(TNODE *root, char *key)
{
    if (root != NULL)
    {
        if (strcmp(key, root->isbn) == 0)
        {
            printf("Book Found: %s\n", root->btitle);
            return 1;
        }
        else if (strcmp(key, root->isbn) < 0)
            return search(root->llink, key);
        else
            return search(root->rlink, key);
    }
    return -1;
}

/* Inorder Traversal */
void inorder(TNODE *root)
{
    if (root != NULL)
    {
        inorder(root->llink);
        printf("%s : %s\n", root->isbn, root->btitle);
        inorder(root->rlink);
    }
}

/* Preorder Traversal */
void preorder(TNODE *root)
{
    if (root != NULL)
    {
        printf("%s : %s\n", root->isbn, root->btitle);
        preorder(root->llink);
        preorder(root->rlink);
    }
}

/* Postorder Traversal */
void postorder(TNODE *root)
{
    if (root != NULL)
    {
        postorder(root->llink);
        postorder(root->rlink);
        printf("%s : %s\n", root->isbn, root->btitle);
    }
}
DFS BFS
#include <stdio.h>
#include <stdlib.h>

#define SIZE 20

/* Function declarations */
void bfs(int n, int source, int adj[SIZE][SIZE], int visited[]);
void dfs(int n, int source, int adj[SIZE][SIZE], int visited[]);

int main()
{
    int n, adj[SIZE][SIZE];
    int visited[SIZE] = {0};
    int source, i, j, choice;

    printf("Enter number of cities (vertices):\n");
    scanf("%d", &n);

    printf("Enter the adjacency matrix:\n");
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            scanf("%d", &adj[i][j]);

    printf("\nAdjacency Matrix:\n");
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
            printf("%d\t", adj[i][j]);
        printf("\n");
    }

    printf("\nEnter source city (vertex):\n");
    scanf("%d", &source);

    printf("\nChoose traversal method:\n");
    printf("1. BFS\n2. DFS\n");
    scanf("%d", &choice);

    /* Reset visited array */
    for (i = 0; i < n; i++)
        visited[i] = 0;

    if (choice == 1)
    {
        printf("\nBFS Traversal starting from city %d:\n", source);
        bfs(n, source, adj, visited);
    }
    else if (choice == 2)
    {
        printf("\nDFS Traversal starting from city %d:\n", source);
        dfs(n, source, adj, visited);
    }
    else
    {
        printf("Invalid choice\n");
        return 0;
    }

    printf("\n\nReachability of cities:\n");
    for (i = 0; i < n; i++)
    {
        if (visited[i])
            printf("City %d is reachable\n", i);
        else
            printf("City %d is NOT reachable\n", i);
    }

    return 0;
}

/* BFS Function */
void bfs(int n, int source, int adj[SIZE][SIZE], int visited[])
{
    int queue[SIZE];
    int front = 0, rear = 0;
    int u, v;

    visited[source] = 1;
    queue[rear++] = source;

    while (front < rear)
    {
        u = queue[front++];

        for (v = 0; v < n; v++)
        {
            if (adj[u][v] == 1 && visited[v] == 0)
            {
                visited[v] = 1;
                queue[rear++] = v;
            }
        }
    }
}

/* DFS Function */
void dfs(int n, int source, int adj[SIZE][SIZE], int visited[])
{
    int v;
    visited[source] = 1;

    for (v = 0; v < n; v++)
    {
        if (adj[source][v] == 1 && visited[v] == 0)
        {
            dfs(n, v, adj, visited);
        }
    }
}
Hashing
#include <stdio.h>
#include <stdlib.h>

#define SIZE 20

/* Function declarations */
void linearProbing(int hashTable[], int m, int regNumbers[], int n);
void quadraticProbing(int hashTable[], int m, int regNumbers[], int n);
void displayHashTable(int hashTable[], int m);

int main()
{
    int m, n, choice;
    int regNumbers[SIZE];
    int hashTable[SIZE];
    int i;

    printf("Enter number of storage locations (m): ");
    scanf("%d", &m);

    printf("Enter number of vehicle registrations to insert: ");
    scanf("%d", &n);

    printf("Enter %d vehicle registration numbers:\n", n);
    for (i = 0; i < n; i++)
        scanf("%d", &regNumbers[i]);

    while (1)
    {
        /* Initialize hash table as empty */
        for (i = 0; i < m; i++)
            hashTable[i] = -1;

        printf("\n==== Vehicle Registration Hashing ====\n");
        printf("1. Insert using Linear Probing\n");
        printf("2. Insert using Quadratic Probing\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1:
                linearProbing(hashTable, m, regNumbers, n);
                displayHashTable(hashTable, m);
                break;

            case 2:
                quadraticProbing(hashTable, m, regNumbers, n);
                displayHashTable(hashTable, m);
                break;

            case 3:
                exit(0);

            default:
                printf("Invalid choice! Try again.\n");
        }
    }

    return 0;
}

/* Linear Probing Function */
void linearProbing(int hashTable[], int m, int regNumbers[], int n)
{
    int i, j, key, index;

    for (i = 0; i < n; i++)
    {
        key = regNumbers[i];
        index = key % m;
        j = 0;

        while (hashTable[(index + j) % m] != -1 && j < m)
            j++;

        if (j < m)
            hashTable[(index + j) % m] = key;
        else
            printf("Hash table is full. Cannot insert %d\n", key);
    }
}

/* Quadratic Probing Function */
void quadraticProbing(int hashTable[], int m, int regNumbers[], int n)
{
    int i, j, key, index;

    for (i = 0; i < n; i++)
    {
        key = regNumbers[i];
        index = key % m;
        j = 0;

        while (hashTable[(index + j * j) % m] != -1 && j < m)
            j++;

        if (j < m)
            hashTable[(index + j * j) % m] = key;
        else
            printf("Hash table is full. Cannot insert %d\n", key);
    }
}

/* Display Hash Table */
void displayHashTable(int hashTable[], int m)
{
    int i;
    printf("\nHash Table State:\n");

    for (i = 0; i < m; i++)
    {
        if (hashTable[i] == -1)
            printf("Slot %d : EMPTY\n", i);
        else
            printf("Slot %d : %d\n", i, hashTable[i]);
    }
}
