
# __The Endomorphism Algebra of a Module__

## Introduction

The endomorphisms of a module form a ring, and because the base ring acts centrally the ring is an algebra. This article studies that algebra in its own right: its structure when the module is free or semisimple, and its **centre**, the commutative part of the ring of operators.

The article assumes the identifications of *Left and Right Multiplication of a Module* and *Module Endomorphisms* — the endomorphism ring as the commutant of the action, its units, and the density theorem — and it assumes the matrix and division-ring vocabulary of *Modules over an Algebra* and *Automorphisms of Modules over an Algebra*. It adds the algebra structure and the centre. It stays inside Part I: no distance, norm, form or limit occurs. Throughout, $R$ is a commutative ring with $1 \neq 0$, $A$ is a unital associative $R$-algebra, $M$ is a left $A$-module, $E=\operatorname{End}_A(M)$, and $Z(E)$ is its centre.

## The Algebra Structure

### The endomorphism algebra

The endomorphism ring is an $R$-algebra, and this is the object of the article.

**Proposition.** With $E=\operatorname{End}_A(M)$, the multiplication by $r \in R$ given by $(rf)(m)=r f(m)$ turns $E$ into a unital associative $R$-algebra, and the inclusion $E \subseteq \operatorname{End}_R(M)$ is a homomorphism of $R$-algebras.

*Proof.* The map $rf$ is $A$-linear because $r$ acts centrally, so $E$ is closed under the $R$-action; the algebra axioms are inherited from $\operatorname{End}_R(M)$, and the inclusion preserves the product, the unit and the scalars. $\square$

The word *algebra* rather than *ring* records that the base ring acts; when $R=F$ is a field and $M$ is finite-dimensional over $F$, the endomorphism algebra is finite-dimensional over $F$, and its dimension is at most $(\dim_F M)^2$.

### The algebra of a free module

For a free module the endomorphism algebra is a matrix algebra, and the matrix is read in the standard basis.

**Theorem.** For $n \geq 1$ there is an isomorphism of $R$-algebras

$$
\operatorname{End}_A({}_A A^n) \xrightarrow{\ \sim\ } M_n(A^{\mathrm{op}}),
$$

given on the row $e_i$ of the standard basis by $f(e_j)=\sum_i e_i\,a_{ij}$, so that $f(v)=vX$ for the matrix $X=(a_{ij})$, and the product on the right is the matrix product in $A^{\mathrm{op}}$.

*Proof.* An $A$-linear map is determined by its values on the basis, and $A$-linearity forces $f(a e_j)=a f(e_j)$, which is the row-vector computation $f(av)=(av)X=a(vX)$ by associativity. Thus every such $f$ is right multiplication by a unique matrix $X$ with entries in $A$. Composition is $f_X \circ f_Y(v)=(vY)X=v(YX)$, so the ring of endomorphisms is the opposite of the matrix ring $M_n(A)$ with the usual product, that is $M_n(A^{\mathrm{op}})$. The $R$-linearity is entrywise. $\square$

For $n=1$ this is the identification $\operatorname{End}_A({}_A A)\cong A^{\mathrm{op}}$ of *Automorphisms of Modules over an Algebra*, and it is the base case of the theorem.

### The algebra of an isotypic module

For a sum of copies of one simple module the endomorphism algebra is a matrix algebra over a division ring, by the density theorem.

**Proposition.** Let $S$ be a simple left $A$-module, $D=\operatorname{End}_A(S)$, and $M=S^n$ a finite direct sum. Then

$$
E \cong M_n(D)
$$

as $R$-algebras, with the entries acting on the components.

*Proof.* This is the isotypic computation of *Module Endomorphisms*: an endomorphism of $S^n$ is a matrix of maps $S \to S$, each in $D$, and composition is matrix composition. $\square$

### The general semisimple structure

The two descriptions combine into the structure theorem for the endomorphism algebra of a semisimple module of finite length.

**Theorem.** Let $M=S_1^{n_1}\oplus\cdots\oplus S_k^{n_k}$ with the $S_i$ pairwise non-isomorphic simple modules and $D_i=\operatorname{End}_A(S_i)$. Then

$$
E \cong M_{n_1}(D_1) \times \cdots \times M_{n_k}(D_k)
$$

as $R$-algebras, and $M$ is the direct sum of the natural modules $D_i^{\,n_i}$ over the factors.

*Proof.* By Schur's lemma there are no nonzero maps between non-isomorphic simple modules, so an endomorphism preserves each isotypic component $S_i^{n_i}$, and on that component it is a matrix over $D_i$ by the proposition; the product decomposition follows. $\square$

The theorem is the operator form of the semisimple structure theorem, and it exhibits $E$ as a product of matrix algebras over division rings, hence as a semisimple ring.

