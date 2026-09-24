
# __Spectral Triples and Noncommutative Geometry__

## Introduction

A spectral triple is the data needed to do Riemannian geometry with a noncommutative algebra of functions: a $*$-algebra $A$ represented on a Hilbert space $H$, together with a self-adjoint operator $D$ on $H$ whose commutators with the elements of $A$ are bounded. The operator $D$ is the metric datum — it defines a distance on the state space of $A$ — and the algebra $A$ is the algebra of coordinates, commutative in the classical case and not otherwise. The whole chain of this category converges here: the Clifford modules supply the operator, the spin representations supply the Hilbert space, the reality conditions supply the real structure, and the index theorem supplies the pairing with $K$-theory.

This article states the definition and the axioms, derives the distance formula, records the role of the real structure and the KO-dimension, explains the reconstruction of a spin manifold from its algebra of functions, describes the Connes–Chern character and the local index formula, defines the spectral dimension, and gives the finite-dimensional examples. The Clifford and spin theory used is from *Spin Representations and Clifford Modules* and *Real Spinors and Reality Conditions*; the twisted Cauchy–Riemann operator is from *Clifford Modules and the Twisted Cauchy–Riemann Operator*; the index pairing is from *The Atiyah–Singer Index Theorem and K-Theory*; and the algebra and module conventions are those of the category.

## Spectral Triples

**Definition.** A **spectral triple** $(A,H,D)$ consists of a unital $*$-algebra $A$, a separable Hilbert space $H$ with a faithful $*$-representation $\pi\colon A\to\mathcal{B}(H)$, and a densely defined self-adjoint operator $D$ on $H$, the **operator** or **metric datum**, such that

1. the commutators $[D,\pi(a)]$ extend to bounded operators on $H$ for all $a\in A$, and
2. $D$ has compact resolvent, $(D-i)^{-1}$ compact.

The triple is **even** if there is a $\mathbb{Z}/2$-grading $\gamma$ on $H$, $\gamma=\gamma^{*}$, $\gamma^{2}=1$, with $\gamma D=-D\gamma$ and $\gamma\pi(a)=\pi(a)\gamma$ for all $a\in A$; and **odd** otherwise.

**Definition.** The **dimension** of a spectral triple is the number $p>0$ such that the eigenvalues $\lambda_n$ of $|D|$, listed with multiplicity, satisfy $\lambda_n\sim C n^{1/p}$; equivalently, such that the heat trace has the asymptotic $\operatorname{Tr}(e^{-tD^{2}})\sim a_0 t^{-p/2}$ as $t\to0^{+}$. A spectral triple of finite dimension is also required to satisfy the following **axioms**: *regularity*, that $\pi(a)$ and $[D,\pi(a)]$ lie in the domain of every iterated commutator with $|D|$; *finiteness*, that the smooth domain $H^{\infty}=\bigcap_k\operatorname{Dom}D^{k}$ is a finitely generated projective $A$-module; *reality*, the existence of a real structure (below); *first order*, that $[[D,\pi(a)],\pi(b)^{o}]=0$ for all $a,b$, where $\pi(b)^{o}$ is the opposite representation; and *orientation*, that the Hochschild cycle representing the volume element maps to the chirality operator.

**Remark.** The axioms are the algebraic shadow of the properties of a first-order elliptic operator on a closed spin manifold. The boundedness of the commutators is the statement that $D$ is a first-order differential operator; the compactness of the resolvent is the statement that the manifold is closed, so that the spectrum of $D$ is discrete; the dimension is the growth rate of the spectrum; and the finiteness axiom makes the smooth domain a projective module, so that it can serve as the module of sections of a bundle.

## The Operator as Metric Datum

The operator $D$ defines a metric on the state space of the algebra, and in the commutative case it recovers the geodesic distance.

**Definition.** Let $\mathcal{S}(A)$ be the set of states of $A$, that is, the positive linear functionals of norm one. The **Connes distance** on $\mathcal{S}(A)$ is

$$
d(\varphi,\psi)=\sup\bigl\{\,|\varphi(a)-\psi(a)| \ :\ a\in A,\ \|[D,\pi(a)]\|\leq1\,\bigr\}.
$$

