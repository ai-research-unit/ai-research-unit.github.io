
# __Operators on a Non-Archimedean Field__

## Introduction

A non-Archimedean field is a field with an ultrametric absolute value, and its additive operators carry a size — the operator norm — together with a finer invariant than the size: the action induced on the residue field and on the value group. This article treats the operator layer of a non-Archimedean field: the bounded additive operators and their operator norm, the contractive operators that preserve the valuation ring, the **residual operator** that a contractive operator induces on the residue field, the isometries and the group they form, and the property of **spherical completeness**, which is the completeness of the nests of balls rather than of the sequences and is exactly the hypothesis under which the extension theorems of the non-Archimedean theory hold.

The article assumes the non-Archimedean field, its absolute value, its valuation ring $\mathcal{O}$, its maximal ideal $\mathrm{M}$, its residue field $k$, its value group $\Gamma$ and the ultrametric geometry of balls from *Absolute Values, Valuations and Completions*; the valuation as a multiplicative operator and its tropical reading from *The Valuation Operator*; the residue operator and its multiplicative part from *The Residue Operator of a Valued Field*; the completion operator and the persistence of the residue field and the value group from *The Completion Operator*; the bounded linear operators and the operator norm on a normed space from *Bounded Operators on a Topological Vector Space*, later in this Part; and the continuous additive operators, the homeomorphisms and the continuous automorphisms from *Operators on a Topological Ring*. The Hahn–Banach theorem over a spherically complete field is named and not proved; the analytic theory of power series over a non-Archimedean field is Part III and is not used. No measure and no form occurs.

Throughout, $(F, \lvert \cdot \rvert)$ is a non-Archimedean field, $\mathcal{O}$, $\mathrm{M}$, $k$ and $\Gamma$ are its valuation ring, maximal ideal, residue field and value group, $\pi$ is a uniformiser when $\Gamma \cong \mathbb{Z}$, and $T$ ranges over the continuous additive operators $F \to F$; the completion is $\widehat{F}$ and the closed ball of radius $r$ about $a$ is $B(a,r) = \{x : \lvert x - a \rvert \leq r\}$.

## The Bounded Operators and the Operator Norm

**Definition.** An additive operator $T : F \to F$ is **bounded** if the set $\{\lvert Tx \rvert : \lvert x \rvert \leq 1\}$ is bounded above in $\mathbb{R}$, and the **operator norm** of a bounded $T$ is

$$
\lVert T\rVert = \sup_{\lvert x \rvert \leq 1} \lvert Tx \rvert .
$$

**Proposition (bounded is continuous).** For an additive operator $T$, the following are equivalent: $T$ is bounded; $T$ is uniformly continuous; $T$ is continuous at $0$; there is a constant $C$ with $\lvert Tx \rvert \leq C\lvert x \rvert$ for all $x$. The least such $C$ is the operator norm, and the operator norm is a norm on the space of bounded operators, submultiplicative under composition.

**Proof.** Boundedness gives the estimate on the unit ball and hence, by scaling, everywhere; an estimate gives continuity at $0$ and therefore, additivity being compatible with the uniform structure, uniform continuity; continuity at $0$ gives a ball $B(0,\rho)$ mapped into $B(0,1)$, whence the estimate with $C = \rho^{-1}$ after scaling. The norm axioms are checked termwise; submultiplicativity is $\lvert(ST)x\rvert \leq \lVert S\rVert\lvert Tx\rvert \leq \lVert S\rVert\lVert T\rVert\lvert x\rvert$ for the least constant.

**Proposition (the norm is attained on the unit ball).** For a bounded additive $T$ the supremum defining $\lVert T\rVert$ is a maximum whenever the value set $\lvert F^\times\rvert$ is discrete, and in all cases it is the least $C$ with $\lvert Tx\rvert \leq C\lvert x\rvert$; the two-sided ideal of operators of norm zero is $\{T : T(F) \subseteq \overline{\{0\}}\} = 0$ on a Hausdorff field.

**Proof.** With a discrete value group the values $\lvert Tx\rvert$ form a discrete subset of $\mathbb{R}$, and a bounded subset of a discrete set attains its supremum; in general the supremum need not be attained, as on a dense value group. The kernel of the norm is the set of operators carried into the closure of zero, which is $\{0\}$ for a Hausdorff field, so the norm is a norm in the strict sense.

## The Contractive Operators and the Residual Operator

**Definition.** A bounded operator $T$ is **contractive** if $\lVert T\rVert \leq 1$, equivalently $T(\mathcal{O}) \subseteq \mathcal{O}$; it is **infinitesimal** if $\lVert T\rVert < 1$, equivalently $T(\mathcal{O}) \subseteq \mathrm{M}$. The contractive operators form a subring $\mathcal{B}_1$ of the ring $\mathcal{B}$ of bounded operators, with the identity as unit, and the infinitesimal operators form a two-sided ideal of $\mathcal{B}_1$.

