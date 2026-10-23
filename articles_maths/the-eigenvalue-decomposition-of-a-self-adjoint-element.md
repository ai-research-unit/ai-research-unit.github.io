# __The Eigenvalue Decomposition of a Self-Adjoint Element__

## Introduction

An element $h$ of an algebra with involution is **self-adjoint** when $h^*=h$. If $h$ has an eigenvalue decomposition $h=\sum_i\lambda_i e_i$, then the involution can be applied to the whole writing, and because the eigenvalue decomposition is unique, the result must be the same decomposition with the labels permuted. This article determines the permutation. The involution sends the eigenprojector of $\lambda$ to the eigenprojector of the conjugate scalar $\varsigma(\lambda)$, and the eigenprojector of $\lambda$ is Hermitian exactly when $\lambda$ is fixed by $\varsigma$. In particular, when the involution is linear over the ground field, every eigenprojector of a self-adjoint element is Hermitian; when the involution is semilinear and nontrivial on the scalars, a non-fixed eigenvalue comes with its conjugate and the two eigenprojectors are exchanged.

The result is the algebraic form of the statement that a Hermitian matrix has an orthonormal basis of eigenvectors with real eigenvalues. The algebra is form-free: no inner product, no positivity and no distance are used. The eigenvalue decomposition is that of *The Eigenvalue Decomposition of an Element*; the involution and the two kinds are those of *Involutive Algebras*; the self-adjoint part and its Jordan structure are *The Self-Adjoint Part of an Algebra*; the unitary analogue is *Unitary Elements and Their Algebraic Decompositions*; and the form-theoretic orthogonality of the Peirce corners is *The Adjoint of the Peirce Projection*. The examples are *Matrix Algebras* and *Examples of Algebras*.

Throughout, $F$ is a field of characteristic not two, $\varsigma$ is an involution of $F$, $A$ is a finite-dimensional unital associative $F$-algebra, and $\sigma$ is a $\varsigma$-semilinear involution of $A$; the image of $x$ is written $x^*=\sigma(x)$, so that $(xy)^*=y^*x^*$ and $(x^*)^*=x$. The fixed field of $\varsigma$ is $F_0=F^\varsigma$, the self-adjoint part is $A^+=H(A)=\{h:h^*=h\}$, and the skew part is $A^-=\{k:k^*=-k\}$. The involution is **of the first kind** when $\varsigma=\mathrm{id}$, and **of the second kind** when $\varsigma\neq\mathrm{id}$; in the second kind $F/F_0$ is quadratic and there is an element $t\in F$ with $\varsigma(t)=-t$ and $F=F_0\oplus F_0t$.

## The Involution on the Polynomial Calculus

### Polynomials in a self-adjoint element

For $p(x)=\sum_k a_kx^k\in F[x]$, write $p^\varsigma(x)=\sum_k\varsigma(a_k)x^k$ for the polynomial with the coefficients conjugated.

**Proposition.** For every $p\in F[x]$ and every $x\in A$,

$$
p(x)^*=p^\varsigma(x^*).
$$

If $h$ is self-adjoint, then $p(h)^*=p^\varsigma(h)$.

*Proof.* The involution is additive and semilinear, and it reverses products, so $(a_kx^k)^*=\varsigma(a_k)(x^*)^k$; summing gives the first identity. The second is the case $x^*=x$.

**Corollary.** If $h$ is self-adjoint and $p(h)=0$, then $p^\varsigma(h)=0$.

*Proof.* Apply the proposition to $p(h)=0$ and use $h^*=h$: $0=p(h)^*=p^\varsigma(h)$.

### The minimal polynomial

**Theorem.** Let $h$ be self-adjoint and let $m_h$ be its minimal polynomial. Then $m_h$ has coefficients in the fixed field $F_0$:

$$
\boxed{\;m_h\in F_0[x]\;}.
$$

Consequently the spectrum of $h$ is stable under $\varsigma$: if $\lambda$ is an eigenvalue of $h$, then so is $\varsigma(\lambda)$.

*Proof.* The polynomial $m_h^\varsigma$ is monic of degree $\deg m_h$ and vanishes at $h$ by the corollary. The minimal polynomial is the unique monic polynomial of least degree vanishing at $h$, so $m_h^\varsigma=m_h$. A polynomial is fixed by the coefficientwise involution exactly when its coefficients lie in $F_0$. For the last statement, apply $\varsigma$ to $m_h(\lambda)=0$: $m_h^\varsigma(\varsigma(\lambda))=m_h(\varsigma(\lambda))=0$.

