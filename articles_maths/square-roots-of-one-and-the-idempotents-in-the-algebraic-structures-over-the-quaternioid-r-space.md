# __Square Roots of One and the Idempotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space__

## Introduction

Let $\star$ be a product on the quaternion space $\mathbb{H}$. An element $\tilde\xi$ is a **root of the central value** $e_t$ when its square in that product is the value,

$$
\tilde\xi\star\tilde\xi=e_t ,
$$

and the **root set of $+1$** is the set of its solutions. An element $\tilde\pi$ is an **idempotent** of the same product when

$$
\tilde\pi\star\tilde\pi=\tilde\pi .
$$

The two equations name one product and one square operator. Beside the algebra product $\tilde q_1\tilde q_2$ of the *Quaternions* category, the space carries the three companion structures of this category, and this article answers both questions once for the three, reading them together because the idempotent set is the root set of $+1$ carried by one map, the halving map $\tilde\pi=\tfrac12(e_t+\tilde\xi)$. The idempotent architecture rests on the roots of $+1$ alone. The algebra product is named once for the contrast and cited, not restated.

The value $e_t$ is central, the centre of the quaternion space over $\mathbb{R}$ being the real line, so it is the value $\lambda e_t$ at $\lambda=+1$. The other signed value, $\lambda=-1$, is not a second subject: its root set is a single closing remark at the end of §*The Roots of One in the Three Companion Structures*, quoted nowhere else in the article. The value $0$, the square-zero elements and the nilpotents are *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*; the general value $\lambda$ is *Square Roots of a General Element in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, the companion article.

**The three companion structures.** The companion products of *The 6 Products of the Quaternioid Real Space* carry three structures, named in *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*:

$$
\mathrm{SPA} , \qquad \mathrm{APA} , \qquad \mathrm{GQA} ,
$$

the **symmetric plain algebra** of the Jordan product $\tilde\xi\bullet\tilde q=\tfrac12(\tilde\xi\tilde q+\tilde q\tilde\xi)$, the **antisymmetric plain algebra** of the cross product $\tilde\xi\wedge\tilde q=\vec\xi\times\vec q$, and the **general quaternionic algebra** of the product $\tilde\xi^{\natural}\tilde q$. Every table of the article follows this order.

**Scope and owners.** This article owns the comparison of the three root sets of $+1$ and of the three idempotent sets, the unit theorem for a root of $+1$, the halving map between the two questions, and the reading of the collapse against the biquaternion case. The per-structure results stay owned by their articles, cited one by one below: for the general quaternionic algebra *Square Roots of One and the Idempotents of the General Quaternionic Algebra*, for the symmetric plain algebra *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, and for the antisymmetric plain algebra *Introduction to the Antisymmetric Plain Algebra*; the algebra-product results are owned by *Square Roots of One and the Idempotents of the Quaternion Algebra* in the *Quaternions* category. The products are *The 6 Products of the Quaternioid Real Space*; the vocabulary stated once for a general product, the root of a central value and the idempotent, is *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*; the two forms are *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*; the value $0$ and the square-zero sets are *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*; the zero divisors and the unit criterion $N\neq0$ are *Zero Divisors in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*; and the biquaternion case that §*The Contrast with the Biquaternion Case* reads is *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**Conventions.** $\mathbb{H}$ has basis $e_t,\vec e_x,\vec e_y,\vec e_z$ with $e_t=1$; a general element is $\tilde\xi=\xi_te_t+\vec\xi$ with $\xi_t\in\mathbb{R}$ and $\vec\xi=\sum_k\xi_k\vec e_k$; the natural conjugation is $\tilde\xi^{\natural}=\xi_t-\vec\xi$; the **plain form** is $\langle\tilde\xi\rangle=\xi_t^{2}-\lvert\vec\xi\rvert^{2}=\mathrm{Sc}(\tilde\xi^{2})$; and the **quaternion form** is $\langle\tilde\xi\rangle_{\natural}=\xi_t^{2}+\lvert\vec\xi\rvert^{2}=\mathrm{Sc}(\tilde\xi^{\natural}\tilde\xi)$, the norm. The algebra product is $\tilde\xi\tilde q$, the general quaternionic product is $\tilde\xi^{\natural}\tilde q$, the Jordan product is $\tilde\xi\bullet\tilde q=\tfrac12(\tilde\xi\tilde q+\tilde q\tilde\xi)$, and the plain cross product is $\tilde\xi\wedge\tilde q=\tfrac12(\tilde\xi\tilde q-\tilde q\tilde\xi)=\vec\xi\times\vec q$. The **square root of a central value** is defined in *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* §*The Element Vocabulary* as an element with $\tilde\xi^{2}=c$ and $c$ central, the class of them being the set of its solutions, with no non-zero requirement; the **idempotent** is defined in the same section as an element with $\tilde\pi^{2}=\tilde\pi$.

