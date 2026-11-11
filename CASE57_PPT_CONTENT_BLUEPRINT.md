# Case 57 PowerPoint Content Blueprint

**Purpose:** Content and visual direction for a 14-slide presentation to be authored in Claude. This is a blueprint only; it is not the final PowerPoint.

**Student:** Manoj — Roll Number 57<br>
**University:** Dayananda Sagar University<br>
**Subject:** AI in Software Engineering<br>
**Case:** 57 — Airline Crew Scheduling

## Source materials inspected

| Material | Exact file/location | Inspection and use |
|---|---|---|
| Full official Assignment Book, 75 cases | `C:\Users\guest pc\Desktop\CAT2_Case57\examportal\ppt component\AI_in_SE_Assignment_Book_75_Cases.pdf` | Trusted project copy used for this completion pass; Case 57 is on printed pages 228–231. The scenario is “An airline schedules 400 crew members under duty-time laws; a violation can ground a flight.” It fixes Spiral, Scrum and ChatGPT; Task A covers rule-conflict risks, B AI-assisted constraint planning, C a duty-limit validator/Git/Jenkins/Docker, D unit tests/AI edge cases/defect prediction, and E correctness/SonarQube/fairness in AI-generated rosters. |
| Short 75-case assignment extract | `C:\Users\guest pc\Desktop\sepm\AI in Software Engineering – Case Study Assignment (75 Cases)_removed.pdf` (byte-identical copy also at Desktop root) | Inspected the Case 57 summary (page labelled 21 of 26). It confirms the fixed choices and module task summaries. The full Assignment Book above is the more detailed source for this blueprint. |
| Reference presentation | `C:\Users\guest pc\Desktop\Case45_EGovernance_Grievance_Portal_Updated_Tanmay.pptx` | Inspected all 13 slides and rendered slide previews. Reference only for structure, visual style and detail level; do not reuse its Case 45 content. |
| Case 57 project instructions | `C:\Users\guest pc\Desktop\CAT2_Case57\examportal\CASE57_INSTRUCTIONS.md` | Read. Confirms fixed choices, 25 labs, implementation rules and the instruction to preserve existing evidence. |
| Previous evidence audit | `C:\Users\guest pc\Desktop\CAT2_Case57\examportal\CASE57_EVIDENCE_AUDIT.md` | Read. Contains per-lab evidence judgments and the exact screenshot inventory. |
| Existing assignment report | `C:\Users\guest pc\Desktop\CAT2_AI_Software_Engineering_Case57\Case57_Roll57_Manoj.docx` | Inspected text and all 25 lab sections. Found useful draft content in T1.1, T1.2, Task B/T2.3 and T2.5; lab evidence tables/placeholders remain mostly incomplete. No media is embedded in the report. |
| Screenshot folder | `C:\Users\guest pc\Desktop\CAT2_AI_Software_Engineering_Case57\LAB SCREENSHOTS` | Accessible; all 22 image files were inspected. `LAB SCREENSHOTS.zip` contains the same 22 files and no additional images. Some filenames have duplicate `.png` suffixes; retain and cite the exact existing names. |
| Project implementation | `duty_validator.py`, `test_duty_validator.py`, `test_ai_generated.py`, `hello.py`, `requirements.txt`, `Dockerfile`, `Jenkinsfile` under `C:\Users\guest pc\Desktop\CAT2_Case57\examportal` | Read to distinguish implemented behaviour/configuration from proposed integrations and unrun services. |

## Visual direction for Claude

Use the friend's deck as a presentation-design reference, not as content to copy:

- 16:9 widescreen; warm off-white background; dark navy headings/body; muted sage/teal and pale sand/amber accents.
- Small numbered section label above a concise, assertive slide title; thin rules, restrained accent lines, generous whitespace, rounded cards, simple arrows, and a small slide number/footer.
- Favor one clear diagram or evidence image per slide, with concise text and a status callout. Keep body text readable; move the fuller explanations below into speaker notes.
- Use status labels consistently: **IMPLEMENTED / EVIDENCED**, **PROPOSED**, **PENDING**. Never style a proposed diagram as if it were a deployed system.
- The reference deck alternates problem, workflow, architecture, process, test/evidence, limitations and wrap-up slides. Preserve that narrative rhythm while keeping this presentation to the requested 14 slides.

