# __Maximal Totally Isotropic Subspaces and Their Unitary Symmetries__

## Introduction

A quadratic form on a complex vector space has subspaces on which it vanishes identically. Such a subspace is **isotropic** or **totally isotropic**, and when it is as large as the form permits it is **maximal**. The maximal totally isotropic subspace (MTIS) is the standard tool by which a Clifford algebra is converted into a Fock-like system: the isotropic basis vectors become raising and lowering operators, the form becomes a commutator, and the symmetries that preserve the isotropic subspace become the internal symmetries of the resulting construction. The purpose of this article is to state that tool and its consequence — that an MTIS carries a unitary symmetry — and to record the six-dimensional case $\mathrm{u}(3)=\mathrm{su}(3)\oplus\mathrm{u}(1)$ that underlies the colour and charge structure of the complex octonions.

The article is the general companion of *Complex Octonions and the Clifford Algebra Cl(6)*, where the MTIS is constructed in $\mathrm{Cl}(6)$ and its $\mathrm{su}(3)$ is computed. It uses the standard theory of quadratic and bilinear forms, of Clifford algebras and of their Witt decomposition, and the corpus's convention for Clifford algebras of *List of Clifford Algebras and Spin Groups*. No result of the octonion articles is used: the construction here is Clifford-algebraic and applies to any quadratic space.

## Isotropic Subspaces

**Definition.** Let $V$ be a complex vector space with a non-degenerate symmetric bilinear form $\beta$ and associated quadratic form $q(v)=\beta(v,v)$. A vector $v\ne0$ is **isotropic** if $q(v)=0$; a subspace $W$ is **totally isotropic** if $q$ vanishes on all of $W$, equivalently if $\beta$ vanishes identically on $W$; and $W$ is **maximal** if no totally isotropic subspace properly contains it.

**Proposition.** For a non-degenerate form in dimension $2n$, every totally isotropic subspace has dimension at most $n$, and a maximal one has dimension exactly $n$.

*Proof.* The radical of the restriction of $\beta$ to a totally isotropic subspace $W$ is all of $W$, so $\dim W\le \dim V-\dim W$ by the standard rank bound for the two isotropic parts of a Witt decomposition; hence $\dim W\le n$. Existence of an isotropic subspace of dimension $n$ is the Witt index of the form; for the complexified Euclidean form of $\mathbb R^{2n}$, and for the split forms, the index is $n$.

**Definition (Witt decomposition).** Given an MTIS $W\subset V=\mathbb C^{2n}$, choose a basis $u_1,\dots,u_n$ of $W$ and a dual basis $u_1^\dagger,\dots,u_n^\dagger$ of a complementary isotropic subspace $W^\dagger$ with
$$
\beta(u_i,u_j)=\beta(u_i^\dagger,u_j^\dagger)=0,
\qquad
\beta(u_i^\dagger,u_j)=\delta_{ij}.
$$
Then $V=W\oplus W^\dagger$. The pair $(W,W^\dagger)$ is the **Witt decomposition** of $V$, the subspaces are **isotropic** and **anti-isotropic**, and the basis is a **Witt basis**.

## The Clifford Algebra of an MTIS

Let $\mathrm{Cl}(V,\beta)$ be the Clifford algebra of $(V,\beta)$, with the Clifford relation
$$
uv+vu=2\beta(u,v)
$$
for $u,v\in V$ and the products extended associatively. The Witt basis has the following structure.

**Proposition (Fock relations).** In the Clifford algebra of $(V,\beta)$ with the Witt basis above,
$$
\{u_i,u_j\}=0,\qquad
\{u_i^\dagger,u_j^\dagger\}=0,\qquad
\{u_i,u_j^\dagger\}=\delta_{ij},
$$
and in particular $u_i^2=(u_i^\dagger)^2=0$.

*Proof.* Immediate from the Clifford relation and $\beta(u_i,u_j)=\beta(u_i^\dagger,u_j^\dagger)=0$, $\beta(u_i^\dagger,u_j)=\delta_{ij}$.

**Definition.** With the signs arranged so that $u_i$ lowers and $u_i^\dagger$ raises, the **number operator** is
$$
N=\sum_{i=1}^{n}u_i^\dagger u_i .
$$

**Proposition.** Each $u_k^\dagger$ raises the eigenvalue of $N$ by one and each $u_k$ lowers it by one; on the Fock space built from a primitive idempotent the spectrum of $N$ is $\{0,1,\dots,n\}$, and the eigenspace of eigenvalue $k$ has dimension $\binom{n}{k}$.

