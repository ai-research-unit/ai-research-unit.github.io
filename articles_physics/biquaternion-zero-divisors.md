# __Biquaternion Zero Divisors__

## Introduction

This article studies the zero divisors of the biquaternion algebra $\mathbb{B}$: it characterises them, splits them into two families and describes their structure. It follows *Biquaternion Norm and Invertibility*, which established the invertibility criterion and the three-way classification of the elements of $\mathbb{B}$.

Physically, the zero divisors are the **null elements**, and the subject of this article is therefore the light-cone structure of the framework. A biquaternion is a zero divisor exactly when its norm form vanishes, and in the physical reading the norm form is the invariant that decides whether an element can be inverted: the units are the frames and the transformations, the null elements are the light rays. That the algebra is not a division algebra is not a defect of the framework but a precondition of it: a division algebra has no null elements, hence no light.

The zero divisors split into two families, and the split is the same one that organises the kinematics:

- the **pure** zero divisors, with vanishing scalar part, which square to zero: the **nilpotent** or **parabolic** elements, the null generators of the algebra's flow;
- the **non-pure** zero divisors, with nonzero scalar part, which are complex multiples of idempotents: a null element of this family is a **scaled projector**, and the normalised element is a pure state.

The article closes with the distribution of the zero divisors over the six distinguished subspaces — this is where the causal structure appears explicitly, as the double cones inside the two Hermitian sectors — and with the zero divisor set itself.

**Conventions.** The quaternion basis is $e_0 = 1,e_1,e_2,e_3$ and the scalar imaginary is $i$; a general element is $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The conjugations are $\bar{\tilde{Q}}$, $\tilde{Q}^*$ and $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$, the anti-Hermitian conjugate is $\tilde{Q}^\flat = -\tilde{Q}^\dagger$, and the norm form is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$. The material coordinate is $ict\,e_0+\mathbf{x}$ and the informational coordinate is $ct'\,e_0+i\mathbf{x}'$.

## Definition and Criterion

### Definition

A biquaternion $\tilde{Q}$ is a **zero divisor** if it is **nonzero** and there exists a **nonzero** $\tilde{R}$ with

$$
\tilde{Q}\circ\tilde{R} = 0 \quad\text{or}\quad \tilde{R}\circ\tilde{Q} = 0 .
$$

Both elements are required to be nonzero; in particular $\tilde{Q} = 0$ is not a zero divisor, although $0\circ\tilde{R} = 0$ for every $\tilde{R}$.

### Criterion

**Theorem.** A nonzero biquaternion $\tilde{Q}$ is a zero divisor if and only if $N(\tilde{Q}) = 0$.

**Proof.** If $\tilde{Q}\neq0$ and $N(\tilde{Q}) = 0$, then $\tilde{Q}\bar{\tilde{Q}} = 0$ and $\bar{\tilde{Q}}\neq0$, so $\tilde{R} = \bar{\tilde{Q}}$ witnesses the definition.

Conversely, if $\tilde{Q}\circ\tilde{R} = 0$ with $\tilde{R}\neq0$ and $N(\tilde{Q})\neq0$, then $\tilde{Q}$ is invertible and left multiplication by $\tilde{Q}^{-1}$ gives $\tilde{R} = 0$, a contradiction. $\square$

### The Three-Way Classification

Combining the invertibility criterion with the criterion above, the elements of $\mathbb{B}$ are partitioned into three classes:

| Condition on $N(\tilde{Q})$ | Condition on $\tilde{Q}$ | Conclusion |
|---|---|---|
| $N(\tilde{Q})\neq0$ | (automatically $\tilde{Q}\neq0$) | $\tilde{Q}$ is invertible |
| $N(\tilde{Q}) = 0$ | $\tilde{Q} = 0$ | $\tilde{Q}$ is the zero element |
| $N(\tilde{Q}) = 0$ | $\tilde{Q}\neq0$ | $\tilde{Q}$ is a zero divisor |

So the zero divisors are exactly the nonzero elements on which the norm form vanishes, and the units are exactly the elements on which it does not.

**Physical reading.** This is the framework's causal trichotomy stated algebraically. An element with $N\neq0$ can be inverted, rescaled and boosted: it is a frame. An element with $N = 0$ cannot: it is a light-like direction, and no rescaling of it is a frame. The unit group $\mathbb{B}^\times$ is where the framework's transformations live; the null cone is its boundary.

### The Algebra Is Not a Division Algebra