## Evidence and accuracy guardrails

- The project uses **sample assumptions**, not confirmed airline law: daily duty maximum 10.0 hours inclusive; minimum rest 10.0 hours inclusive; seven-day duty maximum 60.0 hours inclusive; negative inputs raise `ValueError`. State visibly that faculty/official rules must confirm these values.
- The current validator is a small Python function. The Flask app has only greeting and about routes; it does not call the validator or present a scheduling workflow.
- Existing unit and AI-test files each contain ten tests. `CASE57_INSTRUCTIONS.md` records a latest local result of 20 tests passed. Existing screenshots show separate older 10-test runs; they are not a screenshot of that combined 20-test run.
- The Docker screenshot shows a single-container `docker run` test execution (9 tests in that screenshot), **not Docker Compose**. No app/database Compose stack is evidenced.
- A `Jenkinsfile` exists, but the inspected PR screenshot says Jenkins execution was pending/not configured. Do not claim a Jenkins build ran.
- Existing analyzer screenshots are Pylint, Flake8 and Bandit, **not SonarQube**. The report's SonarQube quality gate is not evidenced.
- No screenshot proves an actual Git merge conflict. A merged PR is not a merge-conflict demonstration.
- L4.3 now has genuine Chrome screenshots for plain and POM Selenium. No existing screenshot proves AI review comments, ChatGPT prompt iterations, or an L1.3 privacy-settings screen.
- Do not imply the assignment prototype generates full crew rosters or has measured 400-crew performance. It currently validates one set of numeric duty inputs.

## Current evidence update

This update supersedes stale slide notes below where they say that lab work is still absent. The current matrix is in `CASE57_EVIDENCE_AUDIT.md`; lab evidence files are under `CASE57_LAB_EVIDENCE`.

- **Current lab totals:** 15 COMPLETE, 5 PARTIAL, 3 PENDING HUMAN and 2 BLOCKED.
- **Verified test run:** the project suite ran locally and reported **20 passed in 0.12s**. This command result is not a new screenshot.
- **Completed practical evidence:** prior written labs plus L4.3 plain/POM Selenium runs in Chrome with recaptured screenshots.
- **Still partial or unavailable:** L1.3 privacy-settings comparison, incomplete L3.1 Prompt 4, SonarQube scans, a real PR review, and L5.4 authoring-time/SonarQube comparison. L2.4/L4.2/L5.1 need genuine human participation. Jenkins remains blocked (Java 8 JRE, no controller). Docker Compose remains blocked (Engine unreachable; Desktop paging-file error). Prepared Compose files exist and were not executed.
- **Screenshot rule:** L4.3 screenshots were recaptured from the Chrome run. Other existing screenshots were not overwritten. The L4.5 sketch contains mock values, not live monitoring data.

---

## Slide 1 — Title slide

**Exact title:** Case 57 — Airline Crew Scheduling

**Presentation-ready content**

- AI in Software Engineering | Dayananda Sagar University
- Manoj | Roll Number 57
- Process model: Spiral | Agile method: Scrum | AI tool: ChatGPT
- Prototype: Duty-Limit Validator
- Scenario: Validate schedules in an airline planning for 400 crew members

**Talking point:** This is a small prototype for demonstrating duty-limit checks, not a production airline roster-generation system.

**Diagram/flowchart for Claude:** A clean four-step motif on the right: `Crew duty inputs → Validate limits → Accept / explain rejection`. Label it “prototype concept”; do not depict an implemented web workflow.

**Existing screenshots:** None needed. The dashboard sketch is not a title graphic.

**Missing evidence/practical work:** None for the title slide. Do not add a fabricated airline logo, production claim or live-system screenshot.

