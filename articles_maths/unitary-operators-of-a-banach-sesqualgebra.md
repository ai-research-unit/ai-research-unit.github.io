# __Unitary Operators of a Banach Sesqualgebra__

## Introduction

The operators of a sesqualgebra that preserve its product form the group of the structure, and the present article is the entry of the topological layer that develops it. The menu names them the unitary operators of the Banach sesqualgebra; the article fixes the class and shows that the name is a historical one, distinct from the unitary operators of the algebraic layer, which are the operators whose adjoint is their inverse. The product-preserving operators are the bounded operators $T$ with

$$
T(x\star y)=Tx\star Ty,
$$

of one of the two parities, and the class is a group under composition once the operators are inverted, carrying the norm topology of *Bounded Operators on a Sesqualgebra*. The article proves the structure theorem that identifies them with the unital $*$-endomorphisms of the algebra, splits the group by parity, shows that it is a topological group with the norm topology, and reads its relation to the unitary group $U(A)$ of the elements through the inner $*$-automorphisms $\alpha_{u}(x)=uxu^{*}$.

Two facts organise the article. First, a bounded operator of one of the two parities preserving the derived product and fixing the unit is exactly a unital $*$-endomorphism of the algebra — multiplicativity plus the commutation with the involution — and this holds for the conjugate-linear operators as well, where the scalar action is carried through $\varsigma$; the identification is the topological form of the proposition of *The Unitary Operators of a Sesqualgebra*. Second, the invertible ones form a group $G$, closed in the group of invertible bounded operators, with the norm topology a topological group; the linear ones are a subgroup $G_{0}$ of index at most two, the conjugate-linear ones being the second coset, and the inner $*$-automorphisms of the unitary elements form a closed subgroup of $G_{0}$ under the map $u\mapsto\alpha_{u}$. The product-preserving condition and the unitary condition of the algebraic layer are independent: the left multiplication by a unitary element is antiunitary and not product-preserving, and a product-preserving operator is unitary exactly when it preserves the trace of the reduced form.

**The boundaries.** The unitary condition $T^{\dagger}=T^{-1}$, the product-preserving condition and their separation are *The Unitary Operators of a Sesqualgebra*; the unitary elements and their inner $*$-automorphisms are *Units and the Unitary Elements*; the bounded operators, the two parities and the graded algebra are *Bounded Operators on a Sesqualgebra*; the one-sided operators are *The Bounded Left and Right Multiplication Operators of a Sesqualgebra*; the adjoint and the reduction that makes it exist are *Adjoints of Bounded Sesquilinear Operators*; and the analytic structure of the group, its connectedness and its homotopy, is *The Topological J\*-Algebra* and the later spectral entries. This article stops before the spectral theory.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$ with the continuous involution $\varsigma$, and $A$ is a **normed sesqualgebra** of *Banach Sesqualgebras*: the standard example $x\star y=xy^{*}$, submultiplicative norm, isometric involution $\lVert x^{*}\rVert=\lVert x\rVert$ and $\lVert1\rVert=1$. The bounded $\mathbb{K}$-linear operators are $B(A)$ and the bounded $\varsigma$-semilinear ones $B^{\varsigma}(A)$, of *Bounded Operators on a Sesqualgebra*; the invertible elements of $A$ are $A^{\times}$ and the **unitary elements** are $U(A)=\{u:uu^{*}=u^{*}u=1\}$, of *Units and the Unitary Elements*; the inner $*$-automorphism of a unitary $u$ is $\alpha_{u}(x)=uxu^{*}$. The derived product is $x\star y=xy^{*}$ and the left multiplication is $L_{a}(x)=ax$.

## The Operators that Preserve the Product

### The Structure Theorem

**Definition.** A bounded operator $T$ of one of the two parities (so $T\in B(A)$ or $T\in B^{\varsigma}(A)$) **preserves the product** when

