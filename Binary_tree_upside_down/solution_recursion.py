def UpsideDownBinaryTree:
	#recursion
	if root is None:
		return
	old_parent = root
	old_left = root.left
	old_right = root.right
	if old_left:
		res = UpsideDownBinaryTree(old_left)
		old_left.left = old_right
		old_left.right = old_parent
		return res
	return old_parent