**Status:** Assignment identity and fixed choices are verified; the motif is a proposed visual.

## Slide 2 — The scheduling problem

**Exact title:** A duty-limit violation can ground a flight

**Presentation-ready content**

- The case scenario concerns an airline scheduling **400 crew members** under duty-time laws.
- A roster that breaches a duty limit can make a flight unschedulable.
- Planners need a clear, repeatable way to check daily duty, rest and weekly totals.
- Case 57 asks for a duty-limit validator; it does **not** ask this prototype to build a full airline management platform.

**Talking point:** Incorrect assumptions are themselves a safety and correctness risk, so the sample rules must be confirmed before operational use.

**Diagram/flowchart for Claude:** Show “400 crew schedules” entering a rules-check stage; split outputs into “Within sample limits” and “Review / rejected with reason.” Add a prominent note: “Conceptual case workflow — no 400-crew system run has been evidenced.”

**Existing screenshots:** `C57_TaskC_01_Validator_Output.png.png` is suitable only as a small example of the validator's terminal output; it does not demonstrate processing 400 crew.

**Missing evidence/practical work:** No 400-crew performance or integration evidence. No new screenshot is needed for the problem statement.

**Status:** 400-crew scenario is assignment context; actual prototype scale testing is pending.

## Slide 3 — Objectives and proposed solution

**Exact title:** A focused validator makes rule checks explicit

**Presentation-ready content**

- **Objective 1:** Check whether a duty input set satisfies the assumed daily, rest and seven-day limits.
- **Objective 2:** Give a clear rejection reason when a limit is exceeded.
- **Objective 3:** Reject negative hour values as invalid input.
- **Implemented now:** `validate_duty(hours_today, hours_last_7_days, rest_hours)` returns `(True/False, message)` or raises `ValueError` for negative values.
- **Scope boundary:** The Flask starter is not connected to this function; the current prototype is a Python validator and tests.

**Talking point:** Keep the proof-of-concept small; first agree the rules, then connect a UI or service only if required.

**Diagram/flowchart for Claude:** Three objective cards leading to one “Duty-Limit Validator” card. A dashed boundary around “Web UI / roster storage / 400-crew batch processing” marked **future, not implemented**.

**Existing screenshots:** `C57_TaskC_01_Validator_Output.png.png` shows a few actual command-line examples. `L1.1_02_Flask_Home.png.png` shows the separate greeting page, not a validator interface.

**Missing evidence/practical work:** No Flask validation form/API or end-to-end scheduler integration. No new screenshot is needed for this scope slide.

**Status:** Core Python function exists; broader integration is proposed only.

## Slide 4 — Spiral model

**Exact title:** Spiral development puts rule risks before expansion

**Presentation-ready content**

- **Fixed case choice:** Spiral model.
- Each loop covers four activities: **set objectives and alternatives → identify and resolve risks → develop and test → review and plan the next loop**.
- Case 57 risk focus: ambiguous duty-law interpretations, boundary values, conflicting daily/weekly constraints, and incorrect AI-generated requirements.
- A sample first loop can establish agreed rules and a tested validator; a later loop can add integration after the rules are confirmed.
- The report identifies possible risks such as overnight duty/rest interpretation and whether standby duty counts; those questions need an authoritative answer.

**Talking point:** Spiral is appropriate to discuss because high-impact rule uncertainty calls for repeated risk review; do not imply that a formal risk register or multiple completed loops are evidenced unless included in the submitted report.

**Diagram/flowchart for Claude:** Four linked quadrants or a circular loop with the four named Spiral activities. Put “rule clarification” and “boundary tests” in the risk quadrant. Mark any future loop “proposed.”

**Existing screenshots:** `C57_TaskC_01_Validator_Output.png.png` can illustrate a tested prototype, but it does not prove a Spiral cycle. `C57_TaskB_01_Backlog.png.png` supports planning context, not Spiral execution.

