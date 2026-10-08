# __The Ternary Product as an Operator__

## Introduction

A sesqualgebra carries its identities at the ternary level. The associator of the binary product is a defect with no identity attached to it, and the ternary product $\{x,y,z\}=xy^{*}z$ is the operation that carries the Jordan triple identity, as *The Sesquilinear Associator and the Ternary Product* and *Algebraic J\*-Algebras* record. The present article reads that ternary product as an **operator**. For a pair $(x,y)$ the third slot is the variable, and

$$
\Theta_{x,y}(z)=\{x,y,z\}=xy^{*}z
$$

is a linear operator on $A$. The article computes the parities of the pair-dependence, shows that the operator is a familiar one-sided operator in each of the three slots of the ternary product, and identifies the family that the pairs generate. Over a unital sesqualgebra the third-slot operators are the plain left multiplications, so that slot carries no new operator and what the ternary product adds is the reading of the same operation in its other two slots. The companion operator of the Lie layer, the inner derivation $z\mapsto[[x,y],z]$, is treated in the same breath, because it is the other ternary operation of the sesquilinear kind, and the contrast is the point of the article: the family of the Jordan layer consists of one-sided operators, the family of the Lie layer of derivations, and the two families are the operator forms of the two ternary products of the sesquilinear kind, the Jordan triple of *The Sesquilinear Associator and the Ternary Product* and the Lie triple of *Lie Algebras of Sesqualgebras*.

**The boundaries.** The ternary product itself, its parities, its Hermitian symmetry and its Jordan triple identity are *The Sesquilinear Associator and the Ternary Product* and *Algebraic J\*-Algebras*; the Lie triple system of the commutator is *Lie Algebras of Sesqualgebras*, and its identities are used here and not proved. The one-sided operators $L_a$ and $R_a$ and the plain two-sided operator $T_{p,q}$ are *The Left and Right Multiplication Operators of a Sesqualgebra*, the sandwich $S_{a,b}$ is *The Sesquilinear Sandwich Operator*, and the adjoint of the operator of this article is *The Adjoint of the Ternary Product*, the later entry of the group. This article stays inside Part I: no distance, no limit, no completeness.

Throughout, $R$ is a commutative ring with $1$, $\varsigma$ is an involution of $R$, and $A$ is a unital associative $R$-algebra with a $\varsigma$-semilinear involution $*$, so that $A$ is a sesqualgebra in the sense of *Sesqualgebras*; the unit satisfies $1^{*}=1$. The derived operation is $x\star y=xy^{*}$ and its ternary companion is $\{x,y,z\}=(x\star y)\star z^{*}=xy^{*}z$. The one-sided operators are $L_a(x)=a\star x=ax^{*}$ and $R_b(x)=x\star b=xb^{*}$, the plain two-sided operator is $T_{p,q}(x)=pxq$, so that $T_{a,1}$ is the plain left multiplication and $T_{1,b}$ the plain right multiplication, and the sandwich is $S_{a,b}(x)=ax^{*}b$. A derived product written $x\star y$ is read on the pair $A\times A^{\varsigma}$ of *The Sesquilinear Product*, whose second entry is the conjugate module.

## The Operator Attached to a Pair

### Definition and Parities

**Definition.** For $x,y\in A$ let

$$
\Theta_{x,y}:A\longrightarrow A,\qquad \Theta_{x,y}(z)=xy^{*}z .
$$

The operator is called the **ternary operator** of the pair $(x,y)$, and the assignment $(x,y)\mapsto \Theta_{x,y}$ the pair map of the ternary product.

**Proposition (parities).** The operator $\Theta_{x,y}$ is $R$-linear, and the pair map is $R$-bilinear with a $\varsigma$-semilinear second slot:

$$
\Theta_{\lambda x,y}=\lambda\,\Theta_{x,y}, \qquad \Theta_{x,\lambda y}=\varsigma(\lambda)\,\Theta_{x,y}, \qquad \lambda\in R .
$$

**Proof.** The variable $z$ enters through the plain product on the right, so $\Theta_{x,y}(\lambda z+\mu w)=\lambda \Theta_{x,y}(z)+\mu \Theta_{x,y}(w)$ and $\Theta_{x,y}\in\operatorname{End}_R(A)$. In the first parameter, $(\lambda x)y^{*}z=\lambda(xy^{*}z)$; in the second, $x(\lambda y)^{*}z=x\,\varsigma(\lambda)y^{*}z=\varsigma(\lambda)xy^{*}z$ by the scalar rule of the involution. $\square$

