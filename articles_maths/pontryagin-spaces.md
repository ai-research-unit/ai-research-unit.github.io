# __Pontryagin Spaces__

## Introduction

A **Pontryagin space** is a Krein space whose negative part is finite-dimensional. The rank of negativity $\kappa = \dim K_{-}$ is then a natural number, the space is written $\Pi_{\kappa}$, and the finiteness of $\kappa$ restores much of the behaviour of a Hilbert space: every self-adjoint operator has an invariant maximal negative subspace, the non-real part of its spectrum is bounded by $\kappa$, and the finite-dimensional theory is a clean linear algebra of the spaces $\mathbb{C}^{p,q}$.

The number $\kappa$ is the defect from a Hilbert space. When $\kappa = 0$ the space is a Hilbert space and the classical spectral theorem holds without exception. When $\kappa$ is positive but finite, an operator that is self-adjoint for the indefinite form may acquire non-real eigenvalues, but only at most $\kappa$ of them, counted with multiplicity, and always in conjugate pairs; a positive invariant subspace of dimension all but $\kappa$ exists; and the operator is "almost" Hilbert. This article fixes the definition, the finite-dimensional linear algebra of $\mathbb{C}^{p,q}$, the spectral theorem in the finite-dimensional and the Pontryagin form, and the role of the single number $\kappa$.

The general indefinite theory is *Indefinite Inner Product Spaces*, the complete case with infinite rank of negativity is *Krein Spaces*, the operator $J$ is *The Fundamental Symmetry*, and the operator theory of the indefinite form – the $J$-self-adjoint and $J$-unitary operators, the definitizable operators and the Krein–Naĭmark theorem – is *J-Self-Adjoint and J-Unitary Operators* and *Definitizable Operators and the Krein–Naĭmark Theorem*. Those are cited. The base is $\mathbb{R}$ or $\mathbb{C}$ with its conjugation, the form is $[\cdot,\cdot]$, and $\kappa$ is the rank of negativity.

## Pontryagin Spaces and the Rank of Negativity

**Definition.** A **Pontryagin space** of rank of negativity $\kappa$ is a Krein space $K$ with $\dim K_{-} = \kappa < \aleph_{0}$; it is written $\Pi_{\kappa}$. The rank of negativity is also called the **index** of the space.

**Proposition.** $\Pi_{0}$ is exactly a Hilbert space. In $\Pi_{\kappa}$ the positive part $K_{+}$ may be of any dimension, finite or infinite, so the signature is $(p,\kappa)$ with $p$ arbitrary; the model spaces are $\mathbb{C}^{p}\oplus-\mathbb{C}^{\kappa}$ and $\ell^{2}\oplus-\mathbb{C}^{\kappa}$.

**Proof.** $\kappa = 0$ makes the negative part zero; the models are the Krein model of *Krein Spaces* with one of the two cardinals finite.

**Proposition (every subspace is almost positive).** Every subspace $L$ of $\Pi_{\kappa}$ satisfies $\dim(L\cap L^{\perp}) \leq \kappa$, and the restriction of the form to $L$ is degenerate only along that radical, of dimension at most $\kappa$. In particular a subspace of dimension exceeding $\kappa$ contains a positive vector.

**Proof.** A neutral vector of $L$ generates a one-dimensional neutral subspace, and a neutral subspace of $\Pi_{\kappa}$ has dimension at most $\kappa$ by counting against the negative part; the last statement follows because a subspace all of whose vectors are non-positive has dimension at most $\kappa$.

**Remark ($\kappa$ as the defect).** The single number $\kappa$ bounds simultaneously: the dimension of a neutral or a negative subspace, the dimension of the radical of a restriction, the number of non-real eigenvalues of a self-adjoint operator, and the codimension of an invariant positive subspace. This is the sense in which $\Pi_{\kappa}$ is a Hilbert space with a bounded defect, and $\Pi_{1}$ – one negative direction – is the most-used instance.

