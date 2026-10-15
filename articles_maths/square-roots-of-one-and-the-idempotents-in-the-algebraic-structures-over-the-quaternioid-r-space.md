# __Square Roots of One and the Idempotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space__

## Introduction

Let $\star$ be a product on the quaternion algebra $\mathbb{H}$. An element $\tilde\xi$ is a **root of the central value** $e_0$ when its square in that product is the value,

$$
\tilde\xi\star\tilde\xi=e_0 ,
$$

and the **root set of $+1$** is the set of its solutions. An element $\tilde\pi$ is an **idempotent** of the same product when

$$
\tilde\pi\star\tilde\pi=\tilde\pi .
$$

The two equations name one product and one square operator, and the space carries six products; this article answers both questions once for all six, and reads them together because the idempotent set is the root set of $+1$ carried by one map, the halving map $\tilde\pi=\tfrac12(e_0+\tilde\xi)$. The idempotent architecture rests on the roots of $+1$ alone.

The value $e_0$ is central, the centre of the quaternion algebra over $\mathbb{R}$ being the real line, so it is the value $\lambda e_0$ at $\lambda=+1$. The other signed value, $\lambda=-1$, is not a second subject: its root set is a single closing remark at the end of §*The Roots of One in the Six Structures*, quoted nowhere else in the article. The value $0$, the square-zero elements and the nilpotents are *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the general value $\lambda$, the two squares and the six-row table of general $\lambda$ are *Square Roots of a General Element in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, the companion article.

**The six names.** The space carries six products, each with a three-letter code: the first letter is the operation, $\mathrm G$ the general product and $\mathrm S$, $\mathrm A$ its symmetric and antisymmetric parts; the second is the product of the family, $\mathrm P$ the plain one and $\mathrm Q$ the quaternionic one, whose first slot is read through the natural conjugation; and the third letter is the same one for the six, $\mathrm A$ the algebra over $\mathbb{R}$. The six are read in the three halves of *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space*,

| the half | the plain algebra | the quaternionic algebra |
|---|---|---|
| general | $\mathrm{GPA}$ | $\mathrm{GQA}$ |
| symmetric | $\mathrm{SPA}$ | $\mathrm{SQA}$ |
| antisymmetric | $\mathrm{APA}$ | $\mathrm{AQA}$ |

and every table of the article follows this order, half by half and, inside a half, the plain structure then the quaternionic one.

**Scope and owners.** This article owns the comparison of the six root sets of $+1$ and of the six idempotent sets, the unit theorem for a root of $+1$, the halving map between the two questions, and the reading of the collapse against the biquaternion case. The per-structure results stay owned by their articles, cited one by one below: the root sets of the six structures by the six *Square Roots of Minus One, Zero and Plus One in the …* of the chapter, and the idempotent sets by the six *Idempotents of the …*. The products are *The 6 Products of the Quaternion Real Space* and *The Two General Products of the Quaternion $\mathbb{R}$ Space*; the structures and the codes are *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the vocabulary stated once for a general product, the root of a central value and the idempotent, is *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the two forms are *The 2 Forms over the Quaternion $\mathbb{R}$ Space*; the value $0$ and the square-zero sets are *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the zero divisors and the unit criterion $N\neq0$ are *Zero Divisors in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the division property of the plain product is *Norm and Invertibility in the General Plain Algebra of Quaternions*; and the biquaternion case that §*The Contrast with the Biquaternion Case* reads is *Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**Conventions.** $\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_0=1$; a general element is $\tilde\xi=\xi_0e_0+\vec\xi$ with $\xi_0\in\mathbb{R}$ and $\vec\xi=\sum_k\xi_ke_k$; the natural conjugation is $\tilde\xi^{\natural}=\xi_0-\vec\xi$; the **plain form** is $B(\tilde\xi)=\xi_0^{2}-\lvert\vec\xi\rvert^{2}=\mathrm{Sc}(\tilde\xi^{2})$; and the **quaternion form** is $N(\tilde\xi)=\xi_0^{2}+\lvert\vec\xi\rvert^{2}=\mathrm{Sc}(\tilde\xi^{\natural}\tilde\xi)$, the norm. The plain product is $\tilde\xi\tilde\eta$, the quaternionic product is $\tilde\xi^{\natural}\tilde\eta$, the Jordan product is $\tilde\xi\bullet\tilde\eta=\tfrac12(\tilde\xi\tilde\eta+\tilde\eta\tilde\xi)$, the symmetrisation of the quaternionic product is the scalar-valued rule $N(\tilde\xi,\tilde\eta)e_0$, the plain cross product is $\tilde\xi\wedge\tilde\eta=\tfrac12(\tilde\xi\tilde\eta-\tilde\eta\tilde\xi)=\vec\xi\times\vec\eta$, and the quaternionic cross product is $\tilde\xi\wedge^{\natural}\tilde\eta=\tfrac12(\tilde\xi^{\natural}\tilde\eta-\tilde\eta^{\natural}\tilde\xi)$. The **square root of a central value** is defined in *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* §*The Element Vocabulary* as an element with $\tilde\xi^{2}=c$ and $c$ central, the class of them being the set of its solutions, with no non-zero requirement; the **idempotent** is defined in the same section as an element with $\tilde\pi^{2}=\tilde\pi$. The origin is therefore counted with the roots of $0$ wherever it solves the equation, and the places where an owner counts the non-zero roots alone are read as the origin alone.

