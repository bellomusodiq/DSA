from data_structures.graph import Graph


def make_graph():
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "E")
    graph.add_edge("D", "F")
    return graph


def test_has_path_returns_true_for_connected_vertices():
    graph = make_graph()

    assert graph.has_path("A", "F") is True
    assert graph.has_path("F", "A") is True


def test_has_path_returns_false_for_missing_or_unreachable_vertices():
    graph = make_graph()
    graph.add_vertex("Z")

    assert graph.has_path("A", "Z") is False
    assert graph.has_path("A", "missing") is False


def test_has_path_returns_true_for_same_vertex():
    graph = make_graph()

    assert graph.has_path("C", "C") is True


def test_shortest_path_returns_path_in_order():
    graph = make_graph()

    assert graph.shortest_path("A", "F") == ["A", "B", "D", "F"]
    assert graph.shortest_path("C", "C") == ["C"]


def test_shortest_path_returns_none_when_no_path_exists():
    graph = make_graph()
    graph.add_vertex("Z")

    assert graph.shortest_path("A", "Z") is None
    assert graph.shortest_path("A", "missing") is None


def test_add_edge_creates_vertices_and_undirected_connection():
    graph = Graph()

    graph.add_edge("A", "B")

    assert graph.has_vertex("A") is True
    assert graph.has_vertex("B") is True
    assert graph.has_edge("A", "B") is True
    assert graph.has_edge("B", "A") is True
    assert graph.neighbors("A") == {"B"}


def test_neighbors_returns_a_copy():
    graph = make_graph()
    neighbors = graph.neighbors("A")

    neighbors.clear()

    assert graph.neighbors("A") == {"B", "C"}


def test_degree_returns_zero_for_missing_vertex():
    graph = make_graph()

    assert graph.degree("A") == 2
    assert graph.degree("missing") == 0
    assert graph.out_degree("A") == 2
    assert graph.in_degree("A") == 2


def test_remove_edge_removes_both_directions():
    graph = make_graph()

    assert graph.remove_edge("A", "B") is True
    assert graph.has_edge("A", "B") is False
    assert graph.has_edge("B", "A") is False
    assert graph.remove_edge("A", "B") is False


def test_remove_vertex_removes_vertex_and_incident_edges():
    graph = make_graph()

    assert graph.remove_vertex("B") is True
    assert graph.has_vertex("B") is False
    assert graph.has_edge("A", "B") is False
    assert graph.has_edge("B", "D") is False
    assert graph.remove_vertex("B") is False


def test_traversals_visit_each_reachable_vertex_once():
    graph = make_graph()
    expected_vertices = {"A", "B", "C", "D", "E", "F"}

    bfs_result = graph.bfs("A")
    dfs_result = graph.dfs("A")
    recursive_dfs_result = graph.dfs_recursive("A")

    assert set(bfs_result) == expected_vertices
    assert set(dfs_result) == expected_vertices
    assert set(recursive_dfs_result) == expected_vertices
    assert len(bfs_result) == len(expected_vertices)
    assert len(dfs_result) == len(expected_vertices)
    assert len(recursive_dfs_result) == len(expected_vertices)
    assert graph.bfs("missing") == []
    assert graph.dfs("missing") == []
    assert graph.dfs_recursive("missing") == []


def test_directed_graph_only_adds_outgoing_edge():
    graph = Graph(directed=True)
    graph.add_edge("A", "B")

    assert graph.has_edge("A", "B") is True
    assert graph.has_edge("B", "A") is False
    assert graph.out_degree("A") == 1
    assert graph.in_degree("B") == 1
    assert graph.in_degree("A") == 0
