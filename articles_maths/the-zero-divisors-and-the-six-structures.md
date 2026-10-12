# __The Zero Divisors and the Six Structures__

## Introduction

A zero divisor of a structure is a nonzero element that kills a nonzero partner. The quaternion space carries six structures, and the zero-divisor set ranges across all of them, from empty to the whole punctured space. This article defines the zero divisor of a structure, gives the operator criterion, and determines the zero-divisor set, the pairs and the annihilators for the six. The products are *The 6 Products of the Quaternion Real Space* and *The Two General Products of the Quaternion $\mathbb{R}$ Space*, the six structures are *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, and the general definitions are *Definitions for the Study of the 6 Algebraic Structures*, all above this article in this category.

## The Zero Divisors of a Structure

**Definition.** Let $\star$ be a product on $\mathbb{H}$. A nonzero element $\tilde p$ is a **zero divisor** of the structure when there is a nonzero element $\tilde q$ with
$$
\tilde p\star\tilde q=0\quad\text{or}\quad\tilde q\star\tilde p=0 ,
$$
and such a $\tilde q$ is a **partner**. When only the first, resp. the second, relation is allowed, $\tilde p$ is a **left**, resp. a **right**, zero divisor. An element is **regular** when it is not a zero divisor; the zero element is regular, the defining clause requiring a nonzero element.

Two of the six products are commutative, the Jordan product and the symmetric quaternionic product, and two are alternating, the two cross products; for those four the left and the right zero-divisor sets coincide at once. The remaining two, the general plain and the general quaternionic products, have no zero divisor at all, so their one-sided sets are empty and coincide as well. In all six structures the left and the right zero divisors coincide, and no side has to be named.

**Criterion (the operator criterion).** For a product linear in its second slot, a nonzero element $\tilde p$ is a left zero divisor exactly when the left multiplication operator $L_{\tilde p}\tilde q=\tilde p\star\tilde q$ is singular. For the six structures of the chapter the operator is a $4\times4$ matrix, so the criterion is the vanishing of its determinant, and the annihilator of $\tilde p$ is its kernel.

*Proof.* A nonzero $\tilde q$ with $\tilde p\star\tilde q=0$ is a nonzero vector of the kernel, and conversely. The determinant detects the kernel of a square matrix. The two-sided statement follows because the left and the right zero-divisor sets of the six products coincide.

## The Two Division Structures

**Theorem.** The general plain product $\tilde p\tilde q$ and the general quaternionic product $\tilde p^{\natural}\tilde q$ have no zero divisor; every nonzero element is regular, and the zero-divisor set is empty.

*Proof.* The plain product is the multiplication of the division algebra $\mathbb{H}$: from $\tilde p\tilde q=0$ with $\tilde p\neq0$ one multiplies by the inverse $\tilde p^{-1}$ and gets $\tilde q=0$, so no partner exists. For the quaternionic product, $\tilde p^{\natural}\tilde q=0$ gives $\tilde q=0$ after multiplication by $(\tilde p^{\natural})^{-1}$, the conjugate of a nonzero quaternion being nonzero. So both sets are empty and the regular elements are all of $\mathbb{H}$.

The two general structures are the only ones with an empty zero-divisor set, and they are also the only ones whose product makes the space a division algebra; the count of the two is the count of the division structures of the six.

## The Two Symmetric Structures

### The Symmetric Plain Structure

**Theorem (the zeros of the Jordan product).** A nonzero element of the Jordan structure is a zero divisor if and only if it is pure:
$$
\tilde p\ \text{is a zero divisor of}\ \mathrm{SPA}\iff p_0=0\iff\tilde p\in\mathrm{Vect}(\mathbb{H})\setminus\{0\} .
$$
The zero-divisor set is the vector subspace with the origin removed, of real dimension three; the criterion is the vanishing of the determinant of the multiplication operator,
$$
\det L^{\bullet}_{\tilde p}=p_0^2\,N(\tilde p) ,
$$
and the pairs are exactly the ordered pairs of orthogonal nonzero pure elements.

