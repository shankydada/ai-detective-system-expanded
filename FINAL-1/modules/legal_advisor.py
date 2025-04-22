def get_legal_actions(best_theory):
    hypothesis = best_theory["hypothesis"].lower()
    ipc_sections = []
    steps = []
    departments = []

    if "knife" in hypothesis or "stab" in hypothesis:
        ipc_sections.extend(["IPC 302 - Murder", "IPC 326 - Causing grievous hurt with weapon"])
        steps.append("Secure weapon and check fingerprints")
        departments.extend(["Forensics", "Homicide Unit"])

    if "broken_window" in hypothesis:
        ipc_sections.append("IPC 457 - House-breaking by night")
        steps.append("Inspect entry point for evidence")
        departments.append("Crime Scene Unit")

    if "overturned_chair" in hypothesis:
        steps.append("Assess struggle evidence")
        departments.append("Field Forensics")

    # Firearm usage
    if "gunshot" in hypothesis or "fired" in hypothesis or "pistol" in hypothesis:
        ipc_sections.extend(["IPC 302 - Murder", "IPC 307 - Attempt to murder", "Arms Act - Illegal possession"])
        steps.append("Collect shell casings and ballistic evidence")
        departments.extend(["Ballistics", "Homicide Unit", "Forensics"])

    # Poisoning
    if "poison" in hypothesis or "toxic" in hypothesis:
        ipc_sections.extend(["IPC 328 - Causing hurt by poison", "IPC 302 - Murder"])
        steps.append("Collect food/water samples for lab analysis")
        departments.extend(["Medical Examiner", "Forensic Toxicology", "Food Safety Unit"])

    # Arson
    if "fire" in hypothesis or "burnt" in hypothesis or "charred" in hypothesis:
        ipc_sections.append("IPC 436 - Mischief by fire or explosive substance")
        steps.append("Investigate source of fire and accelerants")
        departments.append("Fire Department",)
        departments.append("Arson Investigation Team")

    # Kidnapping
    if "abducted" in hypothesis or "kidnapped" in hypothesis:
        ipc_sections.append("IPC 363 - Kidnapping")
        steps.append("Check CCTV and trace last known location")
        departments.append("Anti-Kidnapping Cell")

    # Cyber crime
    if "hacked" in hypothesis or "phishing" in hypothesis or "unauthorized access" in hypothesis:
        ipc_sections.append("IT Act Section 66 - Hacking")
        steps.append("Track IP logs and notify cyber cell")
        departments.append("Cyber Crime Division")

    # Domestic violence
    if "domestic abuse" in hypothesis or "beaten by husband" in hypothesis:
        ipc_sections.extend(["IPC 498A - Cruelty by husband", "IPC 323 - Voluntarily causing hurt"])
        steps.append("File complaint and record medical evidence")
        departments.append("Women Cell")

    # Bribery/corruption
    if "bribe" in hypothesis or "demanded money" in hypothesis:
        ipc_sections.append("Prevention of Corruption Act Section 7")
        steps.append("Conduct sting operation or trap")
        departments.append("Anti-Corruption Bureau")
        # Body disposal / hiding evidence
    if "buried body" in hypothesis or "disposed body" in hypothesis or "hidden corpse" in hypothesis:
        ipc_sections.extend(["IPC 201 - Causing disappearance of evidence", "IPC 302 - Murder"])
        steps.append("Recover body and conduct forensic autopsy")
        departments.extend(["Homicide Unit", "Forensics", "Crime Scene Unit"])

    # Blackmail or extortion
    if "blackmail" in hypothesis or "extortion" in hypothesis or "threatened for money" in hypothesis:
        ipc_sections.append("IPC 384 - Punishment for extortion")
        steps.append("Trace communication, secure voice/video evidence")
        departments.append("Cyber Crime Division")

    # Drug possession or peddling
    if "drugs found" in hypothesis or "narcotics" in hypothesis or "drug peddler" in hypothesis:
        ipc_sections.append("NDPS Act Section 20 - Possession of narcotic drugs")
        steps.append("Send seized drugs for chemical analysis")
        departments.append("Narcotics Control Bureau")

    # Human trafficking
    if "trafficked" in hypothesis or "human trafficking" in hypothesis or "illegal transport of women" in hypothesis:
        ipc_sections.append("IPC 370 - Human trafficking")
        steps.append("Identify victims and rescue operation")
        departments.append("Anti-Human Trafficking Unit",)

    # Mob violence / riot
    if "mob attack" in hypothesis or "group violence" in hypothesis or "lynched" in hypothesis:
        ipc_sections.append("IPC 147 - Rioting")
        steps.append("Identify attackers and analyze video footage")
        departments.append("Riot Control Unit")

    # Hit and run
    if "hit and run" in hypothesis or "driver fled" in hypothesis or "car accident and escaped" in hypothesis:
        ipc_sections.extend(["IPC 304A - Causing death by negligence", "Motor Vehicles Act Section 134"])
        steps.append("Identify vehicle using CCTV and witness testimony")
        departments.append("Traffic Police")

    # Forgery / fake documents
    if "fake documents" in hypothesis or "forged signature" in hypothesis:
        ipc_sections.append("IPC 465 - Forgery")
        steps.append("Verify document origin and handwriting analysis")
        departments.append("Forensic Document Unit")

    # Acid attack
    if "acid attack" in hypothesis or "threw acid" in hypothesis:
        ipc_sections.extend(["IPC 326A - Voluntarily causing grievous hurt by acid", "IPC 307 - Attempt to murder"])
        steps.append("Provide medical treatment and preserve evidence from victim's body and clothes")
        departments.append("Medical Examiner")
    # Theft / Burglary
    if "stolen" in hypothesis or "theft" in hypothesis or "missing valuables" in hypothesis:
        ipc_sections.append("IPC 380 - Theft in dwelling house")
        steps.append("List stolen items and check for fingerprints")
        departments.append("Local Police")

    # Suicide / Suicide attempt
    if "suicide" in hypothesis or "attempted suicide" in hypothesis:
        ipc_sections.append("IPC 309 - Attempt to commit suicide")
        steps.append("Send for psychological evaluation and verify cause")
        departments.append("Medical Examiner")

    # Money laundering / illegal transactions
    if "unaccounted money" in hypothesis or "money laundering" in hypothesis:
        ipc_sections.append("PMLA Section 3 - Offence of money laundering")
        steps.append("Freeze bank accounts and track source of funds")
        departments.append("Enforcement Directorate")

    # Trespassing
    if "trespassing" in hypothesis or "entered property without permission" in hypothesis:
        ipc_sections.append("IPC 447 - Criminal trespass")
        steps.append("Verify land ownership and file complaint")
        departments.append("Land Records Office",)

    # Sexual assault
    if "sexual assault" in hypothesis or "molestation" in hypothesis or "rape" in hypothesis:
        ipc_sections.extend(["IPC 354 - Assault on woman with intent to outrage modesty", "IPC 376 - Rape"])
        steps.append("Record victim statement, collect medical and DNA evidence")
        departments.append("Women Protection Cell")

    # Workplace harassment
    if "harassment at office" in hypothesis or "inappropriate behavior at work" in hypothesis:
        ipc_sections.append("Sexual Harassment of Women at Workplace Act, Section 3")
        steps.append("Initiate internal complaint committee (ICC) proceedings")
        departments.append("Internal Complaints Committee")

    # Possession of illegal arms
    if "illegal gun" in hypothesis or "unlicensed weapon" in hypothesis:
        ipc_sections.append("Arms Act Section 25 - Possession without license")
        steps.append("Confiscate weapon and verify serial number")
        departments.append("Arms Regulation Bureau")

    # Illegal construction / encroachment
    if "unauthorized building" in hypothesis or "illegal construction" in hypothesis:
        ipc_sections.append("Municipal Act - Violation of building codes")
        steps.append("Survey site and issue demolition notice")
        departments.append("Municipal Corporation")

    # Child abuse
    if "child abuse" in hypothesis or "harmed a minor" in hypothesis:
        ipc_sections.extend(["POCSO Act Section 9 - Aggravated sexual assault", "IPC 323 - Causing hurt"])
        steps.append("Rescue child, record child welfare report")
        departments.append("Child Welfare Committee")

    # Stalking
    if "followed constantly" in hypothesis or "threatening messages repeatedly" in hypothesis:
        ipc_sections.append("IPC 354D - Stalking")
        steps.append("Collect phone and digital evidence")
        departments.append("Cyber Crime Division")
    # Honor killing
    if "honor killing" in hypothesis or "killed for love marriage" in hypothesis:
        ipc_sections.extend(["IPC 302 - Murder", "IPC 34 - Common intention"])
        steps.append("Arrest family members and investigate motive")
        departments.append("Crime Branch")

    # Fake currency circulation
    if "fake currency" in hypothesis or "counterfeit notes" in hypothesis:
        ipc_sections.append("IPC 489A - Counterfeiting currency")
        steps.append("Seize notes and inform Reserve Bank cell")
        departments.append("Economic Offences Wing")

    # Illegal wildlife trade
    if "animal skin" in hypothesis or "smuggling exotic animals" in hypothesis:
        ipc_sections.append("Wildlife Protection Act, Section 9 - Hunting of wild animals")
        steps.append("Inform forest department and seize animals/products")
        departments.append("Wildlife Crime Control Bureau")

    # Organ trafficking
    if "illegal organ sale" in hypothesis or "kidney racket" in hypothesis:
        ipc_sections.append("Transplantation of Human Organs Act Section 19 - Commercial dealings")
        steps.append("Locate donors, verify hospital records")
        departments.append("Medical Board",)
        departments.append("Crime Branch")

    # Mob lynching (hate-based)
    if "lynched" in hypothesis or "mob attacked for religion" in hypothesis:
        ipc_sections.extend(["IPC 302 - Murder", "IPC 153A - Promoting enmity between groups"])
        steps.append("Analyze social media, identify leaders")
        departments.append("Communal Harmony Cell")

    # Caste violence
    if "attacked due to caste" in hypothesis or "dalit assaulted" in hypothesis:
        ipc_sections.append("SC/ST Prevention of Atrocities Act")
        steps.append("File FIR under special provisions and provide protection")
        departments.append("Special Task Force for Caste Crimes")

    # Election fraud
    if "fake voting" in hypothesis or "booth capturing" in hypothesis:
        ipc_sections.append("Representation of People Act, Section 171C - Undue influence")
        steps.append("Inspect polling footage and voter list anomalies")
        departments.append("Election Commission Taskforce")

    # Online scams / fraud
    if "online scam" in hypothesis or "fraud call" in hypothesis or "UPI fraud" in hypothesis:
        ipc_sections.append("IT Act Section 66D - Cheating by personation using computer")
        steps.append("Trace phone numbers and bank transaction trails")
        departments.append("Cyber Crime Division")

    # Identity theft
    if "used my aadhar" in hypothesis or "identity stolen" in hypothesis:
        ipc_sections.append("IT Act Section 66C - Identity theft")
        steps.append("Freeze misused accounts and notify UIDAI")
        departments.append("Cyber Crime Division",)

    # Obstruction of justice
    if "destroyed evidence" in hypothesis or "witness threatened" in hypothesis:
        ipc_sections.append("IPC 204 - Destruction of evidence")
        steps.append("Reconstruct chain of evidence, ensure witness safety")
        departments.append("Judicial Protection Unit")
    # Acid attack
    if "acid attack" in hypothesis or "threw acid" in hypothesis:
       ipc_sections.extend(["IPC 326A - Voluntarily causing grievous hurt by use of acid"])
       steps.append("Provide immediate medical aid and collect chemical sample")
       departments.extend(["Medical Board", "Women Cell", "Forensics"])

