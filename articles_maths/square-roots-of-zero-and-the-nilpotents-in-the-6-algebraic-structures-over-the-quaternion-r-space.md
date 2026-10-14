# __Square Roots of Zero and the Nilpotents in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space__

## Introduction

Let $\star$ be a product on the quaternion algebra $\mathbb{H}$. An element $\tilde\xi$ is a **root of the central value** $0$ when its square in that product vanishes,

$$
\tilde\xi\star\tilde\xi=0 ,
$$

and the **root set of $0$** is the set of its solutions. The root set of $0$ is at once the **square-zero set** of the structure, and its nonzero members are the **square-zero elements**, or **nilpotents of index two**. The two names are one computation: this article reads the root set of $0$ of the six structures, and then reads the nilpotents, which are its nonzero members, together with the two other classes a nonzero square-zero element belongs to, the zero divisors and its own annihilations.

The value $0$ is central, the centre of the quaternion algebra over $\mathbb{R}$ being the real line, so it is the value $\lambda e_0$ at $\lambda=0$. The two signed values are the subject of *Square Roots of One and the Idempotents in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, where the value $+1$ and the idempotents are read and the value $-1$ is a closing remark; the general value $\lambda$, the two squares and the six-row table of general $\lambda$ are *Square Roots of a General Element in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*.

**The six names.** The space carries six products, each with a three-letter code: the first letter is the operation, $\mathrm G$ the general product and $\mathrm S$, $\mathrm A$ its symmetric and antisymmetric parts; the second is the product of the family, $\mathrm P$ the plain one and $\mathrm Q$ the quaternionic one, whose first slot is read through the natural conjugation; and the third letter is the same one for the six, $\mathrm A$ the algebra over $\mathbb{R}$. The six are read in the two families of *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*,

| the family | general | symmetric | antisymmetric |
|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\mathrm{SPA}$ | $\mathrm{APA}$ |
| the quaternionic algebra | $\mathrm{GQA}$ | $\mathrm{SQA}$ | $\mathrm{AQA}$ |

and every table of the article follows this order, family by family and, inside a family, general then symmetric then antisymmetric.

**Scope and owners.** This article owns the comparison of the six root sets of $0$ and of the six square-zero sets, the cone reading of the root set of $0$, the comparison of the three classes of the square-zero elements, the zero divisors and the roots of $0$, and the nilpotent as the nonzero member of the set. The per-structure results stay owned by their articles, cited one by one below: the square-zero sets by the six *Nilpotents of the …*. The products are *The 6 Products of the Quaternion Real Space* and *The Two General Products of the Quaternion $\mathbb{R}$ Space*; the structures and the codes are *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the vocabulary stated once for a general product, the root of a central value and the nilpotent, is *Definitions for the Study of the 6 Algebraic Structures*; the two forms are *The 2 Forms over the Quaternion $\mathbb{R}$ Space*; the zero divisors, their sets and the one-sided inverse equations are *Zero Divisors in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the division property of the plain product is *Norm and Invertibility in the General Plain Algebra of Quaternions*; the annihilating partners are *Annihilators in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; and the biquaternion case is *Nilpotents in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**Conventions.** $\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_0=1$; a general element is $\tilde\xi=\xi_0e_0+\vec\xi$ with $\xi_0\in\mathbb{R}$ and $\vec\xi=\sum_k\xi_ke_k$; the natural conjugation is $\tilde\xi^{\natural}=\xi_0-\vec\xi$; the **plain form** is $B(\tilde\xi)=\xi_0^{2}-\lvert\vec\xi\rvert^{2}=\mathrm{Sc}(\tilde\xi^{2})$; and the **quaternion form** is $N(\tilde\xi)=\xi_0^{2}+\lvert\vec\xi\rvert^{2}=\mathrm{Sc}(\tilde\xi^{\natural}\tilde\xi)$, the norm. The plain product is $\tilde\xi\tilde\eta$, the Jordan product is $\tilde\xi\bullet\tilde\eta=\tfrac12(\tilde\xi\tilde\eta+\tilde\eta\tilde\xi)$, the plain cross product is $\tilde\xi\wedge\tilde\eta=\tfrac12(\tilde\xi\tilde\eta-\tilde\eta\tilde\xi)=\vec\xi\times\vec\eta$, the quaternionic product is $\tilde\xi^{\natural}\tilde\eta$, its symmetrisation is the scalar-valued rule $N(\tilde\xi,\tilde\eta)e_0$, and the quaternionic cross product is $\tilde\xi\wedge^{\natural}\tilde\eta=\tfrac12(\tilde\xi^{\natural}\tilde\eta-\tilde\eta^{\natural}\tilde\xi)$. The **root of a central value** is defined in *Definitions for the Study of the 6 Algebraic Structures* §*The Element Vocabulary* as an element $\tilde\xi$ with $\tilde\xi^{2}=c$ for a central $c$, the class of them being the set of its solutions, with no nonzero requirement; the **nilpotent** is defined in the same section as a nonzero square-zero element. The origin is therefore counted with the roots of $0$ wherever it solves the equation, and the places where an owner counts the nonzero roots alone are read as the origin alone.