A **division algebra** is an algebra in which every nonzero element is invertible; for a finite-dimensional algebra this is equivalent to containing no zero divisors. Since $\mathbb{B}$ contains zero divisors, it is **not** a division algebra, in contrast with the Frobenius theorem, which states that the only finite-dimensional associative real division algebras are $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$.

**Physical reading.** The contrast with the Frobenius theorem is the algebraic statement of the existence of light. The quaternion algebra $\mathbb{H}_{\mathbb{B}}$ inside $\mathbb{B}$ is a division algebra and has no null elements at all: every nonzero real quaternion is invertible, as Section *Distribution of the Zero Divisors* confirms by showing that the subspace of real coefficients contains no zero divisors. Extending the coefficients from $\mathbb{R}$ to $\mathbb{C}$ — that is, allowing the imaginary unit into the coefficients — is what creates the null directions, and the null directions are the light cone.

## The Two Families of Zero Divisors

The zero divisors split into two families according to the scalar part $Q_0$, and the split is structural: it is the organising principle of the classification.

### The Pure Case

A biquaternion is **pure** if its scalar part vanishes: $\tilde{Q} = Q_1e_1+Q_2e_2+Q_3e_3$ with $Q_k\in\mathbb{C}$. The pure zero divisors are treated below.

### The Non-Pure Case

A biquaternion is **non-pure** if $\tilde{Q} = Q_0e_0+\mathbf{Q}$ with $Q_0\in\mathbb{C}$, $Q_0\neq0$. The non-pure zero divisors are treated below.

### Why the Scalar Part Is the Right Invariant

The scalar part is the natural invariant because $i$ is central in $\mathbb{B}$: the scalar part is the component in the central direction, the vector part the component perpendicular to it. The two cases are distinguished by whether this central component vanishes.

In the **pure** case the norm form reduces to the complex scalar

$$
N(\tilde{Q}) = (\mathbf{Q},\mathbf{Q}) = Q_1^2+Q_2^2+Q_3^2 ,
$$

whose vanishing is the nilpotent condition. In the **non-pure** case the norm form carries the scalar contribution in addition,

$$
N(\tilde{Q}) = Q_0^2+(\mathbf{Q},\mathbf{Q}) ,
$$

and the vanishing condition allows the scalar and vector contributions to cancel; the resulting solutions are the complex multiples of the idempotents.

**Physical reading.** The two families are the two ways an element can be null. The pure family is null by having no scalar component at all: its two parts cannot cancel, and it is the parabolic case of the generator trichotomy of *Biquaternion Roots of Minus One* — $\xi^2 = 0$, a nilpotent. The non-pure family is null by cancellation between a timelike and a spacelike contribution: that is the familiar light-cone condition, and this is the family to which a photon's momentum belongs.

## Pure Zero Divisors

### The Square of a Pure Biquaternion

For pure $\tilde{Q}$, using the product formula for two pure biquaternions and the antisymmetry of $\epsilon_{jkl}$ against the symmetric $Q_jQ_k$,

$$
\tilde{Q}^2 = -\Big(\sum_{k=1}^{3}Q_k^2\Big)e_0 = -N(\tilde{Q})\,e_0 ,
$$

so the square of a pure element is the scalar $-N(\tilde{Q})$.

### The Criterion

**Theorem.** For a nonzero pure $\tilde{Q}$, the following are equivalent:

1. $\tilde{Q}$ is a zero divisor;
2. $N(\tilde{Q}) = 0$, i.e. $Q_1^2+Q_2^2+Q_3^2 = 0$;
3. $\tilde{Q}^2 = 0$.

**Proof.** (1) $\iff$ (2) is the general criterion, and (2) $\iff$ (3) is the computation of the square. $\square$

A biquaternion with $\tilde{Q}^2 = 0$ is a **nilpotent**, so in the pure case the zero divisors are exactly the nonzero nilpotents.

### Properties

A pure zero divisor $\tilde{Q}$ satisfies:

- **self-annihilation**, $\tilde{Q}\circ\tilde{Q} = 0$: the annihilator contains $\tilde{Q}$, hence the whole complex line spanned by $\tilde{Q}$;
- **non-invertibility**: $\tilde{Q}$ has no inverse;
- **purity is preserved** under squaring.

