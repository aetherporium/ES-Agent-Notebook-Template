# Example: Expert Notebook for AI Agent Architecture

This is a realistic example of what a populated Expert Notebook looks like for someone building AI agent systems.

> **Note:** This is an example. Delete this file and populate your own when you fork the template.

---

## profile/goals.md (Example)

### Primary Goals

- Build production-grade AI agent systems that improve over time
- Maintain clear decision boundaries as agent complexity increases
- Create a knowledge base that both humans and agents can reliably query
- Establish patterns for when to expand vs. when to simplify

### Success Metrics

- Agents successfully reference notebook without external context
- Decision turnaround time reduces each quarter
- Zero contradictions between active decisions and recent updates
- Notebook grows in clarity, not just size

### Time Horizon

**Short-term (0-3 months):**
- Establish core concepts for agent architecture
- Document first 3 active decisions
- Set up review cadence

**Medium-term (3-12 months):**
- Expand to 10+ documented concepts
- Build agent interaction patterns
- Consolidate learnings into frameworks

**Long-term (1+ years):**
- Notebook becomes the source of truth for agent behavior
- Reduces onboarding time for new agents by 80%

---

## notebook/knowledge/concepts.md (Example)

### Agent Memory Architecture

**Definition:** The decision framework for what an agent remembers, forgets, and recalculates.

**Why It Matters:** Bad memory architecture causes agents to either hallucinate context or fail to learn from experience.

**Key Insights:**
- Not all information should be remembered (noise reduction)
- Short-term vs. long-term memory need different refresh rates
- Vector stores can hide decision logic; markdown notebooks are more transparent

**Related Concepts:**
- [Knowledge Distillation](./glossary.md)
- [Agent State Management](./frameworks.md)

**Evidence:**
- OpenAI's memory patterns in GPT agents (2024)
- Our Q4 experiment with stateless vs. stateful agents showed 40% improvement in consistency

---

## notebook/decisions/active.md (Example)

### Decision 1: Markdown-First Knowledge Storage

**What Was Decided:**
All agent knowledge goes in markdown notebooks first. Vector stores are secondary, for speed only.

**Why This Was Chosen:**
- Humans can audit agent knowledge instantly
- No vendor lock-in
- Contradictions are visible (not hidden in embeddings)
- Agents can reference exact sources

**How It Works:**
1. New knowledge enters as markdown
2. Agents parse markdown for semantic meaning
3. Vector store optionally mirrors for performance
4. Truth lives in markdown, always

**Owner/Accountable:**
Engineering lead

**Status:**
Active (since Feb 2026)

**Next Review:**
August 2026

---

### Decision 2: Async Review Workflow

**What Was Decided:**
All agent behavior changes go through a 24-48 hour review cycle before deployment.

**Why This Was Chosen:**
- Catches edge cases humans miss
- Prevents rapid oscillation in agent behavior
- Creates audit trail

**How It Works:**
1. Change submitted to `updates/pending.md`
2. Agents + humans review async
3. Flag concerns or request tests
4. Promote to `updates/accepted.md`
5. Deploy

**Owner/Accountable:**
Product lead

**Status:**
Active (since Jan 2026)

**Next Review:**
September 2026

---

## notebook/updates/pending.md (Example)

### Update 1: Evidence for Semantic Pruning

**What's Proposed:**
Add new framework: "Semantic Pruning" - the practice of removing redundant knowledge that confuses agent decisions.

**Type:**
New knowledge + framework

**Why Now:**
We observed agents getting confused when multiple files said similar things. This framework would let us consolidate systematically.

**Evidence/Source:**
- Internal observation from October sprint
- Reduced agent confidence scores when duplicate concepts existed
- Prompted by Q4 review of notebook growth rate

**Impact If Accepted:**
- Monthly consolidation task becomes standard
- Agents will make 5-15% fewer uncertain queries

**Impact If Rejected:**
- Notebook continues to grow without bounds
- Future reviews become harder

**Flagged Issues:**
None currently. But we should test consolidation on non-critical concepts first.

**Status:**
Awaiting Review

**Reviewer Notes:**
- Engineering: "Agree. Let's pilot on glossary.md first." (Nov 15)
- Product: "Pending final review" (Nov 18)

---

## notebook/questions/open.md (Example)

### Question 1: How Should Agents Handle Conflicting Evidence?

**The Question:**
When the notebook contains two contradictory pieces of evidence, how should an agent decide which to trust?

**Why It Matters:**
Directly affects recommendation quality. Wrong answer = confused agents or bad advice.

**Current Thinking:**
Best guess: Agents should flag the contradiction and ask for clarification rather than choosing. But we're not sure if this scales.

**What Would Answer It:**
A/B test with two approaches:
- Agent chooses (based on timestamp or confidence)
- Agent flags contradiction and requests decision

**Priority:**
High (blocks recommendation confidence)

**Assigned To:**
Research team

**Status:**
In Progress (running experiment)

---

## notebook/reviews/review-log.md (Example)

### Review Cycle: October 2026

**Date:** October 15-18, 2026

**Reviewer/Agent:** Engineering team + Claude agent

**Focus Areas:**
- Knowledge completeness
- Decision consistency
- Update backlog

**Key Findings:**
- 12 updates awaiting review (5 months old)
- 3 contradictions between decisions
- Knowledge section growing 15% per month (unsustainable)

**Actions Taken:**
- Promoted 8 updates to knowledge
- Rejected 2 (outdated)
- Created archival plan for 2 (needs future research)
- Scheduled consolidation sprint

**Updates Promoted:**
- Semantic pruning framework
- Agent state management patterns
- Async review workflow refinements

**Updates Rejected:**
- Vector-only storage (conflicts with active decision)
- Real-time memory sync (premature)

**Insights:**
Notebook is growing too fast. Need to be more aggressive about consolidating and removing. Also shows value of monthly reviews—backlog could have been months old.

---

> **This example section is meant to be deleted and replaced with your own content when you fork.**

> **It demonstrates:** realistic entries at various levels of detail, how links work, what "good" looks like, and the actual format/style of the notebook in use.
