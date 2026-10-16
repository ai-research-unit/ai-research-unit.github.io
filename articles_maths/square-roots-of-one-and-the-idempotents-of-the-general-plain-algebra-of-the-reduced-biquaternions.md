# __Square Roots of One and the Idempotents of the General Plain Algebra of the Reduced Biquaternions__

## Introduction

This article solves the equations $T^{2}=1$ and $T^{2}=T$ in the multiplication of the general plain algebra and reads the solutions. The **roots of one** are the four elements
$$
1,\quad -1,\quad j,\quad -j,
$$
and the **idempotents** are the four elements
$$
0,\quad 1,\quad \Pi_{1}=\tfrac12(1+j),\quad \Pi_{2}=\tfrac12(1-j).
$$
The two lists are exchanged by the **halving map** $T\mapsto\tfrac12(1+T)$, which sends a root of one to an idempotent and back; the two nontrivial idempotents are complementary and orthogonal, $\Pi_{1}+\Pi_{2}=1$ and $\Pi_{1}\Pi_{2}=0$, and each carries a **projection**, the map $T\mapsto\Pi_{i}T$, so that the algebra resolves as the sum of the two idempotent lines.

The computation is short because the multiplication is componentwise in the idempotent coordinates: for $T=(q_1,q_2)$ one has $T^{2}=(q_1^{2},q_2^{2})$, so $T^{2}=1$ is the pair of complex equations $q_1^{2}=1$, $q_2^{2}=1$ and $T^{2}=T$ is the pair $q_1^{2}=q_1$, $q_2^{2}=q_2$. Every list of solutions is therefore a product of two complex lists, and the four figures come from the two solutions $\pm1$ and the two solutions $0,1$ of the complex equations.

**The results.** The roots of one are $1,-1,j,-j$, and they form a group isomorphic to $\mathbb{Z}_{2}\times\mathbb{Z}_{2}$ under the multiplication. The idempotents are $0,1,\Pi_{1},\Pi_{2}$, of which $\Pi_{1}$ and $\Pi_{2}$ are the nontrivial ones and are complementary, orthogonal and zero divisors. Each idempotent $e$ carries the projection $P_{e}(T)=eT$, with $P_{\Pi_{1}}+P_{\Pi_{2}}=\mathrm{id}$, $P_{e}^{2}=P_{e}$ and $P_{\Pi_{1}}P_{\Pi_{2}}=0$; the two projections are the Peirce projections onto the two lines, and the Peirce decomposition itself is *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions*, below this article in this category. The **natural sign** and the **star** both exchange the two nontrivial idempotents, $\Pi_{1}^{\natural}=\Pi_{2}=\Pi_{1}^{*}$, while only the bar fixes each idempotent, $\overline{\Pi_{i}}=\Pi_{i}$.

**Boundaries.** The algebra, its product and its structure as a direct product of two fields are *Introduction to the General Plain Algebra of the Reduced Biquaternions*, above this article in this category. The involutions and the idempotents' behaviour under them are *The Two Involutions and the Group of Involutions*, above this article. The zero divisors and the two lines are *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*, above this article; the annihilators are *Annihilators of the General Plain Algebra of the Reduced Biquaternions*, above this article; and the roots of zero and the nilpotents are *Square Roots of Zero and the Nilpotents of the General Plain Algebra of the Reduced Biquaternions*, below this article. The Peirce decomposition into the ideals the idempotents carry is *Ideals and Peirce Decomposition*, below this article in this category.

## The Roots of One

### The Equation and the Four Roots

**The equation $T^{2}=1$ has exactly four solutions: $1$, $-1$, $j$ and $-j$.**

**Theorem (the roots of one).** The solutions of $T^{2}=1$ in the multiplication are
$$
T=1,\qquad T=-1,\qquad T=j,\qquad T=-j,
$$
and there are no others.

