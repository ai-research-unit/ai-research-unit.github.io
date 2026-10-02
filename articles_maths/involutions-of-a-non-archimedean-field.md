
# __Involutions of a Non-Archimedean Field__

## Introduction

A non-Archimedean field is a field with a valuation satisfying the strong triangle inequality, and an involution of it is an order-two anti-automorphism, an automorphism in the commutative case. The involution meets the valuation in a sharp alternative that has no archimedean analogue: either it preserves the valuation, equivalently the value up to equivalence, in which case the scaling must be one and the involution is isometric and induces an involution of the residue field on every quotient of the valuation filtration; or it does not preserve the valuation at all, and then it carries no residue involution and the valuation ring is not stable. This article treats the involutions of a non-Archimedean field: it proves the alternative, computes the fixed field and shows that it is a valued subfield precisely in the isometric case, treats the residue involution with an arbitrary residue field, including the imperfect ones of positive characteristic and the non-discrete value groups, reads the whole structure through the completion and the spherical completion, and exhibits the function field $k(t)$ with its involutions as the standard family in which both cases occur.

The article assumes the valuation, the absolute value, the valuation ring, the maximal ideal, the residue field, the value group and the completion from *Absolute Values, Valuations and Completions*; the non-Archimedean field, its operators, its valuation ring and its spherical completeness from *Operators on a Non-Archimedean Field*; the valuation as an operator to the value group and the tropical reading from *The Valuation Operator*; the residue operator of a valued field from *The Residue Operator of a Valued Field*; the involution, its fixed and skew sets and the averaging map from *Involutive Rings* and *Involutive Topological Rings and Fields*; and the isometric involution, the residue involution, the ramification dichotomy $ef = 2$ and the norm form from *Involutive Valued Fields*. The local case, in which the value group is $\mathbb{Z}$ and the residue field is finite, is *Involutive Local Fields* and is quoted, not repeated; the central simple algebras over a non-Archimedean field with an involution and the Hermitian forms are named at the boundary and are not developed.

Throughout, $(F, v)$ is a non-Archimedean field with value group $\Gamma$, valuation ring $\mathcal{O} = \{x : v(x)\geq 0\}$, maximal ideal $\mathrm{M} = \{x : v(x) > 0\}$, residue field $k = \mathcal{O}/\mathrm{M}$ and completion $\widehat{F}$; $\sigma$ is an involution of $F$; the fixed field is $F^\sigma$; the norm form is $N(x) = x\,\sigma(x)$; and the **residue involution** $\bar\sigma$ is defined when $\sigma$ preserves the valuation ring.

## The Alternative for the Involution

**Theorem (valuation-preserving is valuation-fixing).** Suppose the involution $\sigma$ preserves the valuation up to equivalence, that is $v(\sigma(x)) = c\,v(x)$ for a constant $c > 0$ and all $x$. Then $c = 1$, so $\sigma$ is isometric; equivalently, $\sigma$ preserves the valuation ring and the maximal ideal, and it is continuous for the valuation topology. If $\sigma$ does not preserve the valuation up to equivalence, then it carries no residue involution, the valuation ring is not stable, and the induced topological structure on $\mathcal{O}$ is not preserved.

**Proof.** Applying the scaling identity to $\sigma(x)$ and using $\sigma^2 = \mathrm{id}$ gives $v(x) = c\,v(\sigma(x)) = c^2 v(x)$, so $c^2 = 1$, and $c = 1$ because $c > 0$; hence the invariance is exact and $\sigma(\mathcal{O}) = \mathcal{O}$, $\sigma(\mathrm{M}) = \mathrm{M}$. The preservation of the filtration and continuity are *Involutive Valued Fields*; the second sentence is the negation.

**Corollary (the value-group action is trivial in the isometric case).** If $\sigma$ is isometric then it acts trivially on the value group $\Gamma$ and on each quotient $\mathrm{M}^\alpha/\mathrm{M}^{\alpha+}$ of the filtration; the induced operator on the associated graded ring is $\bar\sigma$ on every graded piece, and the whole action of the involution on the graded picture is the residue involution.