## The Roots of One in the Six Structures

The square of a structure is its operation read at the two equal arguments, so each of the six carries a root problem of its own, and the six squares are three. They are the squares of *Square Roots of a General Element in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* §*The Two General Products at a General Value*, recalled here:

| the square | the structures | at the two equal arguments |
|---|---|---|
| the plain square | $\mathrm{GPA}$, $\mathrm{SPA}$ | $(\xi_0^{2}-\lvert\vec\xi\rvert^{2})e_0+2\xi_0\vec\xi$ |
| the central square | $\mathrm{GQA}$, $\mathrm{SQA}$ | $N(\tilde\xi)e_0$ |
| the vanishing square | $\mathrm{APA}$, $\mathrm{AQA}$ | $0$ |

**Definition.** The **root set of $+1$** in the structure $\star$ is

$$
\mathcal R_{+1}=\{\tilde\xi:\tilde\xi\star\tilde\xi=e_0\} .
$$

The value is signed, and the quaternion form decides the nature of every root, because the norm of a square is the square of the norm.

**Theorem (a root of $+1$ is a unit of the algebra).** Let $\tilde\xi$ be a root of $+1$ in one of the six structures. Then $N(\tilde\xi)=1$, the element is a unit of $\mathbb{H}$, and its inverse is $\tilde\xi^{-1}=\tilde\xi^{\natural}/N(\tilde\xi)$.

*Proof.* The square of the root is $e_0$, and the norm is multiplicative, $N(\tilde\xi^{2})=N(\tilde\xi)^{2}$, so $N(\tilde\xi)^{2}=N(e_0)=1$ and $N(\tilde\xi)=1$. The criterion of invertibility of the algebra is $N\neq0$ and the two-sided inverse is $\tilde\xi^{\natural}/N(\tilde\xi)$ (*Zero Divisors in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*). The two antisymmetric structures have no root of $+1$ and the statement is empty for them.

The algebra is a division algebra, so it decomposes as

$$
\mathbb{H}=\{0\}\cup\mathbb{H}^{\times} , \qquad \mathcal R_{+1}\subseteq\mathbb{H}^{\times} ,
$$

with no zero-divisor term, the plain product having no zero divisor at all (*Zero Divisors in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*). The roots of $+1$ are therefore the units at which the square reaches the unit.

**Theorem (the root sets of $+1$; quoted).** Among the six structures of the quaternion real space the root set of $+1$ is the pair $\pm e_0$ for the two plain structures, the unit sphere $S^{3}$ of real dimension three for the two quaternionic structures, and the empty set for the two antisymmetric structures.

*Proof.* The plain square is the plain form on the scalar part and twice the product $\xi_0\vec\xi$ on the vector part; the central square is the quaternion form; and the vanishing square is zero. The three readings are below.

