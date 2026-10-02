# __Indefinite Inner Product Spaces__

## Introduction

A positive definite Hermitian form is a length: it decides which vectors are long, which are short, and which are at right angles, and the whole geometry of a Hilbert space follows. Dropping positivity while keeping non-degeneracy gives an **indefinite inner product space**, and the geometry changes in kind. There is no length any more, there are vectors of zero length, the orthogonal complement of a subspace need not meet it only at zero, and the "orthogonal" bases are not the positive ones unless the form is signed.

What survives is a rigid arithmetic. The Gram matrix of an indefinite Hermitian form is a Hermitian matrix, congruence replaces the change of basis, Sylvester's law of inertia fixes the numbers of positive and negative squares, and over $\mathbb{R}$ these two numbers classify the form. The space admits a decomposition into a positive definite part and a negative definite part, orthogonal to each other, and although the decomposition is not unique the two ranks are fixed. Choosing one such decomposition produces an operator $J$, the **fundamental symmetry**, which turns the indefinite form into a positive definite one by $[x,y] = \langle Jx, y\rangle$; $J$ is involutive and is self-adjoint for the indefinite form, and it is the bridge over which the whole definite theory is imported.

This article treats the finite-dimensional case and the general theory of the indefinite form; the complete case is *Krein Spaces*, the finite rank of negativity is *Pontryagin Spaces*, and the operator $J$ with its non-uniqueness and its order structure is *The Fundamental Symmetry*. The definite forms and the inertia law are *Bilinear Forms*, *Quadratic Forms and Polarisation* and *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*, and the conventions for a sesquilinear form are *Conventions in Mathematics*; Sylvester's law of inertia is *Quadratic Forms and Polarisation*. Those are cited. The base is $F = \mathbb{R}$ or $\mathbb{C}$, $\sigma$ is the conjugation, and a form is Hermitian when $[x,y] = \sigma([y,x])$.

## Indefinite Forms and the Gram Matrix

**Definition.** An **inner product space** is a vector space $V$ over $F$ with a sesquilinear form $[\cdot,\cdot] : V\times V\to F$ that is **Hermitian**, $[x,y] = \sigma([y,x])$, and **non-degenerate**, $[x,y] = 0$ for every $y$ only when $x = 0$. It is **indefinite** when there are $x$ with $[x,x] > 0$ and $y$ with $[y,y] < 0$; the value $[x,x]$ is the **scalar square** of $x$.

**Definition.** The **Gram matrix** of a basis $e_1, \ldots, e_n$ is the Hermitian matrix $G$ with entries $G_{ij} = [e_i, e_j]$; if $x = \sum x^{i}e_i$ and $y = \sum y^{j}e_j$ then $[x,y] = \sum_{i,j}x^{i}G_{ij}\sigma(y^{j})$. Under the change of basis with matrix $P$ the Gram matrix becomes $P^{\dagger}GP$, and the form is non-degenerate exactly when $\det G \neq 0$.

**Proof.** Direct expansion of the sesquilinear form in the basis, and the standard criterion for non-degeneracy of a Hermitian form.

**Definition.** Two forms are **congruent** when their Gram matrices are related by $G' = P^{\dagger}GP$ for an invertible $P$, that is when there is a basis change carrying one to the other.

## The Radical and Non-Degeneracy

**Definition.** The **radical** of a Hermitian form is

$$
\mathrm{rad}(V) = \{\, x \in V : [x,y] = 0 \text{ for every } y \in V \,\} .
$$

**Proposition.** $\mathrm{rad}(V)$ is a subspace and the form is non-degenerate exactly when $\mathrm{rad}(V) = 0$. For a subspace $W$, $\dim W + \dim W^{\perp} = \dim V + \dim(W\cap\mathrm{rad}(V))$, so for a non-degenerate form on $V$ one has $\dim W + \dim W^{\perp} = \dim V$, and the form restricted to $W$ is non-degenerate exactly when $W\cap W^{\perp} = 0$.

**Proof.** The first statement is the definition. For the second, the map $x\mapsto [x,\cdot]$ from $V$ to the dual is an isomorphism when the form is non-degenerate, and it carries $W^{\perp}$ to the annihilator of $W$; the dimension count follows, and the restricted form is non-degenerate exactly when $W\cap W^{\perp} = 0$.

**Remark (the radical is the difference from the definite case).** For a positive definite form the radical vanishes and $V = W\oplus W^{\perp}$ for every subspace; for an indefinite form both fail. A subspace containing a nonzero vector of $W^{\perp}$ is its own trap, and the failure $V \neq W\oplus W^{\perp}$ is the source of nearly every difficulty of the indefinite theory.

## Inertia and the Signature

