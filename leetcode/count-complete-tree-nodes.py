/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int countNodes(TreeNode* root) {
        
        if(!root){
            return 0;
        }

        int l=0;
        int r=0;

        TreeNode* leftn=root;
        TreeNode* rightn=root;

        while(leftn){
            l++;
            leftn=leftn->left;
        }

        while(rightn){
            r++;
            rightn=rightn->right;
        }

        return 1+countNodes(root->left)+countNodes(root->right);
    }
};