#include "rbtree.h"
#include "cJSON.h"
#include <stdlib.h>
#include <stdio.h>

// 递归转换树为JSON对象
cJSON* rbTreeToJSON(RBNode* root) {
    if (root == NULL) {
        return cJSON_CreateNull();
    }
    cJSON* node = cJSON_CreateObject();
    cJSON_AddNumberToObject(node, "key", root->key);
    cJSON_AddNumberToObject(node, "val", root->val);
    cJSON_AddStringToObject(node, "color", root->color == RED ? "red" : "black");
    cJSON_AddItemToObject(node, "left", rbTreeToJSON(root->left));
    cJSON_AddItemToObject(node, "right", rbTreeToJSON(root->right));
    return node;
}

// 保存JSON到文件
void saveJSONToFile(const char* filename, RBNode* root) {
    cJSON* jsonTree = rbTreeToJSON(root);
    char* jsonString = cJSON_Print(jsonTree);
    
    FILE* file = fopen(filename, "w");
    if (file) {
        fputs(jsonString, file);
        fclose(file);
    } else {
        perror("Error opening file");
    }

    free(jsonString);
    cJSON_Delete(jsonTree);
}

int main() {
    int keys[] = {539,914,713,751,226,85,337,665,143,398,396,93,194,528,278,393,419,327,596,514,43,314,279,658,880,998,883,519,747,176};
    int values[] = {311,194,132,708,161,315,346,956,331,822,47,859,848,394,56,263,78,582,705,310,603,756,982,173,457,327,364,20,933,834};

    int len = (sizeof(keys)/sizeof(keys[0]));
    RBTree rbt = NULL;
    printf("Staring insert.\n");
    for (int i = i; i < len; ++i) {
        RBInsert(&rbt, keys[i], values[i]);
    }
    printf("Insert: Ok\n");

    saveJSONToFile("tree.json", rbt);
    printf("JSON saved to tree.json\n");

    // 释放节点
    free(rbt->left);
    free(rbt->right);
    free(rbt);

    return 0;
}