*Proof.* In the idempotent coordinates $T=(q_1,q_2)$ with $q_1=A+B$ and $q_2=A-B$, the product is componentwise, so $T^{2}=(q_1^{2},q_2^{2})$ (*Introduction to the General Plain Algebra of the Reduced Biquaternions*). The equation $T^{2}=1$ is the pair $q_1^{2}=1$ and $q_2^{2}=1$; a complex number has the two square roots of $1$, namely $\pm1$, so $q_1,q_2\in\{1,-1\}$. The four pairs $(q_1,q_2)$ give, by $A=\tfrac12(q_1+q_2)$ and $B=\tfrac12(q_1-q_2)$,
$$
(q_1,q_2)=(1,1)\to T=1,\quad (1,-1)\to T=j,\quad (-1,1)\to T=-j,\quad (-1,-1)\to T=-1 .
$$

**Corollary (the roots of one in the real basis).** In the real coordinates the roots are $1=(1,0,0,0)$, $-1=(-1,0,0,0)$, $j=(0,0,1,0)$ and $-j=(0,0,-1,0)$; all four lie in the real subalgebra $\mathbb{R}\{1,j\}$.

*Proof.* The four elements are $\pm1$ and $\pm j$, read in the real basis; both $A$ and $B$ are real at each of them.

**Remark (the roots of $-1$ are different).** The equation $T^{2}=-1$ has the four solutions $\pm i$ and $\pm ij$, the roots of $-1$ of *Conventions in Mathematics*, §*The Roots*: they are the roots of one multiplied by $i$, and they lie in the translate $i\mathbb{R}\{1,j\}$. The roots of one are not the roots of $-1$, and the distinction is stated here because the two families are both four.

### The Group of the Roots

**The four roots of one form a group isomorphic to $\mathbb{Z}_{2}\times\mathbb{Z}_{2}$ under the multiplication.**

**Theorem.** The set $\{1,-1,j,-j\}$ is closed under the multiplication, and it is a group isomorphic to $\mathbb{Z}_{2}\times\mathbb{Z}_{2}$; its non-identity elements are the three involutions $-1$, $j$ and $-j$, and the product of any two distinct non-identity elements is the third.

*Proof.* The products are read from $j^{2}=1$ and $(-1)^{2}=1$:
$$
(-1)j=-j,\qquad (-1)(-j)=j,\qquad j(-j)=-j^{2}=-1,
$$
so the set is closed, and $1$ is the identity; every element is its own inverse. A group of four elements with every element of order two is $\mathbb{Z}_{2}\times\mathbb{Z}_{2}$.

**Corollary (the two lists are distinct).** The roots of one and the idempotents meet in the single element $1$; the halving map of §*The Halving Map* is a bijection between the two lists, and it is not the identity.

## The Idempotents

### The Idempotent Equation and the Four Idempotents

**The equation $T^{2}=T$ has exactly four solutions: $0$, $1$, $\Pi_{1}$ and $\Pi_{2}$.**

**Definition.** An **idempotent** is a solution of $T^{2}=T$; the **nontrivial idempotents** are the idempotents different from $0$ and $1$.

**Theorem (the idempotents).** The solutions of $T^{2}=T$ are
$$
T=0,\qquad T=1,\qquad T=\Pi_{1}=\tfrac12(1+j),\qquad T=\Pi_{2}=\tfrac12(1-j),
$$
and there are no others.

*Proof.* In the idempotent coordinates the equation is the pair $q_1^{2}=q_1$ and $q_2^{2}=q_2$; a complex number satisfies $z^{2}=z$ iff $z=0$ or $z=1$. The four pairs $(q_1,q_2)$ give, by $A=\tfrac12(q_1+q_2)$ and $B=\tfrac12(q_1-q_2)$,
$$
(0,0)\to T=0,\quad (1,1)\to T=1,\quad (1,0)\to T=\Pi_{1},\quad (0,1)\to T=\Pi_{2}.
$$

### The Two Nontrivial Idempotents

**The two nontrivial idempotents are complementary, orthogonal and zero divisors, and they are the generators of the two lines.**

