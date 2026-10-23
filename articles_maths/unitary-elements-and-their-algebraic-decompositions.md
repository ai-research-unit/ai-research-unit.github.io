# __Unitary Elements and Their Algebraic Decompositions__

## Introduction

A **unitary element** of an algebra with involution is an element $u$ with $u^*u=uu^*=1$, equivalently a unit with $u^*=u^{-1}$. The unitary elements form a group, and their eigenvalue decomposition is the algebraic form of the spectral decomposition of a unitary matrix: a writing $u=\sum_i\lambda_i e_i$ in which the eigenprojectors $e_i$ are Hermitian and the eigenvalues $\lambda_i$ have modulus one. This article determines exactly when that writing exists in a bare algebra and what survives when it does not.

The main result is a permutation law. If $u=\sum_i\lambda_i e_i$ is an eigenvalue decomposition and $u$ is unitary, then the involution sends the projector of $\lambda_i$ to the projector of $\varsigma(\lambda_i)^{-1}$, and the eigenvalues are paired by inversion and conjugation. The permutation is the identity exactly when every eigenvalue is **unimodular**, $\lambda_i\varsigma(\lambda_i)=1$; then, and only then, all the eigenprojectors are Hermitian and the spectral writing has the familiar form. The law is the unitary counterpart of the self-adjoint law of *The Eigenvalue Decomposition of a Self-Adjoint Element*: for a self-adjoint element the involution fixes the eigenvalue, and for a unitary element it inverts and conjugates it. In the first kind, where $\varsigma=\mathrm{id}$, unimodularity degenerates to $\lambda^2=1$, so the unit-circle statement is a second-kind statement; the transpose rotation and the group algebra of a cyclic group are the counterexamples that show the difference. Without separability the eigenvalue decomposition may fail altogether: the dual numbers carry a unitary $1+\varepsilon$ whose minimal polynomial is $(x-1)^2$, a unipotent unitary with no eigenvalue decomposition.

The article is algebraic and form-free. The eigenvalue decomposition is *The Eigenvalue Decomposition of an Element*; the Jordan–Chevalley decomposition and its failure are *Nilpotent Elements and the Jordan–Chevalley Decomposition*; the unitary group and the skew Lie algebra are *Unitary Elements of an Involutive Algebra*; the involution, the two kinds and the semilinear scalars are *Involutive Algebras*; and the positive definite case, where the spectral theorem holds without the extra hypotheses, belongs to Part II and *Hilbert Algebras*.

Throughout, $F$ is a field of characteristic not two, $\varsigma$ is an involution of $F$, $A$ is a finite-dimensional unital associative $F$-algebra, and $\sigma$ is a $\varsigma$-semilinear involution of $A$; the image of $x$ is written $x^*=\sigma(x)$. The fixed field of $\varsigma$ is $F_0=F^\varsigma$. The involution is of the **first kind** when it fixes the centre $Z(A)$, and of the **second kind** when it acts nontrivially on $Z(A)$; when $Z(A)=F\cdot1$, this is the same as $\varsigma=\mathrm{id}$ for the first kind and $\varsigma\neq\mathrm{id}$ for the second. An element $\lambda\in F$ is **unimodular** when

$$
\lambda\,\varsigma(\lambda)=1 .
$$

The unitary elements are $\mathrm{U}(A)=\{u:u^*u=uu^*=1\}$, and an element is **normal** when $uu^*=u^*u$. The eigenvalues and the eigenprojectors are those of *The Eigenvalue Decomposition of an Element*; the symbol $\pi$ always denotes the permutation of the eigenprojectors produced by the involution.

## Unitary Elements and Normality

### Definitions

**Definition.** An element $u\in A$ is **unitary** when $u^*u=uu^*=1$; it is **normal** when $uu^*=u^*u$.

**Proposition.** An element $u$ is unitary if and only if $u$ is a unit and $u^*=u^{-1}$. Every unitary element is normal. A normal unit need not be unitary.

