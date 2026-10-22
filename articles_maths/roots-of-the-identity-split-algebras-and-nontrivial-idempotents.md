# __Roots of the Identity, Split Algebras and Nontrivial Idempotents__

## Introduction

A **root of the identity** in an algebra $A$ is an element $u$ with $u^2=1$. The name distinguishes the equation from the roots of unity of higher order: a root of the identity is a solution of $x^2-1=0$, and the article never considers $u^n=1$ for $n>2$. The roots of the identity are the algebraic form of the reflections of a vector space, and their theory is the theory of the simplest spectral decomposition, the one with the two eigenvalues $+1$ and $-1$.

The link with idempotents is the **halving correspondence**. When $2$ is invertible, an idempotent $e$ gives the root $u=2e-1$, and a root $u$ gives the idempotent $e=(1+u)/2$; the two constructions are inverse. The root acts as $+1$ on the image of $e$ and as $-1$ on the image of $1-e$, so the pair $(e,1-e)$ is the spectral decomposition of $u$, and the halving is the passage between an idempotent and its reflection. The correspondence is a bijection of sets, not a ring homomorphism: it does not preserve products, even when the idempotents commute; it preserves instead the Boolean group structure of commuting idempotents, as §*What the correspondence does not preserve* shows. In characteristic two it collapses completely.

The article uses the correspondence to separate three classes of algebras. A **division algebra** has no nontrivial idempotent and no root of the identity other than $\pm1$. A **split algebra**, in the weak sense of this article, has a nontrivial idempotent, equivalently a root other than $\pm1$ when $2$ is invertible. The two classes do not exhaust the algebras: the dual numbers have no nontrivial idempotent and are not a division algebra, and they are the standard warning that "no nontrivial idempotent" is weaker than "division." In the semisimple case the warning disappears: a semisimple algebra has no nontrivial idempotent exactly when it is a division algebra, and it is split exactly when it is not a division algebra.

The article assumes the idempotent theory of *Unital Algebras*, §*Idempotents and the Peirce Decomposition*, the involutions of *Involutive Algebras* only as a contrast, and the primitive idempotents of *Primitive Idempotents and Minimal Left Ideals*. The matrix case is *Matrix Algebras*; the split-complex algebra is *Split-Complex Algebra* and *The Number Systems as Clifford Algebras*; the dual numbers are *Dual-Numbers Algebra*; the semisimple structure is *Simple and Semisimple Modules*, §*Semisimple Algebras and Wedderburn–Artin*; and the Jordan–Chevalley decomposition is *Nilpotent Elements and the Jordan–Chevalley Decomposition*. No form, norm or topology is used.

Throughout, $F$ is a field and $A$ is a unital associative $F$-algebra with $1\neq0$, not assumed commutative. The identity is $1_A$, written $1$ when no confusion is possible. The characteristic is arbitrary unless stated, and the halving correspondence is stated for $2$ invertible; the characteristic-two section records what replaces it. The idempotent is $e$ and its complement is $f=1-e$.

## Roots of the Identity

### Definition and first properties

**Definition.** A **root of the identity** of $A$ is an element $u\in A$ with $u^2=1$. The set of roots is

$$
R(A)=\{u\in A:u^2=1\}.
$$

The trivial roots are $1$ and $-1$; they coincide in characteristic two. A root is a unit, with $u^{-1}=u$, so $R(A)\subseteq A^\times$.

**Proposition.** Let $u,v\in R(A)$.

**(a)** $u^{-1}=u$, and $u^{-1}\in R(A)$.

**(b)** If $u$ and $v$ commute, then $uv\in R(A)$; in particular the central roots $R(A)\cap Z(A)$ form a subgroup of $A^\times$.

**(c)** If $A$ is commutative, $R(A)$ is a subgroup of $A^\times$, the **group of roots of the identity**.

**(d)** If $A$ is not commutative, $R(A)$ need not be closed under multiplication.

