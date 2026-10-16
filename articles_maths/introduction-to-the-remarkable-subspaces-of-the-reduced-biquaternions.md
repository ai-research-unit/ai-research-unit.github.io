# __Introduction to the Remarkable Subspaces__

## Introduction

The reduced biquaternion algebra carries four conjugations and a multiplication by $j$, and the subspaces these maps single out are its **remarkable subspaces**. There are eight of them, all of real dimension two: the fixed and the anti-fixed space of each of the three involutions $\bar{\cdot}$, ${}^{\natural}$ and ${}^{*}$ — six spaces — and the two **idempotent lines** $\mathbb{C}\Pi_{1}$ and $\mathbb{C}\Pi_{2}$ selected by the multiplication by $j$. This article names them, gives for each a defining equation, a basis and a dimension, and states the two readings that organise the list: the six involutive spaces are the **coordinate planes** of the real basis $1,i,j,ij$, and the two idempotent lines are the **diagonal planes** cut out by the multiplication by $j$.

**The results.** The six spaces of the involutions are the three pairs given by the involutions of *The Two Involutions and the Group of Involutions of the Reduced Biquaternions*:

| involution | fixed space | anti-fixed space |
|---|---|---|
| bar $\bar{\cdot}$ | $\mathbb{R}\{1,j\}$, the real subalgebra | $\mathbb{R}\{i,ij\}$, the imaginary space |
| natural sign ${}^{\natural}$ | $\mathbb{C}=\mathbb{R}\{1,i\}$, the scalar line | $\mathbb{C}j=\mathbb{R}\{j,ij\}$, the $j$-line |
| star ${}^{*}$ | $\mathbb{R}\{1,ij\}$, the Hermitian subspace | $\mathbb{R}\{i,j\}$, the anti-Hermitian subspace |

The bar and the natural sign are the two generators, and the star is their composite; each of the three splits the real four-dimensional space into a plane and its complement, and each plane is $\mathbb{C}$-linear or not according to the involution. Because each of the six spaces is the real span of a **pair of the four real basis elements**, the three involutions act on all six; and the four real lines $\mathbb{R}$, $\mathbb{R}i$, $\mathbb{R}j$, $\mathbb{R}ij$ carry the **characters** $(\varepsilon_{\bar{}},\varepsilon_{\natural},\varepsilon_{*})$ of the three involutions, four of the eight possible signs, with $\varepsilon_{*}=\varepsilon_{\bar{}}\varepsilon_{\natural}$. The two idempotent lines are the eigenlines of the multiplication by $j$ and lie on neither list of coordinates; they are the line of $\Pi_{1}$ and the line of $\Pi_{2}$, with $\Pi_{1,2}=\tfrac12(1\pm j)$, and they are the two minimal ideals of *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions*.

**The character of each space.** The six spaces are the sums of the pairs of real lines, and the fourth *character* relation organises them: a space defined by one involution is the sum of the two lines on which that involution has the same sign, and the **Hermitian** subspace is the one fixed by the star while the **anti-Hermitian** is the one negated. On the Hermitian subspace the algebraic norm is positive, $N=a^{2}+b^{2}$, and on the anti-Hermitian it is negative, $N=-(a^{2}+b^{2})$; on the idempotent lines the norm vanishes, and the lines are the zero divisors.

**Boundaries.** The involutions and their fixed spaces are *The Two Involutions and the Group of Involutions of the Reduced Biquaternions*; the bases and the two scalar systems are *Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$*; the idempotents are *Square Roots of One and the Idempotents of the General Plain Algebra of the Reduced Biquaternions*. The norms are those of *The Four Products, Their Forms and Their Algebraic Norms*, and the two sesquilinear forms of the star are *The Forms of the General Plain Algebra of the Reduced Biquaternions*. The spaces as subalgebras and their closure under the product are *Decompositions Along the Remarkable Subspaces* and *Comparison of the Remarkable Subspaces*, below this article in this category; the general biquaternion list is *Introduction to the Remarkable Subspaces* of the biquaternion category, and the complex split-quaternion list is *Remarkable Subspaces of the Split-Complexoid and the Two Forms*.

