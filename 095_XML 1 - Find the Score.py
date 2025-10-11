#XML 1 - Find the Score


return(len(node.attrib) + sum(get_attr_number(child) for child in node))