**Proof.** Triviality on $\Gamma$ is $v(\sigma(x)) = v(x)$; the action on the graded pieces is *The Valuation Operator* and *Involutive Valued Fields*.

## The Fixed Field

**Theorem (the fixed field and the isometric hypothesis).** Let $\sigma$ be a nontrivial involution of $F$. Then $F^\sigma$ is a subfield with $[F : F^\sigma] = 2$, and $F^\sigma$ is a valued subfield of $F$ whose valuation ring is $\mathcal{O}\cap F^\sigma$ exactly when $\sigma$ is isometric; the norm form satisfies $\sigma(N(x)) = N(x)$, and $[F : F^\sigma] = 2$ holds whether or not $\sigma$ is isometric.

**Proof.** The degree statement is the algebraic fact that the fixed field of an order-two automorphism has index at most two, and exactly two when the involution is nontrivial, by *Involutive Valued Fields*; it does not use the valuation. When $\sigma$ is isometric, $\mathcal{O}$ is stable and $\mathcal{O}\cap F^\sigma$ is the valuation ring of the restricted valuation on $F^\sigma$; when it is not isometric, every valuation ring is moved and there is no compatible restriction on the whole of $F^\sigma$ from the given one. The norm statement is $\sigma(N(x)) = \sigma(x)\sigma^2(x) = N(x)$.

**Corollary (the trace and the norm).** For $x\in F$ the elements $x + \sigma(x)$ and $N(x) = x\sigma(x)$ lie in $F^\sigma$; the norm is multiplicative, $N(xy) = N(x)N(y)$, the norm-one set $U(F,\sigma) = \{x\in F^\times : N(x) = 1\}$ is a subgroup, and the norm form is anisotropic in the sense that $N(x) = 0$ only for $x = 0$.

**Proof.** The trace and norm lie in the fixed field as in the quadratic extension; multiplicativity is $\sigma(xy) = \sigma(x)\sigma(y)$ for a commutative field; anisotropy is that a field has no zero divisors.

## The Residue Involution

**Theorem (the residue involution over an arbitrary residue field).** Let $\sigma$ be isometric. Then $\bar\sigma$ is a well-defined order-two operator on the residue field $k = \mathcal{O}/\mathrm{M}$, additive and reversing the product,

$$
\bar\sigma(x + \mathrm{M}) = \sigma(x)+\mathrm{M} ,
$$

and its fixed field is the residue field of the fixed field, $k^{\bar\sigma} = k_{F^\sigma}$; the residue field $k$ may be of positive characteristic and imperfect, and $\bar\sigma$ is then an order-two operator on a possibly imperfect field, not necessarily the identity on the constants.

**Proof.** Well-definedness uses $\sigma(\mathrm{M}) = \mathrm{M}$; the operator properties are inherited from $\sigma$; the fixed field identification is *Involutive Valued Fields*, valid without the finiteness of $k$ or the discreteness of $\Gamma$. When $k$ is imperfect an order-two operator on $k$ may act nontrivially on $k^p$ and need not be of the form of a power of a Frobenius, which exists only when $k$ is finite or perfect.

**Corollary (the case of a non-discrete value group).** For a non-discrete value group $\Gamma$ the residue involution is the same operator and the graded action is the same; the ramification dichotomy $ef = 2$ of the local case has no direct analogue, since $e$ and $f$ are defined for a finite extension with a discrete valuation, and the article states the graded action of $\bar\sigma$ directly instead.

**Proof.** The construction of $\bar\sigma$ uses only the maximal ideal, which exists for every valuation; the local dichotomy is quoted from *Involutive Local Fields* and is not available without the discrete value group.

## Spherical Completeness and the Completion

**Theorem (the completion and the spherical completion).** An isometric involution $\sigma$ extends to an isometric involution $\widehat\sigma$ of the completion with $\widehat\sigma\iota = \iota\sigma$, the completion is non-Archimedean with the same value group and residue field, and $\widehat{F}^{\widehat\sigma} = \widehat{F^\sigma}$; a spherically complete non-Archimedean field with an isometric involution has fixed field spherically complete, and $\sigma$ extends to the maximal immediate extension.