# Chain snatching
    if "chain snatched" in hypothesis or "bike theft" in hypothesis:
       ipc_sections.append("IPC 356 - Assault or criminal force in attempt to commit theft")
       steps.append("Check CCTV and track escape route")
       departments.append("Local Police")

# Cyberbullying or Online Harassment
    if "harassed online" in hypothesis or "cyberbullying" in hypothesis:
        ipc_sections.extend(["IT Act Section 66A - Sending offensive messages", "IPC 507 - Criminal intimidation by anonymous communication"])
        steps.append("Track IP and collect digital evidence")
        departments.append("Cyber Crime Division")

# Child labor
    if "child working in shop" in hypothesis or "underage labor" in hypothesis:
        ipc_sections.append("Child Labour (Prohibition and Regulation) Act Section 3")
        steps.append("Rescue child and take employer into custody")
        departments.append("Child Welfare Committee")

# Medical negligence
    if "wrong treatment" in hypothesis or "doctor's negligence" in hypothesis:
        ipc_sections.append("IPC 304A - Causing death by negligence")
        steps.append("Collect hospital records and patient history")
        departments.append("Medical Council")

# Vandalism
    if "property damaged" in hypothesis or "graffiti on walls" in hypothesis:
        ipc_sections.append("IPC 427 - Mischief causing damage")
        steps.append("Estimate loss and review nearby CCTV footage")
        departments.append("Municipal Police Unit")