The six are read one by one; each names the product, its square and its root set of $+1$, and cites the article that owns them.

### $\mathrm{GPA}$, the general plain algebra

The product is $\tilde\xi\tilde\eta$ and its square is the plain square, of scalar part $B(\tilde\xi)=\xi_0^{2}-\lvert\vec\xi\rvert^{2}$ and vector part $2\xi_0\vec\xi$. The equation $\tilde\xi^{2}=e_0$ is the pair $B(\tilde\xi)=1$, $2\xi_0\vec\xi=0$: the second equation forces $\xi_0=0$ or $\vec\xi=0$, the pure branch gives $-\lvert\vec\xi\rvert^{2}=1$, which is empty, and the central branch gives $\xi_0^{2}=1$ and the two roots $\tilde\xi=\pm e_0$. The root set of $+1$ is the pair $\pm e_0$, the centre of the unit sphere of the algebra. The article is *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde\xi^{\natural}\tilde\eta$, and its square is the central element $N(\tilde\xi)e_0$, so the root problem is the single real equation $N(\tilde\xi)=1$, whose solutions form the unit sphere $S^{3}$ of real dimension three. The article is *Square Roots of One and the Idempotents of the General Quaternionic Algebra*.

### $\mathrm{SPA}$, the symmetric plain algebra

The product is the Jordan product $\tilde\xi\bullet\tilde\eta=\tfrac12(\tilde\xi\tilde\eta+\tilde\eta\tilde\xi)$, and its square is the plain square, $\tilde\xi\bullet\tilde\xi=\tilde\xi^{2}$, so the root set of $+1$ is that of $\mathrm{GPA}$ element for element: the pair $\pm e_0$, although the Jordan structure is not associative. The article is *Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Algebra*.

### $\mathrm{SQA}$, the symmetric quaternionic algebra

The product is the symmetrisation $\tfrac12(\tilde\xi^{\natural}\tilde\eta+\tilde\eta^{\natural}\tilde\xi)=N(\tilde\xi,\tilde\eta)e_0$, the quaternion form read as a product, and its square is the definite form, $\tilde\xi\star\tilde\xi=N(\tilde\xi)e_0$. The root set of $+1$ is the same unit sphere $S^{3}$, the group of the unit quaternions. The article is *Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Algebra*.

### $\mathrm{APA}$, the antisymmetric plain algebra

The product is the commutator $\tilde\xi\wedge\tilde\eta=\vec\xi\times\vec\eta$, the cross product of the two vector parts. It is alternating, so at the two equal arguments it vanishes, $\tilde\xi\wedge\tilde\xi=0$, and the equation reduces to $0=e_0$. The root set of $+1$ is empty. The article is *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Algebra*.

### $\mathrm{AQA}$, the antisymmetric quaternionic algebra

The product is the commutator $\tilde\xi\wedge^{\natural}\tilde\eta=\tfrac12(\tilde\xi^{\natural}\tilde\eta-\tilde\eta^{\natural}\tilde\xi)$, alternating, so $\tilde\xi\wedge^{\natural}\tilde\xi=0$ and the equation reduces to $0=e_0$. The root set of $+1$ is empty. The article is *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Quaternionic Algebra*.

**The two general products at $+1$.** At the value $+1$ the plain product has the pair $\pm e_0$ and the quaternionic product the sphere $S^{3}$, and the two root sets differ.

**The word is *differ*, not *coincide*.** The zero-divisor sets of the two general products are one set read twice, the empty set, the algebra being a division algebra; their root sets at $+1$ are two different sets. The reason is the one on which the whole chapter turns: the two general products read the same norm, and the zero-divisor criterion is the norm, but their squares are $B$ and $N$ on the vector subspace and the two differ by a sign, so the values at which the squares reach the unit are not the same values.

**The two families of the plain reduction.** The reduction of the plain square is the vanishing of the vector part, $2\xi_0\vec\xi=0$, and the two factors give the two families of the plain family.

