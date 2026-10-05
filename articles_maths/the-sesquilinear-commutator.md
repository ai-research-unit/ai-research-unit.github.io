# __The Sesquilinear Commutator__

## Introduction

A sesquilinear product carries a second product, its transpose $y\star x$, and the difference of the two is the antisymmetric half of the split of the product. This article treats that difference for its own sake: the bracket $[x,y]_{\varsigma}=x\star y-y\star x$. Three things are done. The bracket is antisymmetric for free, but it is linear over the fixed ring $R^{\varsigma}$ alone, and the correction term $(\lambda-\varsigma(\lambda))(y\star x)$ is the whole of the difference from the bilinear case. It takes its values in the skew-Hermitian part, $[A,A]_{\varsigma}\subseteq S(A)$, and on the two halves it is one of the classical operations of the envelope: the ordinary commutator on the Hermitian part, its negative on the skew-Hermitian part, and the symmetrised product across the two. And it is not a Lie bracket: the Jacobi identity fails, with the witness $E_{11},E_{22},E_{12}$ of $M_{2}(\mathbb{C})$ and with the observation that the failure needs the noncommutativity and not the twist, since it vanishes for the sesquilinear field. The Lie structure that a sesquialgebra carries instead lives on the skew-Hermitian half, and it is *Lie Algebras of Sesquialgebras*.

The article is the narrow companion of two others: the symmetric half of the same split is *The Sesquilinear Symmetrised Product*, and the bracket, its name and the transposition theorem are introduced in *The Sesquilinear Product*; the whole question of Lie-admissibility, with the collapse theorem and the Lie algebra that the sesquialgebra does carry, is *Lie Algebras of Sesquialgebras* and *The Unitary Lie Algebra*, which are the owners of those results. The Hermitian and the skew-Hermitian elements are *Hermitian and Skew-Hermitian Elements*; the ternary product forced by the failure of associativity is *The Sesquilinear Associator and the Ternary Product*.

The setting is the standard example of *Sesquialgebras*: $A$ is an associative unital $R$-algebra with a $\varsigma$-semilinear involution $*$, the sesquilinear product is the derived operation $x\star y=xy^{*}$, and juxtaposition is the associative product. The bracket is $[x,y]_{\varsigma}=x\star y-y\star x$, the ordinary commutator of the envelope is $[x,y]=xy-yx$, the two halves are $H(A)=\{x:x^{*}=x\}$ and $S(A)=\{x:x^{*}=-x\}$, and $2$ is invertible in $R$.

## The Bracket

### Definition and Antisymmetry

**Definition.** The **sesquilinear commutator**, or the **difference**, of $x,y\in A$ is

$$
[x,y]_{\varsigma}=x\star y-y\star x=xy^{*}-yx^{*} .
$$

**Proposition (antisymmetry).** For all $x,y\in A$,

$$
[y,x]_{\varsigma}=-[x,y]_{\varsigma}, \qquad [x,x]_{\varsigma}=0 .
$$

**Proof.** Both statements are the antisymmetry of the subtraction, applied to the two terms of the difference. $\square$

**Remark.** Antisymmetry is free: it uses neither the involution nor the associativity, and it holds for an arbitrary sesquilinear product. It is the one property the bracket has without a hypothesis, and the rest of the article is the account of the properties it does not have.

### The Scalars and the Correction Term

**Theorem (the scalars of the bracket).** For all $\lambda\in R$ and all $x,y\in A$,

$$
[\lambda x,y]_{\varsigma}=\lambda\,(x\star y)-\varsigma(\lambda)\,(y\star x), \qquad [x,\lambda y]_{\varsigma}=\varsigma(\lambda)\,(x\star y)-\lambda\,(y\star x),
$$

so that

$$
[\lambda x,y]_{\varsigma}-\lambda[x,y]_{\varsigma}=\bigl(\lambda-\varsigma(\lambda)\bigr)(y\star x), \qquad [x,\lambda y]_{\varsigma}-\lambda[x,y]_{\varsigma}=\bigl(\varsigma(\lambda)-\lambda\bigr)(x\star y).
$$