## The Centre

### Definition and first properties

The centre of the endomorphism algebra is the set of operators that commute with every endomorphism.

**Definition.** The **centre** of $E$ is

$$
Z(E)=\{z \in E : zf=fz \text{ for all } f \in E\}.
$$

It is a commutative subalgebra of $E$ containing the image of $R$.

**Proposition.** $Z(E)=E\cap E'$, where $E'$ is the centralizer of $E$ in $\operatorname{End}_R(M)$; consequently $Z(E)$ is a commutative $R$-algebra, and $M$ is a left $Z(E)$-module on which every element of $E$ acts $Z(E)$-linearly.

*Proof.* An element lies in the centre exactly when it belongs to $E$ and commutes with all of $E$, which is $E\cap E'$. For the module statement, $z \in Z(E)$ acts on $M$ through its action as an endomorphism, and $f(zm)=z f(m)$ because $z$ commutes with $f$. $\square$

Since $E=L_A'$ and $L_A \subseteq E'$, the centre sits between the two commutants: it is the part of the endomorphism algebra that is also in the bicommutant of the action.

### The centre of a matrix algebra

The centre of a matrix algebra is the scalars, which is the computation the two structure theorems need.

**Proposition.** For any unital ring $B$ and $n \geq 1$,

$$
Z(M_n(B)) = Z(B)\cdot I_n = \{ \lambda I_n : \lambda \in Z(B) \}.
$$

*Proof.* A matrix $C$ commutes with every matrix unit $E_{ij}$; commuting with $E_{ij}$ forces the entries of $C$ to be constant across each row and column, so $C=\lambda I_n$ for some $\lambda \in B$. Such a scalar matrix commutes with an arbitrary $X=(x_{ij})$ exactly when $\lambda x_{ij}=x_{ij}\lambda$ for all $i,j$; as the entries range over all of $B$, this says $\lambda \in Z(B)$. $\square$

### The centre of a free module's endomorphism algebra

**Corollary.** For a free module ${}_A A^n$,

$$
Z(\operatorname{End}_A(A^n)) \cong Z(A^{\mathrm{op}}) = Z(A),
$$

the scalar matrices with entries in the centre of the algebra.

*Proof.* Combine the matrix theorem with the identification $\operatorname{End}_A(A^n)\cong M_n(A^{\mathrm{op}})$ and $Z(A^{\mathrm{op}})=Z(A)$. $\square$

Thus for the regular module $E=A^{\mathrm{op}}$ and $Z(E)=Z(A)$, and enlarging the rank does not enlarge the centre: the centre of the endomorphism algebra of a free module is the centre of the algebra, whatever the rank.

### The centre of an isotypic module's endomorphism algebra

**Corollary.** With $S$ simple, $D=\operatorname{End}_A(S)$ and $M=S^n$,

$$
Z(E) \cong Z(D),
$$

the set of central endomorphisms of the simple module.

*Proof.* $E\cong M_n(D)$ and the matrix theorem gives $Z(M_n(D))=Z(D)\cdot I_n$. $\square$

In the semisimple case the centre is therefore $\prod_i Z(D_i)$, a product of fields when the $D_i$ are division rings finite-dimensional over a field, and the centre is a field exactly when there is a single isotypic component with $Z(D)$ a field.

### The centre as the algebra of $A$-linear scalars

The centre has an intrinsic description that does not mention matrices.

**Proposition.** $Z(E)$ is exactly the subalgebra of $E$ consisting of the maps $z$ such that $z$ is $A$-linear and commutes with every $A$-linear map; equivalently $z \in E'$, the centralizer of $E$ inside $\operatorname{End}_R(M)$ that happens to lie in $E$.

*Proof.* Restatement of $Z(E)=E\cap E'$. $\square$

The description shows that the centre is the largest subalgebra of $\operatorname{End}_R(M)$ that is centralised by the whole endomorphism algebra; it is the algebra of scalars that the module's own symmetry forces.

## Commutative Endomorphism Algebras

### When the endomorphism algebra is commutative

The endomorphism algebra is commutative exactly when all its operators commute, and the structure theorem makes this a condition on the decomposition.

**Proposition.** Let $M$ be semisimple of finite length, $M=S_1^{n_1}\oplus\cdots\oplus S_k^{n_k}$. Then $E$ is commutative if and only if $n_i=1$ for all $i$ and each $D_i$ is a field.

*Proof.* $E\cong\prod_i M_{n_i}(D_i)$ is commutative exactly when each factor is: $M_{n_i}(D_i)$ is commutative only for $n_i=1$ with $D_i$ commutative, and for $n_i=1$ it is $D_i$, commutative when it is a field. $\square$

In the commutative case $E$ is a product of fields, so every endomorphism is a scalar on each isotypic component, and the module is multiplicity-free.

