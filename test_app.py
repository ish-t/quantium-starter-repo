from app import app

def test_header_presence(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#title", timeout=5)

def test_visualisation_presence(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#pink-morsel-line-graph", timeout=10)

def test_region_picker_presence(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-radio", timeout=5)