**Theorem.** The function $d$ is symmetric, satisfies the triangle inequality, and takes values in $[0,+\infty]$, so it is a pseudometric on the state space; two states satisfy $d(\varphi,\psi)=0$ exactly when they agree on the constraint set $C=\{a\in A:\|[D,\pi(a)]\|\leq1\}$, so $d$ is a metric exactly when $C$ separates the states. It is finite-valued when the constraint set is norm-bounded, in particular in the commutative case of the theorem below.

**Proof.** Symmetry is immediate from the definition. For the triangle inequality, $|\varphi(a)-\psi(a)|\leq|\varphi(a)-\chi(a)|+|\chi(a)-\psi(a)|$ pointwise, and the supremum over the constraint set is subadditive. The vanishing statement is the definition: $d(\varphi,\psi)=0$ says that $\varphi$ and $\psi$ take the same value at every element of $C$. Norm-boundedness of $C$ bounds $d$, because $|\varphi(a)-\psi(a)|\leq2\|a\|$ for states of norm one. $\square$

**Theorem (commutative case).** Let $M$ be a closed spin Riemannian manifold, let $A=C^{\infty}(M)$ act on $H=L^{2}(M,S)$ by pointwise multiplication, and let $D$ be the Cauchy–Riemann operator of the spinor bundle. Then the pure states of $A$ are the points of $M$ and

$$
d(x,y)=\text{the geodesic distance from }x\text{ to }y.
$$

**Proof.** For $f\in C^{\infty}(M)$ the commutator of $D$ with multiplication by $f$ is Clifford multiplication by the gradient, $[D,f]=c(df)$, so $\|[D,f]\|=\|df\|_{\infty}=\sup_M|\nabla f|$. The Connes distance is therefore

$$
d(x,y)=\sup\bigl\{|f(x)-f(y)|:\|\nabla f\|_{\infty}\leq1\bigr\}.
$$

The supremum is at most the geodesic distance, since $|f(x)-f(y)|\leq\|\nabla f\|_\infty\cdot(\text{length of a shortest geodesic})$. It is at least the geodesic distance: the function $f(z)=\min\{\rho(x,z),\rho(x,y)\}$ is $1$-Lipschitz, vanishes at $x$ and equals $\rho(x,y)$ at $y$, and a mollification in local charts produces smooth functions agreeing with it at $x$ and at $y$ up to an arbitrarily small error and having no larger Lipschitz constant, so the constraint $\|\nabla f\|_{\infty}\leq1$ is met and the value $\rho(x,y)$ is approached. Hence equality. $\square$

**Remark.** The distance formula is the reason $D$ is called the metric datum: it is the operator, not a metric tensor, that encodes the geometry. The formula is manifestly algebraic — it uses only the representation and the commutators — so it makes sense for an arbitrary algebra, and it is the definition of the metric in the noncommutative case. In the finite example of the last section it computes the distance between the points of a two-point space, which is a noncommutative-geometric distance on a finite set.

## The Real Structure and the KO-Dimension

**Definition.** A **real structure** on an even spectral triple $(A,H,D,\gamma)$ is an antilinear isometry $J\colon H\to H$ with

$$
J^{2}=\varepsilon\,\mathrm{id}, \qquad JD=\varepsilon'\,DJ, \qquad J\gamma=\varepsilon''\,\gamma J, \qquad \varepsilon,\varepsilon',\varepsilon''\in\{\pm1\},
$$

satisfying the **order-zero** and **order-one** conditions

$$
[\pi(a),J\pi(b)J^{-1}]=0, \qquad [[D,\pi(a)],J\pi(b)J^{-1}]=0 \qquad (a,b\in A).
$$