## The Roots of Zero in the Six Structures

The square of a structure is its operation read at the two equal arguments, so each of the six carries a root problem of its own, and the six squares are three. They are the squares of *Square Roots of a General Element in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* §*The Two General Products at a General Value*, recalled here:

| the square | the structures | at the two equal arguments |
|---|---|---|
| the plain square | $\mathrm{GPA}$, $\mathrm{SPA}$ | $(\xi_0^{2}-\lvert\vec\xi\rvert^{2})e_0+2\xi_0\vec\xi$ |
| the central square | $\mathrm{GQA}$, $\mathrm{SQA}$ | $N(\tilde\xi)e_0$ |
| the vanishing square | $\mathrm{APA}$, $\mathrm{AQA}$ | $0$ |

**Definition.** The **root set of $0$** in the structure $\star$ is

$$
\mathcal R_0=\{\tilde\xi:\tilde\xi\star\tilde\xi=0\} ,
$$

and it is the square-zero set of the structure.

**Definition.** A subset of $\mathbb{H}$ is a **cone** when it contains $\mu\tilde\xi$ for every $\tilde\xi$ it contains and every real $\mu$. Its **apex** is the origin.

**Proposition (the root set of $0$ is the cone, and the root sets of the two signed values carry no apex).** The set $\mathcal R_0$ is a cone whose apex is the origin: a real multiple of a root of $0$ is again a root of $0$. It is the origin alone for the four structures whose square vanishes only there, and the whole space, a cone with the origin as apex, for the two antisymmetric structures. The sets of roots of the two signed values carry no apex: a scaling by $\mu$ carries the value $\lambda$ to $\mu^{2}\lambda$, so no nonzero multiple of a root of $\lambda$ is again a root of $\lambda$ unless $\mu^{2}=1$.

*Proof.* The square of a scaled element is $\mu^{2}(\tilde\xi\star\tilde\xi)$, the six products being bilinear over $\mathbb{R}$, so the vanishing of the square is preserved by every $\mu$ and a signed value is preserved by $\mu=\pm1$ alone. The root set of $0$ of the plain family is the origin and not the cone of the plain form, because the two equations of the pair must hold together: the cone $B=0$ meets the vector subspace at the origin alone, and the other branch is the centre.

**Theorem (the six root sets of $0$; quoted).** Among the six structures of the quaternion real space the root set of $0$ is the origin alone $\{0\}$ for $\mathrm{GPA}$, $\mathrm{SPA}$, $\mathrm{GQA}$ and $\mathrm{SQA}$, and it is the whole space $\mathbb{H}$ for $\mathrm{APA}$ and $\mathrm{AQA}$. Only two root sets occur, and no structure of the six has a root set of $0$ that is neither a point nor the whole space.