*Proof.* (a) $u^2=1$ gives $u^{-1}=u$, and $(u^{-1})^2=u^2=1$. (b) $(uv)^2=uvuv=u^2v^2=1$ when $uv=vu$. The central roots are closed under multiplication, contain $1$, and are closed under inversion by (a), so they form a subgroup. (c) is (b) with every pair commuting. (d) In $M_2(F)$ with $F$ of characteristic not two, let

$$
u=\begin{pmatrix}0&1\\1&0\end{pmatrix}, \qquad v=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

Then $u^2=v^2=1$, but

$$
uv=\begin{pmatrix}0&-1\\1&0\end{pmatrix}, \qquad (uv)^2=\begin{pmatrix}-1&0\\0&-1\end{pmatrix}\neq1.
$$

So the product of two roots need not be a root.

**Remark.** The roots of the identity are not the roots of $-1$. The quaternion algebra $\mathbb{H}$ has the two roots $\pm1$ of $x^2=1$ and the whole sphere of roots of $x^2=-1$; the two equations have different theories. The roots of $-1$ are the subject of the complex structures and the almost-complex geometry, and they are not used here.

### Division algebras

**Proposition.** Let $D$ be a division algebra over $F$.

**(a)** If $2\neq0$ in $F$, then $R(D)=\{1,-1\}$.

**(b)** If $2=0$ in $F$, then $R(D)=\{1\}$.

**(c)** The only idempotents of $D$ are $0$ and $1$.

*Proof.* (a) $u^2-1=(u-1)(u+1)=0$. A division algebra has no zero divisors, so $u-1=0$ or $u+1=0$. (b) In characteristic two, $u^2-1=(u-1)^2$, so $u-1=0$. (c) $e^2=e$ gives $e(e-1)=0$, hence $e=0$ or $e=1$.

The proposition is the model of the division side of the article: no nontrivial idempotent, and no nontrivial root of the identity. The converse is the subject of §*Division Algebras and Nontrivial Idempotents*, where it is shown to fail without a hypothesis.

### Matrix algebras

**Proposition.** Let $A=M_n(F)$ and suppose $2\neq0$ in $F$. A matrix $U\in A$ satisfies $U^2=I$ exactly when it is diagonalisable over $F$ with eigenvalues in $\{1,-1\}$. The idempotents of $A$ are the diagonalisable matrices with eigenvalues in $\{0,1\}$, and the halving correspondence of §*The Halving Correspondence* is a bijection between the two sets.

*Proof.* If $U^2=I$, the polynomial $x^2-1=(x-1)(x+1)$ has distinct roots and annihilates $U$, so the minimal polynomial divides $x^2-1$ and has distinct linear factors; hence $U$ is diagonalisable with eigenvalues $\pm1$. Conversely a diagonalisable matrix with eigenvalues $\pm1$ satisfies $U^2=I$. The idempotent statement is the same argument with $x^2-x=x(x-1)$, and the halving is the bijection $E\mapsto2E-I$ of §*The Halving Correspondence*.

**Remark.** In characteristic two the polynomial $x^2-1=(x-1)^2$ has a repeated root, and a root of the identity is a unipotent matrix $U=1+N$ with $N^2=0$; it need not be diagonalisable. The idempotents are still the diagonalisable matrices with eigenvalues $0,1$, and the halving correspondence is no longer available. The matrix case is therefore the cleanest illustration of both the correspondence and its characteristic-two failure.

**Example (the rank).** In $M_n(F)$ with $2\neq0$, an idempotent of rank $r$ corresponds to a root of the identity with eigenvalue $+1$ of multiplicity $r$ and eigenvalue $-1$ of multiplicity $n-r$. The trace of the root is $2r-n$, and the rank is recovered as $r=(n+\operatorname{tr}U)/2$. The correspondence is a bijection between the idempotents of rank $r$ and the involutions with $+1$-eigenspace of dimension $r$. For $n=2$ the nontrivial idempotents are the rank-one projections, and the nontrivial roots are the reflections $\operatorname{diag}(1,-1)$ and $\operatorname{diag}(-1,1)$ in a suitable basis, together with the off-diagonal reflections; the halving pairs each projection with its reflection.

## The Halving Correspondence

### The bijection