## The Three Involutions and Their Spaces

### The Fixed and Anti-Fixed Space of an Involution

**An involution of the algebra splits the real space into the fixed and the anti-fixed space, and the two are complementary.**

**Definition.** For an involution $\sigma$ of $\mathbb{B}_{\mathrm{r}}$ the **fixed space** is $\{T:\sigma(T)=T\}$ and the **anti-fixed space** is $\{T:\sigma(T)=-T\}$.

**Proposition.** For an involution $\sigma$ the fixed and the anti-fixed space are real subspaces, they meet in $\{0\}$, and their sum is the whole space; over $\mathbb{R}$ they are the eigenspaces of $\sigma$ for the eigenvalues $+1$ and $-1$, and the projections onto them are
$$
P_{+}=\tfrac12(\mathrm{id}+\sigma),\qquad P_{-}=\tfrac12(\mathrm{id}-\sigma).
$$

*Proof.* The two sets are the eigenspaces of the real-linear involution $\sigma$ and its eigenvalues are $\pm1$ since $\sigma^{2}=\mathrm{id}$; the projections are the standard ones, $P_{+}^{2}=P_{+}$, $P_{-}^{2}=P_{-}$, $P_{+}P_{-}=0$, $P_{+}+P_{-}=\mathrm{id}$.

### The Six Spaces

**The fixed and the anti-fixed spaces of the bar, the natural sign and the star are the six coordinate planes.**

**Theorem (the six spaces).** The involutions split the real space as follows, each space having real dimension two:

| involution | fixed space | anti-fixed space |
|---|---|---|
| bar $\bar{\cdot}$ | $\mathbb{R}\{1,j\}$ | $\mathbb{R}\{i,ij\}$ |
| natural sign ${}^{\natural}$ | $\mathbb{C}=\mathbb{R}\{1,i\}$ | $\mathbb{C}j=\mathbb{R}\{j,ij\}$ |
| star ${}^{*}$ | $\mathbb{R}\{1,ij\}$ | $\mathbb{R}\{i,j\}$ |

Each space is the real span of a pair of the four basis elements $1,i,j,ij$.

*Proof.* The action on the basis is $\bar{\cdot}:(1,i,j,ij)\mapsto(1,-i,j,-ij)$, ${}^{\natural}:(1,i,j,ij)\mapsto(1,i,-j,-ij)$ and ${}^{*}:(1,i,j,ij)\mapsto(1,-i,-j,ij)$ (*The Two Involutions and the Group of Involutions of the Reduced Biquaternions*). A basis element is fixed or negated by each involution, so each fixed space is the span of the fixed basis elements and each anti-fixed space the span of the negated ones.

### The Characters and the Four Lines

**Each real line $\mathbb{R}$, $\mathbb{R}i$, $\mathbb{R}j$, $\mathbb{R}ij$ carries a character of the Klein group, and the six coordinate planes are the sums of the lines on which two of the three characters agree.**

**Definition.** For a basis line $L$ the **character** of $L$ is the triple $\varepsilon(L)=(\varepsilon_{\bar{}},\varepsilon_{\natural},\varepsilon_{*})$ with $\sigma$ acting on $L$ by $\varepsilon_{\sigma}\,\mathrm{id}$.

**Theorem (the character table).** The four lines have the characters

| line | $\varepsilon_{\bar{}}$ | $\varepsilon_{\natural}$ | $\varepsilon_{*}$ |
|---|---|---|---|
| $\mathbb{R}$ | $+$ | $+$ | $+$ |
| $\mathbb{R}i$ | $-$ | $+$ | $-$ |
| $\mathbb{R}j$ | $+$ | $-$ | $-$ |
| $\mathbb{R}ij$ | $-$ | $-$ | $+$ |

