
# __The Adjoint under a Hermitian Valuation__

## Introduction

A Hermitian valuation on a ring with an involution is a valuation compatible with the involution and with the norm form: it is isometric, $v(\sigma(x)) = v(x)$, and it satisfies $v(x\sigma(x)) = 2v(x)$, so that the norm form is valued exactly as the square of the element. The Hermitian form $B(x,y) = \tau(x\sigma(y))$ then takes values whose valuation is controlled by those of $x$ and $y$, the adjoint it defines is continuous and carries the valuation ring to itself, and the norm form forces the unitary elements into the valuation units: from $u\sigma(u) = 1$ one reads $2v(u) = 0$ and hence $v(u) = 0$. This article defines the Hermitian valuation, proves that it makes the form valued, computes the adjoint and shows that it preserves the filtration, identifies the unitary elements and the norm form, proves that the unitary group is bounded and closed, and reads the locally compact case, where the unitary group is compact.

The article assumes the valuation, the absolute value, the valuation ring, the residue field and the completion from *Absolute Values, Valuations and Completions*; the valuation as an operator and its extension to the completion from *The Valuation Operator*; the isometric involution, the norm form and the residue involution from *Involutive Valued Fields* and *Involutions of a Non-Archimedean Field*; the involutive topological ring, the closed fixed set and the averaging map from *Involutive Topological Rings and Fields*; the self-adjoint, skew and norm form of a division ring with involution from *Involutive Topological Division Rings*; and the operator adjoint, the form of the category and the `*`-representation from *The Involution on Bounded Operators of a Ring*.

Throughout, $R$ is a ring with a valuation $v$, an involution $\sigma$ and a $\sigma$-invariant trace $\tau$; the valuation is **Hermitian** when $v(\sigma(x)) = v(x)$ and $v(x\sigma(x)) = 2v(x)$ for all $x$; the **Hermitian form** is $B(x,y) = \tau(x\sigma(y))$; the **norm form** is $N(x) = x\sigma(x)$; the adjoint $T^\dagger$ is defined by $B(Tx,y) = B(x,T^\dagger y)$; the **unitary group** is $U(R,\sigma) = \{u\in R^\times : u\sigma(u) = 1\}$; and $\mathcal{O}$, $\mathrm{M}$, $k$ are the valuation ring, maximal ideal and residue field.

## The Hermitian Valuation and the Form

**Theorem (the form is valued).** Let $v$ be a Hermitian valuation. Then $v(B(x,y))\geq v(x)+v(y)$ for all $x,y$, the form $B$ is nondegenerate on the quotient by its radical, and the norm form satisfies $v(N(x)) = 2v(x)$; in particular $N(x)$ has valuation zero exactly when $x$ has, and the norm form is a map from the units to the units.

**Proof.** The valuation is Hermitian and isometric, so $v(x\sigma(y))\geq v(x)+v(\sigma(y)) = v(x)+v(y)$, and the trace does not decrease the valuation beyond the addition of the valuations of the terms; taking $y = x$ gives $v(N(x)) = 2v(x)$ by the Hermitian condition. Nondegeneracy is that the radical consists of the elements whose products with all others are nonunits, which is the maximal ideal when the form is Hermitian, as in *Adjoints under the Residue Pairing*.

**Corollary (the filtration).** For a Hermitian valuation the valuation ring $\mathcal{O}$ is stable under $\sigma$ and under the norm form, $N(\mathcal{O})\subseteq\mathcal{O}$, and the ideals $\mathrm{M}^n$ are stable, so the involution and the norm form preserve the whole filtration; the residue involution is defined and the residue norm form is $a\bar\sigma(a)$.

**Proof.** Isometry gives $\sigma(\mathcal{O}) = \mathcal{O}$ and $\sigma(\mathrm{M}^n) = \mathrm{M}^n$; the Hermitian condition gives $N(\mathcal{O})\subseteq\mathcal{O}$ from $v(N(x)) = 2v(x)\geq 0$ when $v(x)\geq 0$; the residue statements are *Involutive Valued Fields*.