# Stalking
    if "followed repeatedly" in hypothesis or "stalker outside home" in hypothesis:
        ipc_sections.append("IPC 354D - Stalking")
        steps.append("Install surveillance and file restraining order")
        departments.append("Women Cell")

# Money laundering
    if "black money" in hypothesis or "illegal transactions" in hypothesis:
        ipc_sections.append("Prevention of Money Laundering Act, Section 3")
        steps.append("Trace transaction networks and freeze accounts")
        departments.append("Financial Intelligence Unit")

# Trespassing
    if "entered without permission" in hypothesis or "trespasser seen" in hypothesis:
        ipc_sections.append("IPC 447 - Criminal trespass")
        steps.append("Collect witness statements and mark entry points")
        departments.append("Local Police")

# Illegal construction
    if "built without approval" in hypothesis or "violated building norms" in hypothesis:
        ipc_sections.append("Municipal Corporation Act - Unauthorized construction")
        steps.append("Serve notice and inspect building papers")
        departments.append("Urban Planning Authority")
# Human trafficking
    if "trafficked" in hypothesis or "forced labor" in hypothesis:
        ipc_sections.append("IPC 370 - Trafficking of persons")
        steps.append("Rescue victims and identify trafficking network")
        departments.append("Anti-Human Trafficking Unit")

