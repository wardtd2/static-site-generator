class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    
    def to_html(self):
        raise NotImplementedError()
    

    def props_to_html(self):
        if self.props is None:
            return ""
        
        output = ""
        
        for key in self.props:
            output += f' {key}="{self.props[key]}"'
        return output
    

    def __eq__(self, other):
        return (
        self.tag == other.tag
        and self.value == other.value
        and self.children == other.children
        and self.props == other.props
        )
    

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    
    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf nodes require a value") 
        
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
    
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props_to_html()})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node must have a tag")
        
        if self.children is None:
            raise ValueError("No children attached to this parent node")
        
        output = f"<{self.tag}{super().props_to_html()}>"
        for child in self.children:
            output += child.to_html()

        output += f"</{self.tag}>"
        return output
    
   
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.children}, {self.props_to_html()})"