## The Adjoint and the Filtration

**Theorem (the adjoint preserves the filtration).** Under a Hermitian valuation the adjoint of an operator that preserves each $\mathrm{M}^n$ also preserves each $\mathrm{M}^n$; the adjoint of the left multiplication is a left multiplication, $(L_a)^\dagger = L_{\sigma(a)}$, and it is an isometry of the filtration, so the adjointable operators form a subalgebra stable under the filtration and the adjoint map is continuous.

**Proof.** The adjoint identity $B(Tx,y) = B(x,T^\dagger y)$ together with the valued form shows that $T^\dagger$ preserves a filtration step exactly when $T$ does, by taking $y$ in the appropriate power of $\mathrm{M}$; the formula for $L_a$ is *The Adjoint of the Left Multiplication on a Topological Ring*, valid because $\tau$ is cyclic and $\sigma$-invariant. The continuity and the stability of the subalgebra are the theorem of *The Involution on Bounded Operators of a Ring* applied to the filtration topology.

**Proposition (the adjoint operation on the valued operator algebra).** For adjointable operators the identity $B(T^\dagger x, y) = B(x, Ty)$ holds, so the adjoint operation is additive, involutive and anti-multiplicative on the adjointable operators, and by the previous theorem it preserves the filtration; with the Hermitian valuation the operator algebra is therefore an involutive topological algebra whose involution is valued, and the adjoint map is continuous.

**Proof.** The identity $B(T^\dagger x, y) = B(x, Ty)$ is the defining identity of the adjoint read with $T$ and $T^\dagger$ exchanged, using $T^{\dagger\dagger} = T$ of *The Involution on Bounded Operators of a Ring*; additivity, involutivity and anti-multiplicativity are the statements of that article, and the filtration statement is the previous theorem.

## The Unitary Elements and the Norm Form

**Theorem (the unitary group is bounded).** Under a Hermitian valuation a unitary element $u$, with $u\sigma(u) = 1$, generates the norm form value $N(u) = 1$ and therefore has $2v(u) = 0$; for a real-valued valuation this gives $v(u) = 0$, so

$$
U(R,\sigma)\subseteq\mathcal{O}^\times .
$$

The unitary group is a subgroup of the units, it is closed when $N$ is continuous, and it is bounded.

**Proof.** $N(u) = u\sigma(u) = 1$, and $v(N(u)) = 2v(u)$ by the Hermitian condition, so $2v(u) = 0$ and $v(u) = 0$ for a real-valued valuation; hence $u$ is a unit of the valuation ring. Closure under multiplication and inversion is the computation of *Involutive Topological Division Rings*, and closedness is the continuity of the norm form; boundedness is $v(u) = 0$ for all unitary $u$.

**Corollary (compactness in the locally compact case).** If the ring is a locally compact non-Archimedean field with a Hermitian valuation, the unitary group is compact; on a local field it is the compact group of the norm-one elements, and its reduction to the residue field is the residue norm-one group. In the archimedean case $R = \mathbb{C}$ with the Hermitian valuation $|\cdot|$ and the conjugation, the unitary group is the circle, compact, and the norm form is $N(Z) = |Z|^2$.

**Proof.** Closed and bounded in a locally compact space is compact; the reduction statement is that the unitary elements have valuation zero, so they descend to the residue; the archimedean statement is the standard circle.

**Theorem (the self-adjoint elements and the Hermitian valuation).** The self-adjoint elements $x$, with $\sigma(x) = x$, satisfy $N(x) = x^2$, and their valuations satisfy $v(x^2) = 2v(x)$; the skew elements satisfy $N(x) = -x^2$ and the same valuation identity; the self-adjoint and skew elements are closed, and under a Hermitian valuation the set of unitaries acts on the self-adjoint elements preserving the norm form.