## The Finite-Dimensional $\mathbb{C}^{p,q}$

**Definition.** Write $\mathbb{C}^{p,q}$ for $\mathbb{C}^{n}$, $n = p+q$, with the form

$$
[x,y] = \sum_{i=1}^{p}x_{i}\bar y_{i} - \sum_{j=p+1}^{n}x_{j}\bar y_{j} .
$$

It is a Pontryagin space $\Pi_{\kappa}$ with $\kappa = q$ and finite positive part of dimension $p$; the real analogue $\mathbb{R}^{p,q}$ is defined by the same formula.

**Proposition (the operators of the form).** A linear operator $A$ on $\mathbb{C}^{p,q}$ with matrix $A$ in the standard basis is **self-adjoint** for the form exactly when

$$
G A = A^{\dagger} G, \qquad G = \mathrm{diag}(1,\ldots,1,-1,\ldots,-1),
$$

and **unitary** for the form exactly when $A^{\dagger}GA = G$. The self-adjoint operators of the form form a real Lie algebra and the unitary ones a group, the $\dagger$ being the Hilbert adjoint in the standard inner product.

**Proof.** The two identities are the definitions $[Ax,y] = [x,Ay]$ and $[Ax,Ay] = [x,y]$ written in the standard basis, where $[x,y] = x^{\dagger}Gy$.

**Proposition (the admissible normal form).** If $A$ is self-adjoint for the form and the restriction of the form to a spectral subspace is definite, the restriction is diagonalisable with real eigenvalues; a non-real eigenvalue of such an $A$ has a conjugate partner, and the pair occupies at least one dimension of the negative part, so at most $\kappa$ conjugate pairs \u2013 equivalently at most $2\kappa$ non-real eigenvalues counted with multiplicity, or $\kappa$ in the open upper half-plane \u2013 can occur.

**Proof.** On a definite invariant subspace the form is an inner product and $A$ is an ordinary self-adjoint operator there; each non-real eigenvalue consumes at least one dimension of the negative part, and there are only $\kappa$ of them.

**Remark (the standard inner product is the companion).** The Hilbert inner product $\langle x,y\rangle = x^{\dagger}y$ and the indefinite form $[x,y] = x^{\dagger}Gy$ differ by the diagonal sign matrix $G$, which is the fundamental symmetry; the operators of the form are the Hilbert operators satisfying the twisted self-adjointness, and the whole linear algebra of $\mathbb{C}^{p,q}$ is the linear algebra of $\mathbb{C}^{n}$ conjugated by $G$.

## Self-Adjoint Operators and the Spectral Theorem

### The Finite-Dimensional Theorem

**Theorem.** Let $A$ be self-adjoint for the form on a finite-dimensional indefinite inner product space $V$. Then the eigenvalues of $A$ are either real or occur in conjugate pairs; the root subspaces of distinct eigenvalues of the same type are orthogonal when the eigenvalues are real and distinct, and a non-real eigenvalue $\lambda$ has the same algebraic and geometric multiplicity as its conjugate $\bar\lambda$, with the root subspace of $\bar\lambda$ the complex conjugate of that of $\lambda$. The non-real eigenvalues form conjugate pairs; there are at most $\kappa = \min(p,q)$ such pairs occurring in the open upper half-plane, equivalently at most $2\kappa$ non-real eigenvalues counted with multiplicity.

**Proof.** The conjugate pairing is the reality of the characteristic polynomial modulo the order reversal induced by the form; the orthogonality of the real root subspaces is the identity $[Ax,y] = [x,Ay]$ applied to eigenvectors; and each conjugate pair of non-real eigenvalues forces a two-dimensional indefinite subspace on which the form is neutral, so a $\kappa$-dimensional negative part can serve at most $\kappa$ pairs.