**Remark.** The theorem is the algebraic reason for the conjugate pairs of eigenvalues of a real matrix. Over $F=\mathbb{R}$ with the trivial involution every polynomial has coefficients in $F_0=\mathbb{R}$, and the statement is empty; over $F=\mathbb{C}$ with the conjugation, it says that the characteristic and the minimal polynomial of a real matrix have real coefficients, so the non-real roots occur in conjugate pairs. The minimal polynomial, not the characteristic polynomial, is the object that the eigenvalue decomposition uses.

## The Permutation of the Eigenprojectors

### The law

**Theorem.** Let $h$ be self-adjoint with eigenvalue decomposition

$$
h=\sum_{i=1}^{r}\lambda_i e_i,
$$

with the $\lambda_i$ pairwise distinct. Then there is an involution $\pi$ of the index set $\{1,\dots,r\}$ such that

$$
\boxed{\;e_i^*=e_{\pi(i)}, \qquad \lambda_{\pi(i)}=\varsigma(\lambda_i) \qquad (i=1,\dots,r)\;}.
$$

*Proof.* Apply the involution to the decomposition. The left side is $h^*=h$. The right side is $\sum_i\varsigma(\lambda_i)e_i^*$, by semilinearity and anti-multiplicativity. The elements $e_i^*$ are nonzero idempotents: $e_i^*e_i^*=(e_i^2)^*=e_i^*$, and $e_i^*=0$ would give $e_i=(e_i^*)^*=0$. They are orthogonal, $e_i^*e_j^*=(e_je_i)^*=0$ for $i\neq j$, and they resolve the identity, $\sum_i e_i^*=1^*=1$. The scalars $\varsigma(\lambda_i)$ are pairwise distinct because $\varsigma$ is injective. Hence

$$
h=\sum_{i=1}^{r}\varsigma(\lambda_i)e_i^*
$$

is an eigenvalue decomposition of $h$. The eigenvalue decomposition of a given element is unique, so each eigenvalue $\varsigma(\lambda_i)$ of the second writing is one of the eigenvalues $\lambda_j$ of the first, and its projector is the corresponding $e_j$. Define $\pi(i)$ by $e_i^*=e_{\pi(i)}$. Then the eigenvalue carried by $e_{\pi(i)}$ in the second writing is $\varsigma(\lambda_i)$, while in the first it is $\lambda_{\pi(i)}$; hence $\lambda_{\pi(i)}=\varsigma(\lambda_i)$. Applying $*$ to $e_i^*=e_{\pi(i)}$ gives $e_i=e_{\pi(\pi(i))}$, so $\pi^2=\mathrm{id}$.

**Corollary (fixed eigenvalues and Hermitian projectors).** For a self-adjoint $h$ and an index $i$, the following are equivalent:

1. $e_i$ is Hermitian, $e_i^*=e_i$;
2. $\pi(i)=i$;
3. $\lambda_i$ is fixed by $\varsigma$, $\varsigma(\lambda_i)=\lambda_i$.

Consequently all the eigenprojectors are Hermitian exactly when all the eigenvalues are fixed by $\varsigma$.

*Proof.* The equivalence of 1 and 2 is the injectivity of $*$ and the distinctness of the idempotents: $e_i^*=e_i$ means $e_{\pi(i)}=e_i$, hence $\pi(i)=i$, and conversely. The equivalence of 2 and 3 is the law: $\pi(i)=i$ gives $\lambda_i=\varsigma(\lambda_i)$, and if $\lambda_i=\varsigma(\lambda_i)$ then $\lambda_{\pi(i)}=\lambda_i$, so $\pi(i)=i$ by the distinctness of the eigenvalues.

### The two kinds

**Corollary (the first kind).** If $\varsigma=\mathrm{id}$, every eigenprojector of a self-adjoint element is Hermitian.

*Proof.* Every scalar is fixed by the identity, so the corollary above applies with $\pi=\mathrm{id}$.

The first-kind statement is the one that the matrix examples illustrate: a symmetric complex matrix has symmetric eigenprojectors, and a real matrix with a nonreal conjugate pair has the two eigenprojectors of that pair exchanged by entrywise conjugation. The two examples differ because the involution on the scalars is trivial in the first and nontrivial in the second.

