# Pro-Evo

## Process-Aware Agent Evaluation and Reliability Optimization

**Open Core and Public Evidence Release**

> **Language:** [English](README.md) · [简体中文](README.zh-CN.md)

> **Public-release boundary.** This is not the complete Pro-Evo implementation. It publishes selected Open Core abstractions, reproducible Public Evidence, methodology, Offline Replay, and reference examples. The full research Runtime, production experiment infrastructure, private Benchmark assets, Provider integrations, and Hidden Evaluator infrastructure are not included or licensed.

Pro-Evo is an evidence-driven framework for process-aware Agent Evaluation, Reliability diagnosis, Optimization Target discovery, and causally validated Reliability Optimization. It asks not only whether an Agent succeeded, but what observable Execution evidence explains failure and recovery, whether an Intervention changed the recovery trajectory, and whether that change survives Causal Validation.

## Why Pro-Evo

`Final success != reliable execution.` Traditional Agent Evaluation usually follows `Task → Agent → Final Score`. It can answer “did the task succeed?” but generally cannot audit why an Agent failed, how it recovered, whether recovery used observed failure evidence, or whether an Intervention changed recovery behavior rather than reflecting independent sampling variation.

Pro-Evo follows:

`Execution → Process Evidence → Reliability Diagnosis → Optimization Target → Targeted Intervention → Causal Validation → Reliability Optimization`

![Evaluation to Optimization](figures/evaluation-to-optimization.svg)

The figure separates a final-outcome score from the evidence-bearing path that leads to an Optimization decision. It is a method model, not a diagram of the private production Runtime.

## How to Read This Repository

1. Start with the strong causal result below.
2. Read the Evaluation-to-Optimization model.
3. Inspect the Same-checkpoint Causal Validation design.
4. Follow the scientific progression from a Null Result to strong Mechanism Attribution.
5. Replay the Public Evidence locally.
6. Inspect the Open Core / private boundary and claim limitations.

## Strong Mechanism Attribution and Corrective Optimization Validation

Under three prospectively frozen, Same-checkpoint **pre-revision** comparisons, Pro-Evo Treatment produced complete target-linked recovery chains in all three Treatment branches. Both branches performed Workspace Revision. The causal distinction is not whether a revision happened: Treatment produced a target-linked post-treatment recovery trajectory that continued through Public Reverification, Target Resolution, and Verified Completion.

| Frozen Same-checkpoint comparison | Generic Recovery (G) | Pro-Evo Treatment (T) |
| --- | ---: | ---: |
| Matched pre-revision Checkpoints | 3 | 3 |
| Workspace Revision | 3/3 | 3/3 |
| Target Resolution | 0/3 | 3/3 |
| Verified Completion | 0/3 | 3/3 |
| Strong Mechanism Attribution | 0/3 | 3/3 |
| Complete Mechanism Chain | 0/3 | 3/3 |

![Strong Mechanism Attribution result](figures/strong-mechanism-result.svg)

## Same-Checkpoint Causal Validation

Each matched pair begins from the same opaque Pre-revision Checkpoint. Before branching, the frozen protocol holds constant the Workspace, conversation / Execution history, budget, Tool availability, Public Verifier, environment, model / Provider pre-treatment state, and Checkpoint identity. What changes is the post-checkpoint Intervention.

This supports interpretation of observable post-treatment behavioral divergence as a treatment Causal Effect under the frozen protocol—not as a guarantee that every possible confounder is eliminated or that results generalize beyond this study.

![Same-checkpoint Causal Design](figures/same-checkpoint-causal-design.svg)

For the detailed comparison unit, see [Causal Validation](docs/causal-validation.md). The [Strong Mechanism Evidence](evidence/gate22/) remains linked through its immutable Public Evidence path.

## Initial Target-Guided Recovery Validation: A Null Result

The initial Target-Guided Recovery validation is deliberately public: Generic Recovery and Treatment both achieved **2/2 effective recovery**, so the observed effect was **0**. Its public diagnosis is `INTERVENTION_INFORMATION_REDUNDANT`, `GENERIC_RECOVERY_ALREADY_SUFFICIENT`, and `TASK_DIFFICULTY_CEILING`.

This result was not discarded, rerun until positive, or retroactively redefined. The sequence was Null Result → Mechanism Diagnosis → prospective redesign → refrozen validation. That record is central to the project’s Research Integrity.

## Outcome-Level Causal Optimization Validation

The next frozen comparison established an outcome difference: Generic Recovery reached **0/3 Verified Completion** and Pro-Evo Treatment reached **3/3 Verified Completion**. Outcome-level Causal Effect is therefore established under that protocol.

Its Behavioral Attribution is **MODERATE**, not strong. The critical Workspace Revision already existed in the shared pre-treatment prefix, so this comparison does not support strong revision-level Mechanism Attribution. That identified weakness motivated the pre-revision Checkpoint design used in the final validation.

## From a Null Result to Corrective Optimization

![Scientific progression](figures/scientific-progression.svg)

The final validation moves the Checkpoint to the pre-revision state. Treatment then precedes observable inspection and Tool divergence, Corrective Revision, Public Reverification, Target Resolution, and Verified Completion—forming **3/3 complete Mechanism chains**.

## Open Core and Public Evidence Boundary

The release is designed for methodological auditability, evidence auditability, and Offline Replay—not full-system reproducibility. It publishes typed schemas, Process Event projections, target/intervention abstractions, minimal causal comparison utilities, sanitized traces, manifests, Hashes, and documentation. It excludes the private production Runtime, Provider infrastructure, private Benchmark assets, Hidden Evaluator, raw Provider responses, Private CoT, and company/internal assets.

![Public / Private Boundary](figures/public-private-boundary.svg)

The [Architecture](docs/architecture.md) explains the public method layers; [PUBLIC_RELEASE_SCOPE.md](PUBLIC_RELEASE_SCOPE.md) and [LICENSE.md](LICENSE.md) define the release and license boundaries.

## Replay the Public Evidence

No Provider credential or network access is required.

```bash
python -m pytest -q
python examples/evidence-replay/run.py
```

The deterministic Offline Replay loads only sanitized Public Evidence and recomputes: 3 matched pairs; G Target Resolution / Verified Completion = 0/3; T Target Resolution / Verified Completion = 3/3; Strong Mechanism Attribution = 3/3; `public_only = true`; `private_cot_used = false`.

## Research Integrity and Scope Note

Current evidence supports a **strong causal Proof-of-concept under the frozen experimental condition**. It does **not** establish universal Agent improvement, cross-model or cross-Benchmark generalization, production deployment effectiveness, industry-wide SOTA, or statistical population-level superiority.

Public inference does not require Private CoT. It uses treatment timing, public Tool Calls and results, Workspace Revisions, Public Verifier events, Public Reverification, Target Resolution, and Verified Completion. See [Research Integrity](docs/research-integrity.md), [Limitations](docs/limitations.md), [Evidence Guide](docs/evidence-guide.md), [FAQ](docs/faq.md), and [Claim Boundary](CLAIM_BOUNDARY.md).

## License

This is an Open Core and Public Evidence Release. Explicit Open Core software is Apache-2.0; original documentation is CC BY-NC 4.0; sanitized Public Evidence and experimental-result figures are CC BY-NC-ND 4.0. See [LICENSE.md](LICENSE.md) for path-scoped terms.

## Citation

No public author identity is asserted in this release. Citation metadata requires an approved public identity.