*Proof.* For the general plain structure the pair $B(\tilde\xi)=0$, $2\xi_0\vec\xi=0$ forces the origin: the second equation gives $\xi_0=0$ or $\vec\xi=0$, the pure branch gives $\lvert\vec\xi\rvert^{2}=0$ and the central branch $\xi_0^{2}=0$, and the plain form, indefinite though it is, has no real isotropic direction, its isotropic cone being real only after complexification. For the general quaternionic structure the equation is $N(\tilde\xi)=0$ with $N$ a sum of four real squares, so the origin alone vanishes. The two symmetric structures have the same square on the diagonal, the Jordan square being the plain square and the symmetrised quaternionic square being the norm times $e_0$, so they keep the same one-point sets. Both cross products are alternating, so $\tilde\xi\wedge\tilde\xi=0$ and $\tilde\xi\wedge^{\natural}\tilde\xi=0$ for every element, and the equation is satisfied identically. The assertion that no third set occurs is the classification of the squares: the square of a structure of the six is the plain square, the norm times $e_0$, or zero, and the first two have the origin as their only real zero.

The six are read one by one below; each names the product, its square and its root set of $0$, and cites the article that owns it.

### $\mathrm{GPA}$, the general plain algebra

The product is $\tilde\xi\tilde\eta$, and its square is the plain square, of scalar part $B(\tilde\xi)=\xi_0^{2}-\lvert\vec\xi\rvert^{2}$ and vector part $2\xi_0\vec\xi$. The root set of $0$ is $\{0\}$ alone, by the division property of the plain algebra; the isotropic cone of the plain form is real only after complexification, and the second equation of the pair removes it. The article is *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*.

### $\mathrm{SPA}$, the symmetric plain algebra

The product is the Jordan product $\tilde\xi\bullet\tilde\eta$, and its square is the plain square, $\tilde\xi\bullet\tilde\xi=\tilde\xi^{2}$, whose only real zero is the origin. The root set of $0$ is $\{0\}$ alone, element for element that of $\mathrm{GPA}$, although the Jordan structure is not associative. The article is *Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Algebra*.

### $\mathrm{APA}$, the antisymmetric plain algebra

The product is the commutator $\tilde\xi\wedge\tilde\eta=\vec\xi\times\vec\eta$, the cross product of the two vector parts. It is alternating, so at the two equal arguments it vanishes, $\tilde\xi\wedge\tilde\xi=0$, and the equation is satisfied identically. The root set of $0$ is every element of the space; the nonzero ones are at once the square-zero set, the nilpotent set and the zero-divisor set of the block, all three being the punctured space. The article is *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Algebra*.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde\xi^{\natural}\tilde\eta$, and its square is the central element $N(\tilde\xi)e_0$; the equation is the single real equation $N(\tilde\xi)=0$, the vanishing of a sum of four real squares, so only the origin vanishes. The root set of $0$ is $\{0\}$ alone. The article is *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*.

### $\mathrm{SQA}$, the symmetric quaternionic algebra

The product is the symmetrisation $\tfrac12(\tilde\xi^{\natural}\tilde\eta+\tilde\eta^{\natural}\tilde\xi)=N(\tilde\xi,\tilde\eta)e_0$, the quaternion form read as a product, and its square is the definite form, $\tilde\xi\star\tilde\xi=N(\tilde\xi)e_0$, non-negative at every element. The root set of $0$ is $\{0\}$ alone, as for $\mathrm{GQA}$. The article is *Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Algebra*.

### $\mathrm{AQA}$, the antisymmetric quaternionic algebra

The product is the commutator $\tilde\xi\wedge^{\natural}\tilde\eta=\tfrac12(\tilde\xi^{\natural}\tilde\eta-\tilde\eta^{\natural}\tilde\xi)$. It is alternating, $\tilde\xi\wedge^{\natural}\tilde\xi=0$, so the equation is satisfied identically. The root set of $0$ is every element of the space; the nonzero ones are at once the square-zero elements, the nilpotents of the block and its zero divisors, the three sets being the punctured space. The article is *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Quaternionic Algebra*.

**The two general products at $0$.** At the value $0$ the plain product and the quaternionic product have the same root set, the origin alone, whatever the sign between their squares on the vector subspace. The value $0$ is the value at which the two general products agree; at the two signed values they differ, the plain product reading the pair $\pm e_0$ and the sphere $S^{2}$ and the quaternionic product the sphere $S^{3}$ and the empty set, one sign of the vector part apart.

