# __The Gauge Extension of the Central Phase: Why the Centre Caps the Group__

## Introduction

The framework's continuous symmetry is the **central phase**, the group of central unitaries
$e^{i\theta}e_0\cong U(1)$. It is exact and it is global: being central, it multiplies every subspace and
every element by the same factor, so it acts the same way at every point, and the corpus records the fact as
the reading "centrality is globality". A gauge theory needs the opposite — a phase that may differ from
point to point, and a compensating connection that makes the difference covariant — and the question this
article states is what, exactly, blocks the locality and what a gauge extension of the framework would have
to be.

The article owns the statement of the **extension problem**, the reason the centre caps it, and the two
candidate readings. It owns no new theorem. The centre and its triviality are *The Centre of the Biquaternion
Algebra as the Classical Sector*; the ceiling $U(2)$ is *The Gauge Group Ceiling: Why the Biquaternion
Algebra Reaches SU(2) but Not SU(3)*; the generator is *The Central Rotation: Phase, Duality and the Wick
Rotation as One Generator*; the discrete charge the compact phase carries is *Particle Types, Discrete
Charge and Three-Particle Couplings*; and the placement of the gauge row among the products is *The Heat Map
of the Framework: Which Physics Hangs on Which Product*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$; the centre is
$Z(\mathbb{B})=\mathbb{C}_{\mathbb{B}}=\{z e_0\}$, of one complex (two real) dimensions; the unitary slice is
$U=\{\tilde{U}:\tilde{U}\tilde{U}^{*}=e_0\}\cong U(2)$.

## The Central Phase and the Gauge Principle

The central phase is the one-parameter subgroup $\theta\mapsto e^{i\theta}e_0$ of the centre. Three of its
properties are the whole of its relevance.

- It is **central**: $e^{i\theta}e_0$ commutes with every element, so it acts by the same scalar at every
  element and in every subspace.
- It is **compact**: the parameter is an angle and the group is a circle, so its irreducible labels are
  integers and the internal charge it carries is **discrete**.
- It is **the whole continuous symmetry of the algebra that acts uniformly**, because the centre is
  one-dimensional and every uniform continuous symmetry must be central.

The gauge principle asks for the local version: a phase $\theta(x)$ that depends on the point, and a
connection $\tilde{A}_\mu$ that transforms so that the covariant derivative
$\partial_\mu - iq\tilde{A}_\mu$ is phase-covariant. **The framework has the phase and not the connection**,
and the reason is structural rather than technical: a connection is a field valued in the Lie algebra of the
group, and the Lie algebra of the central phase is the one-dimensional span of $ie_0$, which is central. A
central generator produces a field that commutes with everything, so the "connection" it generates cannot
couple to anything and the covariant derivative collapses to the ordinary one. A gauged central phase is
therefore **no gauge theory at all**: an abelian gauge field needs a matter field that transforms
non-trivially, and the framework's matter lives in modules on which a central phase acts by a scalar.

## Why the Centre Caps the Group

The obstruction stated, the reason the gauge group stays at $U(2)$ follows. The intrinsic gauge group of the
algebra is the unitary slice $U=\{\tilde{U}:\tilde{U}\tilde{U}^{*}=e_0\}\cong U(2)$, the central product
$(SU(2)\times U(1))/\mathbb{Z}_2$, and the **abelian factor is exactly the central phase**. The structure of
the group is the structure of the centre:

| piece of the group | where it lives | what it does |
|---|---|---|
| $U(1)$ | the centre, $\{e^{i\theta}e_0\}$ | the global phase, the discrete charge label |
| $SU(2)$ | the unit quaternions, the real slice | the internal rotations acting on the module |
| $\mathbb{Z}_2$ | $\{\pm e_0\}$ | the identification, the spin double cover |

A larger group would need generators outside the centre and outside the real-quaternion triple, and there
are none: the anti-Hermitian sector of $\mathbb{B}$ has real dimension four, giving $\mathfrak{u}(2)$ exactly,
and the Cartan decomposition of that Lie algebra has the compact part $\mathfrak{u}(2)$ and no more. So the
ceiling is not a limit of the framework's ambitions but a computation of the algebra, and the route past it
is an enlarged carrier — $M_n(\mathbb{B})\cong M_{2n}(\mathbb{C})$, whose intrinsic gauge group is $U(2n)$
and which contains $SU(3)$ for $n\ge2$, as the ceiling article computes — and not a new reading of
$\mathbb{B}$. What the enlargement changes is the **algebra** and not its centre: every matrix algebra over
$\mathbb{C}$ has centre the scalars, so the additional generators are non-central, and it is their presence,
and not a larger centre, that carries the larger group. The centre's role is exact and it is narrower than it
may look: it is the whole of the algebra's **uniform** symmetry, so it fixes the abelian factor of the
intrinsic group at $U(1)$ and forbids a second uniform phase, and it does not by itself bound the group,
which is bounded by the dimension of the anti-Hermitian sector.