**Corollary (the second kind).** If $\varsigma\neq\mathrm{id}$, the spectrum of a self-adjoint $h$ is a union of orbits of $\varsigma$ of size one or two, and for a two-element orbit $\{\lambda,\bar\lambda\}$ the projectors are exchanged:

$$
e_\lambda^*=e_{\bar\lambda}, \qquad e_{\bar\lambda}^*=e_\lambda, \qquad \bar\lambda=\varsigma(\lambda).
$$

The eigenvalues of a two-element orbit are not fixed, and neither projector is Hermitian.

*Proof.* The orbit decomposition is the theorem, and the orbit has size at most two because $\varsigma$ has order two. A two-element orbit is exactly a pair $\lambda\neq\varsigma(\lambda)$, and the law gives the exchange. If $e_\lambda$ were Hermitian, the corollary above would give $\lambda=\varsigma(\lambda)$, a contradiction.

### The orbit idempotents

**Theorem (the decomposition over the fixed field).** Let $h$ be self-adjoint and let $\mathcal{O}$ be the set of orbits of $\varsigma$ on the spectrum. For an orbit $J$ put

$$
g_J=\sum_{i\in J}e_i .
$$

Then the $g_J$ are pairwise orthogonal Hermitian idempotents with $\sum_J g_J=1$, and

$$
\boxed{\;h=\sum_{J\in\mathcal{O}}h_J, \qquad h_J=h g_J=g_Jhg_J\;},
$$

where $h_J$ is self-adjoint and lies in the corner $g_JAg_J$. For a one-element orbit $J=\{\lambda\}$, $h_J=\lambda g_J$ with $\lambda\in F_0$. For a two-element orbit $J=\{\lambda,\bar\lambda\}$, put

$$
s=\lambda+\bar\lambda\in F_0, \qquad p=\lambda\bar\lambda\in F_0, \qquad \lambda-\bar\lambda=2bt,
$$

with $b\in F_0$. Then

$$
h_J=\frac{s}{2}g_J+bt\,v_J, \qquad v_J=\frac{h_J-\frac{s}{2}g_J}{bt},
$$

where $v_J\in g_JAg_J$ is skew, $v_J^*=-v_J$, and $v_J^2=g_J$.

*Proof.* The involution permutes the $e_i$ within each orbit, so it fixes the sum $g_J$; distinct orbits are disjoint unions of orthogonal idempotents, so the $g_J$ are orthogonal and sum to the identity. The element $h_J=hg_J$ is fixed by $*$ because $h$ and $g_J$ are, and it lies in $g_JAg_J$ because $g_J$ is an idempotent commuting with $h$. For a singleton, $g_J=e_\lambda$ and $h_J=\lambda e_\lambda$, with $\lambda$ fixed by the corollary. For a pair, $g_J=e_\lambda+e_{\bar\lambda}$, and $h_J=\lambda e_\lambda+\bar\lambda e_{\bar\lambda}$. The scalar $\lambda-\bar\lambda$ is skew and nonzero, so it is $2bt$ with $b\in F_0$ and $b\neq0$, because the skew elements of $F$ are exactly $F_0t$. The element $v_J$ is skew: the numerator is self-adjoint, and $bt$ is skew, so the quotient is skew. Finally,

$$
v_J^2=\frac{\left(h_J-\frac{s}{2}g_J\right)^2}{b^2t^2}
=\frac{\left(\frac{s^2}{4}-p\right)g_J}{b^2t^2}
=\frac{(\lambda-\bar\lambda)^2}{4b^2t^2}g_J=g_J,
$$

using $h_J^2-s h_J+p g_J=0$, which is the Cayley–Hamilton identity of the two eigenvalues, and $\lambda-\bar\lambda=2bt$.

**Remark.** The theorem is the precise sense in which a self-adjoint element over a field with a nontrivial involution has a decomposition over the fixed field. The orbit idempotents $g_J$ are polynomials in $h$ with coefficients in $F_0$, because they are the Chinese remainder idempotents of the minimal polynomial $m_h\in F_0[x]$; the singleton terms are scalar multiples of $g_J$, and the two-element terms are the "complex numbers" $\frac{s}{2}+b\,(tv_J)$ in the corner, with $(tv_J)^2=-t^2g_J$ and $tv_J$ self-adjoint. The pair cannot be split into two scalar multiples of Hermitian idempotents over $F_0$; it splits only after the scalar extension to $F$, where the two projectors $e_\lambda,e_{\bar\lambda}$ appear.