**Remark.** The parities are those of the ternary product, read with one slot promoted to a parameter: the ternary product is $R$-linear in its first and its third slot and $\varsigma$-semilinear in its middle slot, as *The Sesquilinear Associator and the Ternary Product* records. The parameter $x$ is therefore linear, the parameter $y$ is conjugate-linear and the variable $z$ is linear, and the pair map is the only place where the conjugate-linearity of the middle slot survives.

**Remark.** Writing the pair map as a map $A\times A^{\varsigma}\to\operatorname{End}_R(A)$ makes it $R$-bilinear, exactly as it makes the product $A\times A^{\varsigma}\to A$ bilinear; the conjugate module of *The Sesquilinear Product* is the bookkeeping that removes the asymmetry of the parities, and the second parameter is the one that meets the involution.

### The Three Readings

The ternary product has three slots and the variable may be put in any of them. Each reading is an operator of the earlier entries of the group.

**Theorem (the three readings).** For all $x,y,z\in A$,

$$
\Theta_{x,y}(z)=T_{x\star y,\,1}(z)=S_{x,z}(y)=T_{1,\,y^{*}z}(x).
$$

**Proof.** The first identity is $xy^{*}z=(x\star y)z$, the product being read as the plain left multiplication by the derived product $x\star y$; the second is $xy^{*}z=S_{x,z}(y)$ by the definition of the sandwich; the third is $xy^{*}z=x(y^{*}z)=T_{1,\,y^{*}z}(x)$, the product read as the plain right multiplication by the element $y^{*}z$. $\square$

**Remark.** The third slot gives a plain left multiplication, the first slot a plain right multiplication, and the middle slot a sandwich. The middle reading is the only one that is not $R$-linear in the parameters, because the sandwich is $\varsigma$-semilinear in its own parameter, and that is the same statement as the $\varsigma$-semilinearity of the pair map in its second slot. The three readings are three operators of the earlier entries of the group, and the content of the theorem is that the ternary product introduces no operator that those entries had not already named.

**Corollary (the middle reading is the sandwich).** With $x$ and $z$ fixed, the map $y\mapsto x y^{*} z$ is the sandwich operator $S_{x,z}$, hence $\varsigma$-semilinear and of the parity of the sandwich; the ternary operator of the pair and the sandwich are therefore related by the exchange of the last two slots, $\Theta_{x,y}(z)=S_{x,z}(y)$.

## The Operators the Pairs Generate

### The Factorisation through the Derived Product

**Theorem (the pair enters through the derived product).** For all $x,y\in A$,

$$
\Theta_{x,y}=T_{x\star y,\,1}.
$$

Consequently $\Theta_{x,y}=0$ if and only if $x\star y=0$, and $\Theta_{x,y}=\Theta_{u,v}$ if and only if $x\star y=u\star v$; the pair $(x,y)$ is seen by the operator only through the derived product.

**Proof.** The identity is the first reading above. For the kernels, $T_{a,1}$ is the plain left multiplication by $a$, and over a unital $A$ the left multiplication by $a$ vanishes identically only for $a=0$, since $T_{a,1}(1)=a$; the same evaluation at the unit gives $T_{a,1}=T_{c,1}$ only for $a=c$. $\square$

**Corollary (no loss of information).** Over a unital sesqualgebra the map $a\mapsto T_{a,1}$ is an isomorphism of $R$-algebras from $A$ onto the family of the third-slot operators, because $T_{a,1}T_{c,1}=T_{ac,1}$ and $T_{1,1}=\mathrm{id}_A$. In particular $x\star 1=x$ for every $x$, so the derived products already fill $A$ and the third-slot family is the whole left regular family.

**Proof.** The composition law is $T_{a,1}\bigl(T_{c,1}(z)\bigr)=a(cz)=(ac)z=T_{ac,1}(z)$; the unit is $T_{1,1}(z)=z$; the kernel is trivial by the evaluation at $1$ above. The identity $x\star 1=x1^{*}=x$ uses $1^{*}=1$ and the unit of the algebra. $\square$

**Remark.** The theorem is the reason the ternary operator of the third slot is invisible: it is a plain one-sided operator, and over a unital sesqualgebra the pairs generate the whole left regular family. What the reading does carry is the parity: the map $(x,y)\mapsto \Theta_{x,y}$ is $R$-bilinear on $A\times A^{\varsigma}$ and not on $A\times A$, so the derived product is visible in the pair map and not in the operators it produces.

### The Bracket and the Lie Triple System

**Theorem (the operators under the commutator).** For all $x,y,u,v,p,q\in A$,

