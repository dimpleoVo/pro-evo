# Pro-Evo

## Process-Aware Agent Evaluation and Reliability Optimization

**Open Core and Public Evidence Release**

> **语言：** [English](README.md) · [简体中文](README.zh-CN.md)

> **这不是完整的 Pro-Evo implementation。** 本仓库公开选定的 open-core abstractions、可复核的 public evidence、experiment methodology、offline evidence replay 与 reference examples。完整 research runtime、production experiment infrastructure、private benchmark assets、provider integrations 与 hidden evaluation infrastructure 均未开源。

## 为什么需要 Pro-Evo

最终成功（final success）不等于可靠执行（reliable execution）。传统 Agent Evaluation 通常只观察 `task → agent → final score`。Pro-Evo 将 execution trajectory 中可公开的 process evidence 纳入 Evaluation：

`execution → process evidence → reliability diagnosis → optimization target → targeted intervention → causal validation`

本项目不宣称对所有 agent 普遍有效；它检验的是：在冻结的 causal protocol 下，process-aware intervention 是否会改变一个预先定义、可观察的 recovery outcome。

## 从同一 pre-revision checkpoint 解析目标

在三组 prospectively frozen、same-checkpoint 的 **pre-revision** comparison 中，Pro-Evo process-aware intervention 在全部 treatment branch 里形成了完整的 target-linked recovery chain。Generic recovery control 同样会 revision workspace，但三组都没有解析目标（target）。

| Frozen same-checkpoint comparison | Generic recovery (G) | Pro-Evo treatment (T) |
| --- | ---: | ---: |
| Matched pre-revision checkpoints | 3 | 3 |
| Target resolution | 0/3 | 3/3 |
| Verified completion | 0/3 | 3/3 |
| Strong mechanism traces | 0/3 | 3/3 |

![Strong mechanism result](figures/gate22-causal-result.svg)

## Pro-Evo 评估什么

Pro-Evo 将 process trace 视为 evidence。它记录 public-safe process events，将 observable failure 映射为带有 observable success condition 的 optimization target，并检查 intervention 是否产生 target-linked behavior，随后完成 public reverification。open core 仅提供审计这一链条所需的数据 abstractions 与 deterministic analysis。

## 从 Evaluation 到 Optimization

![Evaluation to optimization](figures/evaluation-to-optimization.svg)

完整 architecture 见 [docs/architecture.md](docs/architecture.md)，public methodology 见 [docs/methodology.md](docs/methodology.md)。

## 以同一 checkpoint 进行 causal comparison

每个 matched pair 中，G 和 T 都从相同的 opaque pre-revision checkpoint 开始。这样在 branch decision 前固定 state，使 post-branch difference 可被审计。这并不证明广泛 generalization；它是在该 frozen condition 下的 causal proof-of-concept。

![Same-checkpoint causal design](figures/same-checkpoint.svg)

## 端到端追踪 recovery mechanism

三个 treatment branch 的 public projection 都包含完整链条：

`Public Failure → Process Diagnosis → Pre-revision Checkpoint → Same-checkpoint G/T → Target-guided Intervention → Observable Behavior Divergence → Post-treatment Corrective Revision → Public Reverification → Target Resolution → Verified Completion`

可查看 [public evidence](evidence/gate22/)、[G/T comparison](evidence/gate22/gt-comparison.md) 与 [evidence guide](docs/evidence-guide.md)。

## 保留 null result，并据此改进设计

Gate20 被完整保留：generic 与 treatment recovery 都为 2/2，effect 为零。evidence 记录了 information redundancy、generic recovery 已足够，以及 task difficulty ceiling。它展示的是严谨过程：null result → mechanism diagnosis → prospective redesign → refreeze → Gate21 / Gate22，而非重复运行直至获得正结果。

![Scientific progression](figures/scientific-progression.svg)

Gate21 同样公开且被正确限定：outcome result 很强（G verified 0/3；T verified 3/3），但 behavioral attribution 为 **MODERATE**，因为关键 revision 位于 shared pre-treatment prefix。后续 comparison 将 checkpoint 前移，专门解决这一 attribution weakness。

## Open Core 能做什么

open core 可加载 sanitized public trace、读取 process events、重建 optimization target abstraction、核验 same-checkpoint identity、计算 target resolution 与 verified completion、汇总 G/T effect，并运行 deterministic offline replay。它刻意不包含 provider execution、orchestration、production controller、benchmark runner、task source、hidden evaluator 或 deployment machinery。

## 复现 public demo

无需 provider credential，也无需网络访问：

```bash
python -m pytest -q
python examples/evidence-replay/run.py
```

预期 aggregate：3 个 matched pair；G 的 target resolution 与 verified completion 均为 0；T 均为 3；strong mechanism trace 为 3；`public_only = true`；`private_cot_used = false`。

## Research integrity 与范围限制

evidence 是 sanitization 后的 projection，而不是 raw artifact dump。解释结果前，请阅读 [research integrity](docs/research-integrity.md)、[limitations](docs/limitations.md)、[FAQ](docs/faq.md) 与 [Claim Boundary](CLAIM_BOUNDARY.md)。

## 未开源内容

完整 research runtime、production experiment infrastructure、provider adapter 与 account、benchmark corpus 与 task repository、private artifact、raw provider body、private reasoning、hidden test/evaluator、expected/reference patch、credential 及 internal/company asset 都不在本仓库中。

## License 与发布边界

本仓库是 **Open Core and Public Evidence Release**。明确列出的 Open Core software component 以 Apache License 2.0 公开；原创 documentation 使用 CC BY-NC 4.0；sanitized public research evidence 与 experiment-result figure 使用 CC BY-NC-ND 4.0。路径范围规则见 [LICENSE.md](LICENSE.md)。

完整 Pro-Evo research runtime、production experiment infrastructure、private benchmark asset、provider integration 与 hidden evaluation infrastructure 均未包含，也未授予任何 license。

## Citation

本 staging release 未声明作者公开身份。Citation metadata 需在获得批准的公开身份后再补充。
