# Expert Notebook Template

An Expert Notebook is a structured knowledge base designed for AI expert agents.

The goal is not to store as much information as possible.

The goal is to help an Expert Agent make better decisions over time.

## Core Philosophy

**Information → Knowledge → Decisions**

Most systems stop at information.

This notebook focuses on decisions.

The Expert Agent continuously:

* learns
* reviews
* organizes
* updates
* improves recommendations

while maintaining a clear source of truth.

## Principles

* **Knowledge should be distilled.** Not raw research—synthesized insights.
* **Decisions should be explicit.** With clear rationale, not buried in notes.
* **Updates should be reviewed.** New findings enter a staging area first.
* **Uncertainty should be tracked.** Make it visible, not hidden.
* **Personalization should be separate** from domain knowledge.

## The Workflow

```
New Information
    ↓
Updates (proposed changes)
    ↓
Review (agent + human)
    ↓
Knowledge (trusted insights)
    ↓
Decisions (chosen strategies)
    ↓
Recommendations (expert advice)
```

## Repository Structure

```
expert-notebook/
├── README.md
├── profile/
│   ├── goals.md
│   ├── preferences.md
│   ├── constraints.md
│   └── context.md
├── notebook/
│   ├── knowledge/
│   │   ├── concepts.md
│   │   ├── frameworks.md
│   │   ├── evidence.md
│   │   └── glossary.md
│   ├── decisions/
│   │   ├── active.md
│   │   ├── archived.md
│   │   └── rationale.md
│   ├── updates/
│   │   ├── pending.md
│   │   ├── accepted.md
│   │   └── rejected.md
│   ├── questions/
│   │   ├── open.md
│   │   └── resolved.md
│   └── reviews/
│       ├── review-log.md
│       └── change-history.md
└── prompts/
    ├── expert-agent.md
    └── notebook-rules.md
```

## Section Purposes

### `profile/`
Stores information about the expert/user. This is personalization data.

Examples:
- Goals and long-term direction
- Preferences and priorities
- Constraints and limitations
- Relevant context

### `notebook/knowledge/`
Stores **trusted, distilled knowledge**—not raw research.

Examples:
- Concepts and principles
- Frameworks and methodologies
- Evidence summaries
- Domain-specific glossary

### `notebook/decisions/`
Stores **current conclusions** and chosen strategies.

The Expert Agent should read this section before giving recommendations.

Examples:
- Chosen strategy or approach
- Recommended workflow
- Preferred methodology

### `notebook/updates/`
**Staging area for proposed changes.**

New findings never directly modify trusted knowledge. Everything enters here first. The Expert Agent reviews updates before promoting them into knowledge or decisions.

Examples:
- New research findings
- Contradictions to existing beliefs
- Proposed strategy changes

### `notebook/questions/`
Stores **uncertainty and gaps** to make them visible.

Examples:
- Unresolved debates
- Missing information
- Research gaps
- Areas needing further investigation

### `notebook/reviews/`
Stores **notebook maintenance history** for transparency.

Examples:
- Why decisions changed
- What knowledge was updated
- Review timestamps and agent notes

### `prompts/`
Stores **instructions and rules** for the Expert Agent.

- `expert-agent.md`: System prompt for the agent
- `notebook-rules.md`: Governance rules

## Notebook Rules

1. Knowledge is **not a dump of information.**
2. **Decisions are more important than knowledge.**
3. **Updates must be reviewed** before becoming trusted.
4. **Every important decision should include rationale.**
5. The notebook should become **smaller and clearer over time.**
6. **Duplicate information should be merged.**
7. **Contradictions should be surfaced,** not hidden.
8. The notebook exists to **improve decision quality.**
9. The notebook exists **for the Expert Agent.**
10. The notebook is a **living knowledge base,** not a chat history.

## Design Constraint

> Every markdown file should remain human-readable and agent-readable without requiring a database, vector store, or proprietary platform.

This ensures portability and long-term maintainability.

## Designed For

* Expert AI Agents
* Personal Advisors
* Research Assistants
* Domain Specialists
* Long-Term Knowledge Systems

---

**The notebook is not a memory dump. It is an operating system for expertise.**