## The Roots of One in the Three Companion Structures

The square of a structure is its operation read at the two equal arguments, so each of the three carries a root problem of its own, and the three squares are two. They are read off the squares of *Square Roots of a General Element in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* §*The Two General Products at a General Value*, recalled here:

| the square | the structure | at the two equal arguments |
|---|---|---|
| the plain square | $\mathrm{SPA}$ | $(\xi_t^{2}-\lvert\vec\xi\rvert^{2})e_t+2\xi_t\vec\xi$ |
| the central square | $\mathrm{GQA}$ | $\langle\tilde\xi\rangle_{\natural}e_t$ |
| the vanishing square | $\mathrm{APA}$ | $0$ |

The algebra product of the space carries the plain square as well, and that reading is owned by the *Quaternions* category.

**Definition.** The **root set of $+1$** in the structure $\star$ is

$$
\mathcal R_{+1}=\{\tilde\xi:\tilde\xi\star\tilde\xi=e_t\} .
$$

The value is signed, and the quaternion form decides the nature of every root, because the norm of a square is the square of the norm.

**Theorem (a root of $+1$ is a unit of the algebra).** Let $\tilde\xi$ be a root of $+1$ in one of the three companion structures. Then $\langle\tilde\xi\rangle_{\natural}=1$, the element is a unit of $\mathbb{H}$, and its two-sided inverse is $\tilde\xi^{-1}=\tilde\xi^{\natural}/\langle\tilde\xi\rangle_{\natural}$.

*Proof.* The square of the root is $e_t$, and the norm is multiplicative, $\langle\tilde\xi^{2}\rangle_{\natural}=\langle\tilde\xi\rangle_{\natural}^{2}$, so $\langle\tilde\xi\rangle_{\natural}^{2}=\langle e_t\rangle_{\natural}=1$ and $\langle\tilde\xi\rangle_{\natural}=1$. The criterion of invertibility of the algebra is $N\neq0$ and the two-sided inverse is $\tilde\xi^{\natural}/\langle\tilde\xi\rangle_{\natural}$ (*Norm and Invertibility in the Quaternion Algebra*, *Zero Divisors in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*). The antisymmetric plain structure has no root of $+1$ and the statement is empty for it.

The algebra is a division algebra, so it decomposes as

$$
\mathbb{H}=\{0\}\cup\mathbb{H}^{\times} , \qquad \mathcal R_{+1}\subseteq\mathbb{H}^{\times} ,
$$

with no zero-divisor term, the algebra product having no zero divisor at all (*Zero Divisors of the Quaternion Algebra*). The roots of $+1$ are therefore the units at which the square reaches the unit.

**Theorem (the root sets of $+1$).** Among the three companion structures the root set of $+1$ is the pair $\pm e_t$ for the symmetric plain algebra, the unit sphere $S^{3}$ of real dimension three for the general quaternionic algebra, and the empty set for the antisymmetric plain algebra. The algebra product of the same space has the pair $\pm e_t$, and that reading is owned by the *Quaternions* category.

*Proof.* The plain square is the plain form on the scalar part and twice the product $\xi_t\vec\xi$ on the vector part; the central square is the quaternion form; and the vanishing square is zero. The three readings are below.

The three are read one by one; each names the product, its square and its root set of $+1$, and cites the article that owns them.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde\xi^{\natural}\tilde q$, and its square is the central element $\langle\tilde\xi\rangle_{\natural}e_t$, so the root problem is the single real equation $\langle\tilde\xi\rangle_{\natural}=1$, whose solutions form the unit sphere $S^{3}$ of real dimension three, the group of the unit quaternions. The article is *Square Roots of One and the Idempotents of the General Quaternionic Algebra*.

### $\mathrm{SPA}$, the symmetric plain algebra

