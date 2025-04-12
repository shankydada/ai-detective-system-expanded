def get_legal_actions(best_theory):
    hypothesis = best_theory["hypothesis"].lower()
    ipc_sections = []
    steps = []
    departments = []
    if "knife" in hypothesis or "stab" in hypothesis:
        ipc_sections.extend(["IPC 302 - Murder", "IPC 326 - Voluntarily causing grievous hurt by dangerous weapons"])
        steps.append("Secure the weapon and send for forensic analysis")
        departments.extend(["Forensics Division", "Homicide Squad"])
    if "gun" in hypothesis or "shot" in hypothesis:
        ipc_sections.extend(["IPC 302 - Murder", "Arms Act Section 25"])
        steps.append("Trace bullet trajectory and identify firearm")
        departments.extend(["Ballistics Lab", "Crime Investigation Unit"])
    if "broken_window" in hypothesis or "forced entry" in hypothesis:
        ipc_sections.append("IPC 457 - Lurking house-trespass or house-breaking by night")
        steps.append("Check for fingerprints and signs of tampering")
        departments.append("Crime Scene Unit")
    return {
        "ipc_sections": ipc_sections,
        "recommended_steps": steps,
        "responsible_departments": departments
    }