**Definition.** An element is **pure** when its scalar part vanishes, $\xi_0=0$, and **central** when its vector part vanishes, $\vec\xi=0$.

| | pure, $\xi_0=0$ | central, $\xi_0\neq0$ |
|---|---|---|
| the reduction $2\xi_0\vec\xi=0$ | satisfied identically | forces $\vec\xi=0$ |
| a root of $+1$ | none | the pair $\pm e_0$ |
| the dimension | $3$ | $1$ |

The root of $+1$ of the plain family lies in the centre, where the reduction has already forced the vector part to vanish, and the pure family carries none of them.

**The roots of $-1$.** The other signed value is quoted here once and used nowhere else. The sign does not flip by a central scalar: the centre of $\mathbb{H}$ is the real line, which contains no element of square $-1$, so there is no central imaginary to multiply a root of $+1$ by, and the two signed root sets are read from the squares directly. In the plain family the pure branch of the plain square is the negative-definite form, so the root set of $-1$ is the pure unit sphere $S^{2}$ of the complex structures, of real dimension two, disjoint from the central pair $\pm e_0$ that is the root set of $+1$; the two signed root sets of the plain family are therefore read on the two different branches of the one square, the pure branch at $-1$ and the central branch at $+1$. In the quaternionic family the square is $N(\tilde\xi)e_0$ with $N\geq0$, and in the two antisymmetric structures the square vanishes, so in those four structures the root set of $-1$ is empty.

## The Idempotents in the Six Structures

An idempotent is an element equal to its own square, the equation naming a product, and the six structures answer it with two sets alone. The reading is coarse because the real field has no scalar imaginary and the plain form has no real isotropic direction: the two-parameter and four-parameter families of the biquaternion plain product collapse to the trivial pair.

**Definition.** The **idempotent set** of a structure $\star$ is the set of the solutions of $\tilde\pi\star\tilde\pi=\tilde\pi$, and an **idempotent** is a member of it. The equation is the one of *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, read in the product of the structure.

### The Halving Map from the Roots of One to the Idempotents

A root of $+1$ and an idempotent are two readings of one element when $e_0$ is a two-sided unit of the product, and the map is the halving map $\tilde\pi=\tfrac12(e_0+\tilde\xi)$, with the inverse $\tilde\xi=2\tilde\pi-e_0$. Expanding the square of the halved element,

$$
\tilde\pi\star\tilde\pi=\tfrac14\bigl(e_0\star e_0+e_0\star\tilde\xi+\tilde\xi\star e_0+\tilde\xi\star\tilde\xi\bigr) ,
$$

so that a two-sided unit, $e_0\star e_0=e_0$ and $e_0\star\tilde\xi=\tilde\xi=\tilde\xi\star e_0$, together with $\tilde\xi\star\tilde\xi=e_0$, gives

$$
\tilde\pi\star\tilde\pi=\tfrac14\bigl(2e_0+2\tilde\xi\bigr)=\tfrac12(e_0+\tilde\xi)=\tilde\pi .
$$

The map is therefore a bijection of the root set of $+1$ onto the idempotent set wherever $e_0$ is a two-sided unit, that is for the two plain structures, where it pairs the roots $\pm e_0$ of $+1$ with the idempotents $e_0$ and $0$; the inverse $\tilde\xi=2\tilde\pi-e_0$ reads an idempotent as a root of $+1$.

**For the quaternionic family the map is not a bijection, and the idempotent set is read from the central equation.** There the unit $e_0$ is a left unit alone, $\tilde\xi\star e_0=\tilde\xi^{\natural}$, and the same expansion gives

$$
\tilde\pi\star\tilde\pi=\tfrac14\bigl(2e_0+\tilde\xi+\tilde\xi^{\natural}\bigr)=\tfrac12e_0+\tfrac12\xi_0e_0 \qquad\text{against}\qquad \tilde\pi=\tfrac12e_0+\tfrac12\tilde\xi ,
$$

equal exactly when $\tilde\xi=\xi_0e_0$ is central. Of the sphere of roots of $+1$ only the two central points $\pm e_0$ are carried to idempotents, and the two-point set is read directly from the idempotent equation, which is central there.