and they satisfy $\varepsilon_{*}=\varepsilon_{\bar{}}\varepsilon_{\natural}$ at every line. The six planes of §*The Six Spaces* are the sums of the pairs of lines on which the corresponding involutions have matching signs:
$$
\mathbb{R}\{1,j\}=\mathbb{R}\oplus\mathbb{R}j,\quad \mathbb{R}\{i,ij\}=\mathbb{R}i\oplus\mathbb{R}ij,\quad \mathbb{C}=\mathbb{R}\oplus\mathbb{R}i,
$$
$$
\mathbb{C}j=\mathbb{R}j\oplus\mathbb{R}ij,\quad \mathbb{R}\{1,ij\}=\mathbb{R}\oplus\mathbb{R}ij,\quad \mathbb{R}\{i,j\}=\mathbb{R}i\oplus\mathbb{R}j.
$$

*Proof.* Read the characters from the basis action: $1$ is fixed by all three; $i$ is negated by the bar and the star and fixed by the natural sign; $j$ is negated by the natural sign and the star and fixed by the bar; $ij$ is negated by the bar and the natural sign and fixed by the star. The relation $\varepsilon_{*}=\varepsilon_{\bar{}}\varepsilon_{\natural}$ is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, and the identifications of the planes are read from the table.

**Remark (three pairs, one structure).** The six planes are three complementary pairs, one per involution: the pair $\{\mathbb{C},\mathbb{C}j\}$ of the natural sign, the pair $\{\mathbb{R}\{1,j\},\mathbb{R}\{i,ij\}\}$ of the bar, and the pair $\{\mathbb{R}\{1,ij\},\mathbb{R}\{i,j\}\}$ of the star. Each pair sums to the whole real space and meets in $\{0\}$; the pairs are not the same decompositions, and their comparison is *Decompositions Along the Remarkable Subspaces*.

## The Hermitian and Anti-Hermitian Subspaces

**The Hermitian subspace is the fixed plane of the star and the anti-Hermitian subspace its anti-fixed plane; the two are the real and the imaginary part of the star.**

**Definition.** An element is **Hermitian** when $T^{*}=T$ and **anti-Hermitian** when $T^{*}=-T$; the **Hermitian subspace** is $\mathbb{R}\{1,ij\}$ and the **anti-Hermitian subspace** is $\mathbb{R}\{i,j\}$.

**Proposition.** Every element decomposes uniquely as the sum of a Hermitian and an anti-Hermitian part,
$$
T=T_{+}+T_{-},\qquad T_{\pm}=\tfrac12(T\pm T^{*}),
$$
and the two parts are the projections of §*The Fixed and Anti-Fixed Space of an Involution* for $\sigma={}^{*}$.

*Proof.* This is the projection statement for the star, with $\tfrac12(\mathrm{id}+{}^{*})$ and $\tfrac12(\mathrm{id}-{}^{*})$; the directness is the vanishing of the intersection of the two planes.

**Corollary (the norms on the two planes).** On the Hermitian subspace the algebraic norm is $\langle a+bij\rangle_{\natural}=a^{2}+b^{2}>0$ for a nonzero element, so every nonzero Hermitian element is a unit; on the anti-Hermitian subspace the norm is $\langle ai+bj\rangle_{\natural}=-a^{2}-b^{2}<0$. The star plane is the copy $\mathbb{R}\{1,ij\}\cong\mathbb{C}$ of the complex field inside the algebra, the element $ij$ playing the role of the imaginary unit, since $(ij)^{2}=i^{2}j^{2}=(-1)(+1)=-1$.