The product is the Jordan product $\tilde\xi\bullet\tilde q=\tfrac12(\tilde\xi\tilde q+\tilde q\tilde\xi)$, and its square is the plain square, $\tilde\xi\bullet\tilde\xi=\tilde\xi^{2}$, so the root set of $+1$ is the plain one: the equation $\tilde\xi^{2}=e_t$ is the pair $\langle\tilde\xi\rangle=1$, $2\xi_t\vec\xi=0$. The second equation forces $\xi_t=0$ or $\vec\xi=0$; the pure branch gives $-\lvert\vec\xi\rvert^{2}=1$, which is empty over $\mathbb{R}$, and the central branch gives $\xi_t^{2}=1$ and the two roots $\tilde\xi=\pm e_t$. The root set of $+1$ is the pair $\pm e_t$, although the Jordan structure is not associative. The article is *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*.

### $\mathrm{APA}$, the antisymmetric plain algebra

The product is the commutator $\tilde\xi\wedge\tilde q=\vec\xi\times\vec q$, the cross product of the two vector parts. It is alternating, so at the two equal arguments it vanishes, $\tilde\xi\wedge\tilde\xi=0$, and the equation reduces to $0=e_t$. The root set of $+1$ is empty. The article is *Introduction to the Antisymmetric Plain Algebra*.

**The algebra product and the general quaternionic product at $+1$.** At the value $+1$ the algebra product has the pair $\pm e_t$ and the general quaternionic product the sphere $S^{3}$, and the two root sets differ.

**The word is *differ*, not *coincide*.** The zero-divisor sets of the two are one set read twice, the empty set, the algebra being a division algebra; their root sets at $+1$ are two different sets. The reason is the one on which the whole chapter turns: the two products read the same norm, and the zero-divisor criterion is the norm, but their squares are $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural}$, which differ by a sign on the vector subspace, so the values at which the squares reach the unit are not the same values.

**The two families of the plain reduction.** The reduction of the plain square is the vanishing of the vector part, $2\xi_t\vec\xi=0$, and the two factors give the two families of the plain reduction.

**Definition.** An element is **pure** when its scalar part vanishes, $\xi_t=0$, and **central** when its vector part vanishes, $\vec\xi=0$.

| | pure, $\xi_t=0$ | central, $\xi_t\neq0$ |
|---|---|---|
| the reduction $2\xi_t\vec\xi=0$ | satisfied identically | forces $\vec\xi=0$ |
| a root of $+1$ | none | the pair $\pm e_t$ |
| the dimension | $3$ | $1$ |

The root of $+1$ of the plain square lies in the centre, where the reduction has already forced the vector part to vanish, and the pure family carries none of them.

**The roots of $-1$.** The other signed value is quoted here once and used nowhere else. The sign does not flip by a central scalar: the centre of $\mathbb{H}$ is the real line, which contains no element of square $-1$, so there is no central imaginary to multiply a root of $+1$ by, and the two signed root sets are read from the squares directly. For the plain square the pure branch is the negative-definite form, so the root set of $-1$ is the pure unit sphere $S^{2}$ of the complex structures, of real dimension two, disjoint from the central pair $\pm e_t$; the two signed root sets of the plain square are therefore read on the two different branches of the one square, the pure branch at $-1$ and the central branch at $+1$. The general quaternionic square is $\langle\tilde\xi\rangle_{\natural}e_t$ with $N\geq0$, and the antisymmetric square vanishes, so in these two companion structures the root set of $-1$ is empty.

## The Idempotents in the Three Companion Structures

An idempotent is an element equal to its own square, the equation naming a product, and the three companion structures answer it with two sets alone. The reading is coarse because the real field has no scalar imaginary and the plain form is negative definite on the vector subspace: the two-parameter and four-parameter families of the biquaternion plain product collapse to the trivial pair.

**Definition.** The **idempotent set** of a structure $\star$ is the set of the solutions of $\tilde\pi\star\tilde\pi=\tilde\pi$, and an **idempotent** is a member of it. The equation is the one of *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, read in the product of the structure.

### The Halving Map from the Roots of One to the Idempotents

A root of $+1$ and an idempotent are two readings of one element when $e_t$ is a two-sided unit of the product, and the map is the halving map $\tilde\pi=\tfrac12(e_t+\tilde\xi)$, with the inverse $\tilde\xi=2\tilde\pi-e_t$. Expanding the square of the halved element,