*Proof.* The Jordan product is $\tilde p\bullet\tilde q=(p_0q_0-\mathbf p\cdot\mathbf q)e_0+p_0\mathbf q+q_0\mathbf p$. For a pure $\tilde p=\mathbf u$ and a pure partner, the product is $-\mathbf u\cdot\mathbf v\,e_0$, which vanishes exactly when $\mathbf u$ and $\mathbf v$ are orthogonal; a pure element has a nonzero orthogonal vector in the three-dimensional vector subspace. For a nonpure $\tilde p$ the operator is nonsingular and its determinant is the displayed $p_0^2N(\tilde p)$, which does not vanish; the operator form of the criterion and the proof of the determinant are in *Zero Divisors of the Symmetric Plain Algebra*, above this article in this category.

The partner set of a nonzero pure $\mathbf u$ is the plane
$$
\operatorname{Ann}(\mathbf u)=\{\tilde q:q_0=0,\ \mathbf u\cdot\mathbf q=0\}=\mathbf u^{\perp}\cap\mathrm{Vect}(\mathbb{H}) ,
$$
of dimension two, and the ordered pairs of the structure form a family of real dimension five whose unordered version is the Grassmannian $\mathrm{Gr}(2,3)\cong\mathbb{RP}^2$.

### The Symmetric Quaternionic Structure

**Theorem (the zeros of the scalar-valued product).** Every nonzero element of the symmetric quaternionic structure is a zero divisor; the zero-divisor set is the punctured space $\mathbb{H}\setminus\{0\}$, the annihilator of a nonzero element is the hyperplane $\tilde p^{\perp}$ of the quaternion form, of real dimension three, and the regular elements reduce to $\{0\}$.

*Proof.* The product is $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0$, so the criterion is $N(\tilde p,\tilde q)=0$; for a fixed nonzero $\tilde p$ the linear form $N(\tilde p,\cdot)$ is nonzero and its kernel is a hyperplane, of dimension $4-1=3$, hence contains a nonzero partner. The element $0$ alone is regular, the defining clause requiring a nonzero element.

The structure is the opposite of the symmetric plain one: the Jordan product has the smallest nonzero zero-divisor set of the block, the pure cone, while the scalar-valued product has the largest, the whole punctured space. The contrast shows that a definite form does not prevent zero divisors: the plain form is definite and the pure cone is empty of isotropic vectors, yet the Jordan product has zero divisors because its product vanishes on a *pair* of orthogonal vectors, and the quaternion form is definite and every element is a zero divisor because a nonzero linear form on a space of dimension four always has a kernel of dimension three. The pair $(\tilde p,\tilde q)=(e_0,e_1)$ witnesses it, $e_0\star e_1=N(e_0,e_1)e_0=0$, while in the symmetric plain structure the same element $e_0$ is the unit and not a zero divisor.

## The Two Antisymmetric Structures

**Theorem (the alternating structures).** The two cross products have no nontrivial divisor theory: the operation is alternating, so $\tilde p\wedge\tilde p=0$ and $\tilde p\wedge^{\natural}\tilde p=0$ for every element; every nonzero element is a zero divisor with itself as partner on both sides, and the zero-divisor set is the punctured space $\mathbb{H}\setminus\{0\}$, of real dimension four.

*Proof.* An alternating product on a space of characteristic not two satisfies $x\star x=0$ identically, so the partner $\tilde q=\tilde p$ is available for every nonzero element. No nonzero element is regular.

**Theorem (the criteria and the annihilators).** For nonzero $\tilde p,\tilde q$, the plain cross product vanishes exactly when the vector parts are parallel,
$$
\mathbf p\times\mathbf q=0\iff\mathbf q\in\mathbb{R}\mathbf p\ \text{or}\ \mathbf p\in\mathbb{R}\mathbf q ,
$$
and the annihilator of a noncentral element is the plane
$$
\operatorname{Ann}_{\wedge}(\tilde p)=\mathbb{R}e_0\oplus\mathbb{R}\mathbf p ,
$$
of real dimension two, while the annihilator of a central element is all of $\mathbb{H}$. The quaternionic cross product vanishes exactly when the partner is a multiple of the element,
$$
\tilde p\wedge^{\natural}\tilde q=0\iff\tilde q=\lambda\tilde p ,
$$
and the annihilator of a nonzero element is the line $\mathbb{R}\tilde p$, of real dimension one.

