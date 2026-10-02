
# __The Signed Adjoint of the Left Multiplication on a Topological Vector Space__

## Introduction

The signed left multiplication $\Lambda^{\alpha}_{a} = L_{a}\alpha$ is the signed sandwich with right factor one, and its adjoint with respect to the trace form of the category is the signed right multiplication $\Theta^{\alpha}_{1,\alpha(a)}$, the operator $x \mapsto \alpha(x)\alpha(a)$: the adjoint of the one-sided signed operator is again one-sided, with the parameter imaged by the grade involution and the side exchanged. The article records the computation, its relation to the adjoint of the general signed sandwich, the unsigned case, and the self-adjointness and unitarity criteria of the one-sided operators: $\Lambda^{\alpha}_{a}$ is self-adjoint exactly when $a$ is central and fixed by the grade involution, and unitary exactly when $a$ and $\alpha(a)$ are central involutions.

This article develops the adjoint of the signed left multiplication. The signed left multiplication and its laws are *The Signed Left Multiplication on a Topological Vector Space*; the adjoint computation of the signed family is *The Signed Adjoint Sandwich on a Topological Vector Space*, of which this is the case $b = 1$; the trace form and the unsigned adjoint $(L_{a})^{\dagger} = R_{a}$ are *The Adjoint of the Left Multiplication on a Topological Vector Space*. The module-level variant is *The Graded Adjoint Action on a Module over a Topological Vector Space*. The forms are Part III.

Throughout, $E$ is a Hausdorff locally convex algebra over $\mathbb{K}$ with a unit and jointly continuous multiplication, $\tau$ is a continuous trace and $\langle x, y\rangle = \tau(xy)$ the trace form of the category, assumed non-degenerate, ${}^{\dagger}$ is the trace-adjoint, $\alpha$ is a trace-preserving grade involution, $\Lambda^{\alpha}_{a} = L_{a}\alpha$ is the signed left multiplication, $\Theta^{\alpha}_{a,b}(x) = a\alpha(x)b$ is the signed sandwich and $\Phi_{a,b}(x) = axb$ the unsigned one, and $Z(E)$ is the centre.

## The Adjoint Computation

**Theorem (the adjoint of the signed left multiplication).** For every $a \in E$ the signed left multiplication has the trace-adjoint

$$
(\Lambda^{\alpha}_{a})^{\dagger} = \Theta^{\alpha}_{1,\alpha(a)} = R_{\alpha(a)}\alpha ,
$$

the signed right multiplication by $\alpha(a)$, mapping $x$ to $\alpha(x)\alpha(a)$; the adjoint of a signed left multiplication is a signed right multiplication, with the parameter imaged by the grade involution.

**Proof.** This is *The Signed Adjoint Sandwich on a Topological Vector Space* with right factor $b = 1$: $\Lambda^{\alpha}_{a} = \Theta^{\alpha}_{a,1}$, so $(\Lambda^{\alpha}_{a})^{\dagger} = \Theta^{\alpha}_{\alpha(1),\alpha(a)} = \Theta^{\alpha}_{1,\alpha(a)}$, and $\Theta^{\alpha}_{1,\alpha(a)}(x) = \alpha(x)\alpha(a)$.

**Corollary (relation to the sandwich and the unsigned case).** The adjoint of the one-sided operator is the boundary case $b = 1$ of the general sandwich adjoint, and for $\alpha = \mathrm{id}$ it reduces to

$$
(L_{a})^{\dagger} = R_{a} ,
$$

the adjointness of the left and right multiplications of *The Adjoint of the Left Multiplication on a Topological Vector Space*; the signed left multiplication is therefore the one-sided boundary of the signed family, and the sign enters only in the parameter $\alpha(a)$.

**Proof.** Set $\alpha = \mathrm{id}$ in the theorem; the unsigned statement is the cited one.

**Proposition (the conjugate form).** The signed left multiplication has the conjugate and sandwich forms

$$
\Lambda^{\alpha}_{a} = \Theta^{\alpha}_{a,1} = \alpha\,L_{\alpha(a)} ,
$$

so it is the signed sandwich with right factor one and the grade involution composed with the unsigned left multiplication; consequently its adjoint is also the signed sandwich with left factor one, $(\Lambda^{\alpha}_{a})^{\dagger} = \Theta^{\alpha}_{1,\alpha(a)}$, the symmetry exchanging the two boundary cases.

**Proof.** $\Lambda^{\alpha}_{a}(x) = a\alpha(x) = \alpha(\alpha(a)x) = \alpha(L_{\alpha(a)}x)$, using $\alpha^{2} = \mathrm{id}$; the adjoint is the theorem, and $\Theta^{\alpha}_{1,\alpha(a)}$ is the sandwich with left factor one.

## Self-Adjointness and Unitarity

**Proposition (self-adjointness criterion).** The signed left multiplication is self-adjoint for the trace form,

$$
\Lambda^{\alpha}_{a} = (\Lambda^{\alpha}_{a})^{\dagger} ,
$$

exactly when $a$ is central and fixed by the grade involution,

$$
a \in Z(E) \quad \text{and} \quad \alpha(a) = a .
$$

**Proof.** $\Theta^{\alpha}_{a,1} = \Theta^{\alpha}_{1,\alpha(a)}$ means $a\alpha(x) = \alpha(x)\alpha(a)$ for all $x$; evaluating at $x = 1$ gives $a = \alpha(a)$, and then the identity reads $a\alpha(x) = \alpha(x)a$ for all $x$, that is $a \in Z(E)$ because $\alpha$ is surjective. Conversely a central, $\alpha$-fixed $a$ satisfies both.