*Proof.* If $u^*u=uu^*=1$, then $u$ has the two-sided inverse $u^*$, so $u$ is a unit and $u^*=u^{-1}$. Conversely, if $u$ is a unit and $u^*=u^{-1}$, both products are $1$. A unitary element is normal because $uu^*=1=u^*u$. For the last statement, the scalar $2\cdot1$ in a field of characteristic not two is a normal unit with $(2\cdot1)(2\cdot1)^*=4\cdot1\neq1$.

### The spectrum is nonzero

**Proposition.** Let $u$ be a unit with an eigenvalue decomposition $u=\sum_i\lambda_i e_i$. Then every $\lambda_i$ is nonzero, and

$$
u^{-1}=\sum_i\lambda_i^{-1}e_i .
$$

*Proof.* If $\lambda_i=0$, then $ue_i=0$ with $e_i\neq0$, so $u$ is a zero divisor, contradicting that $u$ is a unit; a unit is not a zero divisor. The inverse is the displayed sum, because the product with $u$ is $\sum_i e_i=1$ by the orthogonality of the idempotents.

**Corollary.** For a unitary $u$ with an eigenvalue decomposition, $u^*=u^{-1}=\sum_i\lambda_i^{-1}e_i$.

*Proof.* The first equality is the unitary condition and the second is the proposition.

## The Permutation Law

### The theorem

**Theorem.** Let $u$ be unitary with eigenvalue decomposition

$$
\boxed{\;u=\sum_{i=1}^{r}\lambda_i e_i\;},
$$

with the $\lambda_i$ pairwise distinct. Then there is an involution $\pi$ of the index set $\{1,\dots,r\}$ such that

$$
e_i^*=e_{\pi(i)}, \qquad \lambda_{\pi(i)}^{-1}=\varsigma(\lambda_i) \qquad (i=1,\dots,r).
$$

Equivalently, $\varsigma(\lambda_i)\lambda_{\pi(i)}=1$ for every $i$.

*Proof.* Apply the involution to the decomposition. The left side is $u^*=u^{-1}=\sum_i\lambda_i^{-1}e_i$ by the corollary above. The right side is $\sum_i\varsigma(\lambda_i)e_i^*$, by semilinearity and anti-multiplicativity. The elements $e_i^*$ are nonzero idempotents, orthogonal and resolving the identity, because $*$ is an algebra anti-automorphism of order two. The scalars $\varsigma(\lambda_i)$ are pairwise distinct. Hence

$$
u^*=\sum_{i=1}^{r}\varsigma(\lambda_i)e_i^*
$$

is an eigenvalue decomposition of $u^*$. The decomposition $u^*=\sum_i\lambda_i^{-1}e_i$ is another one. By the uniqueness of the eigenvalue decomposition, the two writings have the same eigenvalues with the same projectors. The set of projectors is therefore the same, so there is a permutation $\pi$ with $e_i^*=e_{\pi(i)}$. Rename the index in the first writing by $j=\pi(i)$ and compare the coefficients of $e_j$:

$$
\lambda_j^{-1}=\varsigma(\lambda_{\pi^{-1}(j)}),
$$

that is $\lambda_{\pi(i)}^{-1}=\varsigma(\lambda_i)$ for every $i$. Applying $*$ to $e_i^*=e_{\pi(i)}$ gives $e_i=e_{\pi(\pi(i))}$, so $\pi^2=\mathrm{id}$.

### The fixed case

**Theorem (Hermitian projectors and unimodular eigenvalues).** Let $u=\sum_i\lambda_i e_i$ be an eigenvalue decomposition. The following are equivalent:

1. $u$ is unitary and every $e_i$ is Hermitian;
2. every $e_i$ is Hermitian and every $\lambda_i$ is unimodular;
3. the permutation $\pi$ of the law is the identity.