**Theorem.** Suppose $2$ is invertible in $F$. The maps

$$
e\longmapsto u=2e-1, \qquad u\longmapsto e=\frac{1+u}{2}
$$

are inverse bijections between the set $\operatorname{Idem}(A)$ of idempotents and the set $R(A)$ of roots of the identity.

*Proof.* If $e^2=e$, then

$$
(2e-1)^2=4e^2-4e+1=1,
$$

so $u=2e-1$ is a root. If $u^2=1$, then

$$
\left(\frac{1+u}{2}\right)^2=\frac{1+2u+u^2}{4}=\frac{2+2u}{4}=\frac{1+u}{2},
$$

so $e=(1+u)/2$ is idempotent. The two composites are

$$
\frac{1+(2e-1)}{2}=e, \qquad 2\left(\frac{1+u}{2}\right)-1=u,
$$

so the maps are inverse. The use of $2$ is explicit in both formulas.

**Corollary.** Under the correspondence:

**(a)** $e=0$ corresponds to $u=-1$, and $e=1$ corresponds to $u=1$.

**(b)** The complement $1-e$ corresponds to $-u$.

**(c)** The idempotent $e$ is the projection onto the $+1$-eigenspace of $u$, and $1-e$ is the projection onto the $-1$-eigenspace; in formulas,

$$
ue=eu=e, \qquad u(1-e)=(1-e)u=-(1-e).
$$

**(d)** The root $u$ is a reflection: $u^2=1$, and the algebra decomposes as $A=Ae\oplus A(1-e)$ with $u$ acting as $+1$ on the first summand and $-1$ on the second.

*Proof.* (a) and (b) are immediate from the formulas. (c) $ue=(2e-1)e=2e-e=e$ and $u(1-e)=(2e-1)(1-e)=-(1-e)$; the same on the other side. (d) is (c) read on the direct sum.

### What the correspondence does not preserve

The halving is a bijection of sets, and it does not respect the multiplicative structures.

**Proposition.** Let $e,f$ be idempotents with roots $u=2e-1$, $v=2f-1$.

**(a)** $uv$ is a root of the identity exactly when $u$ and $v$ commute, equivalently when $e$ and $f$ commute.

**(b)** When $e$ and $f$ commute, the idempotent corresponding to $uv$ is

$$
1-(e+f-2ef),
$$

the **complement of the symmetric difference** of $e$ and $f$.

**(c)** In a commutative algebra, the idempotents form a Boolean ring under

$$
e\oplus f=e+f-2ef, \qquad e\wedge f=ef,
$$

and the map $e\mapsto1-2e$ is an isomorphism of groups from $(\operatorname{Idem}(A),\oplus)$ onto $(R(A),\cdot)$. The map $e\mapsto2e-1$ is its negative; it is a bijection, but it is not a homomorphism, and it satisfies $w(e\oplus f)=-w(e)w(f)$.

*Proof.* (a) $(uv)^2=uvuv=u^2v^2=1$ exactly when $uv=vu$. Since $u=2e-1$ and $v=2f-1$ are polynomials in $e$ and $f$, $uv=vu$ exactly when $ef=fe$. (b) When $e$ and $f$ commute,

$$
uv=(2e-1)(2f-1)=4ef-2e-2f+1=1-2(e+f-2ef),
$$

and $g=e+f-2ef$ is idempotent because $e$ and $f$ commute; the root $uv$ corresponds to $(1+uv)/2=1-g$. (c) The Boolean ring laws are the usual ones for commuting idempotents, and

$$
(1-2e)(1-2f)=1-2(e+f-2ef)=1-2(e\oplus f),
$$

so $e\mapsto1-2e$ is multiplicative; it is bijective by the theorem and preserves $0\mapsto1$, hence is a group isomorphism. The map $w(e)=2e-1=-(1-2e)$ is the negative of this isomorphism; it is bijective, but $w(e\oplus f)=-(1-2(e\oplus f))=-w(e)w(f)$, so it is not a homomorphism.