**Theorem (the six idempotent sets; quoted).** Among the six structures of the quaternion real space the idempotents are $\{0,e_0\}$ for $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{SPA}$ and $\mathrm{SQA}$, and $\{0\}$ for $\mathrm{APA}$ and $\mathrm{AQA}$. Only two idempotent sets occur, the origin belongs to both, and no nontrivial idempotent exists except the unit $e_0$ of the four non-alternating structures.

*Proof.* For the general plain structure, $\tilde\pi^{2}=\tilde\pi$ reads $\tilde\pi(\tilde\pi-e_0)=0$; the plain algebra is a division algebra, so $\tilde\pi=0$ or $\tilde\pi=e_0$. For the general quaternionic structure, $\tilde\pi^{\natural}\tilde\pi=N(\tilde\pi)e_0=\tilde\pi$ puts $\tilde\pi$ in the scalar line, and the scalar equation $s^{2}=s$ gives $s\in\{0,1\}$. The symmetric plain structure has the plain square on the diagonal, $\tilde\pi\bullet\tilde\pi=\tilde\pi^{2}$, so its equation is the same as the general plain one and its set is the same; the symmetric quaternionic structure has the square $N(\tilde\pi)e_0$, so its equation is the same as the general quaternionic one. The two cross products are alternating, so $\tilde\pi\wedge\tilde\pi=0$ and $\tilde\pi\wedge^{\natural}\tilde\pi=0$ for every element, and the idempotent equation reads $\tilde\pi=0$.

The classification is sharp, and it reads the two ways a square operator can be too coarse to have a nontrivial solution. The **alternating** square vanishes identically, so it destroys the equation and leaves the origin; the **definite scalar** square and the **plain** square vanish only at the origin, so the only solutions are the two idempotents of the scalar field, $0$ and $1$, read on the scalar line. The unit enters the equation because the square of $e_0$ is $e_0$ in the four structures that are not alternating, and it does not for the two cross products: $e_0\wedge e_0=0\neq e_0$.

The six are read one by one below; each names the product, its square and its idempotent set, and cites the article that owns them.

### $\mathrm{GPA}$, the general plain algebra

The product is $\tilde\pi\tilde\eta$, and its square is the plain square, of scalar part $B(\tilde\pi)=\pi_0^{2}-\lvert\vec\pi\rvert^{2}$ and vector part $2\pi_0\vec\pi$. The idempotents are $0$ and $e_0$ alone: the equation $\tilde\pi(\tilde\pi-e_0)=0$ meets the division property of the plain algebra, and no isotropic direction of the plain form is real. The article is *Idempotents of the General Plain Algebra*.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde\pi^{\natural}\tilde\eta$, and its square is the central element $N(\tilde\pi)e_0$; an idempotent is therefore central, $\tilde\pi=se_0$, and the equation on the centre, $s^{2}=s$, leaves $s\in\{0,1\}$. The idempotent set is the trivial pair, the image under the halving map of the two central roots of $+1$. The article is *Square Roots of One and the Idempotents of the General Quaternionic Algebra*.

### $\mathrm{SPA}$, the symmetric plain algebra

The product is the Jordan product $\tilde\pi\bullet\tilde\eta$, and its square is the plain square, $\tilde\pi\bullet\tilde\pi=\tilde\pi^{2}$; the idempotent set is $\{0,e_0\}$, element for element that of $\mathrm{GPA}$, although the Jordan structure is not associative. The article is *Idempotents of the Symmetric Plain Algebra*.

### $\mathrm{SQA}$, the symmetric quaternionic algebra

The product is $N(\tilde\pi,\tilde\eta)e_0$, the quaternion form read as a product, and its square is the definite form, $\tilde\pi\star\tilde\pi=N(\tilde\pi)e_0$; the idempotent set is $\{0,e_0\}$, as for $\mathrm{GQA}$. The article is *Idempotents of the Symmetric Quaternionic Algebra*.

### $\mathrm{APA}$, the antisymmetric plain algebra