*Proof.* From 1 to 2: if $u$ is unitary and $e_i^*=e_i$, then the law gives $\pi(i)=i$, so $\lambda_i^{-1}=\varsigma(\lambda_i)$ and $\lambda_i\varsigma(\lambda_i)=1$. From 2 to 3: if the projectors are Hermitian, $e_i^*=e_i=e_{\pi(i)}$, so $\pi(i)=i$ by the distinctness of the idempotents. From 3 to 2: $\pi=\mathrm{id}$ gives $e_i^*=e_i$ and $\lambda_i^{-1}=\varsigma(\lambda_i)$. From 2 to 1: $u^*=\sum_i\varsigma(\lambda_i)e_i=\sum_i\lambda_i^{-1}e_i=u^{-1}$, so $u$ is unitary.

**Corollary.** A unitary element with an eigenvalue decomposition has Hermitian eigenprojectors exactly when its eigenvalues are unimodular; in that case the decomposition is

$$
\boxed{\;u=\sum_i\lambda_i e_i, \qquad e_i^*=e_i, \qquad \lambda_i\varsigma(\lambda_i)=1\;},
$$

and it is the algebraic spectral decomposition of $u$.

*Proof.* This is the equivalence of 1 and 2 in the theorem.

### The general spectrum

**Corollary.** For a unitary $u$ with an eigenvalue decomposition, the spectrum is stable under the map $\lambda\mapsto\varsigma(\lambda)^{-1}$, and the eigenprojectors are permuted by the same involution. A non-unimodular eigenvalue is paired with $\varsigma(\lambda)^{-1}$, which is distinct from it, and neither projector of the pair is Hermitian.

*Proof.* The law gives $\lambda_{\pi(i)}=\varsigma(\lambda_i)^{-1}$, so the spectrum is stable. If $\lambda_i$ is not unimodular, then $\varsigma(\lambda_i)^{-1}\neq\lambda_i$, so $\pi(i)\neq i$ and $e_i$ is not Hermitian. The same applies to $\pi(i)$.

**Remark.** The law is the precise form of the statement that the spectrum of a unitary element lies on the "unit circle" of the involution. The unit circle is the set of unimodular scalars, but a unitary element need not have all its eigenvalues on it: the involution can exchange a projector with another and carry $\lambda$ to $\varsigma(\lambda)^{-1}$, and the two eigenvalues then form an inverse-conjugate pair. The transpose rotation of §*The transpose rotation* and the group algebra of §*The cyclic group algebra* are the two standard examples.

## The Two Kinds

### The first kind

In the scalar case $Z(A)=F\cdot1$ and $\varsigma=\mathrm{id}$. Then unimodularity is $\lambda^2=1$, and the theorem reads: a unitary element with Hermitian eigenprojectors has eigenvalues $\pm1$. This is the case of an involution of the algebra, $u^2=1$, and its spectral decomposition is the Peirce decomposition of the involution $u$.

**Proposition.** In the first kind, a unitary element with Hermitian eigenprojectors is an involution, $u^2=1$, and its eigenvalue decomposition is $u=1\cdot e_+-(-1)\cdot e_-$ with $e_+=\frac12(1+u)$ and $e_-=\frac12(1-u)$.

*Proof.* If the eigenvalues are $\pm1$, then $u^2=\sum_i\lambda_i^2e_i=\sum_i e_i=1$. The projectors are the Lagrange projectors at $1$ and $-1$, that is $\frac12(1\pm u)$.

**Remark.** The proposition explains why the first kind is the degenerate case for the unitary spectral theorem. In the scalar first kind the unitary group is the group of the elements $u$ with $u^*=u^{-1}$, and the spectral theorem with Hermitian projectors selects the involutions inside it. The other unitaries have at least one two-element orbit of exchanged projectors, as in the rotation and the cyclic group algebra below.

### The second kind