## The Peirce Reading

### The stable corners

Let $h=\sum_i\lambda_i e_i$ be self-adjoint and suppose first that all the eigenvalues are fixed. Then all the $e_i$ are Hermitian, and for the Peirce corners $A_{ij}=e_iAe_j$,

$$
A_{ij}^*=A_{ji}.
$$

The diagonal corners $A_{ii}=e_iAe_i$ are $*$-stable algebras with unit $e_i$, and the off-diagonal corners are paired: $A_{ij}$ and $A_{ji}$ are exchanged by the involution. The Peirce decomposition

$$
A=\bigoplus_{i,j=1}^{r}A_{ij}
$$

is therefore stable under $*$, and the spectral decomposition of $h$ is adapted to it: $h$ acts on $A_{ij}$ by $\lambda_i$ on the left and by $\lambda_j$ on the right, so $h\in\bigoplus_i A_{ii}$, the eigenspace of $L_h$ for $\lambda_i$ is $e_iA=\bigoplus_jA_{ij}$, and the diagonal corner $A_{ii}$ is the common eigenspace of $L_h$ and $R_h$ for $\lambda_i$.

*Proof.* The identity $A_{ij}^*=A_{ji}$ follows from $(e_ix e_j)^*=e_j^*x^*e_i^*=e_jx^*e_i$. The diagonal corners are closed under multiplication and under $*$, and $e_i$ is their unit. The action of $h$ is $h(e_ix e_j)=(\lambda_ie_i)x e_j=\lambda_i e_ix e_j$, and similarly on the right.

**Corollary.** If all the eigenvalues are fixed, the Peirce projections $E_{ij}(x)=e_ix e_j$ satisfy $E_{ij}^\dagger=E_{ij}$ with respect to any associative Hermitian form on $(A,*)$, and the Peirce decomposition is orthogonal in the sense that the idempotents $e_i$ are Hermitian and orthogonal.

*Proof.* The identity for the Peirce projections is that of *The Adjoint of the Peirce Projection*: $T_{a,b}^\dagger=T_{a^*,b^*}$, and $e_i^*=e_i$, $e_j^*=e_j$, so $E_{ij}^\dagger=E_{ij}$. The idempotents are Hermitian and satisfy $e_ie_j=\delta_{ij}e_i$; this is the algebraic orthogonality. The form-orthogonality of the corners follows from $E_{ij}^\dagger=E_{ij}$ and is proved in that article.

**Remark.** "Orthogonal" here has two readings, and the article keeps them apart. The algebraic reading is $e_ie_j=0$ for $i\neq j$, which always holds for an eigenvalue decomposition. The form-theoretic reading is $\langle A_{ij},A_{kl}\rangle=0$ for $(i,j)\neq(k,l)$, which needs a form and is the subject of *The Adjoint of the Peirce Projection* and *Hermitian Idempotents and the Peirce Decomposition*. The self-adjointness of $h$ alone gives the algebraic reading; it gives the form-theoretic reading only when a compatible form is present and the idempotents are Hermitian.

### The exchanged corners

If a two-element orbit $\{\lambda,\bar\lambda\}$ is present, the idempotents $e_\lambda,e_{\bar\lambda}$ are not Hermitian, and the corners $A_{\lambda\lambda}$ and $A_{\bar\lambda\bar\lambda}$ are exchanged by $*$; so are $A_{\lambda\bar\lambda}$ and $A_{\bar\lambda\lambda}$. The orbit idempotent $g=e_\lambda+e_{\bar\lambda}$ is Hermitian, and the corner $gAg$ is $*$-stable. Inside it, the element $h g$ has the form $\frac{s}{2}g+btv$ of the orbit theorem, with $v$ skew and $v^2=g$; the pair is a single "complex" block over $F_0$, not two real blocks.

**Proposition.** In the corner $gAg$, the element $v$ satisfies

$$
v^*=-v, \qquad v^2=g, \qquad vg=gv=v,
$$

and the element $hg$ commutes with $v$. The subalgebra $F_0[v]$ is spanned by $g$ and $v$ with $v^2=g$; it is isomorphic to $F_0\times F_0$ through $g\mapsto(1,1)$, $v\mapsto(1,-1)$, so it is the split algebra of the pair, not a field.