$$
\tilde\pi\star\tilde\pi=\tfrac14\bigl(e_t\star e_t+e_t\star\tilde\xi+\tilde\xi\star e_t+\tilde\xi\star\tilde\xi\bigr) ,
$$

so that a two-sided unit, $e_t\star e_t=e_t$ and $e_t\star\tilde\xi=\tilde\xi=\tilde\xi\star e_t$, together with $\tilde\xi\star\tilde\xi=e_t$, gives

$$
\tilde\pi\star\tilde\pi=\tfrac14\bigl(2e_t+2\tilde\xi\bigr)=\tfrac12(e_t+\tilde\xi)=\tilde\pi .
$$

The map is therefore a bijection of the root set of $+1$ onto the idempotent set wherever $e_t$ is a two-sided unit, that is for the symmetric plain algebra, where it pairs the roots $\pm e_t$ of $+1$ with the idempotents $e_t$ and $0$; the inverse $\tilde\xi=2\tilde\pi-e_t$ reads an idempotent as a root of $+1$. The same bijection holds for the algebra product, $e_t$ being its two-sided unit, and that reading is owned by the *Quaternions* category.

**For the general quaternionic algebra the map is not a bijection, and the idempotent set is read from the central equation.** There the unit $e_t$ is a left unit alone, $\tilde\xi\star e_t=\tilde\xi^{\natural}$, and the same expansion gives

$$
\tilde\pi\star\tilde\pi=\tfrac14\bigl(2e_t+\tilde\xi+\tilde\xi^{\natural}\bigr)=\tfrac12e_t+\tfrac12\xi_te_t \qquad\text{against}\qquad \tilde\pi=\tfrac12e_t+\tfrac12\tilde\xi ,
$$

equal exactly when $\tilde\xi=\xi_te_t$ is central. Of the sphere of roots of $+1$ only the two central points $\pm e_t$ are carried to idempotents, and the two-point set is read directly from the idempotent equation, which is central there.

**Theorem (the three idempotent sets).** Among the three companion structures the idempotents are $\{0,e_t\}$ for the symmetric plain algebra and for the general quaternionic algebra, and $\{0\}$ for the antisymmetric plain algebra. Only two idempotent sets occur, the origin belongs to both, and no nontrivial idempotent exists except the unit $e_t$ of the two non-alternating structures.

*Proof.* For the general quaternionic structure, $\tilde\pi^{\natural}\tilde\pi=\langle\tilde\pi\rangle_{\natural}e_t=\tilde\pi$ puts $\tilde\pi$ in the scalar line, and the scalar equation $s^{2}=s$ gives $s\in\{0,1\}$. The symmetric plain structure has the plain square on the diagonal, $\tilde\pi\bullet\tilde\pi=\tilde\pi^{2}$, and the equation $\tilde\pi^{2}=\tilde\pi$ reads $\tilde\pi(\tilde\pi-e_t)=0$; the algebra product is a division algebra, so $\tilde\pi=0$ or $\tilde\pi=e_t$ (*Zero Divisors of the Quaternion Algebra*), and the idempotent set is the same. The antisymmetric plain product is alternating, so $\tilde\pi\wedge\tilde\pi=0$ for every element and the idempotent equation reads $\tilde\pi=0$.

The classification is sharp, and it reads the two ways a square operator can be too coarse to have a nontrivial solution. The **alternating** square vanishes identically, so it destroys the equation and leaves the origin; the **definite scalar** square and the **plain** square vanish only at the origin, so the only solutions are the two idempotents of the scalar field, $0$ and $1$, read on the scalar line. The unit enters the equation because the square of $e_t$ is $e_t$ in the two non-alternating structures, and it does not for the cross product: $e_t\wedge e_t=0\neq e_t$.

The three are read one by one below; each names the product, its square and its idempotent set, and cites the article that owns them.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde\pi^{\natural}\tilde q$, and its square is the central element $\langle\tilde\pi\rangle_{\natural}e_t$; an idempotent is therefore central, $\tilde\pi=se_t$, and the equation on the centre, $s^{2}=s$, leaves $s\in\{0,1\}$. The idempotent set is the trivial pair, the image under the halving map of the two central roots of $+1$. The article is *Square Roots of One and the Idempotents of the General Quaternionic Algebra*.

### $\mathrm{SPA}$, the symmetric plain algebra