$$
T(x\star y)=Tx\star Ty\qquad\text{for all }x,y\in A,
$$

and is **multiplicative** when moreover $T(1)=1$.

**Theorem (the identification with the unital $*$-maps).** Let $T$ be a bounded operator of one of the two parities with $T(1)=1$. Then $T$ preserves the product if and only if $T$ is a unital $*$-endomorphism of the corresponding parity:

$$
T(xy)=Tx\,Ty,\qquad T(y^{*})=(Ty)^{*} .
$$

For a $\mathbb{K}$-linear $T$ these are the ordinary unital $*$-endomorphisms, and for a $\varsigma$-semilinear $T$ they are the $\varsigma$-semilinear ones, with $T(\lambda y)=\varsigma(\lambda)Ty$.

**Proof.** If $T$ is a unital $*$-map then $T(xy^{*})=Tx\,T(y^{*})=Tx\,(Ty)^{*}=Tx\star Ty$. Conversely the identity is $T(xy^{*})=Tx(Ty)^{*}$. At $y=1$ it reads $T(x)=Tx(T1)^{*}=Tx$, and at $x=1$ it reads $T(y^{*})=T1\,(Ty)^{*}=(Ty)^{*}$, which is the commutation with the involution; then $T(xy)=T\bigl(x(y^{*})^{*}\bigr)=Tx\,(T(y^{*}))^{*}=Tx\,Ty$, which is the multiplicativity. The parity statements are the scalar rules, which are part of the definition of the two classes. $\square$

**Remark.** The theorem is the topological form of the proposition of *The Unitary Operators of a Sesqualgebra*, §*The Operators that Preserve the Product*, and the boundedness hypothesis is the only addition: a unital $*$-endomorphism of a normed algebra is not bounded in general, and the article restricts to the bounded ones, which are the operators of the layer. The derived product and the associative product carry the same structure, by the identity $x\star y=xy^{*}$, so the two readings of the theorem are the same statement.

### The Parities

**Proposition (the product of two).** The composite of two multiplicative operators is multiplicative, and the parity is multiplicative: the composite of two linear ones or of two conjugate-linear ones is linear, and of a linear and a conjugate-linear one is conjugate-linear. Consequently the multiplicative operators of one of the two parities form a $\mathbb{Z}/2$-graded monoid, in which the linear part is a submonoid and the conjugate-linear part a coset.

**Proof.** For the product, $ST(x\star y)=S(Tx\star Ty)=S(Tx)\star S(Ty)$ and $ST(1)=S(1)=1$; the parity is the parity of the composite of two maps, even for equal parities and odd for different ones. $\square$

**Remark.** The conjugate-linear multiplicative operators are the $\varsigma$-semilinear unital $*$-endomorphisms, and their existence is a genuine datum of the layer: over $\mathbb{R}$ with $\varsigma=\mathrm{id}$ every operator is linear and the coset is empty, while over $\mathbb{C}$ the conjugation of the matrix model provides one, as the worked case below shows.

## The Group of the Product-Preserving Operators

### The Group and its Topology

**Theorem (the group).** The invertible multiplicative bounded operators form a group $G$; $G$ is closed in the group $GL(B(A))$ of the invertible bounded operators, and with the topology induced by the operator norm it is a topological group. The linear operators form a subgroup $G_{0}$ of index at most two, which is a normal subgroup and is the kernel of the parity homomorphism $G\to\mathbb{Z}/2$; the conjugate-linear operators are the second coset when it is nonempty.

