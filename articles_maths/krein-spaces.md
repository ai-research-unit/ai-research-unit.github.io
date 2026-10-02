# __Krein Spaces__

## Introduction

A **Krein space** is the complete case of an indefinite inner product space: a vector space with an indefinite Hermitian form that admits a fundamental decomposition into a positive part and a negative part, each of which is complete for the norm it carries. The signature $(p,q)$ is then allowed to be infinite – the two parts may be infinite-dimensional – and the completeness supplies the topology in which the whole theory is done.

The construction has one move. Once a fundamental decomposition is chosen, the indefinite form splits into a positive definite form on the positive part and a negative definite one on the negative part, and summing them with the relative sign removed gives a positive definite inner product on the whole space. The space is complete for this form, so it is a Hilbert space, and the indefinite form is recovered from the Hilbert form by the fundamental symmetry $J$. This is why a Krein space is best described as a Hilbert space with a chosen operator $J$ of square one: the two structures are the same data seen through $J$, and the choice of $J$ is the choice of fundamental decomposition, of which there are many.

What distinguishes a Krein space from a Hilbert space is not the topology – all choices of $J$ give the same topology here, because the norms they induce are equivalent – but the form: it is continuous yet not coercive, it has neutral vectors, and the Cauchy–Schwarz inequality fails along the null directions. This article fixes the definition, the completeness and the norm, the signature, the topology induced by the decomposition, and the precise sense in which a Krein space is not a Hilbert space.

The finite-dimensional indefinite theory, the Gram matrix and the fundamental decomposition are *Indefinite Inner Product Spaces*; the finite rank of negativity is *Pontryagin Spaces*; the operator $J$ is *The Fundamental Symmetry*; the operators that preserve the form are *J-Self-Adjoint and J-Unitary Operators*. Those are cited. The base is $\mathbb{R}$ or $\mathbb{C}$ with its conjugation, the form is $[\cdot,\cdot]$ and the definite inner product it induces through $J$ is $\langle\cdot,\cdot\rangle = [J\cdot,\cdot]$.

## The Definition

**Definition.** A **Krein space** is a vector space $K$ with an indefinite Hermitian form $[\cdot,\cdot]$ such that $K$ admits a fundamental decomposition

$$
K = K_{+} \oplus K_{-}, \qquad K_{+} \perp K_{-},
$$

with $K_{+}$ positive definite and complete for the norm $x\mapsto[x,x]^{1/2}$, $K_{-}$ negative definite and complete for the norm $x\mapsto(-[x,x])^{1/2}$.

**Proposition (the induced Hilbert space).** Let $J$ act as $+\mathrm{id}$ on $K_{+}$ and $-\mathrm{id}$ on $K_{-}$. Then

$$
\langle x, y \rangle = [Jx, y] = [x_{+}, y_{+}] - [x_{-}, y_{-}], \qquad x = x_{+}+x_{-},\ y = y_{+}+y_{-},
$$

is a positive definite inner product on $K$, $K$ is complete for its norm $\|x\|^{2} = \langle x,x\rangle = \|x_{+}\|^{2} + \|x_{-}\|^{2}$, and the indefinite form is recovered by $[x,y] = \langle Jx,y\rangle$. So a Krein space is a Hilbert space with an involutive self-adjoint operator $J$.

**Proof.** The sum of two complete positive definite forms on orthogonal summands is a complete positive definite form, so $K$ is complete for $\langle\cdot,\cdot\rangle$; the recovery is $[x,y] = [J^{2}x,y] = \langle Jx,y\rangle$; the involutivity and the self-adjointness of $J$ are those of *Indefinite Inner Product Spaces*.

**Definition.** The **signature** of the Krein space is the pair $(p,q) = (\dim K_{+}, \dim K_{-})$, each entry a cardinal, possibly infinite. The **rank of negativity** is $q$.

## Completeness and the Norm

**Proposition (completeness is intrinsic).** The completeness of $K$ for the induced norm does not depend on the chosen fundamental decomposition: if $K = K_{+}'\oplus K_{-}'$ is another, the induced norms are equivalent, and $K$ is complete for one exactly when it is complete for the other.

**Proof.** Two fundamental symmetries differ by an operator of the form $\mathrm{id} + T$ with $T$ bounded and $\|T\| < 1$ relative to either induced norm, so each is bounded with bounded inverse for the other; the two norms therefore define the same topology and the same Cauchy sequences.

**Proposition (the form is continuous).** In any of the induced norms the indefinite form is continuous and bounded,

$$
|[x,y]| \leq \|x\|\,\|y\| ,
$$