**Remark.** In a noncommutative algebra the idempotents do not form a Boolean ring, and the halving is only a bijection. The product of two roots can fail to be a root, as the $2\times2$ example of §*Definition and first properties* shows; the product of two commuting roots is a root, but it corresponds to the complement of the symmetric difference of the two idempotents, not to their product. The correspondence is therefore a statement about the **additive** Boolean structure, not about the multiplicative structure of the algebra.

### The spectral reading

The halving is the simplest case of the eigenvalue decomposition. The element $u$ has the two eigenvalues $+1$ and $-1$, and the idempotents $e$ and $1-e$ are the corresponding eigenprojectors:

$$
A=Ae\oplus A(1-e), \qquad u=\;1\cdot e+(-1)\cdot(1-e)=2e-1.
$$

The decomposition is the two-term case of *The Eigenvalue Decomposition of an Element*, and the formula $e=(1+u)/2$ is the Lagrange–Sylvester formula for the two eigenvalues. The root $u$ is diagonalisable in the sense of that article exactly when $e$ exists, which is automatic when $2$ is invertible; in characteristic two the spectral decomposition is not available in this form, and the Jordan–Chevalley decomposition of *Nilpotent Elements and the Jordan–Chevalley Decomposition* is the substitute.

## Division Algebras and Nontrivial Idempotents

### The division implication

**Proposition.** A division algebra has no idempotent other than $0$ and $1$, and no root of the identity other than $\pm1$ when $2\neq0$, or other than $1$ when $2=0$.

*Proof.* This is the proposition of §*Division Algebras*.

The implication is one-way. The converse fails, and the dual numbers are the standard counterexample.

**Example (the dual numbers).** Let $A=F[\varepsilon]/(\varepsilon^2)$ with $2\neq0$. An idempotent $e=a+b\varepsilon$ satisfies $e^2=a^2+2ab\varepsilon$ and $e^2=e$, so $a^2=a$ and $2ab=b$. If $a=0$, then $b=0$; if $a=1$, then $2b=b$, hence $b=0$. Thus the only idempotents are $0$ and $1$. The algebra is not a division algebra, since $\varepsilon\neq0$ and $\varepsilon^2=0$. The roots of the identity are also only $\pm1$: $u=a+b\varepsilon$ gives $u^2=a^2+2ab\varepsilon=1$, so $a=\pm1$ and $b=0$. So the dual numbers have the same idempotents and the same roots as a division algebra, without being one.

**Remark (the correct converse).** The converse holds under a hypothesis that excludes the nilpotent direction. A finite-dimensional algebra over a field with no zero divisors is a division algebra; a finite-dimensional **semisimple** algebra with no nontrivial idempotent is a division algebra. The second statement follows from Wedderburn–Artin: a semisimple algebra is a product of matrix algebras $M_{n_i}(D_i)$, and a factor with $n_i\geq2$ has the nontrivial idempotent $E_{11}$, while a product of two or more factors has the central idempotents $(1,0,\dots,0)$; hence a semisimple algebra with no nontrivial idempotent is a single $M_1(D)=D$, a division algebra. The dual numbers fail both hypotheses: they have zero divisors and they are not semisimple.

### The semisimple dichotomy

**Theorem.** Let $A$ be a finite-dimensional semisimple algebra over $F$. Then $A$ is a division algebra exactly when it has no nontrivial idempotent. Equivalently, $A$ has a nontrivial idempotent exactly when it is not a division algebra.

*Proof.* A division algebra has no nontrivial idempotent by the proposition. Conversely, if $A$ is semisimple and has no nontrivial idempotent, Wedderburn–Artin writes $A\cong\prod_i M_{n_i}(D_i)$; as in the remark, the product has only one factor and $n_1=1$, so $A\cong D_1$ is a division algebra. The contrapositive gives the second statement.

**Corollary.** In the semisimple case the three conditions

$$
A\ \text{is a division algebra}, \qquad A\ \text{has no nontrivial idempotent}, \qquad R(A)=\{\pm1\}\ (2\neq0)
$$

are equivalent. The dual numbers show that none of the equivalences survives without semisimplicity.

## Split Algebras

### Definition