**Proof.** For self-adjoint $x$, $N(x) = x\sigma(x) = x^2$; for skew, $N(x) = x(-x) = -x^2$; the valuation identity is the Hermitian condition; closedness is *Involutive Topological Rings and Fields*. For a unitary $u$ one has $\sigma(u) = u^{-1}$, so the action on a self-adjoint $x$ is $x\mapsto ux\sigma(u) = uxu^{-1}$, which is self-adjoint because $\sigma(uxu^{-1}) = u\sigma(x)u^{-1} = uxu^{-1}$, and it preserves the norm form up to conjugation, $N(uxu^{-1}) = u\,N(x)\,u^{-1}$, hence preserves it exactly when $N(x)$ is central.

## The Norm Form, the Residue and the Lattice

**Theorem (the norm form as a map on the units).** The norm form is a map of the units into the units, $N : R^\times\to R^\times$, with $N(1) = 1$ and the identity

$$
N(uv) = u\,N(v)\,\sigma(u) ,
$$

so $N$ is multiplicative when the values commute with the parameters, in particular on the centre and on a commutative field; it is a homomorphism $R^\times\to (R^\times)^{\sigma}$ when $R$ is commutative, and it factors through the residue, $\bar N(\bar u) = \bar u\,\bar\sigma(\bar u)$, with the residue norm form of *Involutive Valued Fields*.

**Proof.** $N(uv) = uv\sigma(v)\sigma(u) = u\,N(v)\,\sigma(u)$; the multiplicative case is $uN(v) = N(v)u$; the residue statement is that $N$ preserves $\mathcal{O}$ by $v(N(u)) = 2v(u)\geq0$ for a unit and respects $\mathrm{M}$, so it descends.

**Corollary (the unitary group as the kernel of the norm).** The norm form maps the units into the units of the fixed field, $N(R^\times)\subseteq (R^\times)^\sigma$, since $\sigma(N(u)) = N(u)$, and its kernel on the units is the unitary group,

$$
U(R,\sigma) = \{u\in R^\times : N(u) = 1\} .
$$

For a self-adjoint unit $x$ the norm is $x^2$, so the norm form is the obstruction to unitarity: the unitaries are exactly the units of norm one.

**Proof.** $\sigma(N(u)) = \sigma(u\sigma(u)) = \sigma(\sigma(u))\,\sigma(u) = u\sigma(u) = N(u)$, so the values are fixed; the kernel is the unitarity condition by definition; the self-adjoint case is $N(x) = x\sigma(x) = x^2$.

**Theorem (the unitary action on the lattice).** The unitary group preserves the valuation ring and each ideal of the filtration,

$$
u\in U(R,\sigma) \implies u\,\mathcal{O} = \mathcal{O} = \mathcal{O}u , \qquad u\,\mathrm{M}^n = \mathrm{M}^n = \mathrm{M}^n\,u ,
$$

and acts by isometries of the form, $v(B(ux,uy)) = v(B(x,y))$; the induced action on the residue field is by isometries of the residue form, and the residue action is the reduction of the involution.

**Proof.** $v(u) = 0$ gives $u\in\mathcal{O}^\times$, so $u\mathcal{O} = \mathcal{O}$ and $u\mathrm{M}^n = \mathrm{M}^n$. The form transforms as $B(ux,uy) = \tau(ux\,\sigma(uy)) = \tau(ux\,\sigma(y)\sigma(u))$, and $v(u) = v(\sigma(u)) = 0$, so the valuation of the argument of the trace is $v(x\sigma(y))$ and hence $v(B(ux,uy)) = v(B(x,y))$ when the trace does not change the valuation; the residue action is that of a unit of the valuation ring on the residue field.

## Examples

