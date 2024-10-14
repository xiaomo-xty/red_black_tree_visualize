#ifndef RBTREE_H
#define RBTREE_H

#include <stdbool.h>

typedef enum { RED, BLACK } Color;

typedef int Key;
typedef int Value;

typedef struct RBNode {
    Key key;
    Value val;
    struct RBNode* left, *right;
    int N;
    Color color;
} RBNode, *RBTree;


RBNode* newRBNode(Key key, Value val, int N, Color color);
void RBInsert(RBTree* rbt, Key key, Value val);
Value RBGetVal(const RBNode* x, Key key);
bool contains(const RBNode* x, Key key);
void RBDelete(RBTree* rbt, Key key);
void deleteMin(RBTree* rbt);
RBNode* RBMin(RBTree rbt);

#endif  // RBTREE_H