**Definition (this article).** An algebra $A$ is **split** when it contains a nontrivial idempotent. Equivalently, the regular left module splits as a direct sum $A=Ae\oplus A(1-e)$ of two nonzero left ideals, and the regular right module splits in the same way.

The word is used in the weak sense of the title: the algebra splits as a module over itself. It is not the stronger notion **split semisimple**, which requires $A\cong\prod_i M_{n_i}(F)$; the relation between the two is stated at the end of the section.

**Proposition.** Let $A$ be an algebra.

**(a)** $A$ is split exactly when it has a nontrivial idempotent.

**(b)** If $e$ is a nontrivial idempotent, then $A=Ae\oplus A(1-e)$ with both summands nonzero; if $e$ is central, the decomposition is a product of algebras, $A\cong Ae\times A(1-e)$.

**(c)** If $A$ is split and $2$ is invertible, then $A$ has a root of the identity other than $\pm1$.

*Proof.* (a) is the definition. (b) is the Peirce decomposition at the level of the regular module; the product statement is the central idempotent theorem of *Unital Algebras*. (c) If $e$ is nontrivial, $u=2e-1$ is a root by the halving theorem, and $u\neq\pm1$ because $e\neq0,1$.

### The root criterion

**Theorem.** Suppose $2$ is invertible in $F$. An algebra $A$ is split exactly when it has a root of the identity other than $1$ and $-1$.

*Proof.* If $e$ is a nontrivial idempotent, $u=2e-1$ is a root and $u\neq\pm1$. Conversely, if $u\in R(A)$ and $u\neq\pm1$, then $e=(1+u)/2$ is an idempotent and $e\neq0,1$, because $u\neq-1,1$. The two constructions are inverse by the halving theorem.

**Corollary.** For an algebra over a field of characteristic not two, the following are equivalent:

$$
A\ \text{is split}, \qquad A\ \text{has a nontrivial idempotent}, \qquad A\ \text{has a nontrivial root of the identity}.
$$

The equivalence fails in characteristic two, where the halving is unavailable and the roots of the identity can be plentiful while the idempotents are not; §*Characteristic Two* gives the examples.

### Examples

**Example (the split algebra $F\times F$).** The idempotents are $(1,0)$ and $(0,1)$, both nontrivial; the roots of the identity are $(\pm1,\pm1)$, four elements when $2\neq0$, and the halving pairs

$$
(1,0)\longleftrightarrow(1,-1), \qquad (0,1)\longleftrightarrow(-1,1).
$$

The algebra is the split-complex algebra $F[j]/(j^2-1)$ under the identification $j=(1,-1)$; the two nontrivial roots $\pm j$ correspond to the two idempotents $(1\pm j)/2$.

**Example (matrix algebras).** For $n\geq2$, $M_n(F)$ is split: the matrix units $E_{11}$ and $E_{22}$ are nontrivial idempotents, and the rank-one idempotents are the primitive ones. The roots of the identity are the involutions, and the halving pairs an idempotent of rank $r$ with the involution whose $+1$-eigenspace has dimension $r$. For $n=1$ the algebra is the field $F$, a division algebra, and it is not split.

**Example (the split-complex algebra).** $A=F[j]/(j^2-1)$ has the idempotents $e_\pm=(1\pm j)/2$ and the roots $\pm1,\pm j$. The two nontrivial roots $\pm j$ correspond to $e_\pm$; the algebra is isomorphic to $F\times F$ when $2\neq0$, and the isomorphism sends $e_+$ to $(1,0)$ and $e_-$ to $(0,1)$. In characteristic two, $j^2-1=(j-1)^2$, the algebra is the dual numbers $F[\varepsilon]/(\varepsilon^2)$ with $\varepsilon=j-1$, and it is not split: its only idempotents are $0,1$.

**Example (the group algebra of the cyclic group of order two).** Let $A=F[C_2]$ with $C_2=\{1,g\}$, $g^2=1$. If $2\neq0$, the elements $e_\pm=(1\pm g)/2$ are idempotents and $A\cong F\times F$; the roots are $\pm1,\pm g$, and the nontrivial ones correspond to $e_\pm$. If $2=0$, $A\cong F[\varepsilon]/(\varepsilon^2)$ with $\varepsilon=g-1$, and $A$ is not split.