**Missing evidence/practical work:** The SDLC diagram and phase deliverables are now documented in `CASE57_LAB_EVIDENCE/L1.1_Evidence.md`; do not present a screenshot of that Markdown diagram unless one is actually rendered and captured. The Spiral diagram on this slide remains a conceptual explanation, not evidence of completed Spiral loops.

**Status:** Spiral is the fixed assignment method; diagram is a presentation explanation, not proof of completed iterative loops.

## Slide 5 — Scrum methodology

**Exact title:** Scrum organizes constraint work into reviewable stories

**Presentation-ready content**

- **Fixed case choice:** Scrum.
- **Roles in the report's solo simulation:** Product Owner defines stories; Scrum Master facilitates planning; Developer builds and tests. These are simulated roles, not three separate team members.
- **Events:** Sprint planning, daily Scrum, sprint review and retrospective.
- **Artifacts:** Product backlog, selected sprint work and a Definition of Done.
- Existing stories cover daily duty, minimum rest, seven-day duty and a clear rejection reason. The report describes a two-week sprint as an assumption and a goal of validating a roster against R1–R4.

**Talking point:** The existing GitHub Projects image shows four stories, all marked Todo; it proves a backlog view, not completed sprint work or a team ceremony.

**Diagram/flowchart for Claude:** Scrum loop `Backlog → Sprint planning → Sprint work/daily Scrum → Review → Retrospective → Backlog`. Add a side card listing the three solo-simulation roles.

**Existing screenshots:** `C57_TaskB_01_Backlog.png.png` shows four user stories in GitHub Projects with Todo status.

**Missing evidence/practical work:** L2.1–L2.3 planning artifacts are now recorded in the lab evidence folder. L2.4 still needs real estimates from three classmates; the existing backlog screenshot is not evidence of those estimates or team participation.

**Status:** Backlog screenshot is historical; L2.1–L2.3 artifacts are complete. L2.4 is pending genuine human participation.

## Slide 6 — Proposed architecture and workflow

**Exact title:** One validation function anchors the prototype

**Presentation-ready content**

- **Current implementation:** Python caller supplies daily hours, last-seven-days hours and rest hours to `validate_duty`.
- The function checks negative values first, then daily limit, minimum rest and weekly limit.
- It returns a Boolean and a human-readable reason; invalid negative input raises `ValueError`.
- **Not currently connected:** `hello.py` contains `/` and `/about` greeting routes only; there is no validator route, database or roster UI.

**Talking point:** Present the right-hand architecture as a target design; distinguish it from the implemented function and tests on the left.

**Diagram/flowchart for Claude:** Two lanes:

1. Solid **implemented** lane: `Python test/CLI → validate_duty() → accepted / reason / ValueError`.
2. Dashed **proposed** lane: `Planner UI/API → validator → results → optional roster store`.

Add a label that persistence and API integration are not present in the current code.

**Existing screenshots:** `C57_TaskC_01_Validator_Output.png.png` supports the CLI flow. `L1.1_02_Flask_Home.png.png`, `L1.1_04_About_Route.png.png` show the current basic Flask routes, not a validator UI.

**Missing evidence/practical work:** No web form/API integration, database or 400-person workflow. The architecture diagram is proposed; no new screenshot is required.

**Status:** Function and basic Flask starter are implemented separately; the integrated architecture is proposed.

## Slide 7 — ChatGPT and AI-assisted development

**Exact title:** AI can draft ideas; people must verify the rules

**Presentation-ready content**

- ChatGPT is the AI tool specified for this case.
- Appropriate assistance: draft constraint stories, suggest edge cases, explain code and help structure tests.
- Verification loop: compare each output to the approved rule source → inspect the code/test expectation → run tests → record accepted, changed or rejected suggestions.
- Do not provide real crew personal data in prompts.
- A test file named `test_ai_generated.py` exists and has ten tests; the filename alone does not establish which model generated it or what prompt was used.

**Talking point:** The assignment requires AI-assisted planning and testing, but evidence must show actual prompts/outputs before claiming a particular experiment was completed.

