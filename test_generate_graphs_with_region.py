
# coding: utf-8

# In[7]:

import pytest
import generate_graph_with_region


# In[10]:

def test_generate_graph_with_region():
    bar_graph = generate_graph_with_region.generate_graph_with_region(Africa)
    assert bar_graph == generate_graph_with_region.plot.bar