In the scalar second-kind case $Z(A)=F\cdot1$ and $\varsigma\neq\mathrm{id}$. Then $F/F_0$ is quadratic, and unimodularity is the algebraic form of "modulus one": for $F=\mathbb{C}$ with the conjugation it is $\lambda\bar\lambda=1$, the unit circle. A unitary element with Hermitian projectors has its eigenvalues on this circle, and its spectral decomposition is the algebraic spectral theorem.

**The fixed eigenvalues.** A fixed eigenvalue is the special case $\varsigma(\lambda)=\lambda$; it is unimodular exactly when $\lambda^2=1$, that is $\lambda=\pm1$. The general second-kind unitary has eigenvalues on the unit circle but not fixed: $\lambda$ and $\varsigma(\lambda)=\lambda^{-1}$ are different scalars, and the projector of $\lambda$ is Hermitian all the same. The distinction between "fixed" and "unimodular" is the distinction between the real line and the unit circle, and the theorem is stated for the latter.

**The exchange model.** A second-kind involution can move the centre while fixing the scalar field. The model is $A=F\times F$ with the exchange involution $(a,b)^*=(b,a)$: the centre is $F\times F$, the involution exchanges the two factors, and the scalars are fixed. An element $u=(a,a^{-1})$ is unitary, and its eigenvalue decomposition is $u=a(1,0)+a^{-1}(0,1)$. The involution exchanges the two projectors, so neither projector is Hermitian. The eigenvalues are fixed by the involution on the scalar field, but they are not unimodular unless $a^2=1$. The example shows that the hypothesis of the theorem is unimodularity, not the fixedness of the eigenvalues.

## The Algebraic Decompositions

### The orbit decomposition

Let $\pi$ be the permutation of the law and let $\mathcal{O}$ be its set of orbits. For an orbit $J$ put

$$
g_J=\sum_{i\in J}e_i .
$$

**Theorem.** The $g_J$ are pairwise orthogonal Hermitian idempotents with $\sum_J g_J=1$, and

$$
\boxed{\;u=\sum_{J\in\mathcal{O}}u_J, \qquad u_J=ug_J=g_Jug_J\;},
$$

where $u_J$ is unitary in the corner $g_JAg_J$. On a one-element orbit $\{\lambda\}$, $u_J=\lambda g_J$ with $\lambda$ unimodular. On a two-element orbit $\{\lambda,\mu\}$ with $\mu=\varsigma(\lambda)^{-1}$, the corner contains the idempotents $e_\lambda,e_\mu$, exchanged by $*$, and $u_J=\lambda e_\lambda+\mu e_\mu$.

*Proof.* The involution permutes the $e_i$ within each orbit, so it fixes $g_J$; the orbit idempotents are orthogonal and sum to $1$. The element $u_J=ug_J=g_Jug_J$ is unitary in the corner: $u_J^*u_J=g_Ju^*ug_J=g_J$, and similarly on the other side. On a singleton, the eigenvalue is unimodular by the theorem. On a pair, the formula is the decomposition, and $\mu=\varsigma(\lambda)^{-1}$ is the law.

**Remark.** The orbit decomposition is the unitary analogue of the orbit decomposition of a self-adjoint element. There the pair contributed a skew element $v$ with $v^2=g$ and a "complex number" $\frac{s}{2}+btv$; here the pair contributes a unitary $u_J$ with two exchanged projectors and the eigenvalues $\lambda,\varsigma(\lambda)^{-1}$. The two are different normal forms: the self-adjoint pair is a complex number, and the unitary pair is a "phase" whose two eigenvalues are inverse-conjugate. The pair is not a scalar multiple of a Hermitian idempotent over $F_0$; it splits only after the scalar extension.

### The generalized decomposition

When the minimal polynomial is not split separable, the eigenvalue decomposition is replaced by the generalized one of *Nilpotent Elements and the Jordan–Chevalley Decomposition*:

$$
u=\sum_{i=1}^{r}\lambda_i\varepsilon_i(1+n_i),
$$

