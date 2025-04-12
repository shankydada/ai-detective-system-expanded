def match_previous_cases(observations):
    previous_cases = [
        {
            "case_id": "C123",
            "summary": "Victim found with stab wounds near broken window.",
            "elements": ["knife", "blood", "body", "broken_window"]
        },
        {
            "case_id": "C456",
            "summary": "Gunshot heard, body found near open door.",
            "elements": ["gun", "body", "open_door"]
        },
        {
            "case_id": "C789",
            "summary": "Burglary with signs of forced entry but no violence.",
            "elements": ["broken_window"]
        }
    ]
    matched = []
    obs_elements = observations["possible_weapons"] + observations["signs_of_violence"]
    if observations["point_of_entry"]:
        obs_elements.append(observations["point_of_entry"])
    for case in previous_cases:
        match_score = len(set(case["elements"]) & set(obs_elements))
        if match_score >= 2:
            matched.append(case)
    return matched