**Example (the upper triangular algebra).** $T_2(F)$ is split for every field: $E_{11}$ and $E_{22}$ are nontrivial idempotents. When $2\neq0$, the roots of the identity include $\operatorname{diag}(1,-1)$ and $\operatorname{diag}(-1,1)$; in characteristic two the roots are the unipotent triangular matrices with $N^2=0$. The algebra is not semisimple, but it is split in the sense of the definition. This shows that split is not the same as semisimple.

**Example (the dual numbers).** $F[\varepsilon]/(\varepsilon^2)$ is not split when $2\neq0$: it has no nontrivial idempotent and no root other than $\pm1$. It is also not a division algebra. It is the standard example of an algebra that is neither division nor split, and it shows that the dichotomy of §*The Semisimple Dichotomy* is a semisimple phenomenon.

**Example (the quaternions).** $\mathbb{H}$ is a division algebra, so it is not split; its roots of $x^2=1$ are $\pm1$, while its roots of $x^2=-1$ are the unit imaginary quaternions. The example separates the two equations and shows that a division algebra can have many square roots of $-1$ while having no nontrivial idempotent.

### Split versus split semisimple

The word **split** has a second, stronger meaning in the theory of algebras: a finite-dimensional algebra is **split semisimple** when it is isomorphic to a product $\prod_i M_{n_i}(F)$ of matrix algebras over the base field. A split semisimple algebra is semisimple, and every division algebra in its Wedderburn–Artin decomposition is the base field.

**Proposition.** Let $A$ be a finite-dimensional semisimple algebra.

**(a)** If $A$ is split semisimple, then $A$ is split in the weak sense exactly when $A$ is not a single copy of $F$; that is, when it has more than one factor or a factor $M_n(F)$ with $n\geq2$.

**(b)** A central division algebra $D\neq F$ is not split semisimple and is not split in the weak sense; it becomes a matrix algebra after a splitting field extension, but the extension, not the algebra, carries the idempotents.

*Proof.* (a) A factor $M_n(F)$ with $n\geq2$ has $E_{11}$, and a product of two or more factors has the central idempotents; the single factor $M_1(F)=F$ has none. (b) A division algebra has no nontrivial idempotent by §*Division Algebras*; for a central division algebra the splitting field extension $L/F$ with $D\otimes_F L\cong M_n(L)$ produces idempotents in the scalar extension, not in $D$.

**Remark.** The two senses of split are therefore different. The weak sense is a property of the algebra over the base field: it has an idempotent. The strong sense is a property of the semisimple algebra and its division algebra factors: all the factors are matrix algebras over the base field. A central division algebra $D\neq F$ is neither weakly split nor split semisimple, but it is split by a field extension; the phrase "split by $L$" refers to the extension and not to an idempotent of $D$.

## Characteristic Two

In characteristic two the halving correspondence collapses: $2=0$, so the formula $e=(1+u)/2$ is undefined, and $u=2e-1=-1$ for every idempotent. The roots of the identity and the idempotents separate, and neither determines the other.

### The roots

**Proposition.** Let $2=0$ in $F$.

**(a)** If $u^2=1$, then $(u-1)^2=0$; the root $u$ is a unipotent element $1+n$ with $n^2=0$.

**(b)** In a reduced algebra, the only root of the identity is $1$.

**(c)** In a division algebra, the only root of the identity is $1$.

*Proof.* (a) $u^2-1=(u-1)^2$ in characteristic two. (b) A reduced algebra has no nonzero nilpotent, so $n=0$. (c) A division algebra has no nonzero nilpotent, or directly $(u-1)^2=0$ gives $u=1$.