with the $\varepsilon_i$ the generalized eigenprojectors, $n_i$ nilpotent, $n_i\varepsilon_i=\varepsilon_in_i=n_i$, the $\varepsilon_i$ orthogonal and summing to $1$, and the $\lambda_i$ distinct; the nilpotent part has been rescaled by $\lambda_i^{-1}$, which is legitimate because $u$ is a unit. The element $1+n_i$ is the unipotent part of the $i$-th block.

**Proposition.** Suppose that $u=\sum_i\lambda_i\varepsilon_i(1+n_i)$ is a generalized eigen decomposition with the $\varepsilon_i$ Hermitian and the $\lambda_i$ unimodular. Then $u$ is unitary if and only if the unipotent parts satisfy

$$
n_i+n_i^*+n_i^*n_i=0, \qquad n_i+n_i^*+n_in_i^*=0
$$

for every $i$.

*Proof.* The element $u_i=\lambda_i\varepsilon_i(1+n_i)$ is the component of $u$ in the corner $\varepsilon_iA\varepsilon_i$, and the corner is $*$-stable because $\varepsilon_i$ is Hermitian. Suppose first that the two equations hold. Since $\lambda_i\varsigma(\lambda_i)=1$, the first equation gives

$$
u_i^*u_i=(1+n_i^*)(1+n_i)\varepsilon_i=\varepsilon_i,
$$

and the second gives $u_iu_i^*=\varepsilon_i$; summing over $i$ gives $u^*u=uu^*=1$. Conversely, if $u$ is unitary, then $u_i^*u_i=\varepsilon_i$ and $u_iu_i^*=\varepsilon_i$ in the corner. The first of these is $\lambda_i\varsigma(\lambda_i)(1+n_i^*)(1+n_i)=\varepsilon_i$, and $\lambda_i\varsigma(\lambda_i)=1$, so $(1+n_i^*)(1+n_i)=\varepsilon_i$, which is the first equation; the second is the other side.

**Remark.** The proposition is conditional on the unimodularity of the eigenvalues; without it, a scalar multiple of a unipotent can still be unitary in a corner, and the equations acquire the scalar. In the dual numbers, $n=\varepsilon$ satisfies $n^*=-n$ and $n^2=0$, so both equations hold; in a matrix algebra with a positive definite form, a unipotent unitary is the identity, because the only unipotent unitary matrix is $I$.

### Roots

**Proposition.** Let $u=\sum_i\lambda_i e_i$ be a unitary element with Hermitian eigenprojectors and unimodular eigenvalues. Suppose that for each $i$ there is a unimodular $\mu_i$ with $\mu_i^2=\lambda_i$. Then

$$
v=\sum_i\mu_i e_i
$$

is unitary, has Hermitian eigenprojectors, and satisfies $v^2=u$.

*Proof.* The element $v$ has the eigenvalue decomposition with the same Hermitian projectors and the unimodular eigenvalues $\mu_i$, so it is unitary by the theorem. Its square is $\sum_i\mu_i^2e_i=\sum_i\lambda_i e_i=u$.

**Remark.** A unimodular $\lambda$ has two square roots $\pm\mu$ with $\mu\varsigma(\mu)=\pm1$; the proposition needs the sign $+1$ for each $i$. Over $\mathbb{C}$ with the conjugation one chooses $\mu$ on the unit circle, so the sign is always $+1$. Over a general field the sign is an obstruction, and the unitary square root exists exactly when the signs can be chosen consistently; the root is not unique, since the signs may be flipped independently on the distinct eigenspaces.

### The Cayley transform

**Proposition.** Let $u=\sum_i\lambda_i e_i$ be unitary with Hermitian eigenprojectors, and suppose that no $\lambda_i$ equals $-1$. Then

$$
k=\sum_i\frac{\lambda_i-1}{\lambda_i+1}e_i
$$

is skew, and $u=(1+k)(1-k)^{-1}$.