**Proposition (unitarity criterion).** The signed left multiplication is unitary for the trace form exactly when both $a$ and $\alpha(a)$ are central involutions,

$$
a^{2} = \alpha(a)^{2} = 1 , \qquad a, \alpha(a) \in Z(E) ,
$$

the case $b = 1$ of the unitarity criterion of the signed sandwich; for $\alpha = \mathrm{id}$ this is the single condition that $a$ be a central involution.

**Proof.** Substitute $b = 1$ in the products of *The Signed Adjoint Sandwich on a Topological Vector Space*: $u = \alpha(1)\alpha(a) = \alpha(a)$ and $w = a\cdot1 = a$, and apply the criterion that both be central involutions.

**Corollary (the inverse).** For invertible $a$ the signed left multiplication is invertible with

$$
(\Lambda^{\alpha}_{a})^{-1} = \Lambda^{\alpha}_{\alpha(a)^{-1}} ,
$$

and the unitary signed left multiplications with invertible parameter form a subgroup of the unitary group of the trace form; the self-adjoint and the unitary one-sided operators intersect in the central involutions fixed by $\alpha$, that is in the parameters that are both $\alpha$-fixed central and central involutions.

**Proof.** The inverse formula is *The Signed Left Multiplication on a Topological Vector Space*; the unitary elements form a group, and the intersection is read from the two criteria: $a$ central and $\alpha$-fixed, and $a$, $\alpha(a)$ central involutions, together force $a^{2} = 1$ and $a = \alpha(a) \in Z(E)$.

## Examples

**Example (the unsigned case).** For $\alpha = \mathrm{id}$ the signed left multiplication is the left multiplication, $(L_{a})^{\dagger} = R_{a}$; it is self-adjoint exactly when $a$ is central, and unitary exactly when $a$ is a central involution, so the group of unitary left multiplications is the central subgroup of involutions.

**Example (the inner case).** For $\alpha = \alpha_{r} = \mathrm{Ad}_{r}$ an inner grade involution and $a = r$, the signed left multiplication $\Lambda^{\alpha_{r}}_{r}$ has adjoint $\Theta^{\alpha_{r}}_{1,r} = R_{r}\alpha_{r}$, and since $\alpha_{r}(r) = r$ the self-adjointness criterion holds when $r$ is central; the reflection's one-sided signed operator is self-adjoint in that case and unitary when $r$ is a central involution.

**Example (the order-two signed operator).** The signed left multiplication satisfies $\Lambda^{\alpha}_{a}\Lambda^{\alpha}_{b} = L_{a\alpha(b)}$, so the product of two signed left multiplications is an unsigned left multiplication; the two products $\Lambda^{\alpha}_{a}\Lambda^{\alpha}_{b}$ and $\Lambda^{\alpha}_{b}\Lambda^{\alpha}_{a}$ differ by the commutator of $a\alpha(b)$ and $b\alpha(a)$, which is the obstruction to the commuting of the signed left multiplications.

## Summary

The signed left multiplication $\Lambda^{\alpha}_{a} = L_{a}\alpha$ has the trace-adjoint $\Theta^{\alpha}_{1,\alpha(a)} = R_{\alpha(a)}\alpha$, the signed right multiplication by $\alpha(a)$; the adjoint of the one-sided signed operator is one-sided, with the side exchanged and the parameter imaged by the grade involution, and the computation is the case $b = 1$ of the adjoint of the general signed sandwich, reducing to $(L_{a})^{\dagger} = R_{a}$ when $\alpha = \mathrm{id}$. The operator is self-adjoint exactly when $a$ is central and $\alpha$-fixed, and unitary exactly when $a$ and $\alpha(a)$ are central involutions; it is invertible for invertible $a$ with inverse $\Lambda^{\alpha}_{\alpha(a)^{-1}}$, and the invertible unitary signed left multiplications form a subgroup of the unitary group of the trace form. The module-level variant of the group is *The Graded Adjoint Action on a Module over a Topological Vector Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Lambda^{\alpha}_{a} = L_{a}\alpha$ | signed left multiplication, $x \mapsto a\alpha(x)$ |
| $\Lambda^{\alpha}_{a} = \Theta^{\alpha}_{a,1} = \alpha L_{\alpha(a)}$ | sandwich and conjugate forms |
| $(\Lambda^{\alpha}_{a})^{\dagger} = \Theta^{\alpha}_{1,\alpha(a)} = R_{\alpha(a)}\alpha$ | the adjoint |
| $(L_{a})^{\dagger} = R_{a}$ | the unsigned case |
| $a \in Z(E)$, $\alpha(a) = a$ | the self-adjointness criterion |
| $a, \alpha(a)$ central involutions | the unitarity criterion |
| $(\Lambda^{\alpha}_{a})^{-1} = \Lambda^{\alpha}_{\alpha(a)^{-1}}$ | the inverse |
| $\langle x,y\rangle = \tau(xy)$ | trace form |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the one-sided operators, the involutions and the adjointable operators.
- Jacques Dixmier, *von Neumann Algebras* (North-Holland, 1981), for the traces, the unitary elements and the one-sided multiplications.
- Serge Lang, *Algebra* (Springer, third edition, 2002), for the graded algebras and the one-sided operators.
- Albrecht Pietsch, *Operator Ideals* (North-Holland, 1980), for the trace functionals and the duality of the trace form.
- Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces* (Springer, second edition, 1999), for the topological algebras and the bilinear forms.