**Proof.** The multiplicative operators are closed under composition and contain the identity, and the inverse of an invertible one is multiplicative: from $T(x\star y)=Tx\star Ty$ and the invertibility, applying $T^{-1}$ gives $x\star y=T^{-1}(Tx\star Ty)$, and writing $Tx=u$, $Ty=v$ gives $T^{-1}(u\star v)=T^{-1}u\star T^{-1}v$, which is the product-preservation of $T^{-1}$. The set of product-preserving operators is closed in $B(A)$, being the intersection of the closed sets $\{T:T(x\star y)=Tx\star Ty\}$ for $x,y$ varying over a generating set, and $GL(B(A))$ is open in the Banach algebra $B(A)$ with inversion continuous by the Neumann series, *Bounded Operators on a Sesqualgebra*; a closed subgroup of a topological group is a topological group with the subspace topology. The parity is a homomorphism onto a subgroup of the two-element group with kernel $G_{0}$, by the proposition above, whence the index and the normality. $\square$

**Remark.** The group $G_{0}$ is the group of the **bounded unital $*$-automorphisms** of the sesqualgebra. Its elements are isometries only under an additional hypothesis on the norm: a bounded automorphism has $\lVert T\rVert\ge1$ and $\lVert T^{-1}\rVert\ge1$, and it is isometric exactly when both are one. The article proves the topological group structure and not the metric geometry, which is the subject of the form category.

### The Relation to the Unitary Group of the Elements

**Theorem (the inner automorphisms).** For $u\in U(A)$ the map $\alpha_{u}(x)=uxu^{*}$ is a bounded unital $*$-automorphism, hence an element of $G_{0}$, and it is isometric with $\alpha_{u}^{-1}=\alpha_{u^{*}}$. The assignment $u\mapsto\alpha_{u}$ is a continuous homomorphism of topological groups

$$
U(A)\longrightarrow G_{0},\qquad \alpha_{u}\alpha_{v}=\alpha_{uv},
$$

whose kernel is the group $U(A)\cap Z(A)$ of the central unitary elements; its image is the normal subgroup $\operatorname{Inn}(A)$ of the inner $*$-automorphisms, and $G_{0}/\operatorname{Inn}(A)$ is the group of the outer $*$-automorphisms.

**Proof.** The multiplicativity of $\alpha_{u}$ is $u(xy)u^{*}=(uxu^{*})(uyu^{*})$, and its commutation with the involution is $(uxu^{*})^{*}=u x^{*}u^{*}$ because $u^{*}u=uu^{*}=1$; the unit is fixed. The bound is $\lVert uxu^{*}\rVert\le\lVert x\rVert$ and the inverse is $\alpha_{u^{*}}$, so $\alpha_{u}$ is isometric. The homomorphism law is $\alpha_{u}\alpha_{v}(x)=uvxv^{*}u^{*}=\alpha_{uv}(x)$, the kernel is the set of $u$ with $uxu^{*}=x$ for all $x$, that is the central unitaries, and the continuity is the continuity of the product and of the involution in the norm. The normality of the image is the conjugation law $\alpha_{v}\alpha_{u}\alpha_{v}^{-1}=\alpha_{vuv^{*}}$, and $uvu^{*}\in U(A)$ for unitary $u,v$. $\square$

**Remark.** The image of $u\mapsto\alpha_{u}$ is the group of the inner automorphisms of the monoid of units, and it is the part of $G_{0}$ that the algebra supplies without an additional hypothesis. Over a field the unitary group is the group of the elements of modulus one with the circle topology, and $\alpha_{u}$ is nontrivial on a noncentral $u$; for the complex matrices the map is the quotient $U(n)\to U(n)/U(1)=\mathrm{PU}(n)$, and the Skolem–Noether theorem of *Inner Automorphisms of a Ring* makes every $*$-automorphism inner, so $G_{0}=\mathrm{PU}(n)$ there.

## The Relation to the Unitary Operators

**Theorem (the two classes are different).** A multiplicative operator $T$ is unitary in the sense of *The Unitary Operators of a Sesqualgebra*, $T^{\dagger}=T^{-1}$, exactly when it also preserves the reduction of the pairing by a continuous central functional $\tau$,

$$
\tau\circ T=\tau ,
$$