The product is the plain cross product $\tilde\pi\wedge\tilde\eta=\vec\pi\times\vec\eta$, alternating, so its square vanishes identically. The idempotent set is the origin alone, and $e_0$ is not an idempotent here. The article is *Idempotents of the Antisymmetric Plain Algebra*.

### $\mathrm{AQA}$, the antisymmetric quaternionic algebra

The product is the quaternionic cross product $\tilde\pi\wedge^{\natural}\tilde\eta$, alternating, so its square vanishes identically. The idempotent set is the origin alone. The article is *Idempotents of the Antisymmetric Quaternionic Algebra*.

**Remark (the sign of the square).** The two-point set is the set of idempotents of the scalar field $\mathbb{R}$, read on the scalar line, and the four structures inherit it because their square operator is the plain square or the definite scalar $N(\tilde\pi)e_0$, and neither has a real solution beyond the two. The pure elements, which are the zero divisors of the Jordan structure, have the square $-\lvert\vec\pi\rvert^{2}e_0$, of the wrong sign for a nontrivial idempotent: the construction $\tfrac12(e_0+\tilde\pi)$ gives an idempotent only if $\tilde\pi$ is a root of $+e_0$, and a pure vector squares to $-\lvert\vec\pi\rvert^{2}e_0$, which is $+e_0$ for no real $\vec\pi$. So the zero divisors of the Jordan structure carry no idempotent with them.

## Results

The two sets are collected below, the two general products are read at the value, and the collapse against the biquaternion case is read last.

### The Six Root Sets at $+1$

| the half | the structure | the square | the roots of $+1$ |
|---|---|---|---|
| the general products | $\mathrm{GPA}$ | $\tilde\xi^{2}$ | the pair $\pm e_0$ |
| | $\mathrm{GQA}$ | $N(\tilde\xi)e_0$ | the sphere $S^{3}$ of the unit quaternions, real dimension $3$ |
| the symmetric products | $\mathrm{SPA}$ | $\tilde\xi^{2}$ | the pair $\pm e_0$ |
| | $\mathrm{SQA}$ | $N(\tilde\xi)e_0$ | the sphere $S^{3}$ |
| the antisymmetric products | $\mathrm{APA}$ | $0$ | none |
| | $\mathrm{AQA}$ | $0$ | none |

Four structures have a root of $+1$, the pair $\pm e_0$ for the plain family and the sphere $S^{3}$ for the quaternionic family, and the failure of the other two is the vanishing of their square: the two alternating structures have no square to read, so no element is a root of a signed value. The pair $\pm e_0$ is the centre of the quaternionic sphere, and the sphere $S^{2}$ of the roots of $-1$ of §*The Roots of One in the Six Structures* is its twin at the other signed value.

### The Six Idempotent Sets

| structure | product | square of $\tilde\pi$ | idempotents |
|---|---|---|---|
| $\mathrm{GPA}$ | $\tilde\pi\tilde\eta$ | $(\pi_0^{2}-\lvert\vec\pi\rvert^{2})e_0+2\pi_0\vec\pi$ | $\{0,e_0\}$ |
| $\mathrm{GQA}$ | $\tilde\pi^{\natural}\tilde\eta$ | $N(\tilde\pi)e_0$ | $\{0,e_0\}$ |
| $\mathrm{SPA}$ | $\tilde\pi\bullet\tilde\eta$ | $(\pi_0^{2}-\lvert\vec\pi\rvert^{2})e_0+2\pi_0\vec\pi$ | $\{0,e_0\}$ |
| $\mathrm{SQA}$ | $N(\tilde\pi,\tilde\eta)e_0$ | $N(\tilde\pi)e_0$ | $\{0,e_0\}$ |
| $\mathrm{APA}$ | $\tilde\pi\wedge\tilde\eta$ | $0$ | $\{0\}$ |
| $\mathrm{AQA}$ | $\tilde\pi\wedge^{\natural}\tilde\eta$ | $0$ | $\{0\}$ |

