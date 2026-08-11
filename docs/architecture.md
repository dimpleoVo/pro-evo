# Architecture

The public architecture has five minimal layers: public trace schema, process-event projection, optimization-target abstraction, same-checkpoint pair representation, and offline causal aggregation. A trace event is intentionally limited to an opaque event ID, order, kind, and safe projection. The replay layer reads only JSON evidence and uses no provider, shell, runtime controller, or hidden evaluator.

The architecture diagram represents a method boundary, not the private production topology.

