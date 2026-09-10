<!-- last-checked: 2026-09-10 -->
# research-line

<p align="center">
  <img src="logo.jpg" alt="research-line logo" width="925">
</p>

<p align="center">
  <a href="https://github.com/research-line"><img src="https://img.shields.io/badge/GitHub_Org-research--line-0A2540?style=for-the-badge&logo=github" alt="GitHub Org Profile"></a>
  <a href="https://github.com/research-line"><img src="https://img.shields.io/badge/Public_Repos-8-blue?style=for-the-badge" alt="Öffentliche Repos"></a>
  <a href="https://github.com/open-bricks"><img src="https://img.shields.io/badge/Ecosystem-open--bricks-blue?style=for-the-badge" alt="Ecosystem open-bricks"></a>
  <a href="https://github.com/research-line"><img src="https://img.shields.io/badge/Domain-Open_Science_%26_Math_Physics-purple?style=for-the-badge" alt="Domain Open Science"></a>
  <a href="https://zenodo.org"><img src="https://img.shields.io/badge/Zenodo-DOIs_Archival-0298c3?style=for-the-badge&logo=zenodo" alt="Zenodo Archival DOIs"></a>
  <a href="https://github.com/research-line/.github/blob/main/llms.txt"><img src="https://img.shields.io/badge/LLM--Kontext-llms.txt-412991?style=for-the-badge" alt="LLM Kontext llms.txt"></a>
  <a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://img.shields.io/badge/Lizenz-CC--BY_4.0_%2F_MIT-green?style=for-the-badge" alt="Lizenz CC-BY 4.0 / MIT"></a>
</p>

<p align="center"><b>🇬🇧 <a href="README.md">English Version</a></b></p>

**Open-Access-Forschungsrepositories mit Preprints, mathematischen Beweisnotizen, Jupyter Notebooks, reproduzierbaren Forschungsdaten und Zenodo-DOI-Archivierung.**

`research-line` bündelt öffentliche wissenschaftliche Arbeiten aus der mathematischen Physik (Functional Stability Theory), der Kosmologie modifizierter Gravitation (Curvature Relaxation Model), der routenbezogenen Riemann-Hypothesen-Analyse, der Zahlentheorie & Hecke-Quotienten-Verifikation (HCT/abc-Vermutung), der KI-Gesellschaftsforschung (Synthetic Worldview Reconstruction) und der theoretischen Computerbiologie (FST-Nash Chaperon-Dynamiken). Alle Repositories dienen der Inspektion, der Open-Science-Prüfung, dem Peer Review, der Zitation und der weiterführenden Forschung.