**Proof.** The extension is *The Involution and the Completion of a Ring*, and the isometry is the continuity of the absolute value; the value group and residue field of the completion are *The Valuation Operator* and *The Residue Operator of a Valued Field*; the fixed field of the completion is the completion of the fixed field because the fixed field is closed for an isometric involution. For spherical completeness, a spherically complete field's fixed field under an isometry is spherically complete, since a nest of closed balls in $F^\sigma$, being a nest in $F$ with a common point, has a common point fixed by $\sigma$ by the limit argument; the maximal immediate extension is the union of the spherical completions and carries the extension of $\sigma$ as an isometry.

**Corollary (spherical completeness is preserved).** The fixed field of an isometric involution of a spherically complete non-Archimedean field is spherically complete and non-Archimedean for the restricted valuation; in particular the residue involution and the fixed field of a spherically complete field satisfy the same relation $k^{\bar\sigma} = k_{F^\sigma}$.

**Proof.** Combine the spherical completeness statement with the fixed-field identification.

## The Function Field with its Involutions

**Theorem (the involutions of $k(t)$).** Let $k$ be a field and $F = k(t)$ the rational function field, with the $t$-adic valuation $v_0$ and the valuation $v_\infty$ at infinity. The $k$-automorphisms of $k(t)$ are the fractional linear transformations $t\mapsto (at+b)/(ct+d)$ with $ad - bc\neq 0$, forming $\operatorname{PGL}_2(k)$, and the involutions among them are the elements of order two, which fix $k$ and either fix or move the valuations $v_0$ and $v_\infty$. The involution $t\mapsto -t$ fixes both valuations and is isometric for $v_0$; the involution $t\mapsto t^{-1}$ exchanges $v_0$ and $v_\infty$ and is not isometric for either.

**Proof.** The automorphisms of the rational function field are the fractional linear ones; an order-two element of $\operatorname{PGL}_2(k)$ has a matrix of trace zero up to scaling in characteristic other than two, and its action on the two points $0$ and $\infty$ of $\mathbb{P}^1(k)$ determines whether it fixes or moves each valuation. The valuation $v_0$ is preserved by $t\mapsto -t$ because the maximal ideal $(t)$ is carried to $(t)$; the map $t\mapsto t^{-1}$ carries $(t)$ to the ideal of fractions with pole at $0$ only at $\infty$, so it does not preserve $v_0$, and it exchanges $v_0$ with $v_\infty$.

**Corollary (the two cases occur in one family).** In $k(t)$ the involution $t\mapsto -t$ is isometric for the $t$-adic valuation, has fixed field $k(t^2)$ with the induced valuation, and residue involution the identity on $k$; the involution $t\mapsto t^{-1}$ is not isometric for the $t$-adic valuation, has fixed field $k(t + t^{-1})$, and carries no residue involution for the $t$-adic valuation. The family therefore realises both alternatives of the theorem.

**Proof.** The fixed field of $t\mapsto -t$ is $k(t^2)$ and the involution preserves the ideal $(t)$, so the residue involution exists and acts trivially on the residue field $k$; the fixed field of $t\mapsto t^{-1}$ is the subfield generated by $t + t^{-1}$, and the involution does not preserve the valuation ring of $v_0$, so no residue involution exists.

**Remark (the norm form in the two cases).** In the isometric case the norm form $N(x) = x\sigma(x)$ satisfies $v(N(x)) = 2v(x)$ and lands in the fixed field with a valuation, and the unitary group is the norm-one subgroup; in the non-isometric case the norm form still lands in the fixed field but the valuation identity fails, and the norm-one set is not bounded by the valuation ring. This is the boundary at which the arithmetic of the involution separates from its algebra.

## Examples

**Example ($\mathbb{Q}_p$ with the identity).** The $p$-adic field with the identity involution is the trivial isometric case; the residue involution is the identity on $\mathbb{F}_p$ and the fixed field is the whole field.

**Example ($k((t))$ with $t\mapsto -t$).** For any field $k$, the involution $t\mapsto -t$ on the Laurent series field is isometric for the $t$-adic valuation, with fixed field $k((t^2))$ and residue involution the identity; the norm form of $t$ is $-t^2$.