*Proof.* For a unimodular $\lambda$, the scalar $\kappa=(\lambda-1)/(\lambda+1)$ is skew:

$$
\varsigma(\kappa)=\frac{\varsigma(\lambda)-1}{\varsigma(\lambda)+1}
=\frac{\lambda^{-1}-1}{\lambda^{-1}+1}
=\frac{1-\lambda}{1+\lambda}=-\kappa .
$$

The element $k$ is therefore a sum of skew scalar multiples of Hermitian idempotents, hence skew. On the $i$-th component, $1+\kappa=2\lambda/(\lambda+1)$ and $1-\kappa=2/(\lambda+1)$, so $(1+\kappa)/(1-\kappa)=\lambda$. Summing over $i$ gives the identity.

**Remark.** The Cayley transform is the algebraic substitute for the exponential: it maps the skew elements with $1-k$ invertible bijectively onto the unitary elements with $1+u$ invertible. The inverse is $k=(u-1)(u+1)^{-1}$. The transform is treated as a map between the skew part and the unitary group in *Unitary Elements of an Involutive Algebra*; the spectral reading above shows that it acts by the Möbius transformation $\lambda=(1+\kappa)/(1-\kappa)$ on each eigenvalue.

## The Failure Without Separability

### The dual numbers

Let $A=F[\varepsilon]/(\varepsilon^2)$ be the algebra of dual numbers, with the involution

$$
(a+b\varepsilon)^*=a-b\varepsilon .
$$

The map is an involution: it is $F$-linear, it reverses the product because the algebra is commutative, and its square is the identity. The element

$$
u=1+\varepsilon
$$

is unitary:

$$
u^*u=(1-\varepsilon)(1+\varepsilon)=1-\varepsilon^2=1, \qquad uu^*=1 .
$$

Its minimal polynomial is $(x-1)^2$: indeed $u-1=\varepsilon\neq0$ and $(u-1)^2=\varepsilon^2=0$. The algebra $A$ is local with maximal ideal $(\varepsilon)$, and the only idempotents of $A$ are $0$ and $1$: an idempotent $a+b\varepsilon$ satisfies $a^2=a$ and $2ab=b$, so $a=0$ gives $b=0$, and $a=1$ gives $b=0$ in characteristic not two.

**Theorem.** The unitary element $u=1+\varepsilon$ has no eigenvalue decomposition.

*Proof.* An eigenvalue decomposition of $u$ would be a writing $u=\sum_i\lambda_i e_i$ with at least two distinct eigenvalues, or with one eigenvalue $\lambda$ and $e=1$. The only idempotents are $0$ and $1$, so the only possible writing with distinct eigenvalues is $u=\lambda\cdot1$ for a single $\lambda$, which would make $u$ scalar. But $u=1+\varepsilon$ is not scalar. Hence no eigenvalue decomposition exists.

**Remark.** The example is the simplest failure of the spectral theorem in a form-free algebra. The element $u$ is unitary, its minimal polynomial is not separable, and it is unipotent: $u=1+\varepsilon$ with $\varepsilon$ nilpotent. The generalized decomposition is $u=1\cdot1+\varepsilon$, with the single generalized eigenprojector $1$ and the nilpotent part $\varepsilon$; the unipotent factor $1+\varepsilon$ is itself unitary. The failure is not a failure of the involution but of the splitting of the minimal polynomial.

### Why the positive definite case is different

In a matrix algebra over $\mathbb{C}$ with the conjugate transpose and the standard positive definite form, a unitary matrix is normal, and a normal matrix is diagonalizable: its minimal polynomial is squarefree. The proof uses the spectral theorem for normal matrices, which uses positivity. In a general algebra with involution there is no positivity, and the dual numbers show that a unitary element can be as far from semisimple as a nilpotent. The form-free statement is therefore the conditional theorem of §*The fixed case*, not the unconditional spectral theorem; the unconditional version is a theorem of Part II and *Hilbert Algebras*.

## Examples

### The conjugate transpose