> [!NOTE]
> Maschinenlesbarer Ökosystem-Kontext für KI-Agenten, Crawler und automatisierte Tools ist unter **[llms.txt](https://github.com/research-line/.github/blob/main/llms.txt)** verfügbar.
> Öffentlicher Index geprüft gegen live GitHub-API: **10. September 2026** (2026-09-10).

> [!IMPORTANT]
> **Open Science & Statusgrenzen:** Die Repositories dieser Organisation enthalten Forschungscode, Beweisaudits, Preprints und Berechnungsnotebooks. Archivarische Snapshot-DOIs sind auf Zenodo hinterlegt. Bitte beachten Sie die repo-spezifischen `README.md`- und `CITATION.cff`-Dateien bezüglich des konkreten Status (etabliert, konditional, explorativ oder archiviert). Keine der Inhalten stellt medizinische, rechtliche oder finanzielle Beratung dar.

---

## Open-Science-Architektur

```mermaid
flowchart TD
    subgraph Research_Pillars["research-line — Wissenschaftliche Hauptsäulen"]
        FST["Functional Stability Theory<br/><b>functional-stability-theory</b>"]
        CRM["Kosmologie & Modifizierte Gravitation<br/><b>crm-cosmology</b>"]
        RH["Riemann-Hypothese Routen-Analyse<br/><b>rh-even-dominance</b>"]
        HCT["abc-Vermutung & Hecke-Annihilatoren<br/><b>abc-hct</b>"]
        SWR["KI-Elite Weltbild-Rekonstruktion<br/><b>ai-elite-swr</b>"]
        FST_NASH["Chaperon- & Faltungstheorie<br/><b>fst-nash</b>"]
        RFEP["RFEP Brückenframework<br/><b>rfep-framework</b> <i>(Archiviert)</i>"]
    end

    subgraph Outputs["Reproduzierbarkeit & Archivierung"]
        Zenodo["Zenodo Persistente DOIs<br/><i>(Archivierte Publikations-Snapshots)</i>"]
        Notebooks["Berechnungs-Notebooks & Beweisnotizen<br/><i>(Live GitHub Surface)</i>"]
        Data["Offene Datensätze, Prompts & Validierungen"]
    end

    subgraph Sister_Ecosystems["Schwester-Ökosysteme & Netzwerke"]
        OpenBricks["open-bricks<br/><i>(Dach-Organisation)</i>"]
        EllmosAI["ellmos-ai<br/><i>(LLM-OS & Agent Stack)</i>"]
        UmBruch["um-bruch<br/><i>(Angewandte Gesundheitsstudien)</i>"]
    end

    FST --> Notebooks & Zenodo
    CRM --> Notebooks & Zenodo
    RH --> Notebooks & Zenodo
    HCT --> Notebooks & Zenodo
    SWR --> Data & Zenodo
    FST_NASH --> Notebooks
    RFEP --> Zenodo

    Outputs --> Sister_Ecosystems
```

---

## Schnelleinstieg / Start-Empfehlung

| Forschungsziel | Empfohlenes Repository | Kerninhalte & Kontext |
|---|---|---|
| **Mathematisch-Physikalisches Programm** | **[functional-stability-theory](https://github.com/research-line/functional-stability-theory)** | Haupt-FST-Hub mit Domain-Beweisen (NS, YM, TU, DE, Hodge, BSD, P-vs-NP), Anwendungen & Reproduzierbarkeit |
| **Riemann-Hypothesen Routen-Atlas** | **[rh-even-dominance](https://github.com/research-line/rh-even-dominance)** | Konditionaler RH-Atlas mit Verifikations-Skripten, Zertifikaten, Zenodo-Einträgen & Beweisgrenzen |
| **abc-Vermutung & Hecke-Quotienten-Verifikation** | **[abc-hct](https://github.com/research-line/abc-hct)** | HCT abc-Forschungspapiere, Beweisnotizen, Manin-Symbol-Pairings über Hecke-Algebren und reproduzierbare Rang-Zertifikate ohne Magma |
| **Kosmologie & Modifizierte Gravitation** | **[crm-cosmology](https://github.com/research-line/crm-cosmology)** | Curvature Relaxation Model (CRM) Arbeiten & Skripte für Checks bezüglich CMB, Pantheon+, MOND & SPARC |
| **KI-Führungsriegen Weltbild-Analyse** | **[ai-elite-swr](https://github.com/research-line/ai-elite-swr)** | Synthetic Worldview Reconstruction öffentlicher KI-Aussagen mit Preprints, Prompts, Validierungs-Daten & Abbildungen |
| **Proteinfaltung & Spieltheorie** | **[fst-nash](https://github.com/research-line/fst-nash)** | Potentialspiel-Diagnostik für Chaperon-Systeme und Proteinfaltungs-Regime |
| **Historisches RFEP-Material** | **[rfep-framework](https://github.com/research-line/rfep-framework)** | Archivierte Grundlagen des Renormalized Free-Energy Principles mit Zenodo-Verlinkung |

---

## Öffentliches Repository-Verzeichnis

Dieser Index umfasst alle 8 öffentlichen Repositories von `research-line` (Stand: **10. September 2026**). Private oder interne Entwicklungs-Repositories sind im öffentlichen Verzeichnis bewusst ausgeschlossen.

| Repository | Status | Fachbereich | Rolle & Beschreibung |
|---|---|---|---|
| **[.github](https://github.com/research-line/.github)** | Aktiv | Organisationsprofil | GitHub-Startseite, Standard-Community-Dateien und maschinenlesbarer `llms.txt`-Kontext |
| **[abc-hct](https://github.com/research-line/abc-hct)** | Aktiv | Zahlentheorie | HCT abc-Forschungsarbeiten, Beweisnotizen, Manin-Symbol-Pairings über Hecke-Algebren und reproduzierbare Hecke-Quotienten-Artefakte ohne Magma |
| **[ai-elite-swr](https://github.com/research-line/ai-elite-swr)** | Aktiv | KI-Gesellschaftsforschung | Rekonstruktion von Weltbildern führender KI-Akteure mit Arbeiten, Prompts, Validierungen & reproduzierbaren Daten |
| **[crm-cosmology](https://github.com/research-line/crm-cosmology)** | Aktiv | Kosmologie | Curvature Relaxation Model Arbeiten und Code für modifizierte Gravitationsprüfungen |
| **[fst-nash](https://github.com/research-line/fst-nash)** | Aktiv | Computerbiologie-Theorie | Potentialspiel-Diagnostik für Chaperon-Systeme und Proteinfaltungs-Regime |
| **[functional-stability-theory](https://github.com/research-line/functional-stability-theory)** | Aktiv | Mathematische Physik | Functional Stability Theory Programmmaterial, Domain-Beweise und Reproduzierbarkeitsflächen |
| **[rfep-framework](https://github.com/research-line/rfep-framework)** | Archiviert | Mathematische Physik | Früheres RFEP-Brückenmaterial; aufbewahrt für Zitationen, Vergleiche und Historie |
| **[rh-even-dominance](https://github.com/research-line/rh-even-dominance)** | Aktiv | Zahlentheorie | Konditionaler Riemann-Hypothesen-Atlas mit Skripten, Zertifikaten, Zenodo-Einträgen & Beweisgrenzen |

---

## Verwandte angewandte Forschung (Um:bruch)

Einige angewandte Gesundheitspolitik-, Verordnungsrisiko- und Diagnostikprojekte werden unter [um-bruch](https://github.com/um-bruch) gepflegt:

| Repository | Fachbereich | Beschreibung |
|---|---|---|
| **[regressangst](https://github.com/um-bruch/regressangst)** | Gesundheitspolitik | Öffentliches Studienpaket zu Verordnungsrisiken, Prüfanträgen und Versorgungsmustern |
| **[verordnungsampel](https://github.com/um-bruch/verordnungsampel)** | Gesundheitsinformatik | Software zur automatischen Prüfung deutscher Verordnungs- und Arzneimittelregeln |
| **[multiaxial-diagnostic-system](https://github.com/um-bruch/multiaxial-diagnostic-system)** | Klinische Psychologie | Multiaxiales Diagnostiksystem für strukturierte klinische Diagnostikforschung |
| **[system-medicine](https://github.com/um-bruch/system-medicine)** | Systemmedizin | Wissensgraph-Entwicklung für pfadzentrierte differentialmedizinische Logik |
| **[locuterra](https://github.com/um-bruch/locuterra)** | Civic Tech / Gemeingüter | Standortbasierte bürgerschaftliche Plattform für digitale Gemeingüter |

---

## Ökosystem & Schwester-Organisationen

`research-line` ist Teil eines übergreifenden Open-Source-Netzwerks unter dem Dach von **[open-bricks](https://github.com/open-bricks)**:

| Organisation | Hauptbereich | Spezialisierung & Fokus |
|---|---|---|
| **[open-bricks](https://github.com/open-bricks)** | Dachorganisation | Dachstruktur für alle Softwareprodukte, Tools und Forschungsframeworks |
| **[ellmos-ai](https://github.com/ellmos-ai)** | LLM-OS / KI-Infra | Agenten-Betriebssysteme (BACH, Rinnsal), Speicher-Säule (.MEMORY, USMC, gardener), MCP-Server |
| **[file-bricks](https://github.com/file-bricks)** | Desktop-Tools | Local-First PySide6 Desktop-Dateiverwaltungs-, Dubletten- und Speicher-Apps |
| **[doc-bricks](https://github.com/doc-bricks)** | Dokumenten-Tools | Markdown-Tools, PDF-Verarbeitung, OCR-Engines und Dokumenten-Workflows |
| **[dev-bricks](https://github.com/dev-bricks)** | Entwickler-Tools | Entwicklerwerkzeuge und IDEs (DevCenter, CodeBox, pythonbox, MethodenAnalyser, CareCenter) |
| **[research-line](https://github.com/research-line)** | Open Science | Open-Access-Forschung in mathematischer Physik, Kosmologie, Zahlentheorie & KI-Gesellschaft |
| **[biotec-line](https://github.com/biotec-line)** | Bioinformatik | Genomische Varianten-Tools, VCF-Verarbeitung und klinische Genetik |
| **[entertain-and-more](https://github.com/entertain-and-more)** | Entertainment | Spiele mit KI-Integration, interaktives Schach (ChatAndChess) und Audio-Tools (KlangpultLight) |
| **[assistassets-ai](https://github.com/assistassets-ai)** | Finanz-KI | Local-First Finanzanalysen, Indikatoren und Assistenz-Tools (FinancialProof) |
| **[um-bruch](https://github.com/um-bruch)** | Angewandte Gesundheit | Studien zur Versorgungssicherheit, Verordnungsampel und Systemmedizin |
| **[lukisch](https://github.com/lukisch)** | Persönlich / Core | Persönliches Profil, Core-Entwickler-Repositories und disziplinübergreifende Integration |

---

## Aktueller Aktivitäts-Snapshot

Verifizierte Stand-Metadaten via GitHub-API am **10. September 2026** (2026-09-10).
Die Datumsangaben sind der UTC-Tag von `pushed_at`, nicht in Ortszeit umgerechnet:

| Repository | Letzter Push | Ausrichtung & Navigation |
|---|---:|---|
| **[functional-stability-theory](https://github.com/research-line/functional-stability-theory)** | **2026-09-10** | Haupt-FST-Hub für Domain-Beweise, Anwendungen & Reproduzierbarkeitsflächen |
| **[abc-hct](https://github.com/research-line/abc-hct)** | **2026-09-10** | HCT abc-Forschungsarbeiten, Beweisnotizen und reproduzierbare Hecke-Quotienten-Rangzertifikate |
| **[.github](https://github.com/research-line/.github)** | **2026-09-10** | Organisationsprofil, Community-Dateien & maschinenlesbares `llms.txt` |
| **[rh-even-dominance](https://github.com/research-line/rh-even-dominance)** | **2026-09-02** | Konditionaler Riemann-Hypothesen-Atlas mit Skripten, Zertifikaten & Zenodo-Einträgen |
| **[fst-nash](https://github.com/research-line/fst-nash)** | **2026-08-20** | Potentialspiel-Diagnostik für Chaperon-Systeme und Proteinfaltungs-Regime |
| **[crm-cosmology](https://github.com/research-line/crm-cosmology)** | **2026-08-09** | Curvature Relaxation Model Arbeiten & Code für modifizierte Gravitationsprüfungen |
| **[ai-elite-swr](https://github.com/research-line/ai-elite-swr)** | **2026-08-05** | KI-Elite-Weltbildrekonstruktion: Preprints, Prompts, Validierungsdaten & Abbildungen |
| **[rfep-framework](https://github.com/research-line/rfep-framework)** | **2026-03-19** | Früheres RFEP-Brückenmaterial; aufbewahrt für Zitationen, Vergleiche und Historie *(Archiviert)* |

---

## Zitation & Leseweise dieser Repositories

- **Aktueller Status:** Nutzen Sie die `README.md`- und `CITATION.cff`-Dateien des jeweiligen Repositories für offizielle Zitationsmetadaten und aktuelle Statusbeschreibungen.
- **Archivarische Datensätze:** Betrachten Sie Zenodo-DOI-Einträge als persistente Publikations-Snapshots, während GitHub den lebenden Code, laufende Audits und Beweisaktualisierungen bereitstellt.
- **Suchbegriffe:** Nutzen Sie exakte Repository-Namen wie `research-line/abc-hct`, `research-line/functional-stability-theory`, `research-line/crm-cosmology`, `research-line/rh-even-dominance`, `research-line/fst-nash` oder `research-line/ai-elite-swr`.
- **Wichtige Discovery-Phrasen:** `research-line open-access research software`, `research-line Zenodo DOI reproducible research`, `research-line abc-hct`, `research-line abc conjecture Hecke quotient certificates`, `research-line Manin symbol pairing engine`, `research-line Functional Stability Theory`, `research-line FST domain proofs`, `research-line Curvature Relaxation Model CMB Pantheon MOND SPARC`, `research-line conditional Riemann Hypothesis proof audit`, `research-line AI elite worldview reconstruction`, `research-line chaperone systems FST-Nash`.
- **Maschinenlesbarer Kontext:** Nutzen Sie [`research-line/.github/llms.txt`](https://github.com/research-line/.github/blob/main/llms.txt) für KI-Crawler und automatisierte Agenten.

---

<!-- last-checked: 2026-09-10 -->