**Example (the $p$-adic valuation).** $R = \mathbb{Q}_p$ with the identity involution; the valuation is Hermitian because $v_p(x^2) = 2v_p(x)$; the unitary group is $\{u : u^2 = 1\} = \{\pm1\}$, bounded, inside $\mathbb{Z}_p^\times$, and the self-adjoint elements are all of $R$.

**Example ($\mathbb{C}$ with the modulus).** $R = \mathbb{C}$, $\sigma$ the conjugation, $v = \log|\cdot|$ or the usual absolute value; the valuation is Hermitian, the unitary group is the circle, compact, and the norm form is the squared modulus.

**Example (a quaternion division algebra).** $R = \mathbb{H}$ with the quaternion conjugation and the norm valuation; the valuation is Hermitian, the unitary group is the unit sphere, compact, and the norm form is the squared norm; the self-adjoint elements are the reals and the skew elements the pure quaternions.

**Example (a Hermitian form over a local field).** For a finite-dimensional vector space over a local field with a Hermitian form, the unitary group is compact and acts on the bounded lattice, the norm form is the determinant form, and the adjoint of a linear map under the form is the conjugate transpose; this is the linear case, treated with the topological vector spaces of the category that follows.

**Example (a non-Hermitian valuation).** For a valuation with $v(x\sigma(x))\neq 2v(x)$ the unitarity condition no longer forces $v(u) = 0$, the unitary group is not bounded, and the adjoint need not preserve the filtration; this is the boundary at which the Hermitian hypothesis is needed.

## Summary

A Hermitian valuation on a ring with an involution is an isometric valuation satisfying $v(x\sigma(x)) = 2v(x)$; it makes the Hermitian form $B(x,y) = \tau(x\sigma(y))$ valued, with $v(B(x,y))\geq v(x)+v(y)$, nondegenerate modulo its radical, and it forces the norm form to satisfy $v(N(x)) = 2v(x)$, so that the norm form maps units to units and preserves the filtration. The adjoint taken under the form preserves the filtration, is continuous, and is given on the left multiplication by $(L_a)^\dagger = L_{\sigma(a)}$; the operator algebra is an involutive topological algebra with a valued involution. The unitary elements satisfy $u\sigma(u) = 1$ and, by the Hermitian identity $v(N(u)) = 2v(u)$, lie in $\mathcal{O}^\times$; the unitary group is a closed bounded subgroup of the units, hence compact in the locally compact case, and on $\mathbb{C}$ it is the circle. The self-adjoint elements have norm form the square, the skew elements its negative, and both are closed and acted on by the unitary group with the norm form preserved.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $v$ Hermitian | $v(\sigma(x)) = v(x)$ and $v(x\sigma(x)) = 2v(x)$ |
| $B(x,y) = \tau(x\sigma(y))$ | The Hermitian form; valued by $v$ |
| $N(x) = x\sigma(x)$ | The norm form, $v(N(x)) = 2v(x)$ |
| $T^\dagger$, $B(Tx,y) = B(x,T^\dagger y)$ | The adjoint under the form |
| $(L_a)^\dagger = L_{\sigma(a)}$ | The adjoint of the left multiplication |
| $U(R,\sigma) = \{u : u\sigma(u) = 1\}$ | The unitary group, bounded |
| $U(R,\sigma)\subseteq\mathcal{O}^\times$ | Unitarity forces valuation zero |
| $v(B(x,y))\geq v(x)+v(y)$ | The form is valued |

## Further Reading

- Jean-Pierre Serre, *Local Fields* (Springer, 1979), for the valued field, its units, the norm form and the compactness of the norm-one group.
- Jürgen Neukirch, *Algebraic Number Theory* (Springer, 1999), for Hermitian forms over a valued field and the unitary group.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for Hermitian forms, the norm form and the unitary group over a valued field.
- Seth Warner, *Topological Fields* (North-Holland, 1989), for valued rings, the filtration and the continuous operators.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the symmetric and skew elements and the norm form.