**Diagram/flowchart for Claude:** `ChatGPT suggestion → Rule-table check → Human review → Test run → Accept / revise / reject`. Include “No real crew data” as a guardrail.

**Existing screenshots:** `C57_TaskD_03_AI_Generated_Tests.png.png` and `C57_TaskE_06_AI_Tests_Final.png.png` show ten AI-labelled tests being executed; they do not show the prompt or prove model provenance.

**Missing evidence/practical work:** L1.3 has paired outputs and matching tests but lacks verified account-specific privacy settings. L1.4 preserves simulated notes and an actual ChatGPT extraction, with 7 supported, 3 vague and 1 invented item. L1.5 preserves a genuine ChatGPT prompt/output and actual case results (9/10 first-ten expectations matched; the Boolean case failed). L3.1 preserves four ChatGPT records, with Prompt 4 incomplete. No new screenshot was captured for these updates.

**Status:** ChatGPT is the fixed case tool; use the actual L1.4/L1.5 conversation records for those lab claims. L1.3 is partial because account privacy settings were not verified.

## Slide 8 — Duty-Limit Validator

**Exact title:** The validator applies four explicit sample rules

**Presentation-ready content**

- **R1 — Daily duty:** maximum 10.0 hours; exactly 10.0 is accepted.
- **R2 — Rest:** minimum 10.0 hours; exactly 10.0 is accepted.
- **R3 — Rolling seven-day duty:** maximum 60.0 hours; exactly 60.0 is accepted.
- **R4 — Input validation:** any negative hour value raises `ValueError`.
- A violation returns `False` and a reason such as “Daily duty limit exceeded.”; a passing example returns `True` and “Duty schedule accepted.”
- These values are **working assumptions**, not confirmed legal limits. Confirm them before presenting them as airline law.

**Talking point:** The current function checks three numeric totals; it does not calculate duty from flight timestamps or generate a roster.

**Diagram/flowchart for Claude:** Decision flow: `Negative input? → ValueError`; otherwise check `daily > 10? → reject`; `rest < 10? → reject`; `7-day total > 60? → reject`; else accept. Include boundary labels 10/10/60 as inclusive.

**Existing screenshots:** `C57_TaskC_01_Validator_Output.png.png` visibly shows one accepted input, one daily-limit rejection and one rest rejection. `C57_TaskD_01_Pytest.png.png` shows ten unit tests; `C57_TaskD_03_AI_Generated_Tests.png.png` shows ten AI-labelled tests including boundaries.

**Missing evidence/practical work:** L4.1 now has ten direct manual checks and two isolated seeded boundary defects documented in its evidence file. The rule values still await official confirmation. No new screenshot was captured.

**Status:** Rules are implemented and covered by tests as assumptions; official rule confirmation is pending.

## Slide 9 — Git, GitHub, Jenkins and Docker

**Exact title:** Version control and packaging are evidenced; CI execution is pending

**Presentation-ready content**

- **Git:** A feature branch and project history are visible in the existing terminal evidence.
- **GitHub:** A project pull request was merged; this is ordinary PR evidence, not proof of a merge conflict or AI review.
- **Docker:** A Dockerfile installs requirements, copies the validator/test file, switches to a non-root user and runs pytest.
- The existing Docker run screenshot shows a single container running tests (9 passed in that captured run).
- **Jenkins:** A Jenkinsfile is present with Checkout, Install, Test and Package stages, but the inspected PR evidence says Jenkins was not configured and no Jenkins build was run.

**Talking point:** The config and successful Docker test run should not be presented as a completed Jenkins pipeline or Docker Compose app/database deployment.

**Diagram/flowchart for Claude:** Proposed CI path `Git push/PR → Jenkins checkout → install → test → Docker image build`; color the Jenkins execution portion amber and label **configured file / build not evidenced**. Below it, keep the actual Docker `docker run` test as a separate completed proof.