**Example ($k((t))$ with $t\mapsto t^{-1}$).** The map $t\mapsto t^{-1}$ is an involution of the local field $k((t))$ that is not isometric; it does not preserve the valuation ring and has no residue involution. On the subfield $k(t)$ it restricts to the second case of the function field theorem.

**Example (a residue field of positive characteristic).** For a non-Archimedean field whose residue field is the imperfect field $\mathbb{F}_p(s)$ with the operator fixing $s$, the residue involution is the identity; with the operator $s\mapsto s^p$, which is not of order two on the imperfect field, no involution is induced, showing that the residue involution need not be a power of a Frobenius outside the finite or perfect case.

**Example (a spherically complete field).** The field $\mathbb{C}_p$ is spherically complete, and any isometric involution of it, among them the identity and the involutions induced by the algebraic ones, has a spherically complete fixed field; the spherical completion therefore preserves the whole structure.

## Summary

An involution of a non-Archimedean field either preserves the valuation up to equivalence — and then the scaling constant must be one, the involution is isometric, it preserves the valuation ring, the maximal ideal, the whole filtration and the value group, and it induces an involution $\bar\sigma$ of the residue field — or it preserves none of these and carries no residue involution. The fixed field has index two over $F$ in either case, but it is a valued subfield of $F$ exactly in the isometric case; the norm form $N(x) = x\sigma(x)$ is multiplicative, lands in the fixed field and is anisotropic, and the norm-one set is a subgroup. The residue involution is an order-two operator on the residue field $k$ with fixed field $k_{F^\sigma}$; for an imperfect residue field of positive characteristic it is not a power of a Frobenius, and for a non-discrete value group the local ramification dichotomy is unavailable and the graded action of $\bar\sigma$ is stated in its place.

Under completion and spherical completion the isometric structure is preserved: the involution extends isometrically, the value group and residue field are unchanged, the fixed field completes and spherically completes with the field, and the maximal immediate extension carries the extension; the function field $k(t)$ realises both alternatives in one family, $t\mapsto -t$ being isometric for the $t$-adic valuation and $t\mapsto t^{-1}$ not being so, which is the sharpest illustration that the isometry hypothesis of the theory is a real restriction.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(F, v, \Gamma, \mathcal{O}, \mathrm{M}, k)$ | Non-Archimedean field and its valuation data |
| $\sigma$ | An involution of $F$ |
| Isometric | $v(\sigma(x)) = v(x)$; equivalently $v\circ\sigma$ equivalent to $v$ |
| $\bar\sigma(x+\mathrm{M}) = \sigma(x)+\mathrm{M}$ | The residue involution, when $\sigma$ is isometric |
| $F^\sigma$, $[F : F^\sigma] = 2$ | The fixed field |
| $N(x) = x\sigma(x)$, $v(N(x)) = 2v(x)$ | The norm form in the isometric case |
| $U(F,\sigma)$ | The norm-one subgroup |
| $\widehat{F}$, $\widehat{F}^{\widehat\sigma} = \widehat{F^\sigma}$ | The completion and its involution |
| $k(t)$, $t\mapsto \pm t^{\pm 1}$ | The function field and its involutions |
| $\operatorname{PGL}_2(k)$ | The $k$-automorphisms of $k(t)$ |
| $v_0, v_\infty$ | The valuations at $0$ and at infinity |

## Further Reading

- Jean-Pierre Serre, *Local Fields* (Springer, 1979), for non-Archimedean fields, the residue field and the ramification of quadratic extensions.
- Jürgen Neukirch, *Algebraic Number Theory* (Springer, 1999), for valuations, the value group, the residue field and Hermitian forms over a valued field.
- Seth Warner, *Topological Fields* (North-Holland, 1989), for isometric involutions, spherical completeness and the topology of a valued field.
- Wim H. Schikhof, *Ultrametric Calculus* (Cambridge University Press, 1984), for spherical completeness, the maximal immediate extension and the structure of the fixed field of an isometry.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for involutions of valued fields and Hermitian forms over them.
