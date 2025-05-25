class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    return self.depth_first_search(self.root, id)
  
  def depth_first_search(self, node, id):
    if node["id"] == id:
      return node
    
    for child in node["children"]:
      result = self.depth_first_search(child, id)
      if result: return result

    return None
  

root = {
    "tag_name": "div",
    "id": "container",
    "text_content": "",
    "children": [
      {
            "tag_name": "h1",
            "id": "heading",
            "text_content": "Hello",
            "children": []
      },
      {
            "tag_name": "p",
            "id": "intro",
            "text_content": "Welcome",
            "children": []
      }
    ]
  }


tree = Tree(root)
print(tree.get_element_by_id("intro"))

    