# Drunk driving
    if "drunk driving" in hypothesis or "intoxicated driver" in hypothesis:
        ipc_sections.append("IPC 279 - Rash driving or riding on a public way")
        steps.append("Conduct breathalyzer test and impound vehicle")
        departments.append("Traffic Police")

# Dowry death
    if "burnt for dowry" in hypothesis or "dowry death" in hypothesis:
        ipc_sections.extend(["IPC 304B - Dowry death", "IPC 498A - Cruelty by husband"])
        steps.append("Question in-laws and collect marriage details")
        departments.append("Women Cell")

# Land grabbing
    if "land encroached" in hypothesis or "grabbed my land" in hypothesis:
        ipc_sections.append("IPC 441 - Criminal trespass")
        steps.append("Check land records and conduct site survey")
        departments.append("Revenue Department")

# Fake job offer scam
    if "fake job" in hypothesis or "scammed for job" in hypothesis:
        ipc_sections.append("IPC 420 - Cheating and dishonestly inducing delivery of property")
        steps.append("Trace recruiter and verify employment claims")
        departments.append("Cyber Crime Division")

# Illegal mining
    if "unauthorized mining" in hypothesis or "sand mafia" in hypothesis:
        ipc_sections.append("Mines and Minerals (Development and Regulation) Act")
        steps.append("Seize equipment and cancel permits")
        departments.append("Geology and Mining Department")

# Environmental pollution
    if "toxic waste dumped" in hypothesis or "polluted river" in hypothesis:
        ipc_sections.append("Environment Protection Act, Section 15")
        steps.append("Collect samples and fine responsible factory")
        departments.append("Pollution Control Board")

# Sexual harassment at workplace
    if "harassed at office" in hypothesis or "boss touched inappropriately" in hypothesis:
        ipc_sections.append("Sexual Harassment of Women at Workplace Act")
        steps.append("File internal committee report and collect witness statements")
        departments.append("Internal Complaints Committee")

# Communal violence
    if "riots due to religion" in hypothesis or "clash between groups" in hypothesis:
        ipc_sections.extend(["IPC 153A - Promoting enmity", "IPC 295A - Outraging religious feelings"])
        steps.append("Control crowd and identify key instigators")
        departments.append("Rapid Action Force")

# Illegal arms possession
    if "illegal gun found" in hypothesis or "weapon without license" in hypothesis:
        ipc_sections.append("Arms Act Section 25 - Possession without license")
        steps.append("Seize weapon and check ballistic records")
        departments.append("Arms Licensing Authority")

# Bank fraud
    if "fake loan" in hypothesis or "misused bank account" in hypothesis:
       ipc_sections.append("IPC 409 - Criminal breach of trust by public servant or banker")
       steps.append("Freeze bank account and audit transactions")
       departments.append("Economic Offences Wing")

# Smuggling narcotics
    if "drugs found" in hypothesis or "smuggling narcotics" in hypothesis:
        ipc_sections.append("NDPS Act Section 21 - Possession of narcotic drugs")
        steps.append("Seize contraband and conduct raid on storage")
        departments.append("Narcotics Control Bureau")

# Identity fraud in exam
    if "someone else gave exam" in hypothesis or "fake admit card" in hypothesis:
        ipc_sections.append("IPC 419 - Impersonation")
        steps.append("Verify ID proof and exam records")
        departments.append("Education Board Vigilance Team")

# Blackmail
    if "threatened to leak photos" in hypothesis or "blackmailed online" in hypothesis:
        ipc_sections.append("IPC 384 - Extortion")
        steps.append("Trace contact history and digital trail")
        departments.append("Cyber Cell")

