# Causal Validation

## Why Final Outcome Comparison Is Not Enough

Two independent Agent runs can differ because of sampling, environment state, or recovery opportunity. A final score alone cannot show whether an Intervention changed the Recovery trajectory or whether the apparent improvement arose before Treatment.

## Comparison Unit

The public comparison unit is a matched pair in the **Strong Mechanism Attribution and Corrective Optimization Validation**: one Generic Recovery branch and one Pro-Evo Treatment branch begin at the same opaque Pre-revision Checkpoint.

## Pre-Revision Checkpoint

The Checkpoint is placed before the critical corrective revision. This ordering matters: Treatment precedes the observable behavioral divergence, Corrective Revision, Public Reverification, Target Resolution, and Verified Completion recorded in the treatment trajectory.

## What Is Frozen Before Branching

Under the frozen protocol, the pair holds constant the Workspace, conversation / Execution history, budget, Tool availability, Public Verifier, environment, model / Provider pre-treatment state, and Checkpoint identity. The release provides opaque identity rather than private state dumps.

## What Differs After Branching

The post-checkpoint Intervention differs. Both branches may perform Workspace Revision. The public comparison asks whether the Treatment branch follows a target-linked observable trajectory through Public Reverification and verified resolution.

## Observable Behavioral Attribution

Attribution uses observable evidence: treatment timing, public Tool Calls and results, Workspace Revisions, Public Verifier events, Public Reverification, Target Resolution, and Verified Completion. It does not infer mechanism from hidden reasoning.

## Outcome-Level Causal Validation

An earlier frozen comparison found G Verified Completion = 0/3 and T Verified Completion = 3/3. This establishes an outcome-level Causal Effect under that protocol. Behavioral Attribution remains **MODERATE** because the critical revision was already present in the shared pre-treatment prefix; strong revision-level attribution was not yet established.

## Strong Mechanism Attribution

In the final public validation, the Checkpoint is pre-revision and Treatment precedes divergence. Generic Recovery still revised the Workspace in 3/3 comparisons, yet reached 0/3 Target Resolution and 0/3 Verified Completion. Treatment reached 3/3 for both metrics and exposed 3/3 complete Mechanism chains. This supports strong Mechanism Attribution under the frozen condition.

## Public-Only Inference

The public replay is based on sanitized evidence projections and their Hash-bound provenance. It does not require raw Provider response bodies, private task source, expected patches, hidden tests, or a hidden Oracle.

## Why Private CoT Is Not Required

Pro-Evo does not rely on Private CoT to establish the Optimization mechanism. Assistant-visible text may be recorded where safe, but private hidden reasoning is not the core inference source. The causal claim rests on public timing and observable behavior, then Public Reverification.

## Scope and Limitations

This is a strong causal Proof-of-concept under a small, frozen experimental condition. It does not establish universal improvement, cross-model or cross-Benchmark generalization, production effectiveness, or population-level superiority. See [Limitations](limitations.md) and [Claim Boundary](../CLAIM_BOUNDARY.md).