Read down the last column, only two sets occur: the trivial pair $\{0,e_0\}$ for the four structures whose square is the plain square or the definite scalar, and the origin alone $\{0\}$ for the two whose square vanishes identically. The origin is the common member, and the unit $e_0$ is an idempotent of the four and of no other. The symmetric structure of each family repeats the row of its general partner, the two squares agreeing on the diagonal.

### The Contrast with the Biquaternion Case

The idempotent theory is coarser over $\mathbb{R}$ than over $\mathbb{C}$ because the real field has no scalar imaginary and the plain form is anisotropic. The idempotents of the biquaternion plain product are the halved roots of $+e_0$, $\tilde\Pi=\tfrac12(e_0+\tilde\Theta)$ with $\tilde\Theta\star\tilde\Theta=e_0$, the root set of $+e_0$ there carrying a two-parameter family and a four-parameter family; over $\mathbb{R}$ the plain form has no real isotropic direction, so the root set of $+e_0$ of the plain family is the pair $\pm e_0$ alone and the halving map carries it to the two-point set.

| | the biquaternion space $\mathbb{B}$ | the quaternion space $\mathbb{H}$ |
|---|---|---|
| the plain product | $0$, $e_0$, the halved roots of $+e_0$: a two-parameter family and a four-parameter family | $0$ and $e_0$ alone |
| the two cross products | $0$ alone | $0$ alone |

In the biquaternion space the plain product has the idempotent $\tfrac12(e_0+\tilde\Theta)$ for every root $\tilde\Theta$ of $+e_0$, and the plain square therefore acquires a nontrivial idempotent for every isotropic direction; over $\mathbb{R}$ no isotropic direction of the plain form is real, so the equation $\tilde\pi^{2}=\tilde\pi$ has only its central solutions, $0$ and $e_0$, and the family of the biquaternion plain structure collapses to the two-point set. The collapse is the same one the chapter records for the roots of a central value, in *Square Roots of a General Element in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, where the four-parameter root sets of the biquaternion sesqualgebras fall to the origin alone over $\mathbb{R}$.

## Summary

A root of $+1$ is an element whose square in the structure is the unit $e_0$, and an idempotent is an element equal to its own square. The two questions are read on the same square operator and answered once for the six structures of the quaternion real space.

A root of $+1$ has $N=1$ and is a unit of the algebra, with the two-sided inverse $\tilde\xi^{\natural}/N(\tilde\xi)$. The plain family, the general plain and the symmetric plain structures, has the pair $\pm e_0$ as its root set of $+1$; the quaternionic family, the general quaternionic and the symmetric quaternionic structures, has the unit sphere $S^{3}$ of real dimension three; and the two antisymmetric structures have none, their square vanishing identically. The two general products differ at the value $+1$: the plain product reads the central pair and the quaternionic product the sphere, one sign of the vector part apart. The roots of $-1$ are a closing remark: over $\mathbb{R}$ there is no central imaginary to flip the sign, the plain family has the pure unit sphere $S^{2}$ of the complex structures, and the quaternionic and the two antisymmetric structures have no root of $-1$.