**Example (the dual numbers in characteristic two).** Let $A=F[\varepsilon]/(\varepsilon^2)$ with $2=0$. Every element $1+b\varepsilon$ is a root of the identity, since $(1+b\varepsilon)^2=1+2b\varepsilon+b^2\varepsilon^2=1$. The idempotents, however, are only $0$ and $1$: an idempotent $a+b\varepsilon$ satisfies $a^2=a$ and $2ab=0$, the second equation being automatic; if $a=0$ then $b=0$, and if $a=1$ then $b=0$. So the roots form the additive group $F$ under $1+b\varepsilon$, while the idempotents are the two trivial ones. The halving has no inverse and no meaning.

**Example (the split algebra in characteristic two).** Let $A=F\times F$ with $2=0$. The idempotents are $(1,0)$ and $(0,1)$, but the roots of the identity are only $(1,1)$: a root $(a,b)$ satisfies $a^2=1$ and $b^2=1$, and in characteristic two the only solution is $a=b=1$. So the algebra is split and has no nontrivial root. The example is the exact opposite of the dual numbers, where the roots are plentiful and the idempotents are not.

### The table

| Algebra (characteristic two) | Nontrivial idempotents | Nontrivial roots of $x^2=1$ |
|---|---|---|
| $F\times F$ | yes, $(1,0),(0,1)$ | no, only $(1,1)$ |
| $F[\varepsilon]/(\varepsilon^2)$ | no, only $0,1$ | yes, $1+b\varepsilon$ for $b\neq0$ |
| a reduced algebra | may have | no, only $1$ |
| a division algebra | no | no, only $1$ |

The table is the characteristic-two form of the separation: the halving correspondence is a characteristic-not-two theorem, and in characteristic two the two notions must be studied separately.

## Summary

A **root of the identity** is a solution of $u^2=1$. In a division algebra the roots are $\pm1$ when $2\neq0$ and $1$ when $2=0$, and there is no nontrivial idempotent. In a matrix algebra over a field of characteristic not two, the roots are the diagonalisable involutions with eigenvalues $\pm1$, and the idempotents are the diagonalisable projections with eigenvalues $0,1$. When $2$ is invertible, the **halving correspondence** $e\mapsto2e-1$, $u\mapsto(1+u)/2$ is a bijection between idempotents and roots; it sends the complement $1-e$ to $-u$, reads $u$ as the reflection with $+1$-eigenspace the image of $e$ and $-1$-eigenspace the image of $1-e$, and is a Boolean group isomorphism $e\mapsto1-2e$ on a commutative algebra but only a bijection in general. An algebra is **split** in the weak sense of the article when it has a nontrivial idempotent, equivalently when it has a nontrivial root of the identity if $2$ is invertible; $F\times F$, $M_n(F)$ for $n\geq2$, the split-complex algebra, the group algebra $F[C_2]$ and the upper triangular algebra are split, while a division algebra and the dual numbers are not. The dual numbers are neither division nor split, so the division/split dichotomy is a semisimple phenomenon; in the semisimple case a finite-dimensional algebra is division exactly when it has no nontrivial idempotent, and split exactly when it is not division. In characteristic two the halving collapses, the roots of $x^2=1$ are the unipotent elements $1+n$ with $n^2=0$, and the roots and the idempotents separate: $F\times F$ has idempotents and only the trivial root, while the dual numbers have many roots and only the trivial idempotents. The article uses no form, norm or topology.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R(A)$ | the roots of the identity, $\{u:u^2=1\}$ |
| $e,f$ | idempotent and its complement $f=1-e$ |
| $u=2e-1$ | the root of the identity attached to $e$ |
| $e=(1+u)/2$ | the idempotent attached to $u$ |
| $e\oplus f=e+f-2ef$ | the symmetric difference of commuting idempotents |
| split | has a nontrivial idempotent |
| split semisimple | isomorphic to a product of matrix algebras over the base field |
| division | every nonzero element is invertible |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for idempotents, Peirce decompositions and the matrix examples.
- Nathan Jacobson, *Basic Algebra II* (Freeman, 1989), for the halving of an idempotent, the roots of the identity and the Wedderburn–Artin theory.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for the division, semisimple and local cases and the dual-numbers warning.
- John Voight, *Quaternion Algebras* (Springer, 2021), for the division algebras, their splitting fields and the contrast between the roots of $+1$ and the roots of $-1$.
