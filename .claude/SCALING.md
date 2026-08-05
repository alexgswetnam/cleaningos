# When to switch to the parallel commands

`/ingest-fast` and `/lint-fast` exist so you don't have to rediscover this later. They
are **not** upgrades. They're the right tool at a size the vault hasn't reached.

## The switch point

| Vault size | Use | Why |
|---|---|---|
| Under ~200 concepts | `/ingest`, `/lint-vault` | A subagent spends longer reading the Canon than it saves searching |
| Over ~200 concepts | `/ingest-fast`, `/lint-fast` | The duplication check is now the slow part |

Check with:

```bash
ls "03 Concepts" | wc -l
```

## The real signal

Page count is a proxy. The actual trigger is **`/ingest` spending most of its time in
Step 3**, hunting for existing pages. When that step stops feeling instant, switch.

For `/lint-vault`: switch when a full audit stops being something you wait for.

## Why subagents aren't free

Each one starts cold. It knows nothing — not your Canon, not your vocabulary, not what
the vault contains. Every scout has to read `CONSTITUTION.md` and often
`02 Canon/Language.md` before it can do anything useful.

That's a fixed cost per agent, paid every time. It's worth it when a scout then searches
400 pages. It's pure waste when there are 30.

## The risk parallelism introduces

Scouts search in isolation, so two can independently return **NEW** for one concept under
two names — and you've created the exact duplicate the check exists to prevent.

`/ingest-fast` Step 4 closes this with a cross-check of every NEW verdict against the
others' `NEAREST` field. **Never skip it.** Without that step the parallel version is
strictly worse than the sequential one: faster at producing the one error the vault
can't absorb.

## What is never parallelised

- **Writing.** The orchestrator does every write, sequentially. Concurrent writes mean
  git conflicts and race conditions.
- **`/draft`.** Copy needs one mind holding the whole piece. Split it and the hook and
  the close sound like different people.
- **`/reconcile`.** Needs Alex's judgment; parallelism buys nothing.
- **Canon decisions.** Always Alex.

## The agents

`.claude/agents/dedupe-scout.md` — one idea in, one verdict out. Read-only.
`.claude/agents/vault-auditor.md` — one audit dimension, compact report. Read-only.

Both are read-only **by design**, not by oversight. It's the structural guarantee that
parallel agents can't corrupt the vault.
