# Controller: {{ name }}

"""
{{ name }} controller definition.
"""

class {{ name.capitalize() }}Controller:
    def __init__(self):
        print("{{ name.capitalize() }} controller initialized.")

    def get(self):
        """
        Handle GET requests for {{ name }}.
        """
        return "GET request handled."

    def post(self, data):
        """
        Handle POST requests for {{ name }}.
        """
        print(f"Data received: {data}")