*Proof.* The first two identities are the orbit theorem; $vg=v$ and $gv=v$ follow from $v\in gAg$. The commutation is $h g=\frac{s}{2}g+btv$. The algebra $F_0[v]$ is spanned by $g$ and $v$ with $v^2=g$, and the displayed assignment is an isomorphism onto $F_0\times F_0$ because it preserves the unit, is bijective on the two-dimensional spaces, and sends $v^2=g$ to $(1,1)$.

**Remark.** The last proposition is the algebraic model of the two-dimensional real block of a complex conjugate pair. The element $v$ is the "complex structure" of the block, and it is skew, not self-adjoint; the self-adjoint element $hg$ is $\frac{s}{2}g$ plus a multiple of $v$. The notation is consistent with the split complex numbers $\mathbb{R}[j]$, $j^2=+1$, of *Examples of Algebras*: the corner is a split algebra over $F_0$, and the two idempotents $\frac12(g\pm v)$ of that split algebra are the images of $e_\lambda$ and $e_{\bar\lambda}$ after the scalar extension.

## Examples

### The complex numbers with conjugation

Let $A=\mathbb{C}$ over $F=\mathbb{C}$ with $\varsigma$ the conjugation. A self-adjoint element is a real number $h=a$, its minimal polynomial is $x-a$ with $a\in\mathbb{R}=F_0$, and its eigenvalue decomposition is $h=a\cdot1$. The eigenvalue is fixed and the projector $1$ is Hermitian. The example is the degenerate one: the algebra is a field, so the only idempotents are $0$ and $1$, and the only decomposition is the scalar one.

### The conjugate transpose

Let $A=M_n(\mathbb{C})$ with the conjugate transpose $X^*=\overline X^{\mathsf T}$, the involution of the second kind. A self-adjoint element is a Hermitian matrix. Its eigenvalues are real by the spectral theorem for Hermitian matrices, hence fixed by the conjugation, and its eigenprojectors are Hermitian by the corollary above. The decomposition is the spectral theorem of the Hermitian matrices, read algebraically. For $n=2$ and

$$
H=\begin{pmatrix}1&i\\-i&2\end{pmatrix},
$$

the characteristic polynomial is $x^2-3x+1$, with the two real roots $\frac{3\pm\sqrt5}{2}$; the two eigenprojectors are Hermitian and orthogonal, and $H$ is their real linear combination. The positivity of $H$ and the norm of its eigenvectors belong to Part II and to *Hilbert Algebras*, not here.

### The transpose

Let $A=M_n(\mathbb{C})$ with the transpose $X^*=X^{\mathsf T}$, the involution of the first kind. A self-adjoint element is a symmetric matrix. Its eigenvalues need not be real: the symmetric matrix

$$
S=\begin{pmatrix}0&i\\i&0\end{pmatrix}
$$

has the eigenvalues $i$ and $-i$. The eigenprojectors are

$$
e_i=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}, \qquad e_{-i}=\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
$$

both symmetric and Hermitian for the transpose, and $S=i\,e_i+(-i)e_{-i}$. The example shows that the first-kind statement is about the involution on the coefficients, not about the realness of the spectrum: the eigenvalues are not real, but they are fixed by the transpose, and the projectors are fixed as well.

### The entrywise conjugation

Let $A=M_n(\mathbb{C})$ with the entrywise conjugation $X^*=\overline X$, the involution of the second kind. A self-adjoint element is a matrix with real entries. The rotation

$$
R=\begin{pmatrix}0&-1\\1&0\end{pmatrix}
$$

has the eigenvalues $i$ and $-i$, and the eigenprojectors

$$
e_i=\frac12\begin{pmatrix}1&i\\-i&1\end{pmatrix}, \qquad e_{-i}=\frac12\begin{pmatrix}1&-i\\i&1\end{pmatrix}.
$$

The conjugation exchanges the two projectors, and neither is fixed. The orbit idempotent $g=e_i+e_{-i}=I$ is Hermitian. The orbit theorem has $s=i+(-i)=0$, $p=i(-i)=1$ and $\lambda-\bar\lambda=2i$, so $b=1$ and $t=i$, and

$$
v=\frac{R-0}{1\cdot i}=\frac{R}{i}=-iR=\begin{pmatrix}0&i\\-i&0\end{pmatrix}.
$$

The element $v$ is skew, $v^*=iR=-v$, and $v^2=(-i)^2R^2=I$; the orbit formula reads $R=btv=i(-iR)=R$. The matrix $v$ is the complex structure of the rotation.