The product is the Jordan product $\tilde\pi\bullet\tilde q$, and its square is the plain square, $\tilde\pi\bullet\tilde\pi=\tilde\pi^{2}$; the idempotent set is $\{0,e_t\}$, the same two-point set as for the algebra product, although the Jordan structure is not associative. The article is *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*.

### $\mathrm{APA}$, the antisymmetric plain algebra

The product is the plain cross product $\tilde\pi\wedge\tilde q=\vec\pi\times\vec q$, alternating, so its square vanishes identically. The idempotent set is the origin alone, and $e_t$ is not an idempotent here. The article is *Introduction to the Antisymmetric Plain Algebra*.

**Remark (the sign of the square).** The two-point set is the set of idempotents of the scalar field $\mathbb{R}$, read on the scalar line, and the two non-alternating structures inherit it because their square operator is the plain square or the definite scalar $\langle\tilde\pi\rangle_{\natural}e_t$, and neither has a real solution beyond the two. The pure elements, which are the zero divisors of the Jordan structure, have the square $-\lvert\vec\pi\rvert^{2}e_t$, of the wrong sign for a nontrivial idempotent: the construction $\tfrac12(e_t+\tilde\pi)$ gives an idempotent only if $\tilde\pi$ is a root of $+e_t$, and a pure vector squares to $-\lvert\vec\pi\rvert^{2}e_t$, which is $+e_t$ for no real $\vec\pi$. So the zero divisors of the Jordan structure carry no idempotent with them.

## Results

The two sets are collected below, the algebra product and the general quaternionic product are read at the value, and the collapse against the biquaternion case is read last.

### The Three Root Sets at $+1$

| the structure | the square | the roots of $+1$ |
|---|---|---|
| $\mathrm{GQA}$ | $\langle\tilde\xi\rangle_{\natural}e_t$ | the sphere $S^{3}$ of the unit quaternions, real dimension $3$ |
| $\mathrm{SPA}$ | $\tilde\xi^{2}$ | the pair $\pm e_t$ |
| $\mathrm{APA}$ | $0$ | none |

Two companion structures have a root of $+1$, the pair $\pm e_t$ for the symmetric plain algebra and the sphere $S^{3}$ for the general quaternionic algebra, and the failure of the third is the vanishing of its square: the alternating structure has no square to read, so no element is a root of a signed value. The pair $\pm e_t$ is the centre of the quaternionic sphere. The algebra product has the pair $\pm e_t$, as owned by *Square Roots of One and the Idempotents of the Quaternion Algebra*.

### The Three Idempotent Sets

| the structure | the square | the idempotents |
|---|---|---|
| $\mathrm{GQA}$ | $\langle\tilde\pi\rangle_{\natural}e_t$ | $\{0,e_t\}$ |
| $\mathrm{SPA}$ | $\tilde\pi^{2}$ | $\{0,e_t\}$ |
| $\mathrm{APA}$ | $0$ | $\{0\}$ |

**Theorem (the two idempotent sets).** Among the three companion structures the idempotent set is $\{0,e_t\}$ for the two non-alternating structures and $\{0\}$ for the antisymmetric plain algebra.

*Proof.* The two non-alternating rows are the two subsections of §*The Idempotents in the Three Companion Structures*, and the alternating row completes the three.

### The Contrast with the Biquaternion Case

Over $\mathbb{C}$ the same questions have larger answers, and the difference is the field. The biquaternion plain product carries a two-parameter family and a four-parameter family of nontrivial idempotents, and its natural square vanishes on the whole zero-divisor cone; over $\mathbb{R}$ there is no scalar imaginary, so the plain form is negative definite on the vector subspace and the equation $\tilde\pi^{2}=\tilde\pi$ has only its central solutions, $0$ and $e_t$. The collapse is the same one the chapter records for the roots of a central value, in *Square Roots of a General Element in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, where the four-parameter root sets of the biquaternion sesqualgebras fall to the origin alone over $\mathbb{R}$.

## Summary

A root of $+1$ is an element whose square in the structure is the unit $e_t$, and an idempotent is an element equal to its own square. The two questions are read on the same square operator and answered once for the three companion structures of the quaternion real space.

