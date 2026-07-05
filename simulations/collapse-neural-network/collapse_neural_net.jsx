import { useMemo, useState } from "react";

// Compact reference prototype derived from the thread demo.
// Status: toy visualization / concept scaffold, not empirical validation.

function memoryKernel(spatialDist, timeDelta, scale = 1.0) {
  const A = scale * 1.2;
  const lambdaS = 80 + scale * 40;
  const tauS = 3500 + scale * 2000;
  const omegaS = 0.0018 * scale;

  if (timeDelta <= 0) return 0;

  return (
    A *
    Math.exp(-spatialDist / lambdaS) *
    Math.exp(-timeDelta / tauS) *
    Math.cos(omegaS * timeDelta)
  );
}

function createNode(id, x, y, layer, scale = 1) {
  return {
    id,
    x,
    y,
    layer,
    scale,
    threshold: 0.72 + Math.random() * 0.18,
    memoryField: 0,
    potential: 0,
    collapseHistory: [],
    resonancePhase: Math.random() * Math.PI * 2,
    spinState: Math.random() > 0.5 ? 1 : -1,
    dimensionalLayer: Math.floor(Math.random() * 3) + 3,
  };
}

function buildNetwork() {
  const layerCounts = [3, 5, 5, 3];
  const layerX = [80, 220, 390, 540];
  const nodes = [];

  layerCounts.forEach((count, layer) => {
    for (let i = 0; i < count; i += 1) {
      const y = 70 + i * 58 + (5 - count) * 18;
      nodes.push(createNode(nodes.length, layerX[layer], y, layer, 0.6 + layer * 0.15));
    }
  });

  return nodes;
}

function stepNetwork(nodes, now) {
  const next = nodes.map((node) => ({ ...node, collapseHistory: [...node.collapseHistory] }));

  next.forEach((target) => {
    let memoryField = 0;

    next.forEach((source) => {
      if (source.id === target.id) return;
      const dx = target.x - source.x;
      const dy = target.y - source.y;
      const dist = Math.sqrt(dx * dx + dy * dy);

      source.collapseHistory.forEach((event) => {
        memoryField += memoryKernel(dist, now - event.time, source.scale) * event.weight;
      });
    });

    const spinMod = target.spinState * 0.04 * Math.sin(now * 0.0008 + target.resonancePhase);
    const dimShift = Math.cos(now * 0.0003 * target.dimensionalLayer + target.resonancePhase);

    target.memoryField = memoryField;
    target.potential = Math.min(1, Math.max(0, memoryField * 0.38 + spinMod * 0.12 + dimShift * 0.05));

    if (target.potential >= target.threshold) {
      target.collapseHistory.push({ time: now, weight: target.potential });
      target.collapseHistory = target.collapseHistory.slice(-12);
    }
  });

  return next;
}

export default function CollapseNeuralNetReference() {
  const initialNodes = useMemo(() => buildNetwork(), []);
  const [nodes, setNodes] = useState(initialNodes);
  const [time, setTime] = useState(0);

  const injectInput = (id) => {
    setNodes((prev) =>
      prev.map((node) =>
        node.id === id
          ? {
              ...node,
              collapseHistory: [...node.collapseHistory, { time, weight: 1 }].slice(-12),
            }
          : node
      )
    );
  };

  const tick = () => {
    const now = time + 250;
    setTime(now);
    setNodes((prev) => stepNetwork(prev, now));
  };

  return (
    <div style={{ background: "#050c14", color: "#7ab3d4", padding: 24, fontFamily: "monospace" }}>
      <h1>Collapse Neural Network — Reference Prototype</h1>
      <p>K(r, tau, s) = A(s) exp(-r/lambda_s) exp(-tau/tau_s) cos(omega_s tau)</p>
      <p>t = {time} ms</p>
      <button onClick={tick}>step field</button>
      <button onClick={() => setNodes(buildNetwork())}>reset</button>
      <div style={{ marginTop: 16 }}>
        {nodes.map((node) => (
          <button
            key={node.id}
            onClick={() => injectInput(node.id)}
            style={{
              margin: 4,
              padding: 8,
              color: node.potential > node.threshold ? "#00ffcc" : "#4a9eff",
              background: "#07111f",
              border: "1px solid #123456",
            }}
          >
            N{node.id} L{node.layer} d{node.dimensionalLayer} M={node.memoryField.toFixed(2)} P={node.potential.toFixed(2)}
          </button>
        ))}
      </div>
    </div>
  );
}
