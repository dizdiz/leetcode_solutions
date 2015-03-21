def UpsideDownBinaryTree:
	if root is None:
		return
	cur = root
	stack = []
	while cur:
		stack.append(cur)
		cur = cur.left
	newroot = stack[-1]
	while stack:
		p = stack.pop()
		#p.left = p.right = None
		p.left = stack[-1].right
		p.right = stack[-1]
	return newroot