**Corollary (diagonalisation on the definite part).** The definite part of $V$ supports ordinary self-adjoint theory: on the positive definite subspace the restrictions of a self-adjoint $A$ are diagonalisable over $\mathbb{R}$, and the same holds on the negative definite subspace after the sign is changed.

**Proof.** Restriction of the form to a definite subspace is an inner product, and the identity $[Ax,y] = [x,Ay]$ becomes ordinary self-adjointness.

### The Pontryagin Theorem

**Theorem (Pontryagin).** Let $A$ be a self-adjoint operator on $\Pi_{\kappa}$ with $\kappa$ finite. Then the non-real eigenvalues of $A$ occur in conjugate pairs, there are at most $\kappa$ of them in the open upper half-plane, equivalently at most $2\kappa$ counted with multiplicity; $A$ has an invariant maximal negative subspace of dimension at most $\kappa$; and there is an invariant positive definite subspace of $\Pi_{\kappa}$ complementary to it. Consequently $A$ is the orthogonal sum of a self-adjoint operator on a Hilbert space and a finite-dimensional self-adjoint operator on the negative part.

**Proof.** The bound on the non-real eigenvalues is the finite-dimensional argument applied to a Pontryagin subspace containing the negative part of $A$, the existence of the invariant maximal negative subspace is by a fixed-point argument – the same statement for the finite-dimensional case and the extension to $\Pi_{\kappa}$ by the invariance of the negative part; the complementary positive subspace is its orthogonal complement, invariant because the two are invariant.

**Remark (the spectral theorem is finite-dimensional here).** The theorem is stated and proved with eigenvalues and root subspaces, not with a spectral resolution of the identity; the invariant subspace theorem, the bound on the non-real eigenvalues and the conjugate pairing are the content. The general spectral function of an unbounded self-adjoint operator on a Krein space, its critical points and the resolvent are *Spectral Theory on Krein Spaces* and, for the analytic machinery, *Analysis on Linear Spaces* (Part III), which owns the spectral theorem and the resolvent.

## The Role of $\kappa$

**Proposition (six faces of $\kappa$).** In $\Pi_{\kappa}$ the number $\kappa$ is simultaneously: the dimension of the negative part and of every maximal negative subspace; the maximal dimension of a neutral subspace; the bound on $\dim(L\cap L^{\perp})$ for every subspace $L$; the bound $\kappa$ on the number of non-real eigenvalues in the upper half-plane, that is $2\kappa$ with multiplicity, of any self-adjoint operator; the codimension of the invariant positive definite subspace of the Pontryagin theorem; and the dimension of the null eigenspace at the boundary of definitisability.

**Proof.** Each statement is one of the preceding propositions, read in the order in which they appear.

**Remark (why finiteness matters).** Every one of the six statements fails for infinite $\kappa$: an infinite negative part can hold infinitely many neutral directions and infinitely many non-real eigenvalue pairs, and the invariant positive subspace of codimension $\kappa$ need not exist with a complement. The finiteness of $\kappa$ is exactly what makes the theory behave like a finite perturbation of the Hilbert theory.

## Worked Cases

### The Space $\mathbb{C}^{1,1}$

The form $[x,y] = x_{1}\bar y_{1} - x_{2}\bar y_{2}$ has $\kappa = 1$. The operator $A = \mathrm{diag}(1,-1)$ is self-adjoint for the form, with eigenvalues $\pm1$ and eigenvectors $e_1,e_2$; the operator with matrix $\begin{pmatrix}0 & 1 \\ -1 & 0\end{pmatrix}$ is also self-adjoint for the form, with eigenvalues $\pm i$; that is the single non-real pair that $\kappa = 1$ allows.

### A Pontryagin Space of Infinite Positive Part

On $\ell^{2}\oplus-\mathbb{C}$ with $[x,y] = \sum_{n\geq1}x_{n}\bar y_{n} - x_{0}\bar y_{0}$ the index is $1$ and the positive part is infinite-dimensional. A self-adjoint operator that is a compact perturbation of a diagonal real operator has at most one conjugate pair of non-real eigenvalues, and the invariant negative subspace is at most one-dimensional, as the theorem requires.