A root of $+1$ has $\langle\cdot\rangle_{\natural}=1$ and is a unit of the algebra, with the two-sided inverse $\tilde\xi^{\natural}/\langle\tilde\xi\rangle_{\natural}$. The symmetric plain algebra has the pair $\pm e_t$ as its root set of $+1$; the general quaternionic algebra has the unit sphere $S^{3}$ of real dimension three; and the antisymmetric plain algebra has none, its square vanishing identically. The algebra product and the general quaternionic product differ at the value $+1$: the former reads the central pair and the latter the sphere, one sign of the vector part apart. The roots of $-1$ are a closing remark: over $\mathbb{R}$ there is no central imaginary to flip the sign, the plain square has the pure unit sphere $S^{2}$ of the complex structures, and the general quaternionic and the antisymmetric plain structures have no root of $-1$.

The idempotents answer with two sets alone. The two non-alternating structures have the two-point set $\{0,e_t\}$, the origin and the unit; the antisymmetric plain structure has the origin alone, its square vanishing identically, so that $e_t$ is not an idempotent for it. The halving map $\tilde\pi=\tfrac12(e_t+\tilde\xi)$, with the inverse $\tilde\xi=2\tilde\pi-e_t$, is a bijection of the roots of $+1$ onto the idempotents for the symmetric plain algebra, where $e_t$ is a two-sided unit, and for the general quaternionic algebra it carries only the two central roots $\pm e_t$, the idempotent set being read from the central equation. The theory is coarser than over the biquaternion complex space because the real field has no scalar imaginary and the plain form is negative definite on the vector subspace.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\xi\star\tilde\xi=e_t$ | the root equation of the value $+1$ in the structure $\star$ |
| $\mathcal R_{+1}$ | the root set of $+1$ |
| $\tilde\pi\star\tilde\pi=\tilde\pi$ | the idempotent equation of the structure $\star$ |
| $\tilde\pi=\tfrac12(e_t+\tilde\xi)$, $\tilde\xi=2\tilde\pi-e_t$ | the halving map and its inverse |
| $\pm e_t$ | the roots of $+1$ of $\mathrm{SPA}$, and of the algebra product |
| $S^{3}$ | the roots of $+1$ of $\mathrm{GQA}$, the unit sphere of the space, real dimension three |
| $S^{2}$ | the roots of $-1$ of the plain square, the sphere of the pure unit quaternions, real dimension two |
| $\{0,e_t\}$ | the idempotents of $\mathrm{GQA}$ and $\mathrm{SPA}$ |
| $\{0\}$ | the idempotents of $\mathrm{APA}$ |
| $\langle\tilde\xi\rangle=\xi_t^{2}-\lvert\vec\xi\rvert^{2}$ | the plain form, the scalar part of the plain square |
| $\langle\tilde\xi\rangle_{\natural}=\xi_t^{2}+\lvert\vec\xi\rvert^{2}$ | the quaternion form, the square of $\mathrm{GQA}$, and the norm |
| $\mathrm{SPA},\mathrm{APA},\mathrm{GQA}$ | the three companion structures of the space |

## Further Reading

- *Square Roots of a General Element in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/square-roots-of-a-general-element-in-the-algebraic-structures-over-the-quaternioid-r-space.md`), the companion of this article, for the root equation at a general central value and the three-row table.
- *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the roots of the value $0$ and the square-zero elements.
- *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/the-algebraic-structures-over-the-quaternioid-r-space.md`), for the three companion names and the class of each.
- *The 6 Products of the Quaternioid Real Space* (`articles_maths/the-6-products-of-the-quaternioid-real-space.md`), for the companion products and their coordinates.
- *The 2 Forms over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternioid-r-space.md`), for the plain form $\langle\cdot,\cdot\rangle$ of signature $(1,3)$ and the definite quaternion form $\langle\cdot,\cdot\rangle_{\natural}$.
- *Zero Divisors in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/zero-divisors-in-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the empty zero-divisor set of the general quaternionic product and the inverse criterion $N\neq0$.
- *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the root of a central value, the idempotent and the general vocabulary.
- *Square Roots of One and the Idempotents of the General Quaternionic Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-quaternionic-algebra.md`), for the per-structure result in the general quaternionic algebra.
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra* (`articles_maths/the-square-the-idempotents-and-the-jordan-inverse-of-the-symmetric-plain-algebra-of-quaternioid.md`), for the per-structure result in the symmetric plain algebra.
- *Introduction to the Antisymmetric Plain Algebra* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-quaternioid.md`), for the per-structure result in the antisymmetric plain algebra.
- *Square Roots of One and the Idempotents of the Quaternion Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-quaternion-algebra.md`), in the *Quaternions* category, for the algebra product.