and the bound is attained on $K_{+}$; on the whole space it is not coercive, since $[x,x]$ takes both signs on the unit sphere.

**Proof.** Cauchy–Schwarz for the positive definite form gives $|[x,y]| = |\langle Jx,y\rangle| \leq \|x\|\|y\|$ since $J$ is an isometry of $\langle\cdot,\cdot\rangle$; the attainment and the failure of coercivity follow from the two summands.

**Remark (the three norms).** Three norms live on a Krein space: the two incomplete norms $\pm[x,x]$ on the summands, and the complete norm $\|x\|$ of the induced Hilbert space. Only the last is defined on all of $K$ by the displayed formula, and it is the one the topology is taken from.

## The Signature

**Theorem (invariance).** The signature $(p,q)$ is independent of the fundamental decomposition: if $K = K_{+}'\oplus K_{-}'$ with $K_{+}'$ positive definite and maximal, then $\dim K_{+}' = p$ and $\dim K_{-}' = q$.

**Proof.** The finite-dimensional case is Sylvester's law of inertia, *Indefinite Inner Product Spaces*, and the infinite-dimensional case is the same argument with the dimension replaced by the cardinal dimension of a maximal positive definite subspace, using that a positive definite subspace meets $K_{-}'$ only at zero.

**Proposition (the possible signatures).** Any pair of cardinals $(p,q)$ occurs: with $\ell^{2}(\kappa)$ denoting a Hilbert space of Hilbert dimension $\kappa$, the orthogonal sum $\ell^{2}(p)\oplus-\ell^{2}(q)$, the negative part carrying the form with the opposite sign, is a Krein space of signature $(p,q)$.

**Proof.** The two summands are complete; the sum with the relative sign on the second summand is an indefinite Hermitian form; the decomposition of the definition is there by construction.

**Remark (the finite case).** A finite-dimensional indefinite inner product space is complete in every norm and is therefore a Krein space of finite signature; so *Indefinite Inner Product Spaces* and *Pontryagin Spaces* are the finite-signature instances. The genuinely new feature of the infinite case is that the completeness has to be assumed, not implied by the dimension.

## The Topology

**Definition.** The **Krein topology** on $K$ is the topology of the induced Hilbert norm $\|x\|^{2} = \langle x,x\rangle$, taken from a fundamental decomposition.

**Proposition.** The Krein topology is well defined by the preceding proposition, it is a Banach space topology, and the following are continuous for it: the linear operations, the indefinite form, the projections onto $K_{\pm}$, and the fundamental symmetry $J$.

**Proof.** Each is either the operation of the Hilbert space or is bounded by the bounds of the form and of $J$.

**Theorem (the orthogonal decomposition fails).** In the Krein topology the decomposition $K = L\oplus L^{\perp}$ may fail for a closed subspace $L$: if $L$ is closed and neutral then $L\subseteq L^{\perp}$ and $K\neq L\oplus L^{\perp}$. Topologically closed and indefinite-orthogonally complemented are distinct notions.

**Proof.** In the plane $\mathbb{R}^{1,1}$ the line $L = \mathrm{span}(e_1+e_2)$ is closed and neutral, and $[e_1+e_2,e_1+e_2] = 0$ gives $L\subseteq L^{\perp}$; the same neutrality transplanted to a closed subspace of a Krein space gives the general failure.

**Remark (why the topology is nevertheless the right one).** In the definite case the form itself supplies the norm; in the indefinite case it does not, since $[x,x]$ takes both signs, so a norm must come from a choice – and the choice is unique up to equivalence. The theorems above say that the resulting topology is a good one but that indefinite orthogonality is strictly weaker than topological complementation. This is the price of dropping positivity.

## Distinction from a Hilbert Space

**Proposition (what is lost).** A Krein space that is not a Hilbert space – that is, with $q \neq 0$ – fails each of the following properties of a Hilbert space:

- the Cauchy–Schwarz inequality: there are $x, y$ with $|[x,y]| > |[x,x]|^{1/2}|[y,y]|^{1/2}$;
- the positivity of the square: $[x,x]$ may be zero or negative;
- the decomposition $K = L\oplus L^{\perp}$ for closed $L$;
- the representation theorem: the map $x\mapsto[x,\cdot]$ carries $K$ to a proper subspace of its dual.

**Proof.** Every failure is witnessed in the plane $\mathbb{R}^{1,1}$ with $x = e_1+e_2$ neutral and $y = e_1$: $[x,x] = 0$ and $[x,y] = 1$, so the Cauchy–Schwarz inequality is violated; the remaining failures are the same neutrality transplanted to a closed subspace.

**Proposition (what is kept).** A Krein space is a Banach space, its form is bounded, the fundamental symmetry is an involution with both eigenspaces definite, and every von Neumann algebraic statement about its bounded operators is the corresponding statement for the induced Hilbert space conjugated by $J$.

**Proof.** The Banach structure and the boundedness are above; the operator statement is the content of *J-Self-Adjoint and J-Unitary Operators*.

**Remark (the one-line summary).** A Krein space is a Hilbert space whose inner product has been replaced by $[x,y] = \langle Jx,y\rangle$ for an involutive self-adjoint operator $J$ of that Hilbert space; the topology is still a Hilbert topology, and it is the form that changes sign.

## Worked Cases

### The Space $\ell^{2}\oplus-\ell^{2}$

The orthogonal sum of two copies of $\ell^{2}$ with the negative form on the second copy is a Krein space of signature $(\aleph_{0},\aleph_{0})$, the prototype of the infinite indefinite case. The unit vector of the first copy is positive, that of the second negative, and their sum is neutral.

### A Pontryagin Space as a Krein Space

On $\ell^{2}$ with the form $[x,y] = \sum_{n\geq2}x_{n}\bar y_{n} - x_{1}\bar y_{1}$ the rank of negativity is $q = 1$ and the space is a Krein space $\Pi_{1}$; the induced Hilbert inner product is the standard one, and $J = \mathrm{diag}(-1,1,1,\ldots)$.

### The Finite Case

On $\mathbb{R}^{2}$ with $[x,y] = x^{1}y^{1} - x^{2}y^{2}$ the space is a Krein space of signature $(1,1)$; it is complete as a finite-dimensional space, and its Krein topology is the usual one. The form is bounded with bound one and not coercive, and the vector $e_1+e_2$ is neutral.

## Summary

A **Krein space** is a vector space with an indefinite Hermitian form admitting a **fundamental decomposition** $K = K_{+}\oplus K_{-}$ into a positive definite and a negative definite part that are orthogonal and each complete for its own norm. The associated **fundamental symmetry** $J$ has square one and is self-adjoint for the form, and $\langle x,y\rangle = [Jx,y]$ is a positive definite inner product for which $K$ is complete; so a Krein space is a **Hilbert space with a chosen operator** $J$, and $[x,y] = \langle Jx,y\rangle$. The **signature** $(p,q) = (\dim K_{+},\dim K_{-})$ may have infinite entries and is independent of the decomposition; every pair of cardinals occurs, and the **Krein topology** is the Hilbert norm topology, the same for all choices of $J$. The form is continuous and bounded but not coercive, so neutrality, the failure of Cauchy–Schwarz and the failure of the orthogonal decomposition $K = L\oplus L^{\perp}$ are exactly what a Krein space loses against a Hilbert space, and the bounded operator theory conjugated by $J$ is exactly what it keeps. The finite-dimensional theory is *Indefinite Inner Product Spaces*, the finite rank of negativity is *Pontryagin Spaces*, the operator $J$ is *The Fundamental Symmetry*, and the operators are *J-Self-Adjoint and J-Unitary Operators*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K = K_{+}\oplus K_{-}$ | Fundamental decomposition of a Krein space |
| $[\cdot,\cdot]$, $\langle\cdot,\cdot\rangle = [J\cdot,\cdot]$ | Indefinite form and induced inner product |
| $J$ | Fundamental symmetry, $J^{2} = \mathrm{id}$, $[Jx,y] = [x,Jy]$ |
| $\|x\|^{2} = \langle x,x\rangle$ | Krein (Hilbert) norm |
| $(p,q)$ | Signature, entries cardinal, possibly infinite |
| $q = \mathrm{rank}$ of negativity | Dimension of $K_{-}$ |
| $\ell^{2}(p)\oplus-\ell^{2}(q)$ | Model of signature $(p,q)$ |
| $[x,x] = 0$ | Neutral vector; the failure of Cauchy–Schwarz |

## Further Reading

- János Bognár, *Indefinite Inner Product Spaces*, Ergebnisse der Mathematik und ihrer Grenzgebiete 78 (Springer, 1974), for the complete indefinite case and its topology.
- Tomas Ya. Azizov and Iosif S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric* (Wiley, 1989), for Krein spaces and their operators.
- Mark G. Krein, *Introduction to the Theory of Linear Non-Self-Adjoint Operators* (American Mathematical Society, 1969), for the fundamental symmetry and the geometry of the indefinite form.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the finite-signature and the Pontryagin cases as instances.
- Vladimir A. Khatskevich and David Shoiykhet, *Differentiable Operators and Nonlinear Equations* (Birkhäuser, 1994), for the topology of a Krein space and the failure of the orthogonal projection.