### The Signature and the Index

In $\mathbb{R}^{2,3}$ the signature is $(2,3)$ and $\kappa = 3$: there are three negative directions, a maximal neutral subspace has dimension $2 = \min(2,3)$, and a self-adjoint operator can have at most three conjugate pairs of non-real eigenvalues, that is six with multiplicity.

## Summary

A **Pontryagin space** $\Pi_{\kappa}$ is a Krein space with **finite rank of negativity** $\kappa = \dim K_{-}$; the positive part may be infinite, and $\Pi_{0}$ is a Hilbert space. The index $\kappa$ is the defect from a Hilbert space, and it bounds, all at once, the negative and neutral dimensions, the radical of any restricted form, the number of conjugate pairs of non-real eigenvalues of a self-adjoint operator and the codimension of its invariant positive subspace. The finite-dimensional **$\mathbb{C}^{p,q}$** is a Pontryagin space of index $q$: an operator is self-adjoint for the form exactly when $GA = A^{\dagger}G$, and the whole linear algebra is that of $\mathbb{C}^{n}$ twisted by the diagonal sign matrix, the fundamental symmetry. The **spectral theorem** is stated with eigenvalues and root subspaces: a self-adjoint operator has real eigenvalues, and its non-real eigenvalues come in conjugate pairs with at most $\kappa$ of them in the upper half-plane and at most $2\kappa$ counted with multiplicity, and on a definite invariant subspace it is an ordinary self-adjoint operator. **Pontryagin's theorem** supplies an invariant maximal negative subspace and a complementary invariant positive one, so the operator is a Hilbert self-adjoint operator plus a finite-dimensional negative piece. The general indefinite theory is *Indefinite Inner Product Spaces*, the complete case *Krein Spaces*, the operator $J$ *The Fundamental Symmetry*, and the unbounded spectral theory is *Spectral Theory on Krein Spaces* with the analytic machinery deferred to *Analysis on Linear Spaces* (Part III).

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Pi_{\kappa}$ | Pontryagin space of rank of negativity $\kappa$ |
| $\kappa = \dim K_{-}$ | Index, or rank of negativity |
| $\mathbb{C}^{p,q}$, $\mathbb{R}^{p,q}$ | Finite Pontryagin spaces, $\kappa = q$ |
| $G = \mathrm{diag}(1,\ldots,-1,\ldots)$ | Fundamental symmetry, Gram matrix of the standard form |
| $GA = A^{\dagger}G$ | Self-adjointness for the form |
| $A^{\dagger}GA = G$ | Unitarity for the form |
| $\leq\kappa$ conjugate pairs | Spectral theorem: $\leq2\kappa$ non-real eigenvalues with multiplicity |
| $\dim(L\cap L^{\perp})\leq\kappa$ | The radical bound for a subspace |

## Further Reading

- L. S. Pontryagin, "Hermitian operators in spaces with indefinite metric", *Izvestiya Akad. Nauk SSSR. Ser. Mat.* **8** (1944), 243–280, for the invariant subspace theorem and the bound on the non-real eigenvalues.
- János Bognár, *Indefinite Inner Product Spaces*, Ergebnisse der Mathematik und ihrer Grenzgebiete 78 (Springer, 1974), for the theory of $\Pi_{\kappa}$ and its spectral theorem.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for $\mathbb{C}^{p,q}$ and the self-adjoint operators of an indefinite form.
- Tomas Ya. Azizov and Iosif S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric* (Wiley, 1989), for the Pontryagin spaces and their invariant subspaces.
- Mark G. Krein and Heinz Langer, "On the spectral function of a self-adjoint operator in a space with indefinite metric", *Doklady Akad. Nauk SSSR* **152** (1963), 1264–1267, for the boundary of definitisability.