**Physical reading.** A pure null element is a **parabolic generator**: nilpotent, with $\exp(\theta\tilde{Q}) = e_0+\theta\tilde{Q}$, and its own annihilator. It is the degenerate member of the generator trichotomy, and it is the reason the parabolic case sits apart from the elliptic and hyperbolic ones: it is not a unit, so it generates its flow in the algebra but not in the group of units of the polar decomposition.

## Non-Pure Zero Divisors

### The Square of a Non-Pure Biquaternion

For $\tilde{Q} = Q_0e_0+\mathbf{Q}$ with $Q_0\neq0$,

$$
\tilde{Q}^2 = \big(Q_0^2-(\mathbf{Q},\mathbf{Q})\big)e_0+2Q_0\mathbf{Q} .
$$

### The Relation to the Norm Form

Since $N(\tilde{Q}) = Q_0^2+(\mathbf{Q},\mathbf{Q})$, the condition $N(\tilde{Q}) = 0$ is $(\mathbf{Q},\mathbf{Q}) = -Q_0^2$; substituting,

$$
\tilde{Q}^2 = 2Q_0^2e_0+2Q_0\mathbf{Q} = 2Q_0\tilde{Q} .
$$

So every non-pure zero divisor satisfies $\tilde{Q}^2 = 2Q_0\tilde{Q}$: its square is a complex multiple of itself, with multiplier twice the scalar part.

### The Associated Idempotent

Dividing by the nonzero $2Q_0$,

$$
\tilde{P} = \frac{\tilde{Q}}{2Q_0}, \qquad \tilde{P}^2 = \frac{2Q_0\tilde{Q}}{4Q_0^2} = \tilde{P} ,
$$

so $\tilde{P}$ is an **idempotent** and $\tilde{Q} = 2Q_0\tilde{P}$: **every non-pure zero divisor is a complex multiple of an idempotent**. The idempotents themselves — their classification, their bijection with the roots of $-1$ and the dimension of the set they form — are the subject of *Biquaternion Idempotents and Projections*.

### Properties

A non-pure zero divisor $\tilde{Q}$ satisfies:

- **form** $\tilde{Q} = 2Q_0\tilde{P}$ with $\tilde{P}$ idempotent;
- **square** $\tilde{Q}^2 = 2Q_0\tilde{Q}$;
- **non-invertibility**;
- **nontrivial annihilator**: the element $\tilde{Q}-2Q_0e_0 = 2Q_0(\tilde{P}-e_0)$ is annihilated by $\tilde{Q}$ on both sides, since

$$
\tilde{Q}\circ(\tilde{Q}-2Q_0e_0) = \tilde{Q}^2-2Q_0\tilde{Q} = 0 ,
$$

and likewise on the left.

**Physical reading: the photon.** A massless particle's momentum is the case in point. In the material coordinate the momentum of a photon is $\tilde{P} = i(E/c)e_0+\mathbf{p}$ with $|\mathbf{p}| = E/c$, an anti-Hermitian element; its norm form is $-(E/c)^2+|\mathbf{p}|^2 = 0$, so it is a non-pure zero divisor with $Q_0 = iE/c\neq0$, and therefore

$$
\tilde{P}^2 = 2Q_0\tilde{P} = 2i\frac{E}{c}\,\tilde{P}, \qquad \frac{\tilde{P}}{2Q_0} = \frac{\tilde{P}}{2iE/c}\ \text{is idempotent} .
$$

The normalised momentum of a photon is a Hermitian idempotent — a **pure state direction**. The same holds for the informational photon $E/c\,e_0+i\mathbf{p}'$ with $|\mathbf{p}'| = E/c$: the null momentum of either sector, divided by twice its scalar part, is a projector. So the light cone is foliated by scaled projectors, which is the precise algebraic content of the framework's statement that a null momentum defines a state direction. A massive momentum has $N(\tilde{P}) = -m^2c^2\neq0$ and is a unit: it can be boosted to rest, and a photon cannot.

## The Roots of Minus One

The non-pure zero divisors are complex multiples of idempotents, and the idempotents are classified by the roots of $-1$; those roots are classified in *Biquaternion Roots of Minus One*, and the resulting classification of the idempotents is in *Biquaternion Idempotents and Projections*. In the physical reading of those articles the roots are the algebra's imaginary units and generators, and the idempotents are the pure states; a non-pure zero divisor is therefore a scaled state direction.

## Distribution of the Zero Divisors

We now examine how the zero divisors are distributed among the six distinguished subspaces of $\mathbb{B}$. The distribution is where the causal structure becomes visible subspace by subspace.