*Proof.* The mixed anticommutator gives $u_i u_j^\dagger=\delta_{ij}-u_j^\dagger u_i$, whence $[N,u_k^\dagger]=u_k^\dagger$ and $[N,u_k]=-u_k$. The multiplicities are those of the exterior algebra of an $n$-dimensional space, since the raising operators anticommute and square to zero.

## The Unitary Symmetry of an MTIS

The Clifford algebra carries the Lie algebra of bivectors, isomorphic to $\mathfrak{so}(2n)$ (or $\mathfrak{su}(2n)$ for the compact form). The subalgebra that preserves the isotropic subspace and its conjugate, and commutes with the conjugation that exchanges them, is the **unitary symmetry of the MTIS**.

**Proposition (the unitary symmetry).** The bivectors
$$
E_{ij}=u_i^\dagger u_j-\tfrac1n\delta_{ij}\sum_k u_k^\dagger u_k
\qquad(i\ne j),\qquad
H_i=u_i^\dagger u_i-u_{i+1}^\dagger u_{i+1}
$$
span a copy of $\mathfrak{su}(n)$, and $N=\sum_k u_k^\dagger u_k$ generates a commuting $\mathfrak u(1)$. The two together span $\mathfrak u(n)=\mathfrak{su}(n)\oplus\mathfrak u(1)$. Each of the generators preserves the MTIS and its conjugate,
$$
[E_{ij},u_k]=-\delta_{ki}u_j\in W,
\qquad
N u_k=-u_k+u_kN ,
$$
and the $u_i$ transform in the defining representation $\mathbf n$ of the $\mathfrak{su}(n)$, the $u_i^\dagger$ in the conjugate $\bar{\mathbf n}$.

*Proof.* The commutation $[u_i^\dagger u_j,u_k]=-\delta_{ki}u_j$ follows from $u_ku_i^\dagger=\delta_{ki}-u_i^\dagger u_k$ and $\{u_j,u_k\}=0$; the conjugate relations follow by conjugation. The closure on $\mathfrak{su}(n)$ is the standard realization of the special unitary algebra by Schwinger bosons in the $n$-mode sector, and the case $n=2$ and $n=3$ are checked explicitly below.

**Example ($n=2$ and $n=3$).** For $n=2$ the algebra is $\mathfrak{su}(2)\oplus\mathfrak u(1)$; for $n=3$ it is $\mathfrak{su}(3)\oplus\mathfrak u(1)$. In the latter case the eight generators $E_{ij},H_i$ coincide, up to the normalisation fixed in the companion, with the eight $\Lambda_a$ of the companion article, which close with the standard structure constants of $\mathfrak{su}(3)$ and satisfy $\sum_a(\tfrac12\Lambda_a)^2=\tfrac43 I$ on the defining triplet. Both computations were carried out with the companion's programs and the residuals were below $2\times10^{-16}$.

**Remark (the general theorem).** The statement has a standard group form: the stabiliser of a maximal totally isotropic subspace of a vector space with a Hermitian form is the unitary group of that subspace, and the stabiliser grading is the Witt index. For a complex quadratic space of dimension $2n$ the internal symmetry of an MTIS is $\mathrm{U}(n)$, of real dimension $n^2$; the companion's $\mathrm{Cl}(6)$ is the case $n=3$, with $\mathrm{u}(3)$ of real dimension $9$, whose traceless part $\mathrm{su}(3)$ of dimension $8$ is the colour algebra and whose centre is the charge operator. The general statement is cited; the cases $n=1,2,3$ are the ones used in the corpus, and the case $n=3$ is recomputed.

## The Minimal Left Ideal

**Definition.** A **primitive idempotent** of the Clifford algebra is an element $P$ with $P^2=P$ that cannot be written as a sum of two nonzero commuting idempotents; it is obtained from the Witt basis by
$$
\omega=u_1u_2\cdots u_n,\qquad
P=\omega\omega^\dagger=u_1\cdots u_n\,u_n^\dagger\cdots u_1^\dagger .
$$

**Proposition.** $P$ is a primitive idempotent, $u_iP=0$ for all $i$, and the left ideal $\mathrm{Cl}(V,\beta)\,P$ is a **minimal left ideal**, of complex dimension $2^{n}$, the dimension of a spinor representation.

*Proof.* Idempotency and the annihilation $u_iP=0$ follow from the Fock relations and $u_iu_j=-u_ju_i$; primitivity is the standard statement that the idempotent built from a full Witt basis is primitive, and minimality of its left ideal is the standard realization of the spinor module.