The idempotents answer with two sets alone. The four structures whose square is the plain square or the definite scalar $N(\tilde\pi)e_0$ have the two-point set $\{0,e_0\}$, the origin and the unit; the two cross products have the origin alone, their square vanishing identically, so that $e_0$ is not an idempotent for them. The halving map $\tilde\pi=\tfrac12(e_0+\tilde\xi)$, with the inverse $\tilde\xi=2\tilde\pi-e_0$, is a bijection of the roots of $+1$ onto the idempotents for the two plain structures, where $e_0$ is a two-sided unit, and for the quaternionic family it carries only the two central roots $\pm e_0$, the idempotent set being read from the central equation. The theory is coarser than over the biquaternion complex space because the real field has no scalar imaginary and the plain form has no real isotropic direction: the biquaternion plain product carries a two-parameter family and a four-parameter family of nontrivial idempotents, and the quaternion plain product carries neither, though both have the same two cross products with the origin alone.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\xi\star\tilde\xi=e_0$ | the root equation of the value $+1$ in the structure $\star$ |
| $\mathcal R_{+1}$ | the root set of $+1$ |
| $\tilde\pi\star\tilde\pi=\tilde\pi$ | the idempotent equation of the structure $\star$ |
| $\tilde\pi=\tfrac12(e_0+\tilde\xi)$, $\tilde\xi=2\tilde\pi-e_0$ | the halving map and its inverse |
| $\pm e_0$ | the roots of $+1$ of $\mathrm{GPA}$ and $\mathrm{SPA}$ |
| $S^{3}$ | the roots of $+1$ of $\mathrm{GQA}$ and $\mathrm{SQA}$, the unit sphere of the space, real dimension three |
| $S^{2}$ | the roots of $-1$ of the plain family, the sphere of the pure unit quaternions, real dimension two |
| $\{0,e_0\}$ | the idempotents of $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{SPA}$ and $\mathrm{SQA}$ |
| $\{0\}$ | the idempotents of $\mathrm{APA}$ and $\mathrm{AQA}$ |
| $B(\tilde\xi)=\xi_0^{2}-\lvert\vec\xi\rvert^{2}$ | the plain form, the scalar part of the plain square |
| $N(\tilde\xi)=\xi_0^{2}+\lvert\vec\xi\rvert^{2}$ | the quaternion form, the square of the quaternionic family, and the norm |
| $\mathrm{GPA},\dots,\mathrm{AQA}$ | the six structures of the space, the two general products and their four parts |

## Further Reading

- *Square Roots of a General Element in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/square-roots-of-a-general-element-in-the-algebraic-structures-over-the-quaternioid-r-space.md`), the companion of this article, for the root equation at a general central value, the six squares and the six-row table.
- *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the roots of the value $0$ and the square-zero elements.
- *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-algebraic-structures-over-the-quaternioid-r-space.md`), for the six names, the class of each and the two laws of the table.
- *The 6 Products of the Quaternion Real Space* (`articles_maths/the-6-products-of-the-quaternioid-real-space.md`), for the six products and their coordinates.
- *The Two General Products of the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-two-general-products-of-the-quaternioid-r-space.md`), for the plain product and the quaternionic product, whose signs the two signed values read.
- *The 2 Forms over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternioid-r-space.md`), for the plain form $B$ of signature $(1,3)$ and the definite quaternion form $N$.
- *Zero Divisors in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/zero-divisors-in-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the empty zero-divisor set of the two general products and the inverse criterion $N\neq0$.
- *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the root of a central value, the idempotent and the general vocabulary.
- The six owners, for the per-structure results: *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra-of-quaternions.md`), *Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-symmetric-plain-algebra-of-quaternions.md`), *Square Roots of One and the Idempotents of the Antisymmetric Plain Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-antisymmetric-plain-algebra-of-quaternioid.md`) and *Square Roots of Zero and the Nilpotents of the Antisymmetric Plain Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-antisymmetric-plain-algebra-of-quaternioid.md`), *Square Roots of One and the Idempotents of the General Quaternionic Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-quaternionic-algebra-of-quaternioid.md`) and *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Quaternionic Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-antisymmetric-quaternionic-algebra-of-quaternioid.md`), the symmetric block being the merged pair *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-symmetric-quaternionic-algebra-of-quaternioid.md`) and *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-symmetric-quaternionic-algebra-of-quaternioid.md`); and *Idempotents of the General Plain Algebra* (`articles_maths/idempotents-of-the-general-plain-algebra-of-quaternions.md`), *Idempotents of the Symmetric Plain Algebra* (`articles_maths/idempotents-of-the-symmetric-plain-algebra-of-quaternions.md`), *Square Roots of One and the Idempotents of the Antisymmetric Plain Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-antisymmetric-plain-algebra-of-quaternioid.md`), *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-general-quaternionic-algebra-of-quaternioid.md`) and *Idempotents of the Antisymmetric Quaternionic Algebra* (`articles_maths/idempotents-of-the-antisymmetric-quaternionic-algebra-of-quaternioid.md`), the symmetric block's idempotents being read in the merged *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-symmetric-quaternionic-algebra-of-quaternioid.md`).