**The value in coordinates.** Written on the coordinates, the value $0$ is the three equations of the squares, one per family:

| the family | the equation of the root of $0$ |
|---|---|
| the plain family | $\xi_0^{2}-\lvert\vec\xi\rvert^{2}=0$ with $2\xi_0\vec\xi=0$ |
| the quaternionic family | $N(\tilde\xi)=\xi_0^{2}+\lvert\vec\xi\rvert^{2}=0$ |
| the two antisymmetric structures | $0=0$, satisfied identically |

## The Nilpotents in the Six Structures

A nilpotent is the nonzero member of the set just read. The equation is the same diagonal equation, so the six square-zero sets are the six root sets of $0$, and the reading is settled once the nonzero members are counted. The two answers are the two ways a square can fail to be invertible away from the origin: in four structures the square vanishes only at the origin and there is no nilpotent, and in two it vanishes identically and every nonzero element is a nilpotent.

**Definition.** The **square-zero set** of a structure $\star$ is the set of the solutions of $\tilde\xi\star\tilde\xi=0$, and a **square-zero element**, or **nilpotent of index two**, is a nonzero member, written $\tilde\nu$ after the convention of *Conventions in Mathematics*. The **index of nilpotency** of an element is the least $m$ with $\tilde\xi^{\star m}=0$, so that a square-zero element is a nilpotent of index two, and every element of a square-zero set is of index one or two.

**Theorem (the six square-zero sets; quoted).** Among the six structures the square-zero set is $\{0\}$ for $\mathrm{GPA}$, $\mathrm{SPA}$, $\mathrm{GQA}$ and $\mathrm{SQA}$, and it is all of $\mathbb{H}$ for $\mathrm{APA}$ and $\mathrm{AQA}$. Only two square-zero sets occur, and no structure of the six has a square-zero set that is neither a point nor the whole space.

*Proof.* The square-zero set is the root set of $0$ read at the same product, so the theorem is the preceding one, and the two proofs read the same two facts directly. For the general plain structure, a nonzero element is invertible and left multiplication by its inverse turns $\tilde\nu^{2}=0$ into $\tilde\nu=0$; the plain square is indefinite, yet the two equations of the pair force the origin, since the isotropic cone of the plain form is real only after complexification. For the general quaternionic structure, $\tilde\nu^{\natural}\tilde\nu=N(\tilde\nu)e_0$ and the norm is a sum of four real squares, so $N(\tilde\nu)=0$ forces $\tilde\nu=0$. The two symmetric structures have the same square on the diagonal, the Jordan square being the plain square and the symmetrised quaternionic square being the norm times $e_0$, so they keep the same one-point sets. Both cross products are alternating, so the equation is satisfied identically.

The classification is sharp, and it reads the two ways a square can fail to be invertible away from the origin. The **alternating** square vanishes identically, so it makes every element square zero; the **plain** square and the **definite scalar** square vanish only at the origin, the first because the real space has no isotropic direction, the second because the norm is a sum of squares. The four structures of the first kind have no nilpotent at all, and the two of the second kind have the punctured space for nilpotent set.

The six are read one by one below; each names the product, its diagonal and its square-zero set, and cites the article that owns them.

### $\mathrm{GPA}$, the general plain algebra

The product is $\tilde\nu\tilde\eta$, and its diagonal is the plain square, of scalar part $B(\tilde\nu)=\nu_0^{2}-\lvert\vec\nu\rvert^{2}$ and vector part $2\nu_0\vec\nu$. The square-zero set is $\{0\}$ alone, by the division property of the plain algebra, and there is no nilpotent. The article is *Nilpotents of the General Plain Algebra*.

### $\mathrm{SPA}$, the symmetric plain algebra

