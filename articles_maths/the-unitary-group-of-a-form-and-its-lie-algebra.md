# __The Unitary Group of a Form and Its Lie Algebra__

## Introduction

The unitary group $U(A,h)$ of *Isometries and the Unitary Group of a Form* is an algebraic group, and every algebraic group has a Lie algebra: the tangent space at the identity, computed by the **dual numbers**. This article computes it, and the answer is the space of the skew-adjoint operators with the commutator:

$$
\mathfrak{u}(A,h) = \{T : T^{*} = -T\} = \operatorname{Lie}\,U(A,h) .
$$

The computation is algebraic and it uses no limit and no topology. The tangent space is the kernel of the map $U(R[\varepsilon]/\varepsilon^{2}) \to U(R)$, the infinitesimal isometries are the operators whose quadratic form $h(Tx,x)$ vanishes to first order, and the first-order condition is exactly the antisymmetry $T^{*} = -T$; this is the algebraic form of the classical statement that the Lie algebra of the isometry group of a form is the space of the skew operators of that form. The bracket is the commutator, and it closes on the skew operators by the sign rule of *Self-Adjoint and Skew Operators of a Form*.

The corresponding structure on the other eigenspace of the involution is the Jordan algebra of *The Hermitian Jordan Algebra of a Form*; the bilinear original is *The Orthogonal Lie Algebra*, the completed reading is *The Lie Algebra and the Exponential Map* and *Unitary and Isometric Operators of the Form* of Part II, and the exponential map that joins the algebra to the group is *The Lie Algebra and the Exponential Map* in Part II. Throughout, $(A,*,h)$ is a sesqualgebra with a form over a base $(R,\varsigma)$ with $h$ nonsingular, $T^{*}$ is the adjoint of $T$ for $h$, and $R[\varepsilon] = R[\varepsilon]/\varepsilon^{2}$ is the ring of the dual numbers over the base.

## The Lie Algebra by the Dual Numbers

**Definition.** The **Lie algebra** of the unitary group is the set of the operators $T$ with

$$
1 + \varepsilon T \in U(A\otimes_{R}R[\varepsilon], h) ,
$$

that is, the set of the first-order deformations of the identity that remain isometries over the dual numbers.

**Proposition.** The Lie algebra is the space of the **skew-adjoint** operators:

$$
\mathfrak{u}(A,h) = \{T : T^{*} = -T\} .
$$

**Proof.** Compute over the dual numbers with $\varepsilon^{2} = 0$:

$$
h\bigl((1+\varepsilon T)x, (1+\varepsilon T)y\bigr) = h(x,y) + \varepsilon\bigl(h(Tx,y) + h(x,Ty)\bigr) .
$$

The first-order condition for the isometry is therefore $h(Tx,y) + h(x,Ty) = 0$ for all $x, y$. Now $h(x,Ty) = h(T^{*}x, y)$ by the Hermitian property and the definition of the adjoint, so the condition reads $h\bigl((T + T^{*})x, y\bigr) = 0$ for all $x,y$, which the nonsingularity of $h$ converts into $T + T^{*} = 0$, that is $T^{*} = -T$.

**Corollary.** The Lie algebra is an $R^{\varsigma}$-submodule of the operators, and it is the kernel of the restriction of the isometry equation to the first order; it is cut out by the linear equations $T^{*} + T = 0$, so it is a module of the same nature as the operators and needs no completion.

**Corollary (the quadratic reading).** When $2$ is invertible and the diagonal determines the Hermitian form, the condition is equivalent to the vanishing of the trace part of the quadratic form, $h(Tx,x) + \varsigma(h(Tx,x)) = 0$ for every $x$; over the trivial base involution this is the vanishing of $h(Tx,x)$ itself, and then the infinitesimal isometries are exactly the operators whose quadratic form vanishes identically.

**Proof.** If $T^{*} = -T$ then $h(Tx,x) = -h(x,Tx) = -\varsigma(h(Tx,x))$, so $h(Tx,x) + \varsigma(h(Tx,x)) = 0$; over the trivial involution the fixed ring is the whole ring and $h(Tx,x) = 0$ as well. Conversely, the diagonal of the Hermitian form $B(x,y) = h(Tx,y) + h(x,Ty)$ is $h(Tx,x) + \varsigma(h(Tx,x))$, which vanishes under the hypothesis; a Hermitian form with vanishing diagonal vanishes when the diagonal determines the forms, so $B = 0$, which is the antisymmetry $T^{*} = -T$. The last clause is the case $\varsigma = \mathrm{id}$.

## The Bracket

**Proposition.** The space $\mathfrak{u}(A,h)$ closes under the commutator,

$$
S, T \in \mathfrak{u}(A,h) \implies [S,T] = ST - TS \in \mathfrak{u}(A,h) ,
$$

and the commutator makes it a Lie algebra over the fixed ring $R^{\varsigma}$.

**Proof.** The sign rule of *Self-Adjoint and Skew Operators of a Form* gives $(ST - TS)^{*} = -\varepsilon\delta(ST-TS)$ with $\varepsilon = \delta = -1$, hence $(ST-TS)^{*} = -(ST-TS)$, which is the closure. The bilinearity, the antisymmetry and the Jacobi identity of the commutator are the associativity of the product of the operators.