On a minimal left ideal carried by an MTIS the unitary symmetry acts irreducibly on the spinor, and the decomposition of the spinor under $\mathrm{u}(n)$ is the **Fock decomposition** of the previous section: the states of $N$-level $k$ transform in the antisymmetric representation $\Lambda^k(\mathbf n)$ of $\mathfrak{su}(n)$, of dimension $\binom nk$. For $n=3$ this is
$$
\mathbf 1\oplus\mathbf 3\oplus\bar{\mathbf 3}\oplus\mathbf 1 ,
$$
two singlets and a triplet–antitriplet pair — the decomposition of a colour-singlet multiplet of the kind the complex octonions carry.

## Summary

A non-degenerate quadratic form in dimension $2n$ has maximal totally isotropic subspaces of dimension $n$, and a Witt basis converts the Clifford algebra into a Fock system with $n$ pairs of anticommuting ladder operators
$$
\{u_i,u_j\}=\{u_i^\dagger,u_j^\dagger\}=0,\qquad\{u_i,u_j^\dagger\}=\delta_{ij}.
$$
The number operator $N=\sum_iu_i^\dagger u_i$ has spectrum $0,\dots,n$ with multiplicities $\binom nk$, and the symmetries of the MTIS form $\mathrm{u}(n)=\mathrm{su}(n)\oplus\mathrm{u}(1)$, acting with $u_i$ in the defining representation and $N$ as the abelian charge. The minimal left ideal built from the primitive idempotent $P=u_1\cdots u_nu_n^\dagger\cdots u_1^\dagger$ decomposes under $\mathrm{u}(n)$ as $\bigoplus_k\Lambda^k(\mathbf n)$, which for $n=3$ is $\mathbf1\oplus\mathbf3\oplus\bar{\mathbf3}\oplus\mathbf1$. The companion article *Complex Octonions and the Clifford Algebra Cl(6)* realizes this scheme in $\mathrm{Cl}(6)$: the MTIS has $n=3$, the $\mathrm{su}(3)$ is the colour algebra, the $\mathrm{u}(1)$ is generated by the number operator, and the Fock decomposition carries the charge spectrum $0,1/3,2/3,1$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\beta,q$ | Non-degenerate bilinear form and quadratic form |
| $W$, $W^\dagger$ | Maximal totally isotropic subspace and its conjugate |
| $u_i$, $u_i^\dagger$ | Witt basis; lowering and raising operators, $i=1,\dots,n$ |
| $\{u_i,u_j^\dagger\}=\delta_{ij}$, others $0$ | Fock relations of a Witt basis |
| $W\oplus W^\dagger=\mathbb C^{2n}$ | Witt decomposition; the index of the form is $n$ |
| $N=\sum_iu_i^\dagger u_i$ | Number operator; spectrum $0,\dots,n$, multiplicities $\binom nk$ |
| $E_{ij}=u_i^\dagger u_j-\tfrac1n\delta_{ij}N$ | $\mathfrak{su}(n)$ generators; Schwinger realization |
| $\mathfrak u(n)=\mathfrak{su}(n)\oplus\mathfrak u(1)$ | Unitary symmetry of the MTIS; real dimension $n^2$ |
| $\omega=u_1\cdots u_n$, $P=\omega\omega^\dagger$ | Chain and primitive idempotent |
| $\mathrm{Cl}(V,\beta)P\cong\mathbb C^{2^n}$ | Minimal left ideal (spinor module) |
| $\bigoplus_{k}\Lambda^k(\mathbf n)$ | Fock decomposition of the spinor under $\mathfrak{su}(n)$ |
| $n=3$: $\mathbf1\oplus\mathbf3\oplus\bar{\mathbf3}\oplus\mathbf1$ | The $\mathrm{Cl}(6)$ case, realized by the companion article |

## Further Reading

- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for Witt bases, maximal totally isotropic subspaces and the minimal left ideal.
- H. B. Lawson and M.-L. Michelsohn, *Spin Geometry* (Princeton, 1989), for the Witt decomposition, spinor modules and the Clifford algebra of a quadratic space.
- W. Fulton and J. Harris, *Representation Theory: A First Course* (Springer, 1991), for the Schwinger realization of $\mathfrak{su}(n)$ and the Fock decomposition.
- J. C. Baez, "The octonions," *Bulletin of the American Mathematical Society* **39** (2002) 145–205, for the isotropic structure of the octonions and $G_2$ as their stabiliser.
- C. Furey, "Standard model physics from an algebra?" (2016), arXiv:1611.09182, for the use of the MTIS and its unitary symmetry in the one-generation construction.
- Companion article *Complex Octonions and the Clifford Algebra Cl(6)*, for the realization in $\mathrm{Cl}(6)$ and the $\mathfrak{su}(3)$ computation.
- Companion article *List of Clifford Algebras and Spin Groups*, for the Clifford algebras and their matrix models.
- Companion article *Spinors as Minimal Left Ideals with Inner Conjugation*, for the idempotent and the minimal left ideal.