## The Two Candidate Readings

Two readings of the extension problem are consistent with the algebra, and the article states both and
chooses neither.

**Reading A — the central extension is the whole extension.** The gauge structure of the framework is the
central product $U(2)$ and nothing else, and the physically meaningful statement is that the framework's
gauge group is the extension of $SU(2)$ by the central phase. On this reading the framework is a
$U(2)$-gauge theory in which the abelian factor is the algebra's centre, hypercharge is the central phase and
weak isospin is the module action, and the ceiling is a result about the gauge group of the algebra rather
than a defect. The reading is the framework's own position and is labelled as a reading: the algebra fixes
the group and not the names of its factors.

**Reading B — the central phase is the trace of a local structure.** The gauge structure the framework
should carry is a **local** one, and the central phase is the shadow of a connection that the algebra does
not contain. On this reading the interesting object is the obstruction itself: a local phase gauge theory
requires a non-central generator, the algebra has none, and the minimal carrier on which the obstruction
lifts is the enlarged one. The reading makes the ceiling a **constructive programme** — which carrier, which
module, which connection — and it is the reading under which the grand-unification articles work.

The two readings are not contradictory: the first states what the framework **has**, the second what it
would **need**, and the article's position is that both are true and that the disagreement is about which
question is being asked.

## What Is Not Claimed

- The article does not claim that the central phase is **gaugeable** in the sense of producing a
  propagating abelian gauge field. It claims that the framework's continuous symmetry is the central phase
  and that the algebra supplies no non-central generator with which to localise it.
- It does not claim that the ceiling is **permanent**. The ceiling is a statement about $\mathbb{B}$; the
  enlarged carriers of the ceiling article pass it, and the price is stated there and not repeated here.
- It does not claim that the framework's $U(1)$ is the electromagnetic one. The identification of the
  central phase with hypercharge, with electric charge, or with a global phase of the state module is a
  reading of the framework and not a consequence of the algebra, and no experiment is proposed here.

## Physical Readings

- **The centre is the gauge group's abelian factor.** The reading is that the algebra's one continuous
  uniform symmetry is the abelian factor of its intrinsic gauge group, so a framework whose only
  uniform symmetry is a phase is a framework with a $U(1)$ factor and no more. Owner: *The Centre of the
  Biquaternion Algebra as the Classical Sector*.
- **Compactness is the discreteness of the charge.** The reading is that the charge carried by the central
  phase is discrete because the phase is a circle, which is the same mechanism as the compact group of the
  gauge ceiling. Owner: *Particle Types, Discrete Charge and Three-Particle Couplings*.
- **Non-centrality is non-locality's algebraic price.** The reading is that a local gauge symmetry costs a
  non-central generator, so the framework's globality is the price it pays for having a scalar centre, and
  the enlargement is the price it would pay to escape. Owners: *The Gauge Group Ceiling* and *Grand
  Unification and the Biquaternion Algebra Ceiling*.

## Summary

The framework's continuous symmetry is the central phase $e^{i\theta}e_0\cong U(1)$, central, compact and
global, and it is the whole of the algebra's uniform symmetry. Its gauge extension is blocked by centrality:
a local phase needs a connection valued in a non-central generator, the algebra's only uniform generator is
the central $ie_0$, and a central connection couples to nothing. The intrinsic gauge group is the unitary
slice $U(2)=(SU(2)\times U(1))/\mathbb{Z}_2$, whose abelian factor is the central phase and whose size is
fixed by the four-dimensional anti-Hermitian sector; a larger group requires an enlarged carrier with
non-central generators, not a larger centre. Two readings are stated and neither is chosen: that the central
extension is the whole extension, and that the central phase is the trace of a local structure the algebra
does not contain.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e^{i\theta}e_0$ | the central phase, the group $U(1)$ of central unitaries |
| $ie_0$ | the generator of the central phase, central and of one real dimension |
| $U=\{\tilde{U}:\tilde{U}\tilde{U}^{*}=e_0\}\cong U(2)$ | the unitary slice, the algebra's intrinsic gauge group |
| $(SU(2)\times U(1))/\mathbb{Z}_2$ | the structure of the slice, with the abelian factor the central phase |
| $\mathfrak{u}(2)$ | the anti-Hermitian sector of the algebra, the Lie algebra of the slice |

## Further Reading

- *The Centre of the Biquaternion Algebra as the Classical Sector*, for the computation of the centre, its
  five characterisations and its reading as the classical sector.
- *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)*, for the ceiling, the
  Cartan decomposition and the enlargements that pass it.
- *The Central Rotation: Phase, Duality and the Wick Rotation as One Generator*, for the central phase as
  one generator on six subspaces.
- *Particle Types, Discrete Charge and Three-Particle Couplings*, for the compact slice and the discrete
  charge.
- *Grand Unification and the Biquaternion Algebra Ceiling*, for the constructive reading of the obstruction.