**Corollary.** The Lie algebra of the unitary group is the skew part of the algebra of the operators, the self-adjoint part is its complement under the involution of *The Form-Adjoint of an Operator*, and the product of two skew operators splits as

$$
ST = \tfrac{1}{2}[S,T] + \tfrac{1}{2}(ST + TS) ,
$$

with the commutator inside the Lie algebra and the anticommutator leaving it; the anticommutator is the Jordan structure of *The Hermitian Jordan Algebra of a Form*.

## The Algebraic Nature of the Construction

**Proposition.** The tangent space is computed with the dual numbers and not with a limit: the map $U(R[\varepsilon]) \to U(R)$ is the reduction $\varepsilon \mapsto 0$, and its kernel is the Lie algebra. In particular the construction is defined over an arbitrary commutative base with an involution, with no ordered field, no norm and no completion.

**Proof.** The group over the dual numbers is the set of the operators $1 + \varepsilon T$ satisfying the isometry equation with the Gram matrix read over $R[\varepsilon]$; reducing modulo $\varepsilon$ gives the identity, so every element of the kernel is of the shape $1 + \varepsilon T$, and the first-order expansion of the previous section is the computation of the kernel. The reduction map is a homomorphism of groups by the functoriality of the construction of the group.

**Remark (the exponential).** Over $\mathbb{R}$ or $\mathbb{C}$ the exponential of a skew operator is unitary, and the differential of the exponential at $0$ is the identity, so the Lie algebra is the tangent space of the group in the analytic sense as well; the series is analytic, and the exponential and its image are *The Lie Algebra and the Exponential Map* in Part II. In the algebraic layer the Cayley transform of *Self-Adjoint and Skew Operators of a Form* plays the role of the exponential without the series.

## Examples

### The Unitary Group

On $M_n(\mathbb{C})$ with the trace form the Lie algebra is the space of the skew-Hermitian matrices, $\mathfrak{u}(n) = \{T : T^{\dagger} = -T\}$, of real dimension $n^{2}$; its traceless part is $\mathfrak{su}(n)$ of dimension $n^{2}-1$, the Lie algebra of the special unitary group.

### The Orthogonal Group

At the trivial base involution and $* = \mathrm{id}$ the Lie algebra is the space of the matrices with $T^{\mathrm{t}}G + GT = 0$, of dimension $n(n-1)/2$, the orthogonal Lie algebra $\mathfrak{so}(G)$ of *The Orthogonal Lie Algebra*; its structure and its root system are the subject of that article.

### The Symplectic Group

For an alternating form with Gram matrix $J$, the Lie algebra is $\{T : T^{\mathrm{t}}J + JT = 0\}$, the symplectic Lie algebra $\mathfrak{sp}(2n)$, of dimension $n(2n+1)$; the form is alternating and the algebra is the one of the classical groups of the layer.

### The Biquaternion Algebra

On $\mathbb{B}$ with the dagger the Lie algebra of the unitary slice is the space of the anti-Hermitian biquaternions, and the Lie algebra of the Lorentzian form $\operatorname{Sc}(\bar{\tilde Q}\tilde Q')$ is $\mathfrak{so}(2,6)$; the computations are those of *The Form on the Biquaternion Algebra as a General Plain Sesquilinear Form* and *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*.

## Summary

- The **Lie algebra** of the unitary group is the space of the first-order isometries, computed by the dual numbers: $\mathfrak{u}(A,h) = \{T : T^{*} = -T\}$, the **skew-adjoint operators**.
- Equivalently, when $2$ is invertible and the diagonal determines the form, it is the set of the operators whose quadratic form $h(Tx,x)$ has vanishing trace part; over the trivial involution this is $h(Tx,x) = 0$ for every $x$.
- It closes under the commutator by the sign rule, and it is a Lie algebra over the fixed ring $R^{\varsigma}$.
- The construction is algebraic: the kernel of $U(R[\varepsilon]) \to U(R)$, with no limit, no norm and no completion; the analytic exponential is Part II and the Cayley transform is the algebraic substitute.
- The examples are $\mathfrak{u}(n)$, $\mathfrak{su}(n)$, $\mathfrak{so}(G)$, $\mathfrak{sp}(2n)$ and the Lorentzian $\mathfrak{so}(2,6)$ of the biquaternions.
- The complementary structure is the Jordan algebra of the self-adjoint operators, *The Hermitian Jordan Algebra of a Form*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $R[\varepsilon] = R[\varepsilon]/\varepsilon^{2}$ | the ring of the dual numbers over the base |
| $\mathfrak{u}(A,h)$ | the Lie algebra of the skew-adjoint operators |
| $[S,T] = ST - TS$ | the commutator of the operators |
| $\mathfrak{u}(n)$, $\mathfrak{su}(n)$ | the unitary and special unitary Lie algebras |
| $\mathfrak{so}(G)$, $\mathfrak{sp}(2n)$ | the orthogonal and the symplectic Lie algebras |

## Further Reading

- Jean Dieudonné, *La géométrie des groupes classiques*, Ergebnisse der Mathematik 5 (Springer, 1955), for the classical Lie algebras as the skew operators of a form.
- Nathan Jacobson, *Lie Algebras* (Interscience, 1962; Dover reprint, 1979), for the Lie algebra of an algebraic group and the structure of the classical algebras.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for the Lie algebra of the unitary group of a form over a ring with an involution.