The product is the Jordan product $\tilde\nu\bullet\tilde\eta$, and its diagonal is the plain square, $\tilde\nu\bullet\tilde\nu=\tilde\nu^{2}$, whose only real zero is the origin. The square-zero set is $\{0\}$ alone, and there is no nilpotent. The article is *Nilpotents of the Symmetric Plain Algebra*.

### $\mathrm{APA}$, the antisymmetric plain algebra

The product is the plain cross product $\tilde\nu\wedge\tilde\eta=\vec\nu\times\vec\eta$, alternating, so its diagonal vanishes identically. The square-zero set is the whole space, and every nonzero element is a nilpotent of index two. The article is *Nilpotents of the Antisymmetric Plain Algebra*.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde\nu^{\natural}\tilde\eta$, and its diagonal is the central element $N(\tilde\nu)e_0$; the equation is the vanishing of the norm, a sum of four real squares, so only the origin vanishes. The square-zero set is $\{0\}$ alone, and there is no nilpotent. The article is *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*.

### $\mathrm{SQA}$, the symmetric quaternionic algebra

The product is $N(\tilde\nu,\tilde\eta)e_0$, the quaternion form read as a product, and its diagonal is the definite norm, $\tilde\nu\star\tilde\nu=N(\tilde\nu)e_0$. The square-zero set is $\{0\}$ alone; the nonzero nilpotents are the pure elements, of index three. The article is *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra*.

### $\mathrm{AQA}$, the antisymmetric quaternionic algebra

The product is the quaternionic cross product $\tilde\nu\wedge^{\natural}\tilde\eta$, alternating, so its diagonal vanishes identically. The square-zero set is the whole space, and every nonzero element is a nilpotent of index two. The article is *Nilpotents of the Antisymmetric Quaternionic Algebra*.

**A nonzero square-zero element is its own annihilator and a zero divisor.** An element with $\tilde\nu\star\tilde\nu=0$ annihilates itself on both sides, so it is an annihilating partner of itself and a zero divisor of its structure, in the vocabulary of *Definitions for the Study of the 6 Algebraic Structures*. In the two antisymmetric structures, whose square vanishes identically, every nonzero element is such an element, and the square-zero set, the nilpotent set and the zero-divisor set of the structure are the same punctured space; in the four other structures the square-zero set is the origin alone and the three classes separate.

**The three classes and where they agree.** The square-zero elements, the zero divisors and the roots of $0$ are three classes attached to a structure, and the comparison of the six structures reads them together; the zero-divisor sets are those of *Zero Divisors in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*.

**Theorem (the comparison of the three classes).** For the two antisymmetric structures the three classes coincide away from the origin: a nonzero element is square zero exactly when it is a zero divisor, and the square-zero set is also the root set of $0$. For the four other structures the three classes do not coincide: the square-zero set is the origin alone, while the zero-divisor set is empty for the two general structures, the punctured vector subspace for the symmetric plain structure, and the punctured space for the symmetric quaternionic structure.

*Proof.* A nonzero square-zero element is a zero divisor, its own partner, and a root of $0$; the converse fails in the four structures whose square-zero set is the origin alone, where that set is a point while the zero-divisor set is one of the three other values of *Zero Divisors in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*. For the antisymmetric structures the square vanishes identically, so the square-zero set and the root set of $0$ are both $\mathbb{H}$ and the zero-divisor set is $\mathbb{H}$ without the origin, the same set with the origin removed.

The comparison is the visible content of the classification. The three classes collapse onto one another exactly on the alternating structures, where the diagonal of the product is identically zero; they separate as soon as the diagonal does not vanish identically, and the gap between them measures the difference between the vanishing of a square and the vanishing of a product. This is the gap the symmetric quaternionic structure exhibits most sharply, its square nonzero on every nonzero element while every nonzero element is a zero divisor: the vanishing of a *product* does not require the vanishing of a *square*.

## Results

The set is collected once below, with the two readings of the roots of $0$ and the square-zero sets held together, and the three classes are compared last.

### The Six Root Sets of $0$, Which Are the Six Square-Zero Sets