**Proposition (contractive operators and the filtration).** For a bounded $T$,

$$
\lVert T\rVert \leq 1 \iff T(\mathcal{O}) \subseteq \mathcal{O}, \qquad \lVert T\rVert < 1 \iff T(\mathcal{O}) \subseteq \mathrm{M} .
$$

Consequently an infinitesimal operator satisfies $T(\mathrm{M}) \subseteq \mathrm{M}$ and has zero residual operator; a general contractive operator has a residual operator as soon as $T(\mathrm{M}) \subseteq \mathrm{M}$, which holds when $T$ is multiplicative, when $T$ is a scalar multiplication $x \mapsto cx$ with $c$ a unit, and more generally when $T$ carries the open unit ball into itself.

**Proof.** The equivalence of $\lVert T\rVert \leq 1$ with $T(\mathcal{O}) \subseteq \mathcal{O}$ is the definition of the operator norm as a supremum; the second equivalence is the same statement with a strict bound, since $\lVert T\rVert < 1$ means $\lvert Tx\rvert < 1$ for all $x$ of $\lvert x\rvert \leq 1$. An infinitesimal operator therefore carries $\mathcal{O}$ into $\mathrm{M}$, hence $\mathrm{M}$ into $\mathrm{M}$, and its residual operator is zero. A multiplicative operator carries $\mathrm{M}$ into $\mathrm{M}$ because the product of an element of $\mathrm{M}$ with any element of $\mathcal{O}$ lies in $\mathrm{M}$; a scalar multiplication by a unit reverses $\mathcal{O}$ and $\mathrm{M}$ onto themselves.

**Definition.** Let $T$ be a bounded operator with $T(\mathcal{O}) \subseteq \mathcal{O}$. If $T(\mathrm{M}) \subseteq \mathrm{M}$ then $T$ induces a well-defined additive map

$$
\bar T : k \longrightarrow k, \qquad \bar T(x + \mathrm{M}) = Tx + \mathrm{M} ,
$$

the **residual operator** of $T$. The assignment $T \mapsto \bar T$ is the **reduction** of the operator layer.

**Proposition (the residual map is a ring homomorphism).** On the contractive operators with $T(\mathrm{M}) \subseteq \mathrm{M}$ the assignment $T \mapsto \bar T$ is a ring homomorphism onto the additive endomorphisms of $k$ that it reaches, with $\overline{\mathrm{id}} = \mathrm{id}_k$ and $\overline{ST} = \bar S\bar T$; its kernel is the two-sided ideal of the infinitesimal operators, those with $T(\mathcal{O}) \subseteq \mathrm{M}$, equivalently $\lVert T\rVert < 1$.