$$
[\Theta_{x,y},\Theta_{u,v}]=T_{[x\star y,\,u\star v],\,1},
$$

the bracket being the commutator of the endomorphism algebra $\operatorname{End}_R(A)$. Consequently the $R$-span of the operators $\Theta_{x,y}$ is a Lie subalgebra of $\operatorname{End}_R(A)$ isomorphic to $A$ under the commutator, and it is closed under the triple commutator

$$
[[\Theta_{x,y},\Theta_{u,v}],\Theta_{p,q}]=T_{[[x\star y,\,u\star v],\,p\star q],\,1}.
$$

**Proof.** By the factorisation, $\Theta_{x,y}=T_{a,1}$ with $a=x\star y$ and $\Theta_{u,v}=T_{c,1}$ with $c=u\star v$; then $T_{a,1}T_{c,1}=T_{ac,1}$ by the corollary, so the commutator is $T_{ac-ca,1}$; the second identity is the first applied twice. $\square$

**Remark.** The triple commutator is the operation of the Lie triple system of *Lie Algebras of Sesqualgebras*, read with the Lie algebra of the operators as its Lie algebra. The triple system is therefore present twice in the sesquilinear kind: once on the elements, where it is $\{x,y,z\}_{\mathrm{L}}=[[x,y],z]$, and once on the operators of this article, where it is the triple commutator of the one-sided operators produced by the derived products.

## The Lie Companion

### The Inner Derivation of a Pair

The Lie layer of the sesquilinear kind carries the operator attached to the pair $(x,y)$ as well, but it is attached through the commutator and not through the product.

**Definition.** For $x,y\in A$ let

$$
\mathrm{ad}_{[x,y]}:A\longrightarrow A,\qquad \mathrm{ad}_{[x,y]}(z)=[[x,y],z],
$$

the plain commutator being read in the associative algebra $A$.

**Proposition (the Lie companion is an inner derivation).** For all $x,y\in A$,

$$
\mathrm{ad}_{[x,y]}=T_{[x,y],\,1}-T_{1,\,[x,y]},
$$

the operator $z\mapsto[[x,y],z]$; it is a derivation of $A$, it is the difference of a plain left multiplication and a plain right multiplication, and it is a one-sided operator only when $[x,y]$ is central, in which case it vanishes.

**Proof.** The commutator $[a,z]=az-za$ is the difference of the left and the right multiplication by $a$, so it is a derivation by the Leibniz rule; the two one-sided operators are those of the present notation. A difference $T_{a,1}-T_{1,a}$ equals one of its two terms only when the other vanishes, and evaluating at the unit forces the operator to be $0$; so the companion is one-sided only when it vanishes, that is when $[x,y]$ is central. $\square$

**Theorem (the family of the Lie layer).** For all $x,y,u,v,p,q\in A$,

$$
[\mathrm{ad}_{[x,y]},\mathrm{ad}_{[u,v]}]=\mathrm{ad}_{[[x,y],[u,v]]}, \qquad
\mathrm{ad}_{[x,y]}\bigl(\mathrm{ad}_{[u,v]}(z)\bigr)-\mathrm{ad}_{[u,v]}\bigl(\mathrm{ad}_{[x,y]}(z)\bigr)=\mathrm{ad}_{[[x,y],[u,v]]}(z),
$$

and the $R$-span of the operators $\mathrm{ad}_{[x,y]}$ is the image of the commutator subalgebra $[A,A]$ under the adjoint map, a Lie subalgebra of the derivations of $A$ isomorphic to the quotient $[A,A]/\bigl([A,A]\cap Z(A)\bigr)$.

**Proof.** The identity $[\mathrm{ad}_a,\mathrm{ad}_b]=\mathrm{ad}_{[a,b]}$ is the Jacobi identity, in the form $\mathrm{ad}_a\mathrm{ad}_b-\mathrm{ad}_b\mathrm{ad}_a=\mathrm{ad}_{[a,b]}$; the second display is that identity applied to $z$. The image of the adjoint map is a Lie subalgebra because the adjoint map is a Lie homomorphism, and its kernel on the commutator subalgebra is $[A,A]\cap Z(A)$, by the definition of the centre. $\square$

**Remark.** The adjoint map has kernel the centre on $A$, so the family is the inner derivations of the commutator Lie algebra, isomorphic to $[A,A]$ modulo its central part $[A,A]\cap Z(A)$; the definitions are those of *The Commutator Operator* and *Lie Algebras of Sesqualgebras*. The family of the Lie layer is therefore the image of the commutator subalgebra, and it is a Lie algebra and not only a set of operators.