*Proof.* The plain cross product is $\mathbf p\times\mathbf q$, which vanishes exactly on parallel vectors; a partner ranges over the plane spanned by the scalar direction and $\mathbf p$ when $\mathbf p\neq0$, and over all of $\mathbb{H}$ when $\tilde p$ is central, since then the product is identically zero. For the quaternionic cross product, the equation $p_0\mathbf q=q_0\mathbf p+\mathbf p\times\mathbf q$ splits into a parallel part, giving the ratio of the scalar parts, and a perpendicular part $p_0\mathbf q_{\perp}=\mathbf p\times\mathbf q_{\perp}$, which compares the perpendicular component with a quarter turn of itself; a quarter turn has no real eigenvector, so $\mathbf q_{\perp}=0$ and $\tilde q=\lambda\tilde p$. The annihilator is therefore the line $\mathbb{R}\tilde p$, and the left multiplication operator has rank three off the origin, trace $3p_0$ and vanishing determinant, with characteristic polynomial $t(t-p_0)\bigl((t-p_0)^2+|\mathbf p|^2\bigr)$; the computation is in *Zero Divisors of the Antisymmetric Quaternionic Algebra*, above this article in this category.

The two antisymmetric structures agree on the total zero-divisor set and separate on the annihilator: the plain cross product forgets the scalar coordinate of the partner and returns a plane, the quaternionic cross product couples the scalar and the vector coordinates and returns a line. The ordered zero-divisor pairs form a family of real dimension six for the plain cross product and of real dimension five for the quaternionic one, the second argument being constrained to a plane, resp. a line, over the four-dimensional set of nonzero first arguments in both cases.

## The Six Zero-Divisor Sets Side by Side

| structure | product | zero-divisor set | criterion | dimension |
|---|---|---|---|---|
| $\mathrm{GPA}$ | $\tilde p\tilde q$ | $\varnothing$ | division | — |
| $\mathrm{GQA}$ | $\tilde p^{\natural}\tilde q$ | $\varnothing$ | division after conjugation | — |
| $\mathrm{SPA}$ | $\tilde p\bullet\tilde q$ | $\mathrm{Vect}(\mathbb{H})\setminus\{0\}$ | $p_0=0$ | $3$ |
| $\mathrm{SQA}$ | $N(\tilde p,\tilde q)e_0$ | $\mathbb{H}\setminus\{0\}$ | $N(\tilde p,\tilde q)=0$ | $4$ |
| $\mathrm{APA}$ | $\tilde p\wedge\tilde q=\mathbf p\times\mathbf q$ | $\mathbb{H}\setminus\{0\}$ | $\mathbf p\times\mathbf q=0$ | $4$ |
| $\mathrm{AQA}$ | $\tilde p\wedge^{\natural}\tilde q$ | $\mathbb{H}\setminus\{0\}$ | $\tilde q=\lambda\tilde p$ | $4$ |

**Theorem (the six zero-divisor sets).** Two of the six structures have no zero divisor, $\mathrm{GPA}$ and $\mathrm{GQA}$; one has the cone of the pure elements, $\mathrm{SPA}$; and three have the whole punctured space, $\mathrm{SQA}$, $\mathrm{APA}$ and $\mathrm{AQA}$. The zero-divisor sets are nested,
$$
\varnothing\ \subsetneq\ \mathrm{Vect}(\mathbb{H})\setminus\{0\}\ \subsetneq\ \mathbb{H}\setminus\{0\} ,
$$
with the empty set taken by the two general structures, the cone by the symmetric plain one, and the punctured space by the other three.

*Proof.* The theorems of the three preceding sections give the three values; the two general structures take the empty value and the three remaining structures the punctured space. The inclusions are immediate, the vector subspace being a proper subset of the space and the origin being removed in both cases.