the adjoint being taken for the reduced form $h_{\tau}$ of *Adjoints of Bounded Sesquilinear Operators*. In particular every inner $*$-automorphism $\alpha_{u}$ of a unitary element is unitary, and the left multiplication $L_{u}$ of a unitary element is antiunitary and is **not** product-preserving.

**Proof.** For a multiplicative $T$ one has $\varphi(Tx,Ty)=\tau\bigl(Tx\,(Ty)^{*}\bigr)=\tau\bigl(T(xy^{*})\bigr)=(\tau\circ T)(xy^{*})$, which equals $\varphi(x,y)$ for all $x,y$ exactly when $\tau\circ T=\tau$, by the nondegeneracy of the reduced form; this is the proposition of *The Unitary Operators of a Sesqualgebra*, §*The Operators that Preserve the Product*. For the inner automorphism, $\tau\alpha_{u}(x)=\tau(uxu^{*})=\tau(xu^{*}u)=\tau(x)$ by the cyclicity of $\tau$ and $u^{*}u=1$. The left multiplication $L_{u}$ satisfies $L_{u}^{\dagger}=S_{1,u}=L_{u}^{-1}$ for unitary $u$, by *The Adjoint of the Bounded Conjugate Left Multiplication*, so it is antiunitary; it is not product-preserving, because $L_{u}(x\star y)=u\,y\,x^{*}$ while $L_{u}x\star L_{u}y=u\,x^{*}\,y\,u^{*}$, which differ unless $x$, $y$ and $u$ commute suitably. $\square$

**Remark (the two groups).** The group $G_{0}$ of the bounded $*$-automorphisms and the group of the unitary operators of the algebraic layer are therefore different subgroups of $GL(B(A))$, meeting in the $*$-automorphisms that preserve the functional $\tau$: the first preserves the product, the second preserves the reduced form, and an operator of the second kind need not be multiplicative. The left multiplication by a unitary element is the witness: antiunitary, hence in the second group, and not multiplicative, hence outside the first.

## The Collapse and the Worked Cases

**Theorem (the bilinear collapse).** Put $\varsigma=\mathrm{id}$ and $*=\mathrm{id}$, so that $A$ is a commutative normed algebra and the derived product is the ordinary product. Then the conjugate-linear coset is empty, the group is $G=G_{0}=\operatorname{Aut}(A)$ of the bounded unital automorphisms of the algebra, and the article reduces to the automorphism group of a commutative Banach algebra.

**Proof.** With $\varsigma=\mathrm{id}$ every bounded operator is $\mathbb{K}$-linear, so the parity coset is empty and $G=G_{0}$; with $*=\mathrm{id}$ the product is the ordinary one and the $*$-endomorphisms are the automorphisms. The topological group statement is that of the bounded automorphism group, and the inner automorphisms of the unitary elements are the inner automorphisms of the unit group. $\square$

### The Complex Matrices

Let $A=M_{n}(\mathbb{C})$ with the conjugate transpose and the operator norm. The multiplicative operators are the unital $*$-endomorphisms; by the Skolem–Noether theorem every $*$-automorphism is inner, $\alpha_{U}(X)=UXU^{*}$, so $G_{0}=\mathrm{PU}(n)=U(n)/U(1)$, a compact connected Lie group, and the inner map is the quotient of $U(n)$ by its centre. The conjugate-linear coset is nonempty: the entrywise conjugation $X\mapsto\overline{X}$ is a conjugate-linear unital $*$-endomorphism of order two, multiplicative and commuting with the conjugate transpose. (The transpose $X\mapsto X^{\mathsf{T}}$ is a $\mathbb{C}$-linear $*$-anti-automorphism — anti-multiplicative, hence not product-preserving — and it belongs to the algebraic layer and not to $G$.) The left multiplication by a unitary matrix is antiunitary and not multiplicative, the witness of the separation of the two classes.

### The Finite Product and the Field