**Existing screenshots:** `C57_TaskC_01_Git_Log.png.png` (Git history/branch), `C57_TaskC_02_PR_Merged.png.png` (merged PR), `C57_TaskC_03_Docker_Run.png.png` (single-container pytest), `C57_TaskC_04_GitHub_Files.png.png` (repository files), `C57_TaskC_04_PR_Details.png.png` (PR details and Jenkins-pending note).

**Missing evidence/practical work:** L3.3 conflict markers, AI suggestion, resolution and Git verification are now documented from an isolated temporary repository; there is no conflict screenshot. Jenkins success/failure/fix remains blocked. L3.5 Compose files are prepared (`compose.yaml`, `Dockerfile.compose`) and were not run. Do not infer a Compose or Jenkins run from historical images.

**Status:** Git/ordinary PR and single-container Docker test activity have historical screenshots; L3.3 is complete in text evidence; Jenkins and Compose remain blocked. L4.3 Selenium is complete.

## Slide 10 — Testing strategy

**Exact title:** Boundary tests exercise the validator’s core constraints

**Presentation-ready content**

- The unit suite covers valid duty, exact daily/rest/weekly limits, over-limit values and negative-input errors.
- The separate AI-labelled test file has ten more cases, including zero duty, threshold boundaries and negative inputs.
- `CASE57_INSTRUCTIONS.md` records the latest full local test run as **20 passed**. Existing screenshots show separate earlier 10-test runs, not that combined run.
- The earlier coverage screenshot reports **61%** statement coverage for `duty_validator.py`; present it as that captured run, not a current coverage guarantee.
- Tests demonstrate the assumed rules, not legal correctness or full roster-level performance.

**Talking point:** A passing suite is useful evidence of implementation behavior against its test expectations; it does not validate the assumptions against official regulations.

**Diagram/flowchart for Claude:** Small test pyramid with a large unit-test base labeled “20 current local tests recorded (10 standard + 10 AI-labelled),” a thin integration/UI layer labeled “not evidenced,” and a top performance/400-crew layer labeled “not measured.”

**Existing screenshots:** `C57_TaskD_01_Pytest.png.png` (10 unit tests passed), `C57_TaskD_02_Coverage.png.png` (61% captured coverage), `C57_TaskD_03_AI_Generated_Tests.png.png` (10 AI-labelled tests passed), `C57_TaskE_05_Final_Unit_Tests.png.png` and `C57_TaskE_06_AI_Tests_Final.png.png` (later test-run images).

**Missing evidence/practical work:** No 400-crew timing result exists. L4.3 Selenium/POM Chrome runs are documented with screenshots. L4.1's ten manual checks/two seeded defects are documented. L4.4 records ten ChatGPT tests; 9/10 are supported by the case rule table (90%), and the unsupported Boolean expectation was removed from the corrected final set.

**Status:** The current full suite ran with 20 passing tests; prior screenshots show separate runs. L4.1 and L4.4 evidence is complete; performance testing is not measured.

## Slide 11 — Software quality, security and static analysis

**Exact title:** Static-analysis tools found issues to review—not a SonarQube gate

**Presentation-ready content**

- Pylint evidence includes an initial **8.89/10** score and a later **10.00/10** score.
- Flake8 evidence shows `W292` (no newline at end of file) in that captured run.
- Bandit reports “No issues identified” for the code it scanned in that run.
- These are actual Pylint/Flake8/Bandit outputs; none is a SonarQube scan or quality-gate result.
- L5.2 separately documents three current Pylint findings as an alternative analyzer; they are not SonarQube findings.
- Continue to treat code review, rule confirmation and test quality as separate from a linter score.

**Talking point:** A clean Bandit run is limited to the rules and files scanned; it is not proof of complete application security.

**Diagram/flowchart for Claude:** Three analysis cards (Pylint, Flake8, Bandit) flowing to “Review findings / verify fixes”; add a separate dashed “SonarQube project + quality gate — pending” box.