**Theorem (the regular elements).** The regular elements of the six structures are: all of $\mathbb{H}$ for $\mathrm{GPA}$ and $\mathrm{GQA}$; the elements with nonzero scalar part, together with the origin, for $\mathrm{SPA}$; and the origin alone for $\mathrm{SQA}$, $\mathrm{APA}$ and $\mathrm{AQA}$.

*Proof.* An element is regular when it is not a zero divisor, and the origin is always regular. The zero-divisor sets being those of the table, the regular elements are their complements in the space, together with the origin, which gives the three cases.

The table and the two theorems are the comparison. The block of three totals, $\mathrm{SQA}$, $\mathrm{APA}$ and $\mathrm{AQA}$, contains one symmetric structure and both antisymmetric ones; the symmetric plain structure is alone in the middle; and the two general structures, which are opposite in their law tables, agree in having no zero divisor at all. The zero-divisor set is therefore not governed by the general, symmetric or antisymmetric character of the law but by the way the product reads its arguments: a product that multiplies by the whole element is a candidate for division, a product that reads only the vector part, or only a pairing, is not.

## Summary

The zero divisor of a structure is a nonzero element that kills a nonzero partner, and the operator criterion reads it as the singularity of the multiplication operator. The general plain and general quaternionic structures have no zero divisor, every nonzero element being regular. The symmetric plain structure has for zero-divisor set the cone of the pure elements, $\mathrm{Vect}(\mathbb{H})\setminus\{0\}$, of real dimension three, its operator determinant being $p_0^2N(\tilde p)$, and its pairs being the orthogonal nonzero pure pairs. The symmetric quaternionic structure and the two cross products have the whole punctured space for zero-divisor set, because a definite linear form on a space of dimension four always has a kernel, and because an alternating product vanishes on the diagonal; their annihilators are the hyperplane $\tilde p^{\perp}$, the plane $\mathbb{R}e_0\oplus\mathbb{R}\mathbf p$ and the line $\mathbb{R}\tilde p$. The regular elements are all of $\mathbb{H}$, the nonpure elements with the origin, and the origin alone, in the three cases. The sets are nested, $\varnothing\subsetneq\mathrm{Vect}(\mathbb{H})\setminus\{0\}\subsetneq\mathbb{H}\setminus\{0\}$, and the two general structures, opposite in their laws, are equal in having no zero divisor.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde p\star\tilde q=0$, $\tilde p,\tilde q\neq0$ | a zero-divisor pair of the structure $\star$ |
| $L_{\tilde p}$ | the left multiplication operator; its singularity is the criterion |
| $\varnothing$ | the zero-divisor set of GPA and GQA |
| $\mathrm{Vect}(\mathbb{H})\setminus\{0\}$ | the zero-divisor set of SPA, the pure cone |
| $\mathbb{H}\setminus\{0\}$ | the zero-divisor set of SQA, APA and AQA |
| $\tilde p^{\perp}$, $\mathbb{R}e_0\oplus\mathbb{R}\mathbf p$, $\mathbb{R}\tilde p$ | the annihilators of SQA, APA and AQA |
| $p_0^2N(\tilde p)$ | the determinant of the operator of SPA |

## Further Reading

- *Zero Divisors of the Symmetric Plain Algebra* (`articles_maths/zero-divisors-of-the-symmetric-plain-algebra-of-quaternions.md`), above this article in this category, for the Jordan structure.
- *Zero Divisors of the Symmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-algebra-of-quaternions.md`), above this article in this category, for the scalar-valued structure.
- *Zero Divisors of the Antisymmetric Plain Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-plain-algebra-of-quaternions.md`) and *Zero Divisors of the Antisymmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-quaternionic-algebra-of-quaternions.md`), above this article in this category, for the two cross products.
- *The Annihilating Elements of the Six Structures* (`articles_maths/the-annihilating-elements-of-the-six-structures.md`), above this article in this category, for the companion question of the annihilating sets.
- *The Square-Zero Elements of the Six Structures* (`articles_maths/the-square-zero-elements-of-the-six-structures.md`), below this article in this category, for the elements whose square vanishes.