**Remark (Hermitian is not positive).** The name refers to the star and not to a sign of a form: the general plain sesquilinear form has the value $\langle T\rangle_{*}=\lvert A\rvert^{2}-\lvert B\rvert^{2}=a^{2}-b^{2}$ on a Hermitian element $T=a+bij$, which is indefinite in $a,b$. The definite form of the algebra is the general quaternionic sesquilinear form $\langle\cdot,\cdot\rangle_{\natural*}$, and the positivity of $\langle\cdot\rangle_{\natural}$ on the Hermitian subspace is the positivity of the diagonal of a bilinear form, not of $\langle\cdot,\cdot\rangle_{*}$. The forms are *The Forms of the General Plain Algebra of the Reduced Biquaternions*.

## The Idempotent Lines

**The two idempotent lines are the eigenlines of the multiplication by $j$, and they are diagonal planes, not coordinate planes.**

**Theorem (the idempotent lines).** The multiplication by $j$ has the two eigenvalues $+1$ and $-1$ and the two eigenlines
$$
\mathbb{C}\Pi_{1}=\mathbb{R}\{\Pi_{1},i\Pi_{1}\}=\{T:jT=T\},\qquad \mathbb{C}\Pi_{2}=\{T:jT=-T\},
$$
each of real dimension two, with $\Pi_{1,2}=\tfrac12(1\pm j)$.

*Proof.* The element $j$ satisfies $j^{2}=1$, so its minimal polynomial $\lambda^{2}-1$ has the two linear factors $\lambda\mp1$ and the eigenline of the eigenvalue $+1$ is the line of the idempotent $\tfrac12(1+j)=\Pi_{1}$, the eigenline of $-1$ that of $\Pi_{2}$. Each is a complex line, of real dimension two, and the two are independent and complementary.

**Corollary (the diagonal).** In the real basis the two idempotent lines are the graphs
$$
\Pi_{1}=\tfrac12(1+j)=\tfrac12(\mathbf 1+\mathbf j),\qquad \Pi_{2}=\tfrac12(\mathbf 1-\mathbf j),
$$
where $\mathbf 1,\mathbf j$ are the coordinate vectors; the lines are spanned by the vectors $\tfrac12(1,0,1,0)$ and $\tfrac12(0,1,0,1)$ for $\mathbb{C}\Pi_{1}$ and $\tfrac12(1,0,-1,0)$, $\tfrac12(0,1,0,-1)$ for $\mathbb{C}\Pi_{2}$. They are not the spans of pairs of basis elements, and in the matrix model of *The General Plain Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions* they are the two coordinate lines of the diagonal algebra.

**Remark (the involutions on the idempotent lines).** The bar fixes each idempotent, $\overline{\Pi_{i}}=\Pi_{i}$, while the natural sign and the star exchange them, $\Pi_{1}^{\natural}=\Pi_{1}^{*}=\Pi_{2}$, so the two lines are exchanged by ${}^{\natural}$ and ${}^{*}$ and fixed by the bar. This is the behaviour of *Square Roots of One and the Idempotents of the General Plain Algebra of the Reduced Biquaternions*, and it is the reason the idempotent lines are not among the fixed spaces of the three involutions.

## The Relations between the Spaces

### Inclusions and Intersections

**The six coordinate planes meet two by two in a real line or in $\{0\}$, and the pairs summing to the whole space are the three decompositions.**

**Theorem (the intersections).** The real dimensions $\dim(L\cap M)$ of the six coordinate planes are

| | $\mathbb{C}$ | $\mathbb{C}j$ | $\mathbb{R}\{1,j\}$ | $\mathbb{R}\{i,ij\}$ | $\mathbb{R}\{1,ij\}$ | $\mathbb{R}\{i,j\}$ |
|---|---|---|---|---|---|---|
| $\mathbb{C}$ | $2$ | $0$ | $1$ | $1$ | $1$ | $1$ |
| $\mathbb{C}j$ | $0$ | $2$ | $1$ | $1$ | $1$ | $1$ |
| $\mathbb{R}\{1,j\}$ | $1$ | $1$ | $2$ | $0$ | $1$ | $1$ |
| $\mathbb{R}\{i,ij\}$ | $1$ | $1$ | $0$ | $2$ | $1$ | $1$ |
| $\mathbb{R}\{1,ij\}$ | $1$ | $1$ | $1$ | $1$ | $2$ | $0$ |
| $\mathbb{R}\{i,j\}$ | $1$ | $1$ | $1$ | $1$ | $0$ | $2$ |