### The Complex Subspace $\mathbb{C}_{\mathbb{B}}$

An element has the form $\tilde{Q} = Q_0e_0$, and $N(\tilde{Q}) = Q_0^2$ vanishes only at $\tilde{Q} = 0$: $\mathbb{C}_{\mathbb{B}}$ contains **no** zero divisors, which reflects that it is a copy of the field $\mathbb{C}$.

**Physical reading.** The phase sector is never null: a pure phase $e^{i\theta}$ is always a unit, and the central $U(1)$ of the framework has no light-cone part.

### The Vector Subspace $\mathrm{Vect}(\mathbb{B})$

For pure $\tilde{Q} = Q_1e_1+Q_2e_2+Q_3e_3$ the norm form $Q_1^2+Q_2^2+Q_3^2$ is complex-valued and vanishes on a **complex cone of complex dimension 2** in $\mathrm{Vect}(\mathbb{B})\cong\mathbb{C}^3$ — a real cone of real dimension 4 in a real space of dimension 6. Its nonzero elements are exactly the **pure zero divisors**: vanishing scalar part, square zero, i.e. the nilpotents. The cone has real codimension 2, not the codimension 1 of a double cone as in $\mathbb{M}_\pm$. The complement of the cone is connected.

**Physical reading.** This is the cone of parabolic generators: purely vectorial null elements. Its codimension 2 (rather than 1) is the reason the pure null elements do not split the vector subspace into two causal parts the way the light cone splits the Hermitian sectors.

### The Quaternion Subspace $\mathbb{H}_{\mathbb{B}}$

An element has real coefficients and its norm form is a sum of squares of real numbers, vanishing only at $\tilde{Q} = 0$: $\mathbb{H}_{\mathbb{B}}$ contains **no** zero divisors, reflecting the Frobenius theorem — it is a copy of the division algebra $\mathbb{H}$.

**Physical reading.** Rotations are never null: a real quaternion is an elliptic generator or a unit, and the rotation group sits entirely inside the unit group.

### The Anti-Quaternion Subspace $i\mathbb{H}_{\mathbb{B}}$

For $i\tilde{P}$ with $\tilde{P}\in\mathbb{H}_{\mathbb{B}}$, $N(i\tilde{P}) = -(p_0^2+p_1^2+p_2^2+p_3^2)$, which is negative-definite and vanishes only at the origin: $i\mathbb{H}_{\mathbb{B}}$ contains **no** zero divisors, even though it is not a subalgebra.

**Physical reading.** Pure boosts are never null either: $i\mathbb{H}_{\mathbb{B}}$ is the hyperbolic-generator subspace of *Biquaternion Roots of Minus One*, and its norm form is negative-definite, so every nonzero boost is a unit.

### The Hermitian Subspace $\mathbb{M}_+$

An element has the form $\tilde{Q} = q_0e_0+iq'_1e_1+iq'_2e_2+iq'_3e_3$ with real coefficients, and