For $A=\mathbb{K}^{n}$ with the termwise product, the involution $\varsigma$ acting on each coordinate and the norm $\max_{i}|x_{i}|$: a unital multiplicative operator sends a minimal idempotent $e_{i}$ to a minimal idempotent, so the multiplicative operators are the coordinate permutations and $G_{0}=S_{n}$, while for $\mathbb{K}=\mathbb{C}$ the entrywise conjugation is a conjugate-linear multiplicative operator adding the second coset, so $G=S_{n}\times\mathbb{Z}/2$ (over $\mathbb{R}$ the coset is empty and $G=S_{n}$). (A termwise product on a space of sequences is not unital, so the structure theorem is stated for the finite product and for the Banach sesqualgebras of the base entries.) For $A=\mathbb{C}$ the multiplicative operators are the identity and the conjugation, $G=\mathbb{Z}/2$ with $G_{0}$ trivial, the example of the smallest nontrivial parity coset.

## Summary

A bounded operator of one of the two parities preserving the derived product and fixing the unit is exactly a unital $*$-endomorphism of the corresponding parity, $T(xy)=Tx\,Ty$ and $T(y^{*})=(Ty)^{*}$; this holds for the conjugate-linear operators as well, where the scalar action is carried through $\varsigma$. The invertible ones form a group $G$, closed in the invertible bounded operators and, with the norm topology, a topological group; the linear ones form a normal subgroup $G_{0}$ of index at most two, the bounded unital $*$-automorphisms, with the conjugate-linear operators as the second coset. The unitary elements map continuously into $G_{0}$ by $u\mapsto\alpha_{u}$, $uxu^{*}$, with kernel the central unitaries and image the inner $*$-automorphisms, and for the complex matrices this is the quotient $U(n)\to\mathrm{PU}(n)$ with $G_{0}=\mathrm{PU}(n)$. The product-preserving condition and the unitary condition of the algebraic layer are independent: a product-preserving operator is unitary for the reduced form exactly when it preserves the central functional, and the left multiplication by a unitary element is antiunitary and not product-preserving. In the bilinear case the conjugate-linear coset is empty and the group is the bounded automorphism group of the commutative algebra.

## Summary of Notation

| symbol | meaning |
|---|---|
| $T(x\star y)=Tx\star Ty$ | the product-preserving condition |
| $T(1)=1$ | the multiplicative condition |
| $T(xy)=Tx\,Ty$, $T(y^{*})=(Ty)^{*}$ | the equivalent unital $*$-endomorphism form |
| $G$ | the group of the invertible multiplicative bounded operators |
| $G_{0}$ | the linear subgroup, the bounded unital $*$-automorphisms, of index at most two |
| $\alpha_{u}(x)=uxu^{*}$ | the inner $*$-automorphism of a unitary element |
| $U(A)\to G_{0}$, $u\mapsto\alpha_{u}$ | the continuous homomorphism with kernel $U(A)\cap Z(A)$ |
| $\operatorname{Inn}(A)$ | the inner $*$-automorphisms, a normal subgroup of $G_{0}$ |
| $\tau\circ T=\tau$ | the condition that a multiplicative operator be unitary for the reduced form |
| $L_{u}$ | antiunitary and not product-preserving, the witness of the separation |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, volume 1 (Academic Press, 1983), for the group of invertible bounded operators, the Neumann series and the topological group structure.
- Jacques Dixmier, *C\*-Algebras* (North-Holland, 1977), for the automorphism group of a $C^{*}$-algebra, the inner automorphisms and the group of the unitary elements.
- N. E. Wegge-Olsen, *K-Theory and C\*-Algebras* (Oxford University Press, 1993), for the unitary group of a $C^{*}$-algebra and the quotient by the inner automorphisms, the model of the relation to $U(A)$.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the $*$-automorphisms and the $*$-anti-automorphisms of a ring with involution, the algebraic form of the structure theorem.
