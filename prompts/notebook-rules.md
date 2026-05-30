# Notebook Rules

Governance and operational rules for maintaining this Expert Notebook.

## Core Rules

1. **Knowledge is not a dump of information.**
   - Knowledge must be distilled and synthesized.
   - Raw research and notes should not directly appear in `notebook/knowledge/`.
   - Everything passes through the update/review process first.

2. **Decisions are more important than knowledge.**
   - When in doubt, prioritize documenting decisions.
   - Decisions include rationale and trade-offs.
   - Active decisions guide daily work.

3. **Updates must be reviewed before becoming trusted.**
   - New findings always enter `notebook/updates/pending.md` first.
   - No direct edits to knowledge or decisions without review.
   - Review process ensures quality and consistency.

4. **Every important decision should include rationale.**
   - Decisions without clear reasoning are incomplete.
   - Rationale should explain the problem, options, and criteria.
   - Future reviewers need to understand the logic.

5. **The notebook should become smaller and clearer over time.**
   - Regular consolidation removes redundancy.
   - Knowledge should become more concise, not more verbose.
   - Outdated information should be archived or removed.

6. **Duplicate information should be merged.**
   - If two files say the same thing, consolidate.
   - Create links between related concepts instead of repeating.
   - The notebook should have a single source of truth per topic.

7. **Contradictions should be surfaced, not hidden.**
   - If two beliefs contradict, flag it immediately.
   - Create updates to resolve contradictions.
   - Never ignore conflicts—they reveal deeper uncertainty.

8. **The notebook exists to improve decision quality.**
   - Every entry should serve decision-making.
   - If something doesn't improve decisions, question its value.
   - Decision quality is the success metric.

9. **The notebook exists for the Expert Agent.**
   - Structure should be agent-readable.
   - Use consistent markdown, clear formatting, links.
   - Every file should be parseable without context.

10. **The notebook is a living knowledge base, not a chat history.**
    - It's not a running log of conversations.
    - It's organized, indexed, and intentional.
    - Stale information should be removed or archived.

## Process Rules

### Adding New Information

1. Submit as an update to `notebook/updates/pending.md`
2. Include source, evidence, and implications
3. Flag contradictions with existing beliefs
4. Wait for review

### Reviewing Updates

1. Assess evidence quality
2. Check for conflicts with existing knowledge
3. Evaluate impact on decisions
4. Approve, request changes, or reject
5. Document reasoning

### Promoting to Knowledge

1. Update has been approved
2. Synthesize from raw update format
3. Add to appropriate section in `notebook/knowledge/`
4. Record in `notebook/updates/accepted.md`
5. Log in `notebook/reviews/change-history.md`

### Promoting to Decisions

1. Strategic consensus achieved
2. Clear rationale documented
3. Trade-offs explicitly stated
4. Success criteria defined
5. Add to `notebook/decisions/active.md` with rationale in `notebook/decisions/rationale.md`

### Archiving/Retiring

1. Decision no longer active: Move to `notebook/decisions/archived.md`
2. Question resolved: Move to `notebook/questions/resolved.md`
3. Knowledge outdated: Move to archive or remove with documentation

## Quality Standards

- **Clarity:** Every entry should be understandable without external context.
- **Completeness:** Important decisions include full rationale.
- **Consistency:** Use the provided templates and structure.
- **Currency:** Review regularly; archive stale information.
- **Traceability:** Track origins and changes; maintain change history.

## Review Cadence

- **Continuous:** Updates can be submitted and reviewed anytime.
- **Weekly:** Quick maintenance and small updates (if using this actively).
- **Monthly:** Major review cycle, promote significant updates, consolidate knowledge.
- **Quarterly:** Strategic review of decisions and goals, potential major reorganization.

## Permission & Governance

- **Who Can Edit:** [Define this for your context]
- **Who Reviews:** [Define this for your context]
- **Approval Required For:** Major decisions, significant knowledge changes
- **Urgent Updates:** Fast-track review process for time-sensitive information

---

**Version:** 1.0
**Last Updated:** 
**Approved By:** 
