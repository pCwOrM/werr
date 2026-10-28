#!/usr/bin/env node
/**
 * WERR (Wave-Error-Recurse) Cross-Runtime CLI Benchmark
 * Node.js & Bun Zero-Dependency Pure JavaScript Benchmark Runner
 *
 * Evaluates cognitive reflex decision routing over 1,000 synthetic state vectors
 * with microsecond precision using standard performance.now().
 * Strict air-gap: Zero external npm dependencies.
 */

const { performance } = require('perf_hooks');

// Canonical 24-byte coordinate seed for standard WERR baseline
const DEFAULT_SEED = {
  cr: -0.74364388703715870475,
  ci: 0.13182590420531197049,
  maxIter: 64,
  threshold: 4.0
};

/**
 * Procedural WERR escape boundary evaluation (Zero-Memory Decision Kernel)
 * @param {number} cr - Real state coordinate
 * @param {number} ci - Imaginary state coordinate
 * @param {number} maxIter - Recursive boundary iteration depth
 * @returns {number} Escape iteration count
 */
function escapeCount(cr, ci, maxIter = 64) {
  let zr = 0.0;
  let zi = 0.0;
  let n = 0;
  while (n < maxIter && (zr * zr + zi * zi) <= 4.0) {
    const nextZr = zr * zr - zi * zi + cr;
    zi = 2.0 * zr * zi + ci;
    zr = nextZr;
    n++;
  }
  return n;
}

/**
 * Evaluate deterministic reflex decision
 * @param {Object} state - State vector { risk, latency_budget, load_factor }
 * @returns {Object} Decision result
 */
function evaluateReflex(state) {
  const normRisk = Math.max(-1.0, Math.min(1.0, state.risk || 0.0));
  const normLoad = Math.max(0.0, Math.min(2.0, state.load_factor || 1.0));
  const cr = DEFAULT_SEED.cr + (normRisk * 0.05);
  const ci = DEFAULT_SEED.ci + ((normLoad - 1.0) * 0.05);

  const iters = escapeCount(cr, ci, DEFAULT_SEED.maxIter);
  const noulProb = iters / DEFAULT_SEED.maxIter;
  const isAllowed = noulProb < 0.65;

  return {
    allowed: isAllowed,
    noul_probability: noulProb,
    escape_depth: iters,
    action: isAllowed ? 'PERMIT' : 'REVERT'
  };
}

function runBenchmark(numIterations = 1000) {
  console.log('================================================================');
  console.log('  ⚡ WERR Decision Engine — Node.js & Bun CLI Benchmark');
  console.log(`  Runtime: Node.js ${process.version} (${process.platform}-${process.arch})`);
  console.log(`  Iterations: ${numIterations.toLocaleString()} synthetic evaluations`);
  console.log('================================================================\n');

  // Warmup run (100 iterations)
  for (let i = 0; i < 100; i++) {
    evaluateReflex({ risk: (i % 20) / 10 - 1.0, load_factor: 1.0 });
  }

  const latenciesUs = new Float64Array(numIterations);
  let permits = 0;
  let reverts = 0;

  const totalStart = performance.now();

  for (let i = 0; i < numIterations; i++) {
    const risk = Math.sin(i * 0.015);
    const load = 0.8 + 0.4 * Math.cos(i * 0.02);

    const t0 = performance.now();
    const result = evaluateReflex({ risk, load_factor: load });
    const t1 = performance.now();

    latenciesUs[i] = (t1 - t0) * 1000.0; // convert ms to microseconds
    if (result.allowed) permits++; else reverts++;
  }

  const totalDurationMs = performance.now() - totalStart;

  // Compute percentile statistics
  const sorted = Array.from(latenciesUs).sort((a, b) => a - b);
  const sum = sorted.reduce((acc, v) => acc + v, 0);
  const mean = sum / sorted.length;
  const p50 = sorted[Math.floor(sorted.length * 0.50)];
  const p90 = sorted[Math.floor(sorted.length * 0.90)];
  const p95 = sorted[Math.floor(sorted.length * 0.95)];
  const p99 = sorted[Math.floor(sorted.length * 0.99)];
  const min = sorted[0];
  const max = sorted[sorted.length - 1];

  const throughput = Math.round((numIterations / totalDurationMs) * 1000);

  // Render ASCII summary table
  console.log('+----------------------------------+-----------------------+');
  console.log('| Metric                           | Value                 |');
  console.log('+----------------------------------+-----------------------+');
  console.log(`| Total Decisions Evaluated        | ${numIterations.toString().padEnd(21)} |`);
  console.log(`| Total Wallclock Duration         | ${(totalDurationMs.toFixed(2) + ' ms').padEnd(21)} |`);
  console.log(`| Throughput                       | ${(throughput.toLocaleString() + ' ops/sec').padEnd(21)} |`);
  console.log(`| VRAM / Model Weight Footprint    | 0 Bytes (Seed-only)   |`);
  console.log('+----------------------------------+-----------------------+');
  console.log(`| Latency Min                      | ${(min.toFixed(2) + ' µs').padEnd(21)} |`);
  console.log(`| Latency Mean                     | ${(mean.toFixed(2) + ' µs').padEnd(21)} |`);
  console.log(`| Latency p50 (Median)             | ${(p50.toFixed(2) + ' µs').padEnd(21)} |`);
  console.log(`| Latency p90                      | ${(p90.toFixed(2) + ' µs').padEnd(21)} |`);
  console.log(`| Latency p95                      | ${(p95.toFixed(2) + ' µs').padEnd(21)} |`);
  console.log(`| Latency p99                      | ${(p99.toFixed(2) + ' µs').padEnd(21)} |`);
  console.log(`| Latency Max                      | ${(max.toFixed(2) + ' µs').padEnd(21)} |`);
  console.log('+----------------------------------+-----------------------+');
  console.log(`| Distribution: PERMIT / REVERT    | ${permits} / ${reverts}`.padEnd(59) + ' |');
  console.log('+----------------------------------+-----------------------+\n');
  console.log('✅ Benchmark completed successfully with 0 external dependencies.\n');
}

if (require.main === module) {
  const count = parseInt(process.argv[2], 10) || 1000;
  runBenchmark(count);
}

module.exports = { escapeCount, evaluateReflex, runBenchmark };