The **KO-dimension** of the triple is the residue $n\bmod8$ determined by the signs $(\varepsilon,\varepsilon',\varepsilon'')$ according to the table below.

| $n\bmod8$ | $\varepsilon=J^{2}$ | $\varepsilon'$ in $JD=\varepsilon'DJ$ | $\varepsilon''$ in $J\gamma=\varepsilon''\gamma J$ |
|---|---|---|---|
| $0$ | $+1$ | $+1$ | $+1$ |
| $1$ | $+1$ | $-1$ | — |
| $2$ | $-1$ | $+1$ | $-1$ |
| $3$ | $-1$ | $-1$ | — |
| $4$ | $-1$ | $+1$ | $+1$ |
| $5$ | $-1$ | $-1$ | — |
| $6$ | $+1$ | $+1$ | $-1$ |
| $7$ | $+1$ | $-1$ | — |

**Theorem.** The signs $(\varepsilon,\varepsilon',\varepsilon'')$ are the invariants of the real structure, and the KO-dimension is periodic of period eight. For the commutative spectral triple of a closed spin manifold of dimension $m$, the KO-dimension is $m\bmod8$.

**Proof sketch.** The existence of $J$ with prescribed signs is the statement that the spinor bundle carries a charge conjugation compatible with the Clifford action, which is the eightfold periodic reality condition of the classification; the compatibility of the signs with the Clifford relations forces period eight, as in *Bott Periodicity and the Classification*. For the spin manifold the real structure is the charge conjugation on the spinor bundle, and a direct computation of its square and its commutation with the chirality gives the residue of the dimension. $\square$

**Remark.** The KO-dimension is the spectral form of the eightfold way: it is the same period eight that appears in the real Clifford classification, in the reality types of *Real Spinors and Reality Conditions*, and in the real $KO$-theory of *The Atiyah–Singer Index Theorem and K-Theory*. The table records the two signs $\varepsilon$ and $\varepsilon''$ that the charge conjugation carries, arranged by the dimension modulo eight; the trichotomy of real, complex and quaternionic type appears in the commuting normalisation of the Clifford module, where the classes without a commuting conjugation are the complex ones. Its eightfold repetition is the reason the finite geometries of the applications fall into a finite list.

**Remark (normalisation).** The sign of $J^{2}$ in the table is that of the **charge conjugation**, normalised by the order-one condition and by the commutation rule $JD=\varepsilon'DJ$; this is the normalisation standard in the spectral-triple setting, and for a spin manifold of dimension $m$ it gives the residue $m\bmod8$. The type table of *Real Spinors and Reality Conditions* classifies instead the reality structures that commute with Clifford multiplication, which is the normalisation appropriate to the real forms of the Clifford module. The two are related by composition with the volume element, which flips the sign of $J^{2}$ in exactly those dimensions where $\omega^{2}=-1$; consequently the two tables coincide for $m\equiv0,1,4,5\bmod8$, the classes in which $\omega^{2}=+1$, and differ by the twist in the remaining classes, while the eightfold periodicity and the trichotomy of types are common to both.

## The Commutative Case and Reconstruction

**Theorem (Connes' reconstruction).** Let $(A,H,D)$ be a commutative spectral triple satisfying the axioms of dimension, regularity, finiteness, reality, first order and orientation, with $A$ commutative as a $*$-algebra. Then there is a closed spin Riemannian manifold $M$, a spinor bundle $S\to M$ and a spin structure such that

$$
A\cong C^{\infty}(M), \qquad H\cong L^{2}(M,S), \qquad D\cong\text{the Cauchy–Riemann operator of }S,
$$

and the reconstruction is functorial.

**Proof sketch.** The algebra $A$ is the algebra of smooth functions on the space of characters, a closed manifold $M$; the boundedness axiom makes $D$ a first-order differential operator and the compactness of the resolvent makes $M$ compact; the dimension axiom fixes the dimension of $M$; the orientation axiom identifies the Hochschild cycle with the volume form and gives the volume element; and the reality axiom produces the spin structure together with the spinor bundle whose charge conjugation is $J$. The identification of $D$ with the Cauchy–Riemann operator is the local computation of the symbol. $\square$

**Corollary.** A commutative spectral triple satisfying the axioms is exactly a closed spin manifold with its spinor geometry, up to isomorphism. The noncommutative theory therefore generalises rather than replaces the classical one: every spin manifold is a spectral triple, and the spectral triples that satisfy the axioms but whose algebra is not the algebra of functions on a manifold are the genuinely noncommutative geometries.

**Remark.** The reconstruction theorem is the reason the axioms are chosen as they are: they are the minimal algebraic conditions that force the classical theory in the commutative case and remain meaningful in the noncommutative case. The condition of reality, in particular, is what makes the spin structure recoverable; without it the charge conjugation is unavailable and the orientation axioms fix only the oriented Riemannian geometry.

## Cyclic Cohomology and the Connes–Chern Character

**Definition.** For a $*$-algebra $A$, the **cyclic cohomology** $HC^{\bullet}(A)$ is the cohomology of the complex of cyclic multilinear functionals: a cyclic $n$-cochain is a multilinear functional $\varphi\colon A^{n+1}\to\mathbb{C}$ satisfying the cyclicity $\varphi(a_0,\dots,a_n)=(-1)^{n}\varphi(a_n,a_0,\dots,a_{n-1})$, and the differential is the Hochschild coboundary restricted to cyclic cochains.

**Definition.** Let $(A,H,D)$ be an even spectral triple of finite dimension with grading $\gamma$. The **Connes–Chern character** is the cyclic cocycle

$$
\operatorname{ch}(D)(a_0,\dots,a_n)=\operatorname{Tr}\bigl(\gamma\,a_0[D,a_1]\cdots[D,a_n]\,e^{-D^{2}}\bigr),
$$

of even degree, a closed cyclic cocycle modulo coboundaries; the operator $e^{-D^{2}}$ regularises the trace, and the boundedness of the commutators makes each term trace-class.

**Theorem (index pairing).** Let $e\in M_N(A)$ be an idempotent representing a class $[e]\in K_0(A)$. Then the compression $eDe$ is a Fredholm operator on the range of $e$, the pairing of its index with the Connes–Chern character is

$$
\langle\operatorname{ch}(D),[e]\rangle=\operatorname{index}(eDe),
$$

computed in the graded sense, and it depends only on the cyclic cohomology class of $\operatorname{ch}(D)$ and the $K$-theory class of $e$.

**Proof sketch.** The compressed operator $eDe$ is essentially self-adjoint with compact resolvent; its grading splitting has finite-dimensional kernel and cokernel, and the McKean–Singer supertrace argument expresses the index as the trace of $\gamma e\,e^{-(eDe)^{2}}$, which expands into the cyclic expression defining the character. The pairing is well defined because a coboundary in cyclic cohomology pairs trivially with $K$-theory. $\square$

**Theorem (Connes–Moscovici local index formula).** Let $(A,H,D)$ be a spectral triple with finite dimension spectrum. Then the Connes–Chern character is a sum of residues of zeta functions at the points of the dimension spectrum, each residue being a local expression in $D$ and the elements of $A$; in particular the character is computable from the small-time asymptotics of the heat kernel of $D$.

**Proof sketch.** This is the local index theorem of Connes–Moscovici. The zeta functions $\zeta(s)=\operatorname{Tr}(P|D|^{-s})$ have meromorphic continuations whose poles form the dimension spectrum; the coefficients of the heat kernel expansion are the residues, and assembling them into a cyclic cocycle gives the character. $\square$

**Remark.** The two theorems are the spectral analogues of the index theorem and its local form. The index pairing is the pairing of $K$-theory with cyclic cohomology that generalises the Chern character pairing of the manifold case, and the local index formula is the statement that the character is local, so that it can be computed from the asymptotics of $D$ rather than from global data. The reader will recognise in the local formula the spectral version of the heat-kernel proof of *The Atiyah–Singer Index Theorem and K-Theory*.

## Spectral Dimension and Heat Kernel Asymptotics

**Definition.** A spectral triple has **dimension spectrum** $\Sigma$, a discrete subset of $\mathbb{C}$, if for every element $a$ of a suitable algebra the zeta functions $\operatorname{Tr}(a|D|^{-s})$ extend meromorphically to $\mathbb{C}$ with poles contained in $\Sigma$. The **spectral dimension** is the largest real number in $\Sigma$, equal to the growth exponent $p$ of the eigenvalues of $|D|$.

**Theorem.** For a spectral triple of spectral dimension $p$, the heat trace has the small-time asymptotic expansion

$$
\operatorname{Tr}\bigl(e^{-tD^{2}}\bigr)\sim\sum_{k}a_{k}\,t^{-(p-k)/2}\qquad(t\to0^{+}),
$$

with locally computable coefficients, and the **Weyl law** for the counting function $N(\lambda)=\#\{n:|\lambda_n|\leq\lambda\}$ is $N(\lambda)\sim C\lambda^{p}$.

**Proof sketch.** The heat kernel estimate follows from the parametrix construction for the operator $D^{2}$, whose symbol is $|\xi|^{2}$; the leading term is the volume of the manifold (in the commutative case) times $(4\pi t)^{-p/2}$, and the coefficients are integrals of local invariants. The Weyl law is the Abelian theorem relating the asymptotics of the heat trace as $t\to0$ to the counting function. $\square$

**Corollary.** In the commutative case the spectral dimension is the dimension of the manifold and the leading heat coefficient is the volume; the metric dimension is recovered from the spectrum of $D$ alone. The dimension spectrum contains, in addition to the dimension, the smaller integers and half-integers at which the coefficients of the expansion occur, and in the noncommutative case it need not be a single point.

## Finite-Dimensional Examples

**Definition.** A **finite spectral triple** is a spectral triple with $H$ finite-dimensional and $D$ a self-adjoint matrix; the axioms become purely algebraic conditions on a finite-dimensional representation.

**Example (the two-point space).** Let $A=\mathbb{C}\oplus\mathbb{C}$ act on $H=\mathbb{C}^{2}$ by $\pi(a,b)=\operatorname{diag}(a,b)$, and let

$$
D=\begin{pmatrix}0&m\\ m&0\end{pmatrix}
$$

with $m>0$ real. Then $(A,H,D)$ is an odd spectral triple of dimension zero, the commutators are

$$
[D,\pi(a,b)]=\begin{pmatrix}0&m(b-a)\\ m(a-b)&0\end{pmatrix}, \qquad \|[D,\pi(a,b)]\|=m|a-b|,
$$

and the Connes distance between the two pure states $\varphi_1(a,b)=a$ and $\varphi_2(a,b)=b$ is

$$
d(\varphi_1,\varphi_2)=\sup\{|a-b|:m|a-b|\leq1\}=\frac{1}{m}.
$$

The two-point space is thus a metric space whose distance is the inverse of the off-diagonal entry of $D$, and the triple reconstructs a finite geometry from a matrix.

**Example (matrix algebras).** Let $A=M_n(\mathbb{C})$ act on $H=\mathbb{C}^n\oplus\mathbb{C}^n$ and let $D=\begin{pmatrix}0&M\\ M^{*}&0\end{pmatrix}$ for an invertible matrix $M$. The triple is even with grading $\operatorname{diag}(1,-1)$, the KO-dimension is determined by the signs of the reality structure if one is present, and the index pairing with the class of a projection $e\in M_n(\mathbb{C})$ computes the index of the compression of $D$.

**Example (almost commutative geometry).** Let $(A_M,H_M,D_M)$ be the commutative spectral triple of a closed spin manifold $M$ and let $(A_F,H_F,D_F)$ be a finite spectral triple. Then

$$
A=A_M\otimes A_F, \qquad H=H_M\otimes H_F, \qquad D=D_M\otimes1+\gamma_M\otimes D_F
$$

is a spectral triple, the **almost commutative** geometry. Its dimension spectrum contains the dimension of $M$, and the fluctuations of the operator $D$ by the inner automorphisms of $A$, $D\mapsto D+\sum_ia_i[D,b_i]$, are the noncommutative generalisations of the passage from an operator to a twisted one, that is, of the connections of the classical geometry. The finite factor supplies the internal degrees of freedom, and the whole construction is an algebraic and purely mathematical generalisation of the spin geometry of $M$.

**Remark.** The finite examples show that the theory is non-vacuous in degree zero and that the metric information can be entirely discrete. They also exhibit the two roles of the operator: as the metric datum through the distance formula, and as the $K$-homology class through the index pairing. In the almost commutative case both roles are combined, and the operator is the sum of the geometric operator of $M$ and the internal operator of the finite factor.

## Summary

A spectral triple $(A,H,D)$ is a represented $*$-algebra with a self-adjoint operator of compact resolvent whose commutators with the algebra are bounded; it is even when a chirality grading is present, and it satisfies the axioms of dimension, regularity, finiteness, reality, first order and orientation. The operator is the metric datum: the Connes distance $d(\varphi,\psi)=\sup\{|\varphi(a)-\psi(a)|:\|[D,a]\|\leq1\}$ recovers the geodesic distance in the commutative case, where the pure states are the points of a spin manifold and $[D,f]=c(df)$.

A real structure is an antilinear $J$ with signs $J^{2}=\varepsilon$, $JD=\varepsilon'DJ$ and $J\gamma=\varepsilon''\gamma J$, the order-zero and order-one conditions, and a KO-dimension that is periodic of period eight; for a spin manifold of dimension $m$ the KO-dimension is $m\bmod8$. By Connes' reconstruction theorem a commutative spectral triple satisfying the axioms is exactly a closed spin manifold with its spinor geometry, so the noncommutative theory generalises the classical one.

The Connes–Chern character is the cyclic cocycle $\operatorname{ch}(D)(a_0,\dots,a_n)=\operatorname{Tr}(\gamma a_0[D,a_1]\cdots[D,a_n]e^{-D^{2}})$; its pairing with $K_0(A)$ is the index of the compressed operator $eDe$, and the Connes–Moscovici local index formula computes the character as a sum of residues at the points of the dimension spectrum. The spectral dimension is the growth exponent of the spectrum of $D$, the heat trace has the asymptotic expansion $\operatorname{Tr}(e^{-tD^{2}})\sim\sum_ka_kt^{-(p-k)/2}$, and in the commutative case the leading coefficient is the volume. Finite-dimensional examples include the two-point space, where the distance is the inverse of the off-diagonal entry of $D$, and the almost commutative geometries $A_M\otimes A_F$, $D=D_M\otimes1+\gamma_M\otimes D_F$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(A,H,D)$ | Spectral triple: algebra, Hilbert space, operator |
| $\pi\colon A\to\mathcal{B}(H)$ | Representation of $A$ |
| $[D,\pi(a)]$ bounded | First-order condition; $D$ is a first-order operator |
| $(D-i)^{-1}$ compact | Compact-resolvent condition; closed geometry |
| $\gamma$ | Chirality grading, $\gamma^{2}=1$, $\gamma D=-D\gamma$ |
| $d(\varphi,\psi)=\sup\{|\varphi(a)-\psi(a)|:\|[D,a]\|\leq1\}$ | Connes distance |
| $[D,f]=c(df)$ | Commutator of the operator with a function; Clifford multiplication by the gradient |
| $J$ | Real structure, antilinear isometry |
| $\varepsilon,\varepsilon',\varepsilon''$ | Signs $J^{2}=\varepsilon$, $JD=\varepsilon'DJ$, $J\gamma=\varepsilon''\gamma J$ |
| $n\bmod8$ | KO-dimension |
| $HC^{\bullet}(A)$ | Cyclic cohomology |
| $\operatorname{ch}(D)$ | Connes–Chern character, a cyclic cocycle |
| $\langle\operatorname{ch}(D),[e]\rangle$ | Index pairing with $K_0(A)$ |
| $eDe$ | Compression of $D$ by a projection; Fredholm operator |
| $\Sigma$ | Dimension spectrum; poles of the zeta functions |
| $p$ | Spectral dimension; growth exponent of the eigenvalues of $|D|$ |
| $\operatorname{Tr}(e^{-tD^{2}})\sim\sum_ka_kt^{-(p-k)/2}$ | Heat trace asymptotics |
| $N(\lambda)\sim C\lambda^{p}$ | Weyl law |
| $A_M\otimes A_F$, $D=D_M\otimes1+\gamma_M\otimes D_F$ | Almost commutative geometry |

## Further Reading

- Alain Connes, *Noncommutative Geometry* (Academic Press, 1994), for spectral triples, the distance formula, cyclic cohomology and the index pairing.
- Alain Connes, "Noncommutative geometry and reality," *Journal of Mathematical Physics* **36** (1995), 6194–6231, for the real structure, the KO-dimension and the signs table.
- Alain Connes and Henri Moscovici, "The local index formula in noncommutative geometry," *Geometric and Functional Analysis* **5** (1995), 174–243, for the local index formula and the dimension spectrum.
- Alain Connes, "On the spectral characterization of manifolds," *Journal of Noncommutative Geometry* **7** (2013), 1–82, for the reconstruction theorem.
- Joseph C. Várilly, *An Introduction to Noncommutative Geometry* (European Mathematical Society, 2006), for a course-level treatment of spectral triples and their examples.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the commutative case and the spinor geometry recovered by the axioms.