### The division-ring case

**Proposition.** If $M$ is simple then $E=\operatorname{End}_A(M)$ is a division ring and $Z(E)$ is a field.

*Proof.* Schur's lemma gives the division ring, and the centre of a division ring is a field. $\square$

## Examples

**(a) The regular module over a commutative algebra.** For $A$ commutative and $M=A$, $E=A^{\mathrm{op}}=A$ and $Z(E)=Z(A)=A$: every endomorphism is a scalar and the endomorphism algebra is the algebra itself.

**(b) A matrix algebra on its defining module.** For $A=M_n(F)$ and $M=F^n$ simple, $D=\operatorname{End}_A(F^n)=F$, so $E=F$ and $Z(E)=F$; the endomorphism algebra is one-dimensional and equal to its centre.

**(c) A matrix algebra on itself.** For $A=M_n(F)$ and $M=A$, $E=M_n(F)^{\mathrm{op}}$, and $Z(E)=F\cdot I$: the centre is the scalars, one-dimensional, and the endomorphism algebra is not commutative for $n \geq 2$.

**(d) A free module of higher rank.** For $M=A^n$ with $A$ a field $F$, $E=M_n(F)$ and $Z(E)=F$, whatever $n$ is.

**(e) The quaternions.** For $A=\mathbb{H}$ and $M=\mathbb{H}$, $E\cong\mathbb{H}^{\mathrm{op}}\cong\mathbb{H}$ and $Z(E)=\mathbb{R}$, the real scalars; the endomorphism algebra is a division ring and its centre is the base field.

**(f) A semisimple module with two components.** For $A=F$ a field and $M=F\oplus F$, $E\cong M_2(F)$, with centre $F$; for two non-isomorphic simple modules, $A=M_n(F)\times M_m(F)$ and $M=F^n\oplus F^m$, $E\cong F\times F$ is commutative and equal to its centre.

## Summary

The endomorphism ring $E=\operatorname{End}_A(M)$ of a left $A$-module is a unital $R$-algebra, and it is the subject here together with its centre. For a free module, $E\cong M_n(A^{\mathrm{op}})$, the matrices over the opposite algebra, so for the regular module $E\cong A^{\mathrm{op}}$; for a finite isotypic module $S^n$ over a simple $S$, $E\cong M_n(D)$ with $D=\operatorname{End}_A(S)$ a division ring; and for a semisimple module of finite length $M=S_1^{n_1}\oplus\cdots\oplus S_k^{n_k}$, $E\cong\prod_i M_{n_i}(D_i)$. The centre of a matrix algebra is the scalar matrices with entries in the centre of the coefficient ring, so the centre of the endomorphism algebra of a free module of any rank is $Z(A)$, that of an isotypic module is $Z(D)$, and in the semisimple case it is $\prod_i Z(D_i)$. The centre is $E\cap E'$, the operators that are $A$-linear and commute with every $A$-linear operator, and $M$ is a module over it on which $E$ acts by $Z(E)$-linear maps. The endomorphism algebra is commutative exactly when the module is multiplicity-free with commutative division-ring endomorphisms, and it is a division ring exactly when the module is simple.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | commutative ring with identity, the base ring |
| $A$ | unital associative $R$-algebra, generally noncommutative |
| $M$ | left $A$-module |
| $S$, $S_i$ | simple left $A$-modules |
| $E=\operatorname{End}_A(M)$ | the endomorphism algebra of $M$ |
| $Z(E)$ | the centre of $E$ |
| $E'$ | the centralizer of $E$ in $\operatorname{End}_R(M)$ |
| $A^{\mathrm{op}}$ | opposite algebra, product $a \cdot_{\mathrm{op}} b = ba$ |
| $M_n(A^{\mathrm{op}})$ | matrices over the opposite algebra, $=\operatorname{End}_A(A^n)$ |
| $D=\operatorname{End}_A(S)$ | the division ring of a simple module |
| $M_n(D)$ | matrix ring over $D$, $=\operatorname{End}_A(S^n)$ |
| $Z(A)$, $Z(D)$ | the centres of $A$ and of $D$ |
| $n_i$ | the multiplicity of $S_i$ in $M$ |

## Further Reading

- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, second edition, 1992), for the endomorphism ring of a free module and the structure of endomorphism rings of semisimple modules.
- Nicolas Bourbaki, *Algebra I* (Springer, 1989), for the centre of a matrix ring and the double centralizer theorem.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for linear algebra over a division ring and the endomorphism algebra of a free module.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, second edition, 2001), for the Wedderburn–Artin structure theorem of which the product decomposition is the module-level form.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for matrix algebras, their centres and the endomorphism algebras of finite-dimensional modules.