| the family | the structure | the square | the square-zero equation | the root set of $0$, the square-zero set | the nilpotents |
|---|---|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\tilde\xi^{2}$ | $B(\tilde\xi)=0$, $2\xi_0\vec\xi=0$ | $\{0\}$ | none |
| | $\mathrm{SPA}$ | $\tilde\xi^{2}$ | $B(\tilde\xi)=0$, $2\xi_0\vec\xi=0$ | $\{0\}$ | none |
| | $\mathrm{APA}$ | $0$ | satisfied identically | $\mathbb{H}$ | every nonzero element |
| the quaternionic algebra | $\mathrm{GQA}$ | $N(\tilde\xi)e_0$ | $N(\tilde\xi)=0$ | $\{0\}$ | none |
| | $\mathrm{SQA}$ | $N(\tilde\xi)e_0$ | $N(\tilde\xi)=0$ | $\{0\}$ | none |
| | $\mathrm{AQA}$ | $0$ | satisfied identically | $\mathbb{H}$ | every nonzero element |

Read down the fifth column, only two sets occur: the origin alone $\{0\}$ for the four structures whose square is the plain square or the definite scalar $N(\tilde\xi)e_0$, and the whole space $\mathbb{H}$ for the two whose square vanishes identically. The origin is the common member, and it is square zero without being a nilpotent, the nilpotents being the nonzero members. The symmetric structure of each family repeats the row of its general partner, the two squares agreeing on the diagonal. The root set of $0$ is a cone in every one of the six structures: the origin, a degenerate cone with the origin as apex, in the four, and the whole space, a cone with the origin as apex, in the two.

### The Three Classes

| structure | square-zero set | zero-divisor set | roots of $0$ | the three agree |
|---|---|---|---|---|
| $\mathrm{GPA}$ | $\{0\}$ | $\varnothing$ | $\{0\}$ | trivially, at the origin |
| $\mathrm{SPA}$ | $\{0\}$ | $\mathrm{Vect}(\mathbb{H})\setminus\{0\}$ | $\{0\}$ | no |
| $\mathrm{APA}$ | $\mathbb{H}$ | $\mathbb{H}\setminus\{0\}$ | $\mathbb{H}$ | yes, away from the origin |
| $\mathrm{GQA}$ | $\{0\}$ | $\varnothing$ | $\{0\}$ | trivially, at the origin |
| $\mathrm{SQA}$ | $\{0\}$ | $\mathbb{H}\setminus\{0\}$ | $\{0\}$ | no |
| $\mathrm{AQA}$ | $\mathbb{H}$ | $\mathbb{H}\setminus\{0\}$ | $\mathbb{H}$ | yes, away from the origin |

The four structures whose square-zero set is the origin alone have no nilpotent, and the two whose square vanishes identically have the punctured space for nilpotent set. The three classes of the table coincide away from the origin exactly for the two antisymmetric structures; for the four other structures the square-zero set is the origin alone while the zero-divisor set is empty, the punctured vector subspace of the plain structure, or the punctured space of the symmetric quaternionic structure.

## Summary

The root set of $0$ of a structure is the set of elements whose square vanishes, and it is the square-zero set of the structure. The general plain structure has the origin alone, by the division property of the plain product, the plain form being indefinite yet without a real isotropic direction; the symmetric plain structure keeps the same one-point set, the Jordan square being the plain square; the antisymmetric plain structure, being alternating, has the whole space; the general quaternionic structure has the origin alone, by the definiteness of the norm; the symmetric quaternionic structure keeps the same one-point set, its square being the definite norm $N(\tilde\xi)e_0$; and the antisymmetric quaternionic structure has the whole space, being alternating. So only two sets occur among the six, the origin and the whole space, and no structure has an intermediate set.