**Theorem (complementarity and orthogonality).** The two nontrivial idempotents satisfy
$$
\Pi_{1}^{2}=\Pi_{1},\qquad \Pi_{2}^{2}=\Pi_{2},\qquad \Pi_{1}\Pi_{2}=0,\qquad \Pi_{1}+\Pi_{2}=1 .
$$

*Proof.* Read in the idempotent coordinates, $\Pi_{1}=(1,0)$ and $\Pi_{2}=(0,1)$, so the four relations are the componentwise relations in $\mathbb{C}\oplus\mathbb{C}$; equivalently, the direct computation of *Reduced Biquaternion Space*. The orthogonality $\Pi_{1}\Pi_{2}=0$ makes each a **zero divisor**, and the two lines they generate are the null cone of *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*.

**Corollary (the idempotents and the roots of one).** The two nontrivial idempotents are $\Pi_{1}=\tfrac12(1+j)$ and $\Pi_{2}=\tfrac12(1-j)$, the halves of the sum and the difference of the identity and the root $j$ of one.

*Proof.* The two displays are the definitions; the root of one used is $j$, since $j^{2}=1$ is what makes $\Pi_{i}^{2}=\Pi_{i}$.

## The Projections

### The Projection onto an Idempotent Line

**Each idempotent $e$ carries the projection $P_{e}(T)=eT$, the orthogonal projection onto the line $\mathbb{C}e$ along the other line.**

**Definition.** For an idempotent $e$ of the multiplication, the **projection** it carries is
$$
P_{e}(T)=eT.
$$

**Theorem (the projections are projections).** For $e=\Pi_{1}$ and $e=\Pi_{2}$,
$$
P_{e}^{2}=P_{e},\qquad P_{\Pi_{1}}+P_{\Pi_{2}}=\mathrm{id},\qquad P_{\Pi_{1}}P_{\Pi_{2}}=0=P_{\Pi_{2}}P_{\Pi_{1}}.
$$

*Proof.* $P_{e}^{2}(T)=e(eT)=e^{2}T=eT$; the sum is $(\Pi_{1}+\Pi_{2})T=1\,T=T$; and the product is $\Pi_{1}\Pi_{2}T=0$. The identity $P_{\Pi_{1}}+P_{\Pi_{2}}=\mathrm{id}$ is the **resolution of the identity**, and the two projections are the Peirce projections of the algebra.

**Proposition (the explicit projections).** For $T=C+Dj$,
$$
P_{\Pi_{1}}(T)=(C+D)\Pi_{1},\qquad P_{\Pi_{2}}(T)=(C-D)\Pi_{2},
$$
so the image of $P_{\Pi_{1}}$ is the first idempotent line and the image of $P_{\Pi_{2}}$ the second.

*Proof.* $\Pi_{1}T=\Pi_{1}(C+Dj)=C\Pi_{1}+D\Pi_{1}j$; and $\Pi_{1}j=\tfrac12(1+j)j=\tfrac12(j+1)=\Pi_{1}$, so $\Pi_{1}T=(C+D)\Pi_{1}$. The same for $\Pi_{2}$, using $\Pi_{2}j=-\Pi_{2}$.

### The Resolution of the Identity

**The algebra is the direct sum of the two images, and the resolution of the identity is the decomposition of every element into its two idempotent coordinates.**

**Theorem (the direct sum).** The algebra is the direct sum of the two images,
$$
\mathbb{B}_{\mathrm{r}}=\operatorname{im}P_{\Pi_{1}}\oplus\operatorname{im}P_{\Pi_{2}}=\mathbb{C}\Pi_{1}\oplus\mathbb{C}\Pi_{2},
$$
and every element has the unique decomposition $T=P_{\Pi_{1}}(T)+P_{\Pi_{2}}(T)$.