Let $A=M_n(\mathbb{C})$ with $X^*=\overline X^{\mathsf T}$, the involution of the second kind. A unitary element is a unitary matrix. For

$$
U=\begin{pmatrix}0&i\\i&0\end{pmatrix},
$$

the product $U^*U$ is the identity, the eigenvalues are $i$ and $-i$, and the eigenprojectors are

$$
e_i=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}, \qquad e_{-i}=\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
$$

both Hermitian. The eigenvalues are unimodular, $\lambda\bar\lambda=1$, and the decomposition is $U=i\,e_i+(-i)e_{-i}$. The example is the standard second-kind unitary with the spectral writing of the theorem.

### The transpose rotation

Let $A=M_2(\mathbb{C})$ with the transpose $X^*=X^{\mathsf T}$, the involution of the first kind, and let

$$
R=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$

Then $R^{\mathsf T}R=I$, so $R$ is unitary, and the eigenvalues are $i$ and $-i$. The eigenprojectors are

$$
e_i=\frac12\begin{pmatrix}1&-i\\i&1\end{pmatrix}, \qquad e_{-i}=\frac12\begin{pmatrix}1&i\\-i&1\end{pmatrix},
$$

and the transpose exchanges them: $e_i^{\mathsf T}=e_{-i}$. Neither is symmetric, the eigenvalues are not unimodular for the trivial involution ($i^2=-1$), and the permutation $\pi$ swaps the two indices. The law reads $\lambda_{\pi(i)}^{-1}=\varsigma(\lambda_i)$: for $i$ with $\lambda_i=i$, $\lambda_{\pi(i)}=-i$, and $(-i)^{-1}=i=\varsigma(i)$. The example shows that a unitary element of the first kind need not have Hermitian projectors, and that the unit-circle statement is false when the involution is trivial on the scalars.

### The cyclic group algebra

Let $G=\langle g\rangle$ be cyclic of order three and let $A=k[G]$ with the inversion involution $g^*=g^{-1}$. The element $g$ is unitary, $g^*g=g^{-1}g=1$. If $k$ contains a primitive cube root $\zeta$ and $3\neq0$, the eigenvalues are $1,\zeta,\zeta^2$, and the eigenprojectors are the Lagrange projectors

$$
e_1=\frac{(g-\zeta)(g-\zeta^2)}{(1-\zeta)(1-\zeta^2)}, \qquad
e_\zeta=\frac{(g-1)(g-\zeta^2)}{(\zeta-1)(\zeta-\zeta^2)}, \qquad
e_{\zeta^2}=\frac{(g-1)(g-\zeta)}{(\zeta^2-1)(\zeta^2-\zeta)} .
$$

The inversion sends $g$ to $g^2$, and it exchanges $e_\zeta$ and $e_{\zeta^2}$; the eigenvalues $\zeta$ and $\zeta^2$ are exchanged as well. The law holds with $\lambda_{\pi(\zeta)}^{-1}=\zeta^{-2}=\zeta=\varsigma(\zeta)$. The projectors are not Hermitian, and the eigenvalues are not unimodular in the first-kind sense ($\zeta^2\neq1$). The example is the group-algebra form of the rotation: the inversion is the algebraic "reflection" that swaps the two non-real characters.

### The repeated eigenvalue

Let $U=\operatorname{diag}(i,i,-i)$ with the conjugate transpose. The distinct eigenvalues are $i$ and $-i$, and the eigenprojectors are

$$
e_i=E_{11}+E_{22}, \qquad e_{-i}=E_{33}.
$$

Both are Hermitian, both eigenvalues are unimodular, and the decomposition groups the repeated eigenvalue $i$ into one term of rank two. The refinement into the two one-dimensional eigenspaces is not unique, as in the self-adjoint case; the eigenvalue decomposition is by distinct eigenvalues.

### The exchange involution