**Existing screenshots:** `C57_TaskE_01_Pylint.png.png` (initial score), `C57_TaskE_02_Flake8.png.png` (W292), `C57_TaskE_03_Bandit.png.png` (no issues identified in that scan), `C57_TaskE_04_Pylint_Final.png.png` (final 10/10 score).

**Missing evidence/practical work:** No SonarQube issue list, project scan, or quality gate is present. L5.2's actual Pylint findings are documented but remain PARTIAL because Pylint is not SonarQube. L5.4 also lacks SonarQube scans and reliable timing observations.

**Status:** Pylint, Flake8 and Bandit runs are evidenced; SonarQube is not.

## Slide 12 — Fairness, ethics and responsible AI

**Exact title:** Apply the same rules—and keep people accountable

**Presentation-ready content**

- The current validator uses duty-hour inputs and does not use a crew member’s name or demographic characteristics in its decision.
- A rejection message gives a reason that a planner can review.
- AI-suggested rules, tests or roster decisions need human verification against the approved source.
- Do not place real crew names, personal data or confidential roster details in AI prompts.
- **Scope limit:** This prototype does not generate AI crew rosters; fairness in generated rosters remains a design and review requirement, not a demonstrated feature.

**Talking point:** Fairness is not established by code alone. A future roster generator would need defined fairness criteria, representative evaluation and human oversight.

**Diagram/flowchart for Claude:** Decision flow with a “same duty rules for each person” gate; show “human planner review” before any future roster is approved. Use a dotted outline for the not-yet-built AI roster component.

**Existing screenshots:** `C57_TaskC_01_Validator_Output.png.png` shows reason-bearing validator responses. No existing image demonstrates fairness evaluation or an AI roster.

**Missing evidence/practical work:** No fairness test set or roster-bias analysis exists. L5.5 disclosure, one-page policy and Flask licence check are now documented. L5.3 has only a local-code AI review, not a real pull-request review. No new screenshot was captured.

**Status:** Current decision logic is numeric and explanatory; AI roster fairness evaluation is not implemented or evidenced.

## Slide 13 — Challenges, limitations and next improvements

**Exact title:** Rule confirmation and integration are the next gates

**Presentation-ready content**

- **Rule uncertainty:** 10/10/60-hour values are assumptions pending official/faculty confirmation.
- **Prototype boundary:** one Python function; no timestamp-based rest calculation, roster generation, database, or validator web/API integration.
- **Input robustness:** the implementation checks negative values, but does not explicitly reject all wrong types or non-finite numeric values.
- **Automation gap:** Jenkinsfile exists but no Jenkins build is evidenced; Docker Compose is blocked (engine down); Selenium POM is evidenced; SonarQube was not run; the AI review was not on an actual PR.
- **Scale claim not tested:** the 400-crew target comes from the scenario; no measured 400-crew run is available.

**Talking point:** The priority order is confirm rules → strengthen input validation → add a small validator UI/API if needed → automate verified tests → measure performance and fairness.

**Diagram/flowchart for Claude:** Roadmap with two swimlanes: **Now / evidenced** (validator, tests, Selenium POM, Docker test container, static analyzers) and **Next / pending** (rule sign-off, input hardening, integration, Jenkins, Compose, SonarQube, 400-crew test).

**Existing screenshots:** `C57_TaskC_04_PR_Details.png.png` supports the Jenkins-pending status; `C57_TaskC_03_Docker_Run.png.png` supports the limited Docker test container; `C57_TaskE_01_Pylint.png.png`, `C57_TaskE_02_Flake8.png.png` and `C57_TaskE_03_Bandit.png.png` support the static-analysis status.

**Missing evidence/practical work:** Complete the partial/blocked labs in the current audit matrix and obtain genuine classmate participation for L2.4, L4.2 and L5.1. No new screenshot is necessary for this roadmap.

**Status:** Limitations are based on inspected code, project files and evidence; roadmap items are proposals.

## Slide 14 — Conclusion and references