# Cheque bounce
    if "cheque bounced" in hypothesis or "gave me fake cheque" in hypothesis:
        ipc_sections.append("Negotiable Instruments Act Section 138")
        steps.append("File complaint and send legal notice")
        departments.append("Commercial Court")

# Public nuisance
    if "blocking road" in hypothesis or "loud speaker at night" in hypothesis:
        ipc_sections.append("IPC 268 - Public nuisance")
        steps.append("Serve warning and remove obstruction")
        departments.append("Local Police")

# Animal cruelty
    if "beat stray dog" in hypothesis or "animal tortured" in hypothesis:
        ipc_sections.append("Prevention of Cruelty to Animals Act")
        steps.append("Rescue animal and arrest offender")
        departments.append("Animal Welfare Board")

# Illegal abortion
    if "aborted without consent" in hypothesis or "clinic did secret abortion" in hypothesis:
        ipc_sections.append("MTP Act Section 3 - Medical Termination of Pregnancy")
        steps.append("Inspect clinic records and verify consent forms")
        departments.append("Health Department")

# Attempted suicide
    if "tried to end life" in hypothesis or "attempted suicide" in hypothesis:
        ipc_sections.append("IPC 309 - Attempt to commit suicide")
        steps.append("Provide psychological support and assess mental health")
        departments.append("Mental Health Unit")

# Forgery of documents
    if "fake documents used" in hypothesis or "forged signature" in hypothesis:
       ipc_sections.append("IPC 465 - Forgery")
       steps.append("Verify authenticity and collect handwriting samples")
       departments.append("Document Examination Lab")
# Phone tapping / Surveillance
    if "phone tapped" in hypothesis or "illegally recorded call" in hypothesis:
        ipc_sections.append("Indian Telegraph Act Section 25 - Unlawful interception")
        steps.append("Trace intercept source and secure devices")
        departments.append("Cyber Surveillance Unit")

# Acid attack
    if "threw acid" in hypothesis or "acid attack" in hypothesis:
        ipc_sections.append("IPC 326A - Causing grievous hurt by acid")
        steps.append("Arrest accused and collect chemical evidence")
        departments.append("Women Protection Cell")

# Child abuse
    if "child beaten" in hypothesis or "abused minor" in hypothesis:
        ipc_sections.append("POCSO Act Section 3 - Penetrative sexual assault / IPC 323")
        steps.append("Medical examination and child counseling")
        departments.append("Child Welfare Committee")

# Stalking
    if "followed me" in hypothesis or "stalker" in hypothesis:
        ipc_sections.append("IPC 354D - Stalking")
        steps.append("Collect CCTV footage and social media proof")
        departments.append("Women Cell")

# Illegal betting
    if "betting online" in hypothesis or "IPL satta" in hypothesis:
        ipc_sections.append("Public Gambling Act Section 3")
        steps.append("Raid location and seize betting equipment")
        departments.append("Gambling Control Bureau")

# Obscene publication
    if "shared nude photos" in hypothesis or "published obscene content" in hypothesis:
        ipc_sections.append("IPC 292 - Obscenity")
        steps.append("Take down media and trace uploader")
        departments.append("Cyber Crime Division")

# Trespassing into restricted area
    if "entered army base" in hypothesis or "crossed into airport zone" in hypothesis:
        ipc_sections.append("IPC 447 - Criminal trespass")
        steps.append("Detain and question motive")
        departments.append("Defense Intelligence Bureau")

# Election code violation
    if "speech after voting hours" in hypothesis or "cash distributed during elections" in hypothesis:
        ipc_sections.append("Representation of People Act Section 123 - Corrupt practices")
        steps.append("Record statements and notify EC")
        departments.append("Election Commission Taskforce")

# Copyright violation
    if "pirated movie" in hypothesis or "copied software" in hypothesis:
        ipc_sections.append("Copyright Act Section 63 - Infringement")
        steps.append("Identify upload source and takedown link")
        departments.append("IPR Cell")

# Food adulteration
    if "mixed chemicals in food" in hypothesis or "adulterated oil" in hypothesis:
        ipc_sections.append("IPC 272 - Adulteration of food or drink")
        steps.append("Collect food sample for lab testing")
        departments.append("Food Safety Department")

# Loan shark harassment
    if "threatened by money lender" in hypothesis or "harassed for loan" in hypothesis:
        ipc_sections.append("IPC 384 - Extortion")
        steps.append("Record threats and seize loan documents")
        departments.append("Local Police",)

