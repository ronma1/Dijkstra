## Graph Generator

This script is a command line tool for generating a random graph using Networkx.<br/>

**The graph will be generated is generated with the following format:** <br/> 
*Line1:* number of nodes<br/> 
*Line2:* number of edges<br/> 
*line3:* node(i) node(j) weight<br/> 
.<br/> 
.<br/> 
.<br/> 
*Line(n):* node(i) node(j) weight<br/> 

## Using the tool: 
**The script takes 2 arguments:**
- base_name_format - the base name for file's format for example:<br/>
For base name g the following will be generated: g0, g1, g2 .....
- num_of_graphs - number of graphs to be generated. 

```Terminal
Python graph_generator.py base_name_format num_of_graphs
```

The following sample will be generate 10 graphs with the names: <br/>
G0.txt, G1.txt ..... G9.txt 

```Terminal
Python graph_generator.py G 10 
```