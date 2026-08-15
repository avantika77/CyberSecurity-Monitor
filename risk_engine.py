def calculate_risk(severity, criticality):
    """
    Calculate risk based on vulnerability severity
    and asset criticality.
    """

    severity = str(severity).strip().title()
    criticality = str(criticality).strip().title()

    if severity == "Critical" or criticality == "Critical":
        return "Critical"

    if severity == "High" or criticality == "High":
        return "High"

    if severity == "Medium" or criticality == "Medium":
        return "Medium"

    return "Low"