*Proof.* $P_{\Pi_{1}}+P_{\Pi_{2}}=\mathrm{id}$ gives the decomposition, and $P_{\Pi_{1}}P_{\Pi_{2}}=0$ gives its uniqueness; the images are the two lines, which meet only at the origin (*Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*). The decomposition of a general element reads $T=(A+B)\Pi_{1}+(A-B)\Pi_{2}$ (*Reduced Biquaternion Space*).

**Remark (the Peirce decomposition).** The projections and the lines they carry are the **Peirce** data of the two idempotents; the spaces in the general Peirce decomposition of a pair of idempotents, the four subspaces $e\mathbb{B}e$, $e\mathbb{B}(1-e)$, $(1-e)\mathbb{B}e$ and $(1-e)\mathbb{B}(1-e)$, are *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions*, below this article in this category; here only the two projections and the two lines they carry are read.

## The Idempotents Under the Involutions

**The natural sign and the star both exchange the two nontrivial idempotents, and only the bar fixes every idempotent.**

**Theorem.** $\Pi_{1}^{\natural}=\Pi_{2}=\Pi_{1}^{*}$, $\Pi_{2}^{\natural}=\Pi_{1}=\Pi_{2}^{*}$, and $\overline{\Pi_{i}}=\Pi_{i}$; the flat sends each idempotent to the negative of the other, $\Pi_{1}^{\flat}=-\Pi_{2}$ and $\Pi_{2}^{\flat}=-\Pi_{1}$, which is not an idempotent.

*Proof.* $\Pi_{1}^{\natural}=\tfrac12(1+j)^{\natural}=\tfrac12(1-j)=\Pi_{2}$, and $\Pi_{2}^{\natural}=\Pi_{1}$ (*The Two Involutions and the Group of Involutions*); the bar conjugates the coefficients of $\Pi_{i}=\tfrac12\pm\tfrac12 j$, which are real, so it fixes $\Pi_{i}$; the star is $\bar{\cdot}\circ{}^{\natural}$, so $\Pi_{1}^{*}=\overline{\Pi_{1}^{\natural}}=\overline{\Pi_{2}}=\Pi_{2}$ and $\Pi_{2}^{*}=\Pi_{1}$, the star exchanging the two as the natural sign does. The flat is $-{}^{*}$, so it sends $\Pi_{i}$ to the negative of the other idempotent.

**Corollary (the involution swaps the two lines).** The natural sign restricts to a $\mathbb{C}$-linear exchange of the two idempotent lines, $\mathbb{C}\Pi_{1}\leftrightarrow\mathbb{C}\Pi_{2}$, and the two lines are therefore conjugate under the intrinsic conjugate.

## The Halving Map

**The map $T\mapsto\tfrac12(1+T)$ sends the roots of one bijectively to the idempotents, and its inverse on the idempotents is $e\mapsto 2e-1$.**

**Theorem (the halving map).** The map
$$
H(T)=\tfrac12(1+T)
$$
restricts to a bijection from the roots of one $\{1,-1,j,-j\}$ onto the idempotents $\{0,1,\Pi_{1},\Pi_{2}\}$, with
$$
H(1)=1,\qquad H(-1)=0,\qquad H(j)=\Pi_{1},\qquad H(-j)=\Pi_{2},
$$
and the inverse on the idempotents is $e\mapsto 2e-1$.

*Proof.* The four values are direct: $\tfrac12(1+1)=1$, $\tfrac12(1-1)=0$, $\tfrac12(1+j)=\Pi_{1}$, $\tfrac12(1-j)=\Pi_{2}$. If $T^{2}=1$ then $H(T)^{2}=\tfrac14(1+2T+T^{2})=\tfrac14(2+2T)=H(T)$, so $H$ maps roots of one into idempotents; if $e^{2}=e$ then $2e-1$ has $(2e-1)^{2}=4e^{2}-4e+1=1$, so $2e-1$ is a root of one; and the two maps are inverse, since $H(2e-1)=\tfrac12(1+2e-1)=e$.