# Child marriage
    if "married underage girl" in hypothesis or "child marriage took place" in hypothesis:
        ipc_sections.append("Prohibition of Child Marriage Act Section 9")
        steps.append("Nullify marriage and counsel families")
        departments.append("Women and Child Welfare")

# Begging racket
    if "forced to beg" in hypothesis or "child begging in traffic" in hypothesis:
        ipc_sections.append("Juvenile Justice Act Section 76 - Exploitation of child")
        steps.append("Rescue and rehabilitate victim")
        departments.append("Social Welfare Department")

# Custodial death
    if "died in police custody" in hypothesis or "beaten by police in lockup" in hypothesis:
        ipc_sections.append("IPC 302 - Murder / NHRC Guidelines")
        steps.append("Post-mortem and independent inquiry")
        departments.append("Human Rights Commission")

# Noise pollution
    if "loud speaker after 10PM" in hypothesis or "DJ at night" in hypothesis:
        ipc_sections.append("Noise Pollution Rules under EPA")
        steps.append("Issue fine and confiscate equipment")
        departments.append("Local Police",)

# Fake caste certificate
    if "used fake sc certificate" in hypothesis or "forged caste document" in hypothesis:
        ipc_sections.append("IPC 420 - Cheating, IPC 465 - Forgery")
        steps.append("Verify document with issuing authority")
        departments.append("Caste Verification Board")

# Illegal construction
    if "constructed on drain" in hypothesis or "no permission building" in hypothesis:
        ipc_sections.append("Municipal Act - Unauthorized construction")
        steps.append("Issue demolition notice and take photos")
        departments.append("Urban Development Authority")

# Pornography circulation
    if "shared porn in group" in hypothesis or "sent obscene videos" in hypothesis:
        ipc_sections.append("IT Act Section 67 - Obscene electronic material")
        steps.append("Identify distributor and report group admin")
        departments.append("Cyber Crime Division")

# Fake news / rumor spreading
    if "spread false news" in hypothesis or "created panic with rumor" in hypothesis:
        ipc_sections.append("IPC 505 - Statements conducing to public mischief")
        steps.append("Trace origin of message and fact-check")
        departments.append("Cyber Surveillance Cell")

# Money laundering
    if "converted black money" in hypothesis or "hawala transaction" in hypothesis:
        ipc_sections.append("Prevention of Money Laundering Act (PMLA)")
        steps.append("Trace financial route and notify ED")
        departments.append("Enforcement Directorate")
# Human trafficking
    if "trafficked for labor" in hypothesis or "sold women" in hypothesis:
        ipc_sections.append("IPC 370 - Trafficking of persons")
        steps.append("Rescue victims and investigate trafficking ring")
        departments.append("Anti-Human Trafficking Unit")

# Loan fraud
    if "fake documents for loan" in hypothesis or "loan scam" in hypothesis:
        ipc_sections.append("IPC 420 - Cheating and dishonesty")
        steps.append("Verify submitted documents with bank")
        departments.append("Bank Fraud Cell")

# Blackmail
    if "demanded money with photos" in hypothesis or "threatened to leak video" in hypothesis:
        ipc_sections.append("IPC 384 - Extortion")
        steps.append("Track source of threat and secure devices")
        departments.append("Cyber Crime Division")

# Cow slaughter in restricted area
    if "killed cow" in hypothesis or "illegal cow slaughter" in hypothesis:
        ipc_sections.append("Prevention of Cow Slaughter Act (State specific)")
        steps.append("Seize remains and arrest involved persons")
        departments.append("Animal Welfare Division")

# Medical negligence
    if "doctor left instrument" in hypothesis or "wrong surgery done" in hypothesis:
        ipc_sections.append("IPC 304A - Causing death by negligence")
        steps.append("Medical board inquiry and patient testimony")
        departments.append("Medical Council",)

# Passport forgery
    if "used fake passport" in hypothesis or "travelled with forged visa" in hypothesis:
        ipc_sections.append("IPC 468 - Forgery for cheating")
        steps.append("Inform immigration and seize forged documents")
        departments.append("Immigration Bureau")

# Illegal arms possession
    if "found gun without license" in hypothesis or "illegal pistol" in hypothesis:
        ipc_sections.append("Arms Act Section 25 - Illegal possession")
        steps.append("Seize firearm and run ballistic check")
        departments.append("Forensic Ballistics Department")

# Train sabotage
    if "placed object on railway track" in hypothesis or "train blast" in hypothesis:
       ipc_sections.append("Railways Act Section 150 - Endangering safety")
       steps.append("Alert railway security and inspect site")
       departments.append("RPF (Railway Protection Force)")