and for every pair $\dim(L+M)=\dim L+\dim M-\dim(L\cap M)=4-\dim(L\cap M)$.

*Proof.* Each plane is the span of two of the four real lines, so the intersection of two planes is the span of the common lines and its dimension is $0$, $1$ or $2$ by the character table; the displayed entries are read off the four-line table, and the dimension formula is the standard one for two subspaces.

**Corollary (the three complementary pairs).** Exactly three pairs of distinct planes sum to the whole real space, namely the three pairs of one involution:
$$
\mathbb{C}\oplus\mathbb{C}j,\qquad \mathbb{R}\{1,j\}\oplus\mathbb{R}\{i,ij\},\qquad \mathbb{R}\{1,ij\}\oplus\mathbb{R}\{i,j\}=\mathbb{B}_{\mathrm{r}}.
$$
All the other pairs sum to a real three-dimensional space, since their intersection is a line.

**Corollary (the idempotent lines).** The idempotent lines meet the whole space as $\mathbb{C}\Pi_{1}\oplus\mathbb{C}\Pi_{2}=\mathbb{B}_{\mathrm{r}}$ and $\mathbb{C}\Pi_{1}\cap\mathbb{C}\Pi_{2}=0$; each idempotent line meets a coordinate plane either in a real line or in $\{0\}$, since it is diagonal and the coordinate planes are not.

### The Norm on the Spaces

**On the six coordinate planes the norm is either positive definite, negative definite or split, and on the idempotent lines it vanishes identically.**

**Theorem (the norms).** The algebraic norm $\langle T\rangle_{\natural}=A^{2}-B^{2}$ restricted to the spaces is

| space | parametrisation | $N$ | sign |
|---|---|---|---|
| $\mathbb{C}$ | $A$ | $A^{2}$ | complex |
| $\mathbb{C}j$ | $Bj$ | $-B^{2}$ | complex |
| $\mathbb{R}\{1,j\}$ | $a+bj$ | $a^{2}-b^{2}$ | split |
| $\mathbb{R}\{i,ij\}$ | $i(a+bj)$ | $-(a^{2}-b^{2})$ | split |
| $\mathbb{R}\{1,ij\}$ | $a+bij$ | $a^{2}+b^{2}$ | positive definite |
| $\mathbb{R}\{i,j\}$ | $ai+bj$ | $-(a^{2}+b^{2})$ | negative definite |
| $\mathbb{C}\Pi_{1},\mathbb{C}\Pi_{2}$ | $x\Pi_{i}$ | $0$ | zero |

with $a,b\in\mathbb{R}$.

*Proof.* Substitute each parametrisation into $\langle T\rangle_{\natural}=A^{2}-B^{2}$: for $T=a+bj$ the coordinates are $A=a$, $B=b$, so $N=a^{2}-b^{2}$; for $T=a+bij$ they are $A=a$, $B=ib$, so $N=a^{2}-(ib)^{2}=a^{2}+b^{2}$; for $T=ai+bj$ they are $A=ai$, $B=b$, so $N=(ai)^{2}-b^{2}=-(a^{2}+b^{2})$; and for $T=x\Pi_{i}$ the coordinates have $A\pm B=0$, so $N=0$. The complex cases are the two complex lines and the two split planes.

**Corollary (the zero divisors).** The two idempotent lines are exactly the null set of the norm, and their nonzero elements are the zero divisors of *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*; the Hermitian and anti-Hermitian subspaces are the two kinds of element on which the norm has a definite sign, and the real subalgebra and its $i$-multiple are the two split planes.