**Proof.** In the first slot, $(\lambda x)\star y=\lambda(x\star y)$ by the first scalar rule and $y\star(\lambda x)=\varsigma(\lambda)(y\star x)$ by the second, the scalar sitting in the second slot of the transposed product; the second display is the first read with the two slots exchanged, the antisymmetry carrying the sign of the bracket; the two transposed products differ, so the two corrections carry $y\star x$ and $x\star y$ respectively. The correction terms are the differences of the two displays from $\lambda[x,y]_{\varsigma}=\lambda(x\star y)-\lambda(y\star x)$. $\square$

**Corollary (linearity over the fixed ring).** For $\lambda$ in the fixed ring $R^{\varsigma}=\{\lambda:\varsigma(\lambda)=\lambda\}$,

$$
[\lambda x,y]_{\varsigma}=\lambda[x,y]_{\varsigma}=[x,\lambda y]_{\varsigma},
$$

so the bracket is $R^{\varsigma}$-bilinear as a map $A\times A\to A$. It is $R$-bilinear exactly in the degenerate case $\bigl(\lambda-\varsigma(\lambda)\bigr)(y\star x)=0$ for all $\lambda,x,y$, that is when $\varsigma=\mathrm{id}$ or the product vanishes identically.

**Remark.** The correction term is the whole difference from the bilinear case, and it is the same term that the transposed product and the symmetrised product carry: an operation that reads the two slots of the product in one expression inherits the difference of the two scalar rules. The bracket is therefore an $R^{\varsigma}$-bilinear object and not an $R$-bilinear one, which is the first respect, after the antisymmetry, in which it parts company with a Lie bracket over $R$.

## The Values in the Skew-Hermitian Part

**Proposition (the split of the product).** With $2$ invertible in $R$,

$$
x\star y=x\circ y+\tfrac12[x,y]_{\varsigma}, \qquad x\circ y=\tfrac12\bigl(x\star y+y\star x\bigr),
$$

where $\circ$ is the symmetrised product of *The Sesquilinear Symmetrised Product*: the bracket is the antisymmetric half of the split and the symmetrised product the symmetric half.

**Proof.** Add and subtract $\tfrac12(y\star x)$. $\square$

**Proposition (the values).** For all $x,y\in A$,

$$
[x,y]_{\varsigma}^{*}=-[x,y]_{\varsigma} .
$$

So the bracket takes its values in the skew-Hermitian part,

$$
[A,A]_{\varsigma}\subseteq S(A),
$$

and it is a skew-symmetric $R^{\varsigma}$-bilinear map $A\times A\to S(A)$.

**Proof.** The conjugate of a product reverses it, $(x\star y)^{*}=y\star x$, so $[x,y]_{\varsigma}^{*}=(y\star x)-(x\star y)=-[x,y]_{\varsigma}$. $\square$

**Remark.** The values are skew-Hermitian for every pair and not merely for skew-Hermitian arguments, so the bracket is an operator $A\times A\to S(A)$ and its image never meets $H(A)$ unless it vanishes. This is the second sharp difference from the ordinary commutator, which moves between the two halves: the commutator of two Hermitian elements is skew-Hermitian, of a Hermitian and a skew-Hermitian element Hermitian, of two skew-Hermitian elements skew-Hermitian, so that $S(A)$ is its even part and $H(A)$ its odd part. The sesquilinear bracket has only the first of those three behaviours, and it has it everywhere.

## The Two Halves

**Theorem (the bracket on the two halves).** For $h,h'\in H(A)$ and $s,s'\in S(A)$,

$$
[h,h']_{\varsigma}=[h,h'], \qquad [s,s']_{\varsigma}=-[s,s'], \qquad [s,h]_{\varsigma}=sh+hs .
$$

So on the Hermitian part the sesquilinear bracket is the ordinary commutator of the envelope, on the skew-Hermitian part it is the negative of the ordinary commutator, and across the two halves it is the **symmetrised** product $sh+hs$.