# Suicide abetment
    if "forced to die" in hypothesis or "driven to suicide" in hypothesis:
        ipc_sections.append("IPC 306 - Abetment of suicide")
        steps.append("Recover suicide note, check mental health report")
        departments.append("Local Police",)

# False dowry case
    if "filed false dowry case" in hypothesis or "dowry misuse" in hypothesis:
        ipc_sections.append("IPC 182 - False information to public servant")
        steps.append("Verify complaint with evidence and counter statements")
        departments.append("Women Cell & Legal Advisory")

# Drunk driving
    if "driver was drunk" in hypothesis or "hit by drunk car" in hypothesis:
        ipc_sections.append("IPC 279 - Rash driving, MV Act Section 185")
        steps.append("Conduct breathalyzer test and impound vehicle")
        departments.append("Traffic Police")

# Forged educational certificates
    if "submitted fake degree" in hypothesis or "duplicate mark sheet" in hypothesis:
        ipc_sections.append("IPC 471 - Using forged document")
        steps.append("Cross-verify with issuing university")
        departments.append("Academic Fraud Investigation Wing")

# Crypto scam
    if "lost money in crypto app" in hypothesis or "scammed via bitcoin" in hypothesis:
        ipc_sections.append("IT Act Section 66D - Online fraud")
        steps.append("Track blockchain trail and freeze digital wallet")
        departments.append("Cyber Intelligence Unit")

# Match-fixing in sports
    if "rigged the match" in hypothesis or "players were paid to lose" in hypothesis:
       ipc_sections.append("IPC 420 - Cheating")
       steps.append("Check betting patterns and player communications")
       departments.append("Sports Integrity Unit")

# Police brutality
    if "beaten in station" in hypothesis or "excessive police force" in hypothesis:
        ipc_sections.append("IPC 323 - Voluntarily causing hurt")
        steps.append("CCTV review and medical report")
        departments.append("Human Rights Commission")

# Drug overdose at party
    if "collapsed due to drugs" in hypothesis or "drug overdose at rave" in hypothesis:
        ipc_sections.append("NDPS Act Section 21 - Possession and consumption")
        steps.append("Test blood sample and raid party venue")
        departments.append("Narcotics Control Bureau")

# Prison break
    if "escaped from jail" in hypothesis or "broke prison lock" in hypothesis:
        ipc_sections.append("IPC 224 - Resistance to lawful apprehension")
        steps.append("Alert checkpoints and scan CCTV trail")
        departments.append("Jail Administration",)

# Dowry harassment
    if "pressured for car in marriage" in hypothesis or "asked for gold post-marriage" in hypothesis:
        ipc_sections.append("IPC 498A - Cruelty",)
        steps.append("Take statement and check financial records")
        departments.append("Women Cell")

# Sand mafia / Illegal mining
    if "mining without permit" in hypothesis or "illegal sand transport" in hypothesis:
        ipc_sections.append("Mines and Minerals Act Section 21")
        steps.append("Seize vehicles and document land damage")
        departments.append("Mining & Geology Department")

# Foreign currency smuggling
    if "caught with foreign notes" in hypothesis or "illegal forex" in hypothesis:
        ipc_sections.append("Customs Act Section 135 - Smuggling")
        steps.append("Notify customs and investigate route")
        departments.append("Directorate of Revenue Intelligence (DRI)")
# Acid attack
    if "threw acid" in hypothesis or "acid attack" in hypothesis:
        ipc_sections.extend(["IPC 326A - Causing grievous hurt by acid", "IPC 326B - Attempt to throw acid"])
        steps.append("Provide emergency medical aid, collect acid sample")
        departments.append("Women Protection Cell")

# Public rioting
    if "violent mob" in hypothesis or "public unrest" in hypothesis:
        ipc_sections.append("IPC 147 - Rioting")
        steps.append("Deploy forces and identify instigators via CCTV")
        departments.append("Riot Control Squad")

# Child marriage
    if "minor girl married" in hypothesis or "underage marriage" in hypothesis:
        ipc_sections.append("Prohibition of Child Marriage Act, Section 3")
        steps.append("Rescue minor and arrest guardians")
        departments.append("Child Welfare Committee")