The example is the two-dimensional real rotation, the standard conjugate pair; the "complex structure" of the pair is $-iR$, a real matrix that squares to $I$ and is skew for the entrywise conjugation.

### A repeated eigenvalue

Let $H=\operatorname{diag}(1,1,2)$ with the conjugate transpose. The eigenvalues are $1$ and $2$, both fixed, and the projectors are

$$
e_1=E_{11}+E_{22}, \qquad e_2=E_{33},
$$

both Hermitian. The eigenvalue $1$ has algebraic multiplicity two and the eigenprojector $e_1$ has rank two; the eigenvalue decomposition groups the two equal eigenvalues into one term. This is the point at which the eigenvalue decomposition differs from a decomposition into one-dimensional eigenspaces: the decomposition is by distinct eigenvalues, and the projector of a repeated eigenvalue is the sum of the projectors of its one-dimensional pieces. The refinement into one-dimensional pieces is not unique and is not part of the eigenvalue decomposition.

## Summary

For a self-adjoint element $h$ of an algebra with a $\varsigma$-semilinear involution, the eigenvalue decomposition $h=\sum_i\lambda_i e_i$ is permuted by the involution: there is an involution $\pi$ of the index set with $e_i^*=e_{\pi(i)}$ and $\lambda_{\pi(i)}=\varsigma(\lambda_i)$. The eigenprojector $e_i$ is Hermitian exactly when the eigenvalue $\lambda_i$ is fixed by $\varsigma$; consequently all the projectors are Hermitian exactly when all the eigenvalues are fixed. In the first kind ($\varsigma=\mathrm{id}$) this is automatic, so every eigenprojector of a self-adjoint element is Hermitian; in the second kind the non-fixed eigenvalues occur in conjugate pairs, the two projectors of a pair are exchanged, and neither is Hermitian. The Hermitian orbit idempotents $g_J=\sum_{i\in J}e_i$ give a decomposition $h=\sum_J h_J$ over the fixed field, with a singleton term $\lambda g_J$ for a fixed eigenvalue and a two-element term $\frac{s}{2}g_J+btv_J$ for a conjugate pair, where $v_J$ is skew, $v_J^2=g_J$ and $v_J$ is the algebraic complex structure of the pair. When all the eigenvalues are fixed, the Peirce corners satisfy $A_{ij}^*=A_{ji}$, the diagonal corners are $*$-stable, and the decomposition is orthogonal in the algebraic sense. The eigenvalue decomposition is *The Eigenvalue Decomposition of an Element*; the involution is *Involutive Algebras*; the self-adjoint part is *The Self-Adjoint Part of an Algebra*; the unitary analogue is *Unitary Elements and Their Algebraic Decompositions*; and the form-theoretic Peirce theory is *The Adjoint of the Peirce Projection*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | the ground field, of characteristic not two |
| $\varsigma$ | an involution of $F$ |
| $F_0=F^\varsigma$ | the fixed field of $\varsigma$ |
| $A$ | a finite-dimensional unital associative $F$-algebra |
| $x^*=\sigma(x)$ | the adjoint of an element |
| $A^+=H(A)$ | the self-adjoint elements, $h^*=h$ |
| $A^-$ | the skew elements, $k^*=-k$ |
| $h=\sum_i\lambda_i e_i$ | the eigenvalue decomposition |
| $e_i$ | the eigenprojectors, $e_ie_j=\delta_{ij}e_i$, $\sum_i e_i=1$ |
| $\pi$ | the involution of the index set with $e_i^*=e_{\pi(i)}$ |
| $g_J=\sum_{i\in J}e_i$ | the orbit idempotent of a $\varsigma$-orbit $J$ |
| $t$ | a skew scalar, $\varsigma(t)=-t$, $F=F_0\oplus F_0t$ |
| $v_J$ | the skew element of a pair orbit, $v_J^2=g_J$ |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the involutions of the first and the second kind and the descent to the fixed field.
- Israel Nathan Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the symmetric and the skew elements and their polynomial calculus.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the eigenvalue decomposition and the Peirce decomposition in a finite-dimensional algebra.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the self-adjoint part and its structure under the symmetrised product.
- The fixed-field case, with fixed eigenvalues and Hermitian projectors, is [The Eigenvalue Decomposition of a Hermitian Element](the-eigenvalue-decomposition-of-a-hermitian-element.html).