**Proof.** If $x - x' \in \mathrm{M}$ then $Tx - Tx' = T(x - x') \in \mathrm{M}$, so $\bar T$ is well defined; it is additive because $T$ is. For the product, $\overline{ST}(x + \mathrm{M}) = STx + \mathrm{M}$ and $\bar S\bar T(x+\mathrm{M}) = \bar S(Tx + \mathrm{M}) = STx + \mathrm{M}$, so the maps agree, using $S(\mathrm{M})\subseteq \mathrm{M}$; the identity reduces to the identity. The kernel is the set of contractive $T$ with $T(\mathcal{O}) \subseteq \mathrm{M}$, that is the infinitesimal operators $\lVert T\rVert < 1$; this is a two-sided ideal because composition with a contractive operator preserves the condition and the sum of two infinitesimal operators is infinitesimal.

**Corollary (the residual operator is the operator on the residue field).** The residual operator is the operator-theoretic form of the residue map of *The Residue Operator of a Valued Field*: reduction of elements $x \mapsto x + \mathrm{M}$ is the case $T = \mathrm{id}$, and the residual operator of a product $ST$ is the product of the residual operators, so the reduction is a homomorphism of the operator layers that carries the contractive operators onto the operators of the residue field.

**Proof.** The case $T = \mathrm{id}$ gives $\bar T = \mathrm{id}_k$, which is the identity residue map; multiplicativity of the reduction is the proposition. The image is the set of induced maps, which is a subring of $\operatorname{End}(k)$.

## Isometries

**Definition.** An additive operator $T$ is an **isometry** if $\lvert Tx \rvert = \lvert x \rvert$ for all $x$, equivalently if $\lVert T\rVert = 1$ and $T$ is injective; the isometries of $F$ onto itself form a group $\operatorname{Isom}(F)$, the **isometry group**. A **scaling** is a map $x \mapsto c x$ for $c \in F^\times$, and a **rotation** is a map $x \mapsto ux$ with $u \in \mathcal{O}^\times$.

**Proposition (the isometry group).** Every isometry preserves the valuation ring and the maximal ideal, $T(\mathcal{O}) = \mathcal{O}$ and $T(\mathrm{M}) = \mathrm{M}$, so it has a residual operator $\bar T$, and $T \mapsto \bar T$ is a homomorphism from $\operatorname{Isom}(F)$ onto a subgroup of the isometry group of $k$. The rotations form a subgroup $\mathcal{O}^\times$ of $\operatorname{Isom}(F)$ with residual image $k^\times$ acting by multiplication, and the scalings form a subgroup $F^\times$ of $\operatorname{Isom}(F)$ with residual image trivial on the classes of the value group.

**Proof.** An isometry maps $\{x : \lvert x\rvert \leq 1\}$ onto itself, giving $T(\mathcal{O}) = \mathcal{O}$, and maps $\mathrm{M}$ onto $\mathrm{M}$; hence it has a residual operator. The map $T\mapsto\bar T$ is a homomorphism by the previous section, and it takes values in the additive automorphisms of $k$ preserving the multiplication by the residue of the rotation, whence the statements about the two subgroups.

**Proposition (the isometries are a closed subgroup).** In the topology of uniform convergence on the balls, the isometry group $\operatorname{Isom}(F)$ is a closed subgroup of the group of homeomorphisms of $F$, and it is contained in the group of uniformly continuous bijections.

**Proof.** An isometry is uniformly continuous and bijective onto $F$ by the inverse function theorem for isometries of a complete field (the inverse is the isometry that reverses it); the isometry condition is closed, being the intersection of the closed conditions $\lvert Tx\rvert = \lvert x\rvert$ for all $x$, so the group is closed. The uniform continuity is immediate from the definition.

## Spherical Completeness

**Definition.** A non-Archimedean field $F$ is **spherically complete** if every decreasing sequence of closed balls $B(a_0, r_0) \supseteq B(a_1, r_1) \supseteq \cdots$ has nonempty intersection. Equivalently, every **nest** of closed balls, any two of which are nested, has nonempty intersection.

**Proposition (spherical completeness is stronger than completeness).** A spherically complete field is complete; the converse fails, and $\mathbb{C}_p$ is complete but not spherically complete.

**Proof.** If $F$ were not complete there would be a Cauchy sequence with no limit; its tail balls form a nest with empty intersection, by the ultrametric estimate $\lvert x_m - x_n\rvert \leq \max_{n\leq k<m}\lvert x_{k+1} - x_k\rvert$, so spherical completeness implies completeness. For $\mathbb{C}_p$, the value group is $\mathbb{Q}$, which is dense; the balls of radii tending to a limit in $\mathbb{R}\setminus\lvert \mathbb{C}_p^\times\rvert$ form a nest with empty intersection, by the standard argument of non-Archimedean analysis. So the two notions differ, and spherical completeness is the strictly stronger one.

**Theorem (characterisations).** For a non-Archimedean field $F$ the following are equivalent: $F$ is spherically complete; $F$ has no nontrivial immediate extension, where an immediate extension is one with the same value group and the same residue field; every additive operator from a subspace of a normed $F$-space to $F$ that is bounded extends to the whole space with the same norm (the non-Archimedean Hahn–Banach theorem, or Ingleton's theorem).

**Proof sketch.** The equivalence of the first two is the standard theorem of Krull: a maximal immediate extension of $F$ is obtained by adjoining the limits of the nests, and it is nontrivial exactly when a nest has empty intersection, so an immediate extension can be built from a nest with no common point and conversely a missing point of a nest yields an immediate extension. The third is Ingleton's theorem: spherical completeness is exactly the hypothesis that makes the ultrametric Hahn–Banach argument close, because the argument produces a nest of balls whose common point is the value to be assigned.

**Corollary (spherical completeness is stable under the standard operations).** A discretely valued complete field is spherically complete, so $\mathbb{Q}_p$ and $k((t))$ are; the completion of a spherically complete field is spherically complete; and a finite extension of a spherically complete field is spherically complete.

**Proof.** In a discretely valued complete field a nest of balls has radii taking finitely many values or tending to a limit in the value group, so it is eventually constant or its centres form a Cauchy sequence, whose limit lies in the intersection; hence the field is spherically complete. The completion statement is the same argument applied to the denser field; the finite-extension statement follows from the equivalence with the absence of immediate extensions, because an immediate extension of a finite extension restricts to an immediate extension of the base.

**Remark (the boundary).** Spherical completeness is used in the non-Archimedean theory of normed spaces — the Hahn–Banach extension theorem, the structure of the dual and the theory of orthogonal bases — which are the modules and vector spaces of this Part, treated by *Topological Modules and Vector Spaces* and *Bounded Operators on a Topological Vector Space*. This article only fixes the property and its operator-theoretic content; the normed-space theory that uses it is deferred, and the analytic theory over a non-Archimedean field is Part III.

## Examples

**Example ($\mathbb{Q}_p$).** The value group is $\mathbb{Z}$, discrete, and $\mathbb{Q}_p$ is complete, so it is spherically complete; the residue field is $\mathbb{F}_p$, the contractive operators reduce to the additive operators of $\mathbb{F}_p$, and the rotations are $\mathbb{Z}_p^\times$.

**Example ($k((t))$).** Spherically complete, with the same argument; the residual operator of a contractive operator is an additive endomorphism of $k$, and the rotation by $u = 1 + t$ is a residue $1$ isometry.

**Example ($\mathbb{C}_p$).** Complete but not spherically complete; the value group is $\mathbb{Q}$ and the residue field is $\overline{\mathbb{F}_p}$, both infinite, and the nest of balls of radii tending to a limit outside the value group witnesses the failure. Consequently the non-Archimedean Hahn–Banach theorem does not apply over $\mathbb{C}_p$ in the same form.

## Summary

On a non-Archimedean field the bounded additive operators are exactly the continuous ones, they carry the operator norm $\lVert T\rVert = \sup_{\lvert x\rvert\leq1}\lvert Tx\rvert$, submultiplicative under composition and attained on the unit ball for a discrete value group, and the contractive operators $\lVert T\rVert \leq 1$, equivalently $T(\mathcal{O}) \subseteq \mathcal{O}$, form a unital subring. A contractive operator with $T(\mathrm{M}) \subseteq \mathrm{M}$ induces a **residual operator** $\bar T$ on the residue field $k$, and $T \mapsto \bar T$ is a ring homomorphism whose kernel is the ideal of the infinitesimal operators, so the residue operator of a valued field extends from the elements to the operators. The isometries preserve $\mathcal{O}$ and $\mathrm{M}$, they form a closed subgroup $\operatorname{Isom}(F)$ containing the rotations $\mathcal{O}^\times$ and the scalings $F^\times$, and reduction maps them onto a subgroup of the operators of the residue field.

A non-Archimedean field is **spherically complete** when every nest of closed balls has nonempty intersection; this implies completeness, fails for $\mathbb{C}_p$, holds for the discretely valued complete fields $\mathbb{Q}_p$ and $k((t))$, and is characterised by the absence of a nontrivial immediate extension and by the validity of the non-Archimedean Hahn–Banach theorem. It is the property of the completeness of the nests, finer than the completeness of the sequences, and the normed-space theory that uses it is later in this Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(F, \lvert \cdot \rvert)$ | The non-Archimedean field |
| $\mathcal{O}$, $\mathrm{M}$, $k$, $\Gamma$ | Valuation ring, maximal ideal, residue field, value group |
| $\pi$ | A uniformiser when $\Gamma \cong \mathbb{Z}$ |
| $\lVert T\rVert = \sup_{\lvert x\rvert\leq1}\lvert Tx\rvert$ | The operator norm of a bounded additive $T$ |
| $\mathcal{B}$, $\mathcal{B}_1$ | Bounded operators, and the contractive subring $\lVert T\rVert\leq1$ |
| $\bar T$ | The residual operator on $k$, defined when $T(\mathrm{M})\subseteq\mathrm{M}$ |
| $T\mapsto\bar T$ | The reduction, a ring homomorphism with kernel the infinitesimal operators |
| $\operatorname{Isom}(F)$ | The isometry group, closed in the homeomorphism group |
| $B(a,r)$ | Closed ball of radius $r$ about $a$ |
| Spherical completeness | Every nest of closed balls has nonempty intersection |
| Immediate extension | An extension with the same value group and residue field |

## Further Reading

- A. C. M. van Rooij, *Non-Archimedean Functional Analysis* (Marcel Dekker, 1978), for spherically complete valued fields, the residual operators and the Hahn–Banach theorem.
- Wim H. Schikhof, *Ultrametric Calculus* (Cambridge University Press, 1984), for the ultrametric geometry of balls and the structure of a valued field.
- Jean-Pierre Serre, *Local Fields* (Springer, 1979), for the discretely valued complete fields $\mathbb{Q}_p$ and $k((t))$ and their residue fields.
- A. W. Ingleton, "The Hahn–Banach theorem for non-Archimedean valued fields", *Proceedings of the Cambridge Philosophical Society* **48** (1952), 41–45, for the non-Archimedean Hahn–Banach theorem and spherical completeness.
- Lawrence Narici and Edward Beckenstein, *Topological Vector Spaces* (CRC Press, 2nd ed. 2011), for the operator theory of non-Archimedean normed spaces and the residual structure.