**Proof.** For Hermitian $h$ the derived operation is the algebra product in the first slot, $h\star h'=hh'^{*}=hh'$, and the transposed product is the same in the other order, so $[h,h']_{\varsigma}=hh'-h'h=[h,h']$. For skew-Hermitian $s$ the involution contributes a sign, $s^{*}=-s$, so $[s,s']_{\varsigma}=(-ss')-(-s's)=-[s,s']$, and $[s,h]_{\varsigma}=sh^{*}-hs^{*}=sh+hs$. $\square$

**Corollary (the Lie algebra of the skew-Hermitian half).** On $S(A)$ the sesquilinear bracket is $R$-bilinear, antisymmetric and satisfies the Jacobi identity, being the negative of the commutator of the associative envelope; the negation being an isomorphism of brackets, the sesquilinear bracket and the ordinary commutator make $S(A)$ one and the same Lie algebra, up to the sign of the bracket. That Lie algebra is *The Unitary Lie Algebra*, and its place in the sesquialgebra is *Lie Algebras of Sesquialgebras*, §*The Skew-Hermitian Half*.

**Proof.** By the theorem, $[s,s']_{\varsigma}=-[s,s']$ on $S(A)$, and $[S,S]\subseteq S$ for the ordinary commutator; the commutator of an associative algebra is $R$-bilinear, antisymmetric and satisfies the Jacobi identity, and the sign carries through the three terms. $\square$

**Remark (why the Hermitian half does not work).** The Hermitian half is not stable under the bracket, since $[h,h']_{\varsigma}=[h,h']$ is skew-Hermitian and not Hermitian unless it vanishes; and it does not satisfy the Jacobi identity either. The reason is the substance of the next section: three Hermitian elements produce inner brackets in $S(A)$, and the outer brackets that meet those values obey the symmetrised rule of the theorem and not the commutator rule, so the reassociation a Jacobi identity performs is performed with a different operation. The failing triple of the next section can be taken with all three elements Hermitian, so the failure is not a defect of the mixed case alone.

## The Failure of the Jacobi Identity

**Theorem.** The Jacobi identity for the sesquilinear bracket fails in general. In $A=M_{2}(\mathbb{C})$ with the conjugate transpose, for $x=E_{11}$, $y=E_{22}$ and $z=E_{12}$,

$$
[[x,y]_{\varsigma},z]_{\varsigma}+[[y,z]_{\varsigma},x]_{\varsigma}+[[z,x]_{\varsigma},y]_{\varsigma}=E_{21}-E_{12}\neq0 .
$$

**Proof.** By the multiplication of the matrix units, $E_{ab}E_{cd}=\delta_{bc}E_{ad}$, and the reality of the units, $[E_{11},E_{22}]_{\varsigma}=E_{11}E_{22}-E_{22}E_{11}=0$ and $[E_{12},E_{11}]_{\varsigma}=E_{12}E_{11}-E_{11}E_{21}=0$, while $[E_{22},E_{12}]_{\varsigma}=E_{22}E_{12}^{*}-E_{12}E_{22}^{*}=E_{22}E_{21}-E_{12}E_{22}=E_{21}-E_{12}$. Only the middle of the three terms survives, and $[E_{21}-E_{12},E_{11}]_{\varsigma}=(E_{21}-E_{12})E_{11}^{*}-E_{11}(E_{21}-E_{12})^{*}=(E_{21}-E_{12})E_{11}-E_{11}(E_{12}-E_{21})=E_{21}-E_{12}$. The sum is $E_{21}-E_{12}\neq0$. $\square$

**Remark (three Hermitian elements suffice).** The witness uses an element outside the two halves, the matrix unit $E_{12}$, but the failure does not need one. With $X=E_{12}+E_{21}$, which is Hermitian, the triple $E_{11},E_{22},X$ has the three inner brackets $0$, $E_{21}-E_{12}$ and $E_{21}-E_{12}$, and the Jacobi sum is $2(E_{21}-E_{12})$, so three Hermitian elements already fail. This is the mechanism described above: the inner brackets of a Hermitian triple are ordinary commutators and land in $S(A)$, and the outer brackets then read those values with the symmetrised rule.

**Remark (the failure needs noncommutativity and not the twist).** The obstruction is not the semilinearity alone. On the sesquilinear field $\mathbb{C}$ over $(\mathbb{C},\varsigma)$ with $x\star y=x\overline{y}$ the bracket is $[x,y]_{\varsigma}=x\overline{y}-y\overline{x}=2i\,\mathrm{Im}(x\overline{y})$, antisymmetric and linear over $\mathbb{R}$, and its values are purely imaginary, that is in $S(\mathbb{C})$; the Jacobi identity holds identically on it. For the verification write $x=a+bi$, $y=c+di$ and $z=e+fi$ with real coordinates: the bracket is $[x,y]_{\varsigma}=2i(bc-ad)$, so the three cyclic terms of the Jacobi sum are $4i(bc-ad)e$, $4i(de-cf)a$ and $4i(fa-eb)c$, whose sum telescopes to zero. The failure of the theorem is therefore produced by the noncommutativity of $M_{2}(\mathbb{C})$ and not by the semilinearity of the product, and the bracket of the field is a Lie bracket over the fixed field $\mathbb{R}$, in agreement with the dichotomy that *Biquaternion Lie Algebras* records, where among the four antisymmetrisations of the four products exactly the commutator satisfies the identity.

**Remark (the delegation).** The Lie-admissibility of the antisymmetrisation, the collapse theorem, which reduces a Lie-admissible antisymmetrisation of full type to the bilinear case and forces both involutions to be trivial, and the Lie algebra that the sesquialgebra does carry are *Lie Algebras of Sesquialgebras*. This article records the bracket, the failure and the reason for it, and nothing beyond.

## The Vanishing and the Involution

**Proposition.** For all $x,y$,

$$
[x,1]_{\varsigma}=x-x^{*}, \qquad [1,y]_{\varsigma}=y^{*}-y .
$$

**Proof.** $[x,1]_{\varsigma}=x\star1-1\star x=x1^{*}-1x^{*}=x-x^{*}$, and $[1,y]_{\varsigma}=1y^{*}-y1^{*}=y^{*}-y$. $\square$

**Corollary.** The bracket detects the involution: $[x,1]_{\varsigma}=0$ exactly for the Hermitian $x$, and $[x,y]_{\varsigma}=0$ for all $x,y$ exactly when $*=\mathrm{id}$ and $A$ is commutative. The second statement is the transposition theorem of *The Sesquilinear Product* read as a statement about the bracket, and it is the sense in which a genuine sesquilinear bracket never vanishes.

**Proposition (the bracket does not commute with the involution).** In $M_{2}(\mathbb{C})$, for $x=E_{12}$ and $y=E_{11}$,

$$
[x^{*},y^{*}]_{\varsigma}=E_{21}-E_{12}, \qquad [x,y]_{\varsigma}=0,
$$

so $[x^{*},y^{*}]_{\varsigma}$ is neither $[x,y]_{\varsigma}^{*}$ nor its negative. The involution does not act on the bracket as it would have to for the bracket of an algebra with involution, and this is a third respect, after the $R^{\varsigma}$-bilinearity and the Jacobi identity, in which the bracket is not that of a Lie algebra with involution.

**Proof.** $[x,y]_{\varsigma}=E_{12}E_{11}-E_{11}E_{21}=0$, and $[x^{*},y^{*}]_{\varsigma}=[E_{21},E_{11}]_{\varsigma}=E_{21}E_{11}-E_{11}E_{12}=E_{21}-E_{12}$, the two products being $E_{21}$ and $E_{12}$ by the multiplication of the matrix units. $\square$

## Worked Cases

### The Complex Matrices

For $A=M_{n}(\mathbb{C})$ with the conjugate transpose the bracket is $[X,Y]_{\varsigma}=XY^{*}-YX^{*}$, with values in $S(A)$, the skew-Hermitian matrices. On the Hermitian matrices it is the ordinary commutator $XY-YX$, on the skew-Hermitian matrices its negative; the ordinary commutator makes $S(A)$ a Lie algebra and the sesquilinear bracket makes it the same Lie algebra with the sign reversed, which is *The Unitary Lie Algebra*. The witness of the theorem is in $M_{2}(\mathbb{C})$, and the failure is already produced there by the three Hermitian elements $E_{11}$, $E_{22}$ and $E_{12}+E_{21}$.

### The Field

For $A=\mathbb{C}$ over $(\mathbb{C},\varsigma)$ with $x\star y=x\overline{y}$ the bracket is $[x,y]_{\varsigma}=2i\,\mathrm{Im}(x\overline{y})$, antisymmetric and linear over $\mathbb{R}$, with values in the purely imaginary numbers, which are $S(A)$. The Jacobi identity holds, so the bracket is a Lie bracket over the fixed field $\mathbb{R}$; it does not vanish, since $[1,i]_{\varsigma}=-2i$, so a commutative algebra carries a non-abelian bracket of this kind. The failure of the Jacobi identity in the noncommutative case is therefore produced by the noncommutativity of the coefficients and not by the twist.

### The Skew-Hermitian Half

The Lie structure that a sesquialgebra carries is on $S(A)$, where the bracket is the negative of the commutator of the envelope, so that antisymmetry, the two scalar rules and the Jacobi identity all hold; the Hermitian half carries no Lie algebra under the sesquilinear bracket, its bracket leaving it and the Jacobi identity failing on it. This is the sense in which the sesquialgebra replaces the antisymmetrisation of its own product by the commutator of the associative structure, and the replacement is *Lie Algebras of Sesquialgebras* and *The Unitary Lie Algebra*.

## Summary

The sesquilinear commutator is the difference of the product and its transpose, $[x,y]_{\varsigma}=x\star y-y\star x$, the antisymmetric half of the split of the product whose symmetric half is the symmetrised product. It is antisymmetric for free; it is linear over the fixed ring $R^{\varsigma}$ and not over $R$, the correction term $(\lambda-\varsigma(\lambda))(y\star x)$ being the whole difference from the bilinear case; and it takes its values in the skew-Hermitian part, $[A,A]_{\varsigma}\subseteq S(A)$, for all arguments. On the two halves it is one of the operations of the envelope: the ordinary commutator on $H(A)$, its negative on $S(A)$, and the symmetrised product across the two. It is not a Lie bracket. The Jacobi identity fails, with the witness $E_{11},E_{22},E_{12}$ in $M_{2}(\mathbb{C})$, whose sum is $E_{21}-E_{12}$; three Hermitian elements already fail; and the failure needs the noncommutativity and not the twist, since on the commutative sesquilinear field the identity holds identically. The bracket does not commute with the involution either. The Lie algebra that a sesquialgebra does carry is on the skew-Hermitian half, where the sesquilinear bracket is the negative of the commutator of the associative envelope and therefore satisfies the identity; that Lie algebra is *Lie Algebras of Sesquialgebras* and *The Unitary Lie Algebra*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $x\star y=xy^{*}$ | the derived sesquilinear product |
| $[x,y]_{\varsigma}=x\star y-y\star x$ | the sesquilinear commutator, the difference of the product and its transpose |
| $[x,y]=xy-yx$ | the ordinary commutator of the associative envelope |
| $x\circ y=\tfrac12(x\star y+y\star x)$ | the symmetrised product, the symmetric half of the split |
| $R^{\varsigma}$ | the fixed ring, over which the bracket alone is linear |
| $(\lambda-\varsigma(\lambda))(y\star x)$ | the correction term of the scalar rule |
| $H(A)$, $S(A)$ | the Hermitian and the skew-Hermitian elements |
| $[A,A]_{\varsigma}\subseteq S(A)$ | the values of the bracket |
| $[h,h']_{\varsigma}=[h,h']$ | the bracket on the Hermitian part |
| $[s,s']_{\varsigma}=-[s,s']$ | the bracket on the skew-Hermitian part |
| $[s,h]_{\varsigma}=sh+hs$ | the bracket across the two halves |
| $E_{11},E_{22},E_{12}$ | the witness triple in $M_{2}(\mathbb{C})$ |

## Further Reading

- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the two halves of a ring with involution and the operations they carry.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the antisymmetrisation of an associative algebra and the Lie algebra of the skew elements.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for the skew elements of an algebra with involution and the Lie structure they carry.
- The companion articles of this series: *Sesquialgebras*, *The Sesquilinear Product*, *The Sesquilinear Symmetrised Product*, *Hermitian and Skew-Hermitian Elements*, *The Sesquilinear Associator and the Ternary Product*, *Lie Algebras of Sesquialgebras* and *The Unitary Lie Algebra*.