### The Two Operators of a Pair

The two families answer the same question, the pair acting on the algebra, and they differ in what the action is made of.

| | the Jordan layer $\Theta_{x,y}$ | the Lie layer $\mathrm{ad}_{[x,y]}$ |
|---|---|---|
| definition | $z\mapsto xy^{*}z=\{x,y,z\}$ | $z\mapsto[[x,y],z]$ |
| what it reads | the derived product $x\star y$ | the commutator $[x,y]$ |
| its kind | a plain left multiplication by $x\star y$ | an inner derivation |
| the family | the left regular family, isomorphic to $A$ | the image of $[A,A]$ under $\mathrm{ad}$, isomorphic to $[A,A]/([A,A]\cap Z(A))$ |
| the parities of the pair | $R$-bilinear on $A\times A^{\varsigma}$ | $R$-bilinear on $A\times A$ |
| the triple system | the triple commutator of the one-sided operators | the Lie triple system of $\mathrm{ad}$ |

**Remark.** The table is the comparison the article was for. The Jordan operator is a one-sided operator, and the pairs produce the left regular family; the Lie operator is a derivation, and the pairs produce the inner derivations. The two families are the operator forms of the two triple systems of the sesquilinear kind, and the difference of parities in the pair is the visible trace of the involution in the Jordan layer, where the Lie layer has no involution at all.

## The Quadratic Representation

The ternary operator of the pair $(x,x)$ is the quadratic object of the Jordan theory when the sesquilinear kind degenerates to the bilinear one.

**Theorem (the quadratic representation).** Let $A$ be commutative and let $\varsigma=\mathrm{id}$ and $*=\mathrm{id}$, so that the derived operation is the product. Then

$$
\Theta_{x,x}(z)=x^{2}z=U_x(z), \qquad \{x,z,x\}=xzx=U_x(z),
$$

where $U_x$ is the quadratic representation of the Jordan algebra of the product; equivalently

$$
U_x=2T_{x,1}^{2}-T_{x^{2},1},
$$

the operator $T_{x,1}$ being the plain left multiplication, $T_{x,1}(z)=xz$.

**Proof.** With $*=\mathrm{id}$ the ternary product is $xy^{*}z=xyz$ and the commutativity gives $xyz=x^{2}z$ for $y=x$; the middle slot gives $xzx=x^{2}z$. The identity $U_x=2T_{x,1}^{2}-T_{x^{2},1}$ is the classical form of the quadratic representation in a commutative associative algebra, read on $z$: $2x(xz)-x^{2}z=x^{2}z$. $\square$

**Remark.** The quadratic representation is therefore the diagonal of the pair map, the case $x=y$ of the ternary operator, and the two readings of the theorem are the two slots in which the quadratic variable may sit. In the sesquilinear case the diagonal $\Theta_{x,x}$ is the plain left multiplication by $x\star x=xx^{*}$, the square of the element in the derived sense, and it is the operator $z\mapsto xx^{*}z$ and not the classical $z\mapsto xzx$; the difference is the involution, and it is what the degenerate case recovers.

## Worked Cases

### The Complex Matrices

Let $A=M_n(\mathbb{C})$ with the conjugate transpose and $\varsigma$ the conjugation, the standard example of *Sesqualgebras*. The derived products $x\star y=xy^{*}$ fill $M_n(\mathbb{C})$, since $x\star 1=x$; so the third-slot operators $\Theta_{x,y}=T_{x\star y,1}$ are all the plain left multiplications, and the family is the left regular family isomorphic to $M_n(\mathbb{C})$. The middle reading gives the sandwiches $S_{x,z}$ for all pairs, the family of *The Sesquilinear Sandwich Operator*, and the first reading gives the plain right multiplications. The Lie companion gives the inner derivations $\mathrm{ad}_{[x,y]}$; the commutator subalgebra is $[A,A]=\mathfrak{sl}_n$, the traceless matrices, the adjoint map is injective on it, and the family is $\mathrm{ad}(\mathfrak{sl}_n)\cong\mathfrak{sl}_n$, while the adjoint map on the whole algebra has kernel the scalars $\mathbb{C}1$.

### The Biquaternion Algebra