## Summary

The remarkable subspaces of the reduced biquaternion algebra are eight planes of real dimension two: the fixed and the anti-fixed space of each of the three involutions — the bar giving the real subalgebra $\mathbb{R}\{1,j\}$ and the imaginary space $\mathbb{R}\{i,ij\}$, the natural sign giving the scalar line $\mathbb{C}=\mathbb{R}\{1,i\}$ and the $j$-line $\mathbb{C}j$, the star giving the Hermitian subspace $\mathbb{R}\{1,ij\}$ and the anti-Hermitian subspace $\mathbb{R}\{i,j\}$ — and the two idempotent lines $\mathbb{C}\Pi_{1}$ and $\mathbb{C}\Pi_{2}$. The six involutive spaces are the coordinate planes, each spanned by a pair of the four real basis elements, and they are spanned by the four real lines $\mathbb{R}$, $\mathbb{R}i$, $\mathbb{R}j$, $\mathbb{R}ij$, whose characters $(\varepsilon_{\bar{}},\varepsilon_{\natural},\varepsilon_{*})$ are $+++$, $-+-$, $+--$ and $--+$ and satisfy $\varepsilon_{*}=\varepsilon_{\bar{}}\varepsilon_{\natural}$. The two idempotent lines are the eigenlines of the multiplication by $j$, diagonal planes spanned by $\Pi_{1}$ and by $\Pi_{2}$ and exchanged by the natural sign and the star while fixed by the bar. The six coordinate planes form three complementary pairs, one per involution, and any two of them meet in a real line or in $\{0\}$. The norm is positive definite on the Hermitian subspace, negative definite on the anti-Hermitian subspace, split on the real subalgebra and its $i$-multiple, complex on the two complex lines, and identically zero on the two idempotent lines, which are the null set and the zero divisors.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\bar{\cdot},\ {}^{\natural},\ {}^{*}$ | the bar, the natural sign and the star, the three involutions |
| $\mathbb{C}=\mathbb{R}\{1,i\}$ | the scalar line, the fixed space of the natural sign |
| $\mathbb{C}j=\mathbb{R}\{j,ij\}$ | the $j$-line, the anti-fixed space of the natural sign |
| $\mathbb{R}\{1,j\}$ | the real subalgebra, the fixed space of the bar |
| $\mathbb{R}\{i,ij\}$ | the imaginary space, the anti-fixed space of the bar |
| $\mathbb{R}\{1,ij\}$ | the Hermitian subspace, the fixed space of the star |
| $\mathbb{R}\{i,j\}$ | the anti-Hermitian subspace, the anti-fixed space of the star |
| $\mathbb{C}\Pi_{1},\ \mathbb{C}\Pi_{2}$ | the idempotent lines, the eigenlines of the multiplication by $j$ |
| $\varepsilon(L)=(\varepsilon_{\bar{}},\varepsilon_{\natural},\varepsilon_{*})$ | the character of a real line |
| $N=A^{2}-B^{2}$ | the algebraic norm read on each space |

## Further Reading

- *The Two Involutions and the Group of Involutions of the Reduced Biquaternions* (`articles_maths/the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions.md`), for the involutions and their fixed spaces.
- *Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$* (`articles_maths/reduced-biquaternions-as-a-vector-space-over-r-and-c.md`), for the bases and the two scalar systems.
- *Square Roots of One and the Idempotents of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the idempotents and the two lines.
- *Decompositions Along the Remarkable Subspaces* (`articles_maths/decompositions-along-the-remarkable-subspaces-of-the-reduced-biquaternions.md`), for the decompositions the spaces carry.
- *Comparison of the Remarkable Subspaces* (`articles_maths/comparison-of-the-remarkable-subspaces-of-the-reduced-biquaternions.md`), for the spaces at a glance.
- *The Forms of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/the-forms-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the forms the star carries.