# ATM skimming
    if "card cloned" in hypothesis or "atm skimming" in hypothesis:
        ipc_sections.append("IT Act Section 66C - Identity theft")
        steps.append("Collect CCTV and track card duplicator")
        departments.append("Cyber Crime Division")

    # Medical seat scam
    if "paid for medical seat" in hypothesis or "admission fraud" in hypothesis:
        ipc_sections.append("IPC 420 - Cheating")
        steps.append("Trace financial transaction and impersonators")
        departments.append("Education Fraud Wing")

    # Noise pollution from event
    if "loudspeaker past midnight" in hypothesis or "illegal DJ" in hypothesis:
        ipc_sections.append("Noise Pollution Rules under EPA Act")
        steps.append("Measure decibel levels and fine organizer")
        departments.append("Municipal Control Authority")

    # Fake job offer
    if "scammed for job" in hypothesis or "paid for fake job letter" in hypothesis:
        ipc_sections.append("IPC 419 - Impersonation")
        steps.append("Track scam network and refund victims")
        departments.append("Cyber Crime & Economic Offences Wing")

    # Illegal liquor sale
    if "sold alcohol without license" in hypothesis or "illicit liquor" in hypothesis:
        ipc_sections.append("Excise Act - Illegal possession and sale")
        steps.append("Confiscate stock and shut location")
        departments.append("Excise Department")

    # Sexual harassment at workplace
    if "boss touched inappropriately" in hypothesis or "unwanted advances" in hypothesis:
        ipc_sections.append("IPC 354A - Sexual harassment")
        steps.append("Initiate ICC inquiry and protect complainant")
        departments.append("Internal Complaints Committee")

    # Unauthorized construction
    if "built floor illegally" in hypothesis or "no building permit" in hypothesis:
        ipc_sections.append("Municipal Building By-laws Violation")
        steps.append("Serve demolition notice and seal site")
        departments.append("Urban Development Authority")

    # Insider trading
    if "sold shares with secret info" in hypothesis or "traded illegally" in hypothesis:
        ipc_sections.append("SEBI Act Section 15G - Insider trading")
        steps.append("Audit transactions and notify SEBI")
        departments.append("SEBI Investigation Division")

    # Data breach
    if "user data leaked" in hypothesis or "company exposed private info" in hypothesis:
        ipc_sections.append("IT Act Section 72A - Breach of confidentiality")
        steps.append("Identify breach point and alert data subjects")
        departments.append("Cyber Security Authority")

    # Arms smuggling
    if "transported illegal guns" in hypothesis or "arms smuggling racket" in hypothesis:
        ipc_sections.append("Arms Act Section 25 & IPC 120B - Criminal conspiracy")
        steps.append("Track suppliers and seize weapons")
        departments.append("Anti-Terror Squad")

    # Currency exchange fraud
    if "exchanged counterfeit currency" in hypothesis or "fake forex dealer" in hypothesis:
        ipc_sections.append("IPC 489B - Using counterfeit currency")
        steps.append("Track exchange center and freeze operations")
        departments.append("Financial Intelligence Unit")

    # Trespassing
    if "entered private land" in hypothesis or "trespassed into farm" in hypothesis:
        ipc_sections.append("IPC 447 - Criminal trespass")
        steps.append("Record statements and verify property ownership")
        departments.append("Revenue Department")

    # Wildlife poaching
    if "killed deer" in hypothesis or "caught with tiger skin" in hypothesis:
        ipc_sections.append("Wildlife Protection Act, Section 51 - Punishment for offenses")
        steps.append("Seize evidence and track hunting tools")
        departments.append("Forest Department")

    # Sedition
    if "shouted anti-national slogans" in hypothesis or "plotted against state" in hypothesis:
        ipc_sections.append("IPC 124A - Sedition")
        steps.append("Record speech, monitor online activity")
        departments.append("State Intelligence Unit")

    # Child pornography
    if "found child explicit videos" in hypothesis or "shared minor’s obscene image" in hypothesis:
        ipc_sections.append("POCSO Act + IT Act Section 67B")
        steps.append("Seize devices and involve child protection unit")
        departments.append("Cyber Crime & Juvenile Protection Unit")

    # Election code violation
    if "campaign during silent period" in hypothesis or "used religion in speech" in hypothesis:
        ipc_sections.append("Representation of People Act - Model Code Violation")
        steps.append("Notify EC and take legal action against candidate")
        departments.append("Election Monitoring Cell")

    # Public indecency
    if "undressed in public" in hypothesis or "performed vulgar act" in hypothesis:
        ipc_sections.append("IPC 294 - Obscene acts in public")
        steps.append("Issue public warning and initiate arrest if repeated")
        departments.append("Local Police Patrol Unit")


    return {
        "ipc_sections": ipc_sections,
        "recommended_steps": steps,
        "responsible_departments": departments
    }