**Definition.** A vector is **positive**, **negative** or **neutral** according as $[x,x] > 0$, $[x,x] < 0$ or $[x,x] = 0$; a subspace is **positive definite**, **negative definite** or **neutral** when every nonzero vector in it is positive, negative or neutral. The **rank of positivity** $p$ and the **rank of negativity** $q$ are the maximal dimensions of a positive definite and of a negative definite subspace, and $(p,q)$ is the **signature**.

**Theorem (Sylvester's law of inertia).** In finite dimension the signature is independent of the space and of the basis: if $V = W_{+}\oplus W_{-}$ with $W_{+}$ positive definite and $W_{-}$ negative definite and orthogonal, then $p = \dim W_{+}$ and $q = \dim W_{-}$ for every such decomposition. Equivalently, there is a basis in which the Gram matrix is the diagonal matrix with $p$ entries $+1$ and $q$ entries $-1$, and the pair $(p,q)$ is an invariant.

**Proof.** The finite-dimensional argument of *Quadratic Forms and Polarisation* and *Hermitian Forms*: a maximal positive definite subspace has its dimension bounded by the sign of the form on a complement, and two such subspaces have the same dimension by counting the neutral vectors of a difference.

**Definition.** The **inertia index** is the triple $(p,q,z)$ with $z = \dim \mathrm{rad}(V)$; for a non-degenerate form $z = 0$ and the inertia index is the signature.

**Proposition.** $p + q + z = \dim V$, and the form is positive definite exactly when $q = 0$, negative definite exactly when $p = 0$, definite when $pq = 0$, and indefinite otherwise.

**Proof.** The sum is the statement that a maximal positive definite and a maximal negative definite subspace are orthogonal and their orthogonal sum meets the radical only at zero, which is the last part of Sylvester's theorem.

## Classification over $\mathbb{R}$ and $\mathbb{C}$

**Theorem (classification over $\mathbb{R}$).** A non-degenerate symmetric bilinear form on a finite-dimensional real space is determined up to congruence by its signature $(p,q)$; equivalently, two forms are congruent exactly when they have the same signature. The orthogonal group of the form is $O(p,q)$, and the definite cases are $O(n)$ and $O(n)$ for the two signs.

**Proof.** Sylvester's law gives the normal form $\mathrm{diag}(1,\ldots,1,-1,\ldots,-1)$, and two normal forms with the same signature are congruent by a permutation of the basis.

**Theorem (classification over $\mathbb{C}$).** A non-degenerate Hermitian form on a finite-dimensional complex space is determined up to congruence by its **signature** $(p,q)$, and the isometry group is the unitary group $U(p,q)$.

**Proof.** For a Hermitian form over $\mathbb{C}$ the scalar square $[\lambda x,\lambda x] = |\lambda|^{2}[x,x]$ is real and its sign is unchanged by the scaling, so the sign of a diagonal entry is an invariant and the normal form $\mathrm{diag}(1,\ldots,1,-1,\ldots,-1)$ cannot be altered beyond a permutation; the argument is the one over $\mathbb{R}$ with $|\lambda|^{2}$ in place of $\lambda^{2}$.

**Corollary (bilinear against sesquilinear over $\mathbb{C}$).** A **symmetric bilinear** form over $\mathbb{C}$ is classified by its rank alone, because then $[\lambda x,\lambda x] = \lambda^{2}[x,x]$ and the scaling by $i$ turns $-1$ into the square $i^{2}$; the signature is a Hermitian phenomenon and survives over $\mathbb{C}$ precisely because the scalar square is a modulus square. The indefinite theory is therefore stated over a field with an involution and a real-valued scalar square, of which $\mathbb{R}$ and $\mathbb{C}$ are the two familiar cases.

## Positive, Negative and Neutral Subspaces

**Proposition.** A subspace $W$ is positive definite exactly when $[x,x] > 0$ for every nonzero $x \in W$; equivalently, the restricted form is positive definite. The maximal positive definite subspaces have dimension $p$ and the maximal negative definite subspaces have dimension $q$; the orthogonal complement of a maximal positive definite subspace is negative semidefinite, and every vector decomposes uniquely as its component in that subspace plus a component orthogonal to it.

**Proof.** The characterisation is the definition and the dimension statement is Sylvester's theorem. For the rest, let $W$ be a maximal positive definite subspace and $v\in W^{\perp}$: if $[v,v] > 0$ then $W\oplus Fv$ is an orthogonal sum of two definite subspaces and hence positive definite of dimension $p+1$, contradicting maximality, so $[v,v]\leq 0$ and $W^{\perp}$ is negative semidefinite. Conversely, since $W$ is definite the map $w'\mapsto[\cdot,w']$ is an isomorphism $W\to W^{*}$, so every $v$ has a unique decomposition $v = w + v_{\perp}$ with $w\in W$ and $v_{\perp}\perp W$; the scalar square is additive, $[v,v] = [w,w] + [v_{\perp},v_{\perp}]$, so a negative $v$ has $[v_{\perp},v_{\perp}]\leq[v,v] < 0$.

**Remark (neutral vectors and the light cone).** The set of neutral vectors is the **null cone** of the form, and through every neutral vector there is a one-dimensional maximal neutral subspace; in signature $(p,q)$ the maximal neutral subspaces have dimension $\min(p,q)$. The language of the null cone is differential-geometric and is not used here; only its linear-algebraic part, the maximal neutral subspace, belongs to this article.

## The Fundamental Decomposition

**Definition.** A **fundamental decomposition** of $V$ is an orthogonal direct sum

$$
V = V_{+} \oplus V_{-}, \qquad V_{+} \perp V_{-},
$$

with $V_{+}$ positive definite and $V_{-}$ negative definite.

**Theorem (existence and non-uniqueness).** Every indefinite inner product space of finite dimension has a fundamental decomposition, with $\dim V_{+} = p$ and $\dim V_{-} = q$; and if both $p$ and $q$ are nonzero the decomposition is not unique, the space admitting as many as the positive definite subspaces of dimension $p$.

**Proof.** Take a maximal positive definite subspace $V_{+}$ and let $V_{-} = V_{+}^{\perp}$; since $V_{+}$ is maximal and the form is non-degenerate, $V_{-}$ is negative definite and $V = V_{+}\oplus V_{-}$. For the non-uniqueness, the graph $M_T = \{v_{+} + Tv_{+} : v_{+} \in V_{+}\}$ of a linear map $T : V_{+}\to V_{-}$ with $[v_{+},v_{+}] + [Tv_{+},Tv_{+}] > 0$ for $v_{+}\neq0$, that is $|[Tv_{+},Tv_{+}]| < [v_{+},v_{+}]$ is again positive definite and maximal, and different $T$ give different decompositions.

**Remark (the decomposition is the substitute for an orthonormal basis).** A fundamental decomposition is the indefinite replacement of the orthogonal splitting into eigenspaces of a definite form: it separates the positive from the negative directions, and its two ranks are the signature. It is the first structure that the indefinite case possesses and the definite case does not need to name.

## The Fundamental Symmetry

**Definition.** Associated with a fundamental decomposition $V = V_{+}\oplus V_{-}$ is the operator $J$ acting as $+\mathrm{id}$ on $V_{+}$ and as $-\mathrm{id}$ on $V_{-}$.

**Proposition.** $J$ is linear, $J^{2} = \mathrm{id}$, $J$ is self-adjoint for the indefinite form, $[Jx,y] = [x,Jy]$, and it commutes with the projections onto $V_{\pm}$; conversely every involutive self-adjoint operator whose eigenspaces are definite arises from a fundamental decomposition.

**Proof.** The first two statements are immediate from the definition; for the self-adjointness, both sides are $[x_{+},y_{+}] - [x_{-},y_{-}]$ after decomposing; the converse is the spectral decomposition of an involutive operator with definite eigenspaces.

**Theorem (the bridge).** With $J$ as above, the form

$$
\langle x, y \rangle = [Jx, y]
$$

is a positive definite inner product on $V$, and the indefinite form is recovered from it by $[x,y] = \langle Jx,y\rangle$. So every indefinite inner product space is, after the choice of a fundamental decomposition, a definite one, and the two differ by the operator $J$.

**Proof.** Decompose $x = x_{+}+x_{-}$ and $y = y_{+}+y_{-}$ with $x_{\pm},y_{\pm}\in V_{\pm}$; the orthogonality of $V_{+}$ and $V_{-}$ kills the mixed terms and $\langle x,y\rangle = [Jx,y] = [x_{+},y_{+}] - [x_{-},y_{-}]$, a sum of two definite forms of the same sign and hence positive definite. For the recovery, $\langle Jx,y\rangle = [J^{2}x,y] = [x,y]$ because $J^{2} = \mathrm{id}$.

**Remark (the non-uniqueness of $J$).** The operator $J$ depends on the chosen fundamental decomposition and is not unique when both $p$ and $q$ are nonzero; all the choices are conjugate by the isometries of the indefinite form. The one thing that is unique is the pair of ranks, and therefore the induced positive definite inner products all have the same Hilbert-space completion. The full theory of $J$, its order structure and its role as the bridge, is *The Fundamental Symmetry*.

## Worked Cases

### The Plane $\mathbb{R}^{1,1}$

On $\mathbb{R}^{2}$ with form $[x,y] = x^{1}y^{1} - x^{2}y^{2}$ the signature is $(1,1)$: the vector $e_1$ is positive, $e_2$ is negative, and $e_1+e_2$ is neutral. The fundamental decompositions are the spans of $e_1$ and $e_2$, and the graphs of the maps $e_1\mapsto te_2$ with $|t| < 1$; the associated $J$'s are $\mathrm{diag}(1,-1)$ in each adapted basis, and the positive definite forms $\langle x,y\rangle = [Jx,y]$ are all equivalent.

### The Space $\mathbb{C}^{2,1}$

On $\mathbb{C}^{3}$ with $[x,y] = x^{1}\overline{y^{1}} + x^{2}\overline{y^{2}} - x^{3}\overline{y^{3}}$ the signature is $(2,1)$, the null cone is a cone of neutral complex directions, and the maximal neutral subspaces are one-dimensional.

### Inertia of a Form by Congruence

On $\mathbb{R}^{3}$ with $[x,y] = x^{1}y^{2}+x^{2}y^{1} - x^{3}y^{3}$ the Gram matrix of the standard basis is $\mathrm{diag}$-free with determinant $1$, so the form is non-degenerate; its inertia index is $(1,2,0)$: a positive direction is $e_1+e_2$, of square $2$, and a negative definite plane is $\mathrm{span}(e_1-e_2,\,e_3)$, of squares $-2$ and $-1$ and orthogonal. The signature is $(1,2)$, the form is indefinite, and the computation is Sylvester's law in action.

## Summary

An **indefinite inner product space** is a vector space with a non-degenerate Hermitian form that is neither positive nor negative definite; its Gram matrix is Hermitian, and congruence is the change of basis. The **radical** is the set orthogonal to everything, non-degeneracy is its vanishing, and the failure of $V = W\oplus W^{\perp}$ is the hallmark of the indefinite case. **Sylvester's law of inertia** fixes the signature $(p,q)$, the numbers of positive and negative squares, and the signature classifies the form over $\mathbb{R}$ and over $\mathbb{C}$ alike; a **symmetric bilinear** form over $\mathbb{C}$, by contrast, has only its rank as an invariant, because a bilinear scaling squares the scalar. Vectors are positive, negative or neutral, and the maximal neutral subspaces have dimension $\min(p,q)$. Every space admits a **fundamental decomposition** $V = V_{+}\oplus V_{-}$ into a positive definite and a negative definite part, orthogonal, with $\dim V_{\pm} = p, q$, and the decomposition is not unique when both ranks are nonzero. Each decomposition produces the **fundamental symmetry** $J$, involutive and self-adjoint for $[\,,\,]$, and $\langle x,y\rangle = [Jx,y]$ is a positive definite inner product; so $J$ is the bridge between the indefinite and the definite theories. The complete case is *Krein Spaces*, the finite rank of negativity *Pontryagin Spaces*, and $J$ itself *The Fundamental Symmetry*; the definite forms and the inertia law are *Bilinear Forms*, *Quadratic Forms and Polarisation* and *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $[\cdot,\cdot]$ | Indefinite Hermitian form |
| $[x,x]$ | Scalar square of $x$ |
| $G$, $P^{\dagger}GP$ | Gram matrix; congruence |
| $\mathrm{rad}(V)$ | Radical of the form |
| $W^{\perp}$, $W\cap W^{\perp}$ | Orthogonal complement; the test for non-degeneracy of $W$ |
| $(p,q)$, $z$ | Signature and the dimension of the radical |
| $V = V_{+}\oplus V_{-}$ | Fundamental decomposition |
| $J$, $\langle x,y\rangle = [Jx,y]$ | Fundamental symmetry and the definite inner product |
| $O(p,q)$ | Isometry group of the real form of signature $(p,q)$ |

## Further Reading

- János Bognár, *Indefinite Inner Product Spaces*, Ergebnisse der Mathematik und ihrer Grenzgebiete 78 (Springer, 1974), for the finite-dimensional theory and the fundamental decomposition.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the Gram matrix and the inertia of an indefinite form.
- Sergei G. Krein, *Functional Analysis* (Pergamon, 1972), for linear operators and the elements of the indefinite theory.
- Winfried Scharlau, *Quadratic and Hermitian Forms*, Grundlehren der mathematischen Wissenschaften 270 (Springer, 1985), for Sylvester's law and the classification over $\mathbb{R}$ and $\mathbb{C}$.
- Tomas Ya. Azizov and Iosif S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric* (Wiley, 1989), for the indefinite form, its subspaces and the operators that preserve it.