**Remark (the classical form of the correspondence).** The correspondence between the roots of one and the idempotents by halving is the classical correspondence between an involution and the projection it carries; here it reads the two nontrivial idempotents as the halves of the sum and the difference of the identity and the two nontrivial roots $j$ and $-j$.

## Summary

The roots of one of the general plain algebra are the four elements
$$
1,\quad -1,\quad j,\quad -j,
$$
and they form a group isomorphic to $\mathbb{Z}_{2}\times\mathbb{Z}_{2}$ under the multiplication; they all lie in the real subalgebra $\mathbb{R}\{1,j\}$. The idempotents are the four elements
$$
0,\quad 1,\quad \Pi_{1}=\tfrac12(1+j),\quad \Pi_{2}=\tfrac12(1-j),
$$
solutions of $T^{2}=T$, and the two nontrivial ones are complementary, orthogonal and zero divisors,
$$
\Pi_{1}^{2}=\Pi_{1},\quad \Pi_{2}^{2}=\Pi_{2},\quad \Pi_{1}\Pi_{2}=0,\quad \Pi_{1}+\Pi_{2}=1 .
$$

Each idempotent $e$ carries the projection $P_{e}(T)=eT$, with $P_{\Pi_{1}}+P_{\Pi_{2}}=\mathrm{id}$, $P_{e}^{2}=P_{e}$ and $P_{\Pi_{1}}P_{\Pi_{2}}=0$; the explicit projections are $P_{\Pi_{1}}(C+Dj)=(C+D)\Pi_{1}$ and $P_{\Pi_{2}}(C+Dj)=(C-D)\Pi_{2}$, and they give the resolution of the identity and the decomposition $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_{1}\oplus\mathbb{C}\Pi_{2}$. The **natural sign** and the **star** both exchange the two nontrivial idempotents, $\Pi_{1}^{\natural}=\Pi_{2}=\Pi_{1}^{*}$ and $\Pi_{2}^{\natural}=\Pi_{1}=\Pi_{2}^{*}$, while only the bar fixes each idempotent, $\overline{\Pi_{i}}=\Pi_{i}$. The **halving map** $H(T)=\tfrac12(1+T)$ is a bijection from the roots of one onto the idempotents, with inverse $e\mapsto2e-1$, and it sends $-1$ to $0$, $j$ to $\Pi_{1}$ and $-j$ to $\Pi_{2}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $1,-1,j,-j$ | the four roots of one, a group $\mathbb{Z}_{2}\times\mathbb{Z}_{2}$ |
| $0,1,\Pi_{1},\Pi_{2}$ | the four idempotents |
| $\Pi_{1,2}=\tfrac12(1\pm j)$ | the two nontrivial idempotents |
| $P_{e}(T)=eT$ | the projection carried by an idempotent |
| $P_{\Pi_{1}}+P_{\Pi_{2}}=\mathrm{id}$ | the resolution of the identity |
| $\mathbb{C}\Pi_{1}\oplus\mathbb{C}\Pi_{2}$ | the direct sum, the Peirce lines |
| $H(T)=\tfrac12(1+T)$ | the halving map from the roots of one to the idempotents |
| $e\mapsto2e-1$ | the inverse halving map |

## Further Reading

- *Introduction to the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/introduction-to-the-general-plain-algebra-of-the-reduced-biquaternions.md`), above this article in this category, for the algebra and the idempotent coordinates.
- *The Two Involutions and the Group of Involutions* (`articles_maths/the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions.md`), above this article, for the action of the four maps on the idempotents.
- *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), above this article, for the two lines the idempotents generate.
- *Annihilators of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/annihilators-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), above this article, for the annihilators of the idempotent lines.
- *Square Roots of Zero and the Nilpotents of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), below this article, for the companion equation $T^{2}=0$.
- *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), below this article in this category, for the full Peirce decomposition.
- *Square Roots of One and the Idempotents of the Biquaternion Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.md`), the non-commutative counterpart, where the roots of one and the idempotents form larger families.
