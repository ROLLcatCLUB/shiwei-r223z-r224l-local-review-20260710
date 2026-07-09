# R224A Risk And Misuse Notes

stage_id: 1013R_R224A_UNIT_LEVEL_PRACTICE_INTENSITY_ROUTER_PLANNING

## Main Risks

### 1. Every art lesson becomes practice-heavy

Risk:

The system may assume that art means making, so every lesson expands into long creation blocks.

Control:

Use `unit_phase_role`, `lesson_position_in_unit`, and `practice_intensity` before classroom event expansion.

### 2. Understanding lessons are under-supported

Risk:

Low practice may be misread as low teaching value.

Control:

Low-practice lessons still need strong observation, comparison, vocabulary, and evidence of understanding.

### 3. Technique preparation becomes final product pressure

Risk:

Technique lessons may be forced to produce polished works too early.

Control:

For `technique_preparation`, prioritize trial samples, method comparison, and learning sheet evidence.

### 4. Practice creation becomes teacher over-explanation

Risk:

High-practice lessons may get too much teacher talk.

Control:

For `practice_creation`, reduce explanation density and strengthen circulation support, rescue moves, and evidence capture.

### 5. Evidence collection becomes bureaucratic

Risk:

The system may generate evidence fields for every activity.

Control:

Evidence must connect to stage responsibility and performance task link.

### 6. Router fields become decorative

Risk:

The router labels may be filled but not affect generated classroom events.

Control:

Validator and later regression must check that router output changes explanation density, demonstration density, work time, teacher support, and evidence mode.

## Boundary Risks

R224A must not:

- modify R223M/N/O teacher manuscripts;
- publish v0.2;
- create HTML;
- open UI or R97B;
- connect runtime / provider / model / prompt / db;
- write back lesson body.