Let $A=\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with the conjugation of *Biquaternions as a General Plain Sesqualgebra (GPS) over $\mathbb{C}$*, namely the quaternionic conjugation of the basis with conjugated complex coefficients, so that $\varsigma$ is the conjugation, $*$ is an anti-automorphism and $1^{*}=1$; the algebra is a unital sesqualgebra in the sense of this article. The derived products fill $\mathbb{B}$, since $x\star 1=x$; so the third-slot operators are all the plain left multiplications and the family is the left regular family; the middle reading is the family of the sandwiches; and the Lie companion is the image of the commutator subalgebra under the adjoint map, the inner derivations of $\mathbb{B}$, the adjoint map being injective on that subalgebra; the adjoint map on the whole algebra has kernel the centre $\mathbb{C}\cdot1$. The biquaternion algebra is the $2\times2$ complex matrix algebra, by *Biquaternion $2\times2$ Matrix Element Representation*, and its centre is $\mathbb{C}\cdot1$ there; so the operators of this worked case are those of the previous one under the isomorphism, and the two examples carry the same operator shape and differ only in the involution that names the sesquilinear structure.

## Summary

The ternary product of a sesqualgebra is an operator attached to a pair, $\Theta_{x,y}(z)=\{x,y,z\}=xy^{*}z$, linear in its argument, linear in the first parameter and $\varsigma$-semilinear in the second, so that the pair map is $R$-bilinear on $A\times A^{\varsigma}$. Read in its third slot it is the plain left multiplication by the derived product, $\Theta_{x,y}=T_{x\star y,1}$; read in its middle slot it is the sandwich $S_{x,z}$; read in its first slot it is the plain right multiplication by $y^{*}z$. The pair is visible in the operator only through the derived product, and over a unital sesqualgebra the pairs produce the whole left regular family, an algebra isomorphic to $A$, so the third slot carries no new operator. The operators are closed under the commutator, where $[\Theta_{x,y},\Theta_{u,v}]=T_{[x\star y,u\star v],1}$, hence under the triple commutator, and they are the operator form of the Lie triple system of *Lie Algebras of Sesqualgebras*. The companion of the Lie layer, $\mathrm{ad}_{[x,y]}(z)=[[x,y],z]$, is an inner derivation, the difference of a plain left and a plain right multiplication, and the pairs produce the image of the commutator subalgebra under the adjoint map, isomorphic to $[A,A]/([A,A]\cap Z(A))$. The contrast is the content of the article: the Jordan layer produces one-sided operators and the Lie layer produces derivations, and the involution is visible in the pair of the first family and absent from the second. In the commutative degenerate case the diagonal $\Theta_{x,x}$ is the quadratic representation $U_x=2P_x^{2}-P_{x^{2}}$, and the classical form $z\mapsto xzx$ is the middle-slot reading of the same operator.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Theta_{x,y}(z)=xy^{*}z$ | the ternary operator of the pair $(x,y)$, the third slot the variable |
| $\Theta_{x,y}=T_{x\star y,1}$ | the factorisation of the ternary operator through the derived product |
| $S_{x,z}(y)=xy^{*}z$ | the middle-slot reading, the sandwich of the pair $(x,z)$ |
| $T_{1,\,y^{*}z}(x)$ | the first-slot reading, the plain right multiplication by $y^{*}z$ |
| $[\Theta_{x,y},\Theta_{u,v}]=T_{[x\star y,u\star v],1}$ | the operators under the commutator |
| $\mathrm{ad}_{[x,y]}(z)=[[x,y],z]$ | the Lie companion of the pair, the inner derivation of the pair |
| $\mathrm{ad}_{[x,y]}=T_{[x,y],1}-T_{1,[x,y]}$ | the Lie companion as a difference of one-sided operators |
| $U_x=2T_{x,1}^{2}-T_{x^{2},1}=\Theta_{x,x}$ | the quadratic representation in the commutative degenerate case |
| $\{x,y,z\}$ | the ternary product, owned by *The Sesquilinear Associator and the Ternary Product* |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the quadratic representation of a Jordan algebra as the operator attached to a pair and for the triple systems, the setting in which the diagonal of the pair map of this article is read.
- Ottmar Loos, *Jordan Pairs* (Lecture Notes in Mathematics 460, Springer, 1975), for the pair as the primary datum of a Jordan structure and for the operators attached to it, which is the reading of the present article taken as the definition.
- Harald Upmeier, *Jordan Algebras in Analysis, Operator Theory, and Quantum Mechanics* (American Mathematical Society, 1987), for the ternary product of a $J^{*}$-algebra, its quadratic representation and the operators it generates, taken here algebraically.
- Cho-Ho Chu, *Jordan Structures in Geometry and Analysis* (Cambridge University Press, 2012), for the algebra-free theory of the $J^{*}$-triple, in which the ternary product is the primary object and no binary product is at hand to serve as the operator.