**Exact title:** A tested prototype is a starting point—not legal approval

**Presentation-ready content**

- Case 57 choices remain fixed: **Spiral + Scrum + ChatGPT + Duty-Limit Validator**.
- The current Python prototype demonstrates explicit daily, rest and weekly checks against sample assumptions.
- The recorded local suite has 20 passing tests; existing screenshots document individual test and tool runs.
- Before a real scheduling use: confirm rules, complete practical evidence, review edge cases, and validate any larger integration with accountable human oversight.
- **References:** Official Case 57 assignment entry; `CASE57_INSTRUCTIONS.md`; Case 57 report draft; project validator/tests; inspected Case 45 reference deck (visual structure only).

**Talking point:** The project demonstrates a focused engineering prototype and an evidence-aware process; it does not certify compliance with aviation law.

**Diagram/flowchart for Claude:** Three closing cards: **What exists** (validator/tests), **What it shows** (sample-rule checking), **What remains** (official rule approval and integrations).

**Existing screenshots:** `C57_TaskC_01_Validator_Output.png.png`, `C57_TaskD_01_Pytest.png.png` and `C57_TaskD_03_AI_Generated_Tests.png.png` are suitable as small examples of actual prototype/test evidence. Do not use the Case 45 screenshots as Case 57 evidence.

**Missing evidence/practical work:** Follow the current lab status matrix before claiming completion; do not omit partial, blocked or human-dependent work. No closing-slide screenshot is necessary.

**References to show on slide or in speaker notes**

1. *AI in Software Engineering – Assignment Book (75 Cases)*, Case 57 — Airline Crew Scheduling, printed pages 228–231. Exact local file: `C:\Users\guest pc\Desktop\sepm\AI_in_SE_Assignment_Book_75_Cases.pdf`.
2. *AI in Software Engineering – Case Study Assignment (75 Cases)*, Case 57 summary, page labelled 21 of 26. Exact local file: `C:\Users\guest pc\Desktop\sepm\AI in Software Engineering – Case Study Assignment (75 Cases)_removed.pdf`.
3. `CASE57_INSTRUCTIONS.md`, Sections 1–8, project root.
4. `Case57_Roll57_Manoj.docx`, Section 0.2 (assumed rules), Tasks A–E and lab requirements. Exact local file: `C:\Users\guest pc\Desktop\CAT2_AI_Software_Engineering_Case57\Case57_Roll57_Manoj.docx`.
5. `duty_validator.py`, `test_duty_validator.py`, `test_ai_generated.py`, project root.
6. `Case45_EGovernance_Grievance_Portal_Updated_Tanmay.pptx` — presentation design/structure reference only; not a Case 57 factual source.

**Status:** Case choices and core implementation are verified; assignment completion and legal rule confirmation are not implied.

---

## Current pending-evidence checklist for Claude

- **Can reuse directly:** Dashboard sketch (`C57_L4.5_01_Dashboard_Sketch.png.png`), backlog (`C57_TaskB_01_Backlog.png.png`), validator examples, test runs, coverage and existing static-analysis screenshots—only for the specific claims they visibly support.
- **Do not claim as done:** Jenkins success/failure/fix; Docker Compose/database communication (files prepared, engine down); SonarQube; account privacy settings for L1.3; completed Prompt 4 code; actual PR review; 400-crew performance; classmate estimates/sign-offs; fairness evaluation of generated rosters.
- **Already evidenced:** L3.3 merge conflict (text/transcript in `L3.3_Evidence.md`); L4.1 manual checks/seeded defects; L4.3 Selenium plain vs POM Chrome run; L4.5 dashboard sketch; L5.5 disclosure/policy/licence check.
- **Evidence still to collect:** ChatGPT-specific output where required, Jenkins/Compose/SonarQube runs when tools are available, actual PR review, genuine peer/classmate input and any measured 400-crew/fairness results.
- **Never fabricate or infer:** test/build results, prompts, AI provenance, tool configuration, classmate participation, legal approval, or screenshots.