Let $A=B\times B^{\mathrm{opp}}$ with the exchange involution $(b,c)^*=(c,b)$, and let $b\in B$ be a unit with an eigenvalue decomposition $b=\sum_i\lambda_i e_i$. The element $u=(b,b^{-1})$ is unitary, and

$$
u=\sum_i\lambda_i(e_i,0)+\sum_i\lambda_i^{-1}(0,e_i).
$$

The idempotents $(e_i,0)$ and $(0,e_i)$ are exchanged by the involution, and the eigenvalues $\lambda_i$ and $\lambda_i^{-1}$ are paired by the law. The orbit idempotent $(e_i,e_i)$ is Hermitian, and the unitary $u$ is the direct sum of the "inverse pairs" of the two blocks. The example is the exchange-involution model of the permutation law: the involution does not fix the projectors, and it inverts the eigenvalues.

## Summary

A unitary element $u$ is a unit with $u^*=u^{-1}$, and it is normal. If $u$ has an eigenvalue decomposition $u=\sum_i\lambda_i e_i$, the involution permutes the eigenprojectors by an involution $\pi$ of the index set and acts on the eigenvalues by $\lambda_{\pi(i)}^{-1}=\varsigma(\lambda_i)$: the eigenvalue is inverted and conjugated. The permutation is the identity exactly when every eigenvalue is unimodular, $\lambda_i\varsigma(\lambda_i)=1$; then all the eigenprojectors are Hermitian, the writing is the algebraic spectral decomposition, and conversely a Hermitian-projector writing with unimodular eigenvalues is unitary. In the first kind unimodularity is $\lambda^2=1$, so the Hermitian-projector unitaries are the involutions; in the second kind it is the algebraic unit circle, and the conjugate transpose is the model. The orbit idempotents $g_J=\sum_{i\in J}e_i$ decompose $u$ into unitary blocks: scalar blocks on the fixed eigenvalues and inverse-conjugate pairs on the two-element orbits. When the minimal polynomial is not separable the eigenvalue decomposition fails; the dual numbers carry the unipotent unitary $1+\varepsilon$ with minimal polynomial $(x-1)^2$, and its generalized decomposition is $1+\varepsilon$ with the single generalized eigenprojector $1$. The eigenvalue decomposition is *The Eigenvalue Decomposition of an Element*; the Jordan–Chevalley theory is *Nilpotent Elements and the Jordan–Chevalley Decomposition*; the unitary group and the skew Lie algebra are *Unitary Elements of an Involutive Algebra*; the involution and the two kinds are *Involutive Algebras*; the self-adjoint analogue is *The Eigenvalue Decomposition of a Self-Adjoint Element*; and the positive definite case is Part II and *Hilbert Algebras*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | the ground field, of characteristic not two |
| $\varsigma$ | an involution of $F$ |
| $F_0=F^\varsigma$ | the fixed field of $\varsigma$ |
| $A$ | a finite-dimensional unital associative $F$-algebra |
| $x^*=\sigma(x)$ | the adjoint of an element |
| $\mathrm{U}(A)$ | the unitary elements, $u^*u=uu^*=1$ |
| $\lambda\varsigma(\lambda)=1$ | a unimodular scalar |
| $u=\sum_i\lambda_i e_i$ | the eigenvalue decomposition |
| $\pi$ | the involution of the index set with $e_i^*=e_{\pi(i)}$ |
| $g_J=\sum_{i\in J}e_i$ | the orbit idempotent |
| $1+n_i$ | the unipotent part of a generalized eigenblock |
| $k=\sum_i\frac{\lambda_i-1}{\lambda_i+1}e_i$ | the Cayley transform of $u$ |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the unitary groups, the involutions of the first and the second kind, and the unitary elements of a central simple algebra.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the eigenvalue decomposition, the Peirce decomposition and the unitary elements of a finite-dimensional algebra.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the self-adjoint part and the Jordan structure of the fixed elements.
- Israel Nathan Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the symmetric and the skew elements and the normal elements.