$$
N(\tilde{Q}) = q_0^2-(q'_1)^2-(q'_2)^2-(q'_3)^2 .
$$

This vanishes for the nonzero elements with $q_0^2 = (q'_1)^2+(q'_2)^2+(q'_3)^2$: a **double cone** in the four-dimensional real space $\mathbb{M}_+$, of dimension 3 as a submanifold. Outside the cone, $N\neq0$ and the elements are invertible, and the complement has **three** connected components:

- the **future timelike region** ($q_0>0$, $q_0^2>(q'_1)^2+(q'_2)^2+(q'_3)^2$, with $N>0$);
- the **past timelike region** ($q_0<0$, same inequality, with $N>0$);
- the **spacelike region** ($q_0^2<(q'_1)^2+(q'_2)^2+(q'_3)^2$, with $N<0$).

### The Anti-Hermitian Subspace $\mathbb{M}_-$

An element has the form $\tilde{Q} = iq'_0e_0+q_1e_1+q_2e_2+q_3e_3$ with real coefficients, and

$$
N(\tilde{Q}) = -(q'_0)^2+q_1^2+q_2^2+q_3^2 .
$$

Again a **double cone**, defined by $(q'_0)^2 = q_1^2+q_2^2+q_3^2$, with $N\neq0$ and invertibility outside it and **three** connected components:

- the **spacelike region** ($q_1^2+q_2^2+q_3^2>(q'_0)^2$, with $N>0$);
- the **future timelike region** ($q'_0>0$, $(q'_0)^2>q_1^2+q_2^2+q_3^2$, with $N<0$);
- the **past timelike region** ($q'_0<0$, same inequality, with $N<0$).

**Physical reading.** The double cones in $\mathbb{M}_\pm$ are the framework's light cones, and the connected components of the complement are the causal regions. The two sectors carry the two coordinate conventions, and the sign of the norm form records which: the **informational** coordinate $ct'\,e_0+i\mathbf{x}'$ is Hermitian, so it lies in $\mathbb{M}_+$ and a timelike event has $N = c^2t'^2-|\mathbf{x}'|^2>0$, while the **material** coordinate $ict\,e_0+\mathbf{x}$ is anti-Hermitian, lies in $\mathbb{M}_-$, and a timelike event has $N = -c^2t^2+|\mathbf{x}|^2<0$. In both sectors the two timelike components are the two sheets of the causal region, separated by the cone, and the spacelike complement is the third. That the causal structure is the *component structure of a group complement* is the reason the framework can speak of the future and past sheets as group-theoretic objects rather than as conventions.

### Summary of the Distribution

Of the six distinguished subspaces:

- $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ contain no zero divisors: the first two are the subalgebras among the six that are division algebras, and $i\mathbb{H}_{\mathbb{B}}$ is a module over $\mathbb{H}_{\mathbb{B}}$ with negative-definite norm form.
- $\mathbb{M}_+$ and $\mathbb{M}_-$ contain a three-dimensional double cone of zero divisors, all of them non-pure; outside it the elements are invertible.
- $\mathrm{Vect}(\mathbb{B})$ contains the pure zero divisors, the nilpotent cone, of real dimension 4.

The two cones in $\mathbb{M}_\pm$ have the same structure, the special coordinate being $q_0$ in $\mathbb{M}_+$ and $q'_0$ in $\mathbb{M}_-$ — the real and the imaginary scalar parts.

The three cones do **not** exhaust the zero divisor set: a generic zero divisor has nonzero scalar part and a vector part that is neither purely real nor purely imaginary, so it lies in none of the six subspaces. The distinction explains the two dimensions that occur — the light cones in $\mathbb{M}_\pm$ have real codimension 1 in their four-dimensional spaces, the nilpotent cone in $\mathrm{Vect}(\mathbb{B})$ real codimension 2 in its six-dimensional space — and is why the distribution is stated subspace by subspace rather than as a partition.

## Structure of the Zero Divisors

### The Pure Case

A pure $\tilde{Q}$ is a zero divisor if and only if $Q_1^2+Q_2^2+Q_3^2 = 0$, and then $\tilde{Q}^2 = 0$: the pure zero divisors are exactly the nonzero nilpotents, i.e. the zero divisors with vanishing scalar part.

### The Non-Pure Case

A non-pure $\tilde{Q}$ with $Q_0\neq0$ is a zero divisor if and only if $N(\tilde{Q}) = 0$, and then $\tilde{Q}^2 = 2Q_0\tilde{Q}$: the non-pure zero divisors are exactly the nonzero complex multiples of the nontrivial idempotents.

### The Comparison Table

| | Pure case ($Q_0 = 0$) | Non-pure case ($Q_0\neq0$) |
|---|---|---|
| Form | $\tilde{Q} = Q_1e_1+Q_2e_2+Q_3e_3$ | $\tilde{Q} = Q_0e_0+Q_1e_1+Q_2e_2+Q_3e_3$ |
| Criterion | $Q_1^2+Q_2^2+Q_3^2 = 0$ | $Q_0^2+Q_1^2+Q_2^2+Q_3^2 = 0$ |
| Square | $\tilde{Q}^2 = 0$ | $\tilde{Q}^2 = 2Q_0\tilde{Q}$ |
| Structure | nilpotent | complex multiple of an idempotent |
| Annihilator | contains $\tilde{Q}$ | contains $\tilde{Q}-2Q_0e_0$ |
| Idempotent | none | $\tilde{P} = \tilde{Q}/(2Q_0)$ |
| Physical type | parabolic generator | scaled projector; the light cone of a sector |

### The Union

The zero divisor set is the union of the two families, and they are **disjoint** (they are separated by whether $Q_0$ vanishes, and the origin is excluded from both). Their union is the zero divisor set $\mathcal{Z}$.

As complex cones, the two families have different dimensions: the pure family (the nilpotent cone) is a complex cone of complex dimension 2, real dimension 4, being one complex equation in $(Q_1,Q_2,Q_3)$; the non-pure family is an open dense subset of the full zero divisor cone (the condition $Q_0\neq0$ is open, and its closure is the whole cone), of complex dimension 3, real dimension 6, matching the full set.

## The Zero Divisor Set

The zero divisor set is

$$
\mathcal{Z} = \{\tilde{Q}\in\mathbb{B} : \tilde{Q}\neq0,\ N(\tilde{Q}) = 0\} = \mathbb{B}\setminus(\{0\}\cup\mathbb{B}^\times) .
$$

**Basic properties.**

- The closed cone $\{N = 0\}$ is the zero-set of the polynomial map $N:\mathbb{B}\to\mathbb{C}$, hence closed; $\mathcal{Z}$ is that cone with the origin removed, and so is **not** closed — a closed cone minus its apex.
- $\mathcal{Z}$ is a cone away from the origin: if $\tilde{Q}\in\mathcal{Z}$ and $\alpha\in\mathbb{C}\setminus\{0\}$, then $\alpha\tilde{Q}\in\mathcal{Z}$, since $N(\alpha\tilde{Q}) = \alpha^2N(\tilde{Q}) = 0$.

**Dimension.** $\mathcal{Z}$ has **real dimension 6** (complex dimension 3). The norm form is one complex equation in the four complex coefficients — two real equations in eight real coordinates — so its solution set is a complex hypersurface in $\mathbb{C}^4$ of complex dimension 3. The two real equations are independent at every nonzero point of the zero set, so the zero set is a smooth real 6-manifold away from the origin.

## Summary

The zero divisors of the biquaternion algebra are the nonzero elements on which the norm form vanishes. They split into two families:

- the **pure zero divisors**, with vanishing scalar part and $Q_1^2+Q_2^2+Q_3^2 = 0$: exactly the nonzero nilpotents, with square zero and annihilator containing themselves; a complex cone of real dimension 4; physically the parabolic generators, the purely vectorial null directions;
- the **non-pure zero divisors**, with nonzero scalar part and $Q_0^2+Q_1^2+Q_2^2+Q_3^2 = 0$: exactly the nonzero complex multiples of the nontrivial idempotents, with square $2Q_0\tilde{Q}$ and annihilator containing $\tilde{Q}-2Q_0e_0$; an open dense subset of the full cone; physically the light-cone elements of the two sectors, whose normalised form is a pure state direction — the photon's momentum being the instance in point.

The idempotents appearing here — trivial, Hermitian and general, with their bijection with the roots of $-1$ — are classified in *Biquaternion Idempotents and Projections*.

Of the six distinguished subspaces, $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ contain no zero divisors (phases, rotations and pure boosts are never null), while $\mathbb{M}_+$ and $\mathbb{M}_-$ contain a three-dimensional double cone — the light cone of the informational and of the material sector, whose complement's three components are the future timelike, past timelike and spacelike regions — and $\mathrm{Vect}(\mathbb{B})$ contains the nilpotent cone of real dimension 4. A generic zero divisor lies in none of the six.

The zero divisor set is a complex cone of complex dimension 3, real dimension 6, in $\mathbb{B}\cong\mathbb{C}^4$, with the origin removed.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | General biquaternion |
| $Q_\mu = q_\mu+iq'_\mu$ | Complex coefficient |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form; vanishes exactly on the zero divisors |
| $\mathcal{Z}$ | Zero divisor set: the null cone minus the origin |
| $\tilde{Q}^2 = 0$ | Nilpotent equation: the pure (parabolic) zero divisors |
| $\tilde{P} = \tilde{Q}/(2Q_0)$ | The idempotent of a non-pure zero divisor |
| $\mathbb{C}_{\mathbb{B}},\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}}$ | Subspaces with no zero divisors: phase, rotations, boosts |
| $\mathrm{Vect}(\mathbb{B})$ | Vector subspace; contains the nilpotent cone |
| $\mathbb{M}_+$ | Hermitian subspace; informational coordinate; light cone of the informational sector |
| $\mathbb{M}_-$ | Anti-Hermitian subspace; material coordinate; light cone of the material sector |
| $ict\,e_0+\mathbf{x}$, $ct'\,e_0+i\mathbf{x}'$ | Material and informational coordinates |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original discovery of the zero divisors and the nilpotents.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the classification of the zero divisors.
- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63–68, for the classification of the roots of $-1$.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the semi-norm and the algebraic properties of the biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