The nilpotents are the nonzero members of the square-zero sets: none in the four structures whose square vanishes only at the origin, and every nonzero element in the two whose square vanishes identically. The square-zero set is a cone with the origin as apex in every structure, since a real multiple of a root of $0$ is again a root of $0$; the root sets of the two signed values carry no apex, and the value $0$ is the value at which the two general products agree while at $\pm1$ they differ. A nonzero square-zero element is its own annihilating partner and a zero divisor of its structure, and the three classes of the square-zero elements, the zero divisors and the roots of $0$ coincide away from the origin exactly for the two antisymmetric structures; for the four other structures the square-zero set is the origin alone while the zero-divisor set is empty, the punctured vector subspace, or the punctured space.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\xi\star\tilde\xi=0$ | the root equation of the value $0$ in the structure $\star$ |
| $\mathcal R_0$ | the root set of $0$, which is the square-zero set |
| $\tilde\nu$ | a square-zero element, or nilpotent of index two, the nonzero member of the set |
| $\{0\}$ | the square-zero set of GPA, SPA, GQA and SQA, and their nilpotent set |
| $\mathbb{H}$ | the square-zero set of APA and AQA |
| $\mathbb{H}\setminus\{0\}$ | the nilpotent set, and the zero-divisor set, of APA and AQA |
| $B(\tilde\xi)=\xi_0^{2}-\lvert\vec\xi\rvert^{2}$ | the plain form, the scalar part of the plain square |
| $N(\tilde\xi)=\xi_0^{2}+\lvert\vec\xi\rvert^{2}$ | the quaternion form, the square of the quaternionic family, and the norm |
| $\mathrm{Vect}(\mathbb{H})\setminus\{0\}$ | the zero-divisor set of SPA, for the comparison |
| cone, apex | a set that contains every real multiple of each of its elements, and its origin |
| $\mathrm{GPA},\dots,\mathrm{AQA}$ | the six structures of the space, the two general products and their four parts |

## Further Reading

- *Square Roots of One and the Idempotents in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/square-roots-of-one-and-the-idempotents-in-the-6-algebraic-structures-over-the-quaternion-r-space.md`), for the two signed values, the roots of $+1$ and the idempotents, whose value $0$ is the one read here.
- *Square Roots of a General Element in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/square-roots-of-a-general-element-in-the-6-algebraic-structures-over-the-quaternion-r-space.md`), the companion of this article, for the root equation at a general central value, the six squares and the six-row table.
- *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-6-algebraic-structures-over-the-quaternion-r-space.md`), for the six names, the class of each and the two laws of the table.
- *The 6 Products of the Quaternion Real Space* (`articles_maths/the-6-products-of-the-quaternion-real-space.md`), for the six products and their coordinates.
- *The Two General Products of the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-two-general-products-of-the-quaternion-r-space.md`), for the plain product and the quaternionic product, whose squares the value $0$ reads.
- *The 2 Forms over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternion-r-space.md`), for the plain form $B$ of signature $(1,3)$ and the definite quaternion form $N$.
- *Zero Divisors in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/zero-divisors-in-the-6-algebraic-structures-over-the-quaternion-r-space.md`), for the zero-divisor sets, the empty set of the two general products, and the one-sided inverse equations.
- *Annihilators in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/annihilators-in-the-6-algebraic-structures-over-the-quaternion-r-space.md`), for the annihilating partners of an element, which a nonzero square-zero element supplies for itself.
- *Norm and Invertibility in the General Plain Algebra of Quaternions* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra-of-quaternions.md`), for the division property that leaves the plain square-zero set at the origin.
- *Definitions for the Study of the 6 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-6-algebraic-structures.md`), for the root of a central value, the nilpotent and the general vocabulary.
- The six owners, for the square-zero set of each structure: *Nilpotents of the General Plain Algebra* (`articles_maths/nilpotents-of-the-general-plain-algebra-of-quaternions.md`), *Nilpotents of the Symmetric Plain Algebra* (`articles_maths/nilpotents-of-the-symmetric-plain-algebra-of-quaternions.md`), *Square Roots of Zero and the Nilpotents of the Antisymmetric Plain Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-antisymmetric-plain-algebra-of-quaternions.md`), *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-general-quaternionic-algebra-of-quaternions.md`), *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-symmetric-quaternionic-algebra-of-quaternions.md`) and *Nilpotents of the Antisymmetric Quaternionic Algebra* (`articles_maths/nilpotents-of-the-antisymmetric-quaternionic-algebra-of-quaternions.md`).
