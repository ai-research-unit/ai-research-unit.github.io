# __Zero Divisors in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space__

## Introduction

Let $\star$ be a product on the quaternion space $\mathbb{H}$. A nonzero $\tilde q_1\in\mathbb{H}$ is a **zero divisor of $\star$** when it kills a nonzero partner: when $\tilde q_1\star\tilde q_2=0$ or $\tilde q_2\star\tilde q_1=0$ for some nonzero $\tilde q_2$. The first case makes it a left zero divisor, the second a right zero divisor, and an element of both kinds a two-sided zero divisor.

**The three companion structures.** Beside the algebra product $\tilde q_1\tilde q_2$ of the *Quaternions* category, the space carries the companion products of *The 6 Products of the Quaternioid Real Space*, which this category organises into three structures in *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*:

$$
\mathrm{SPA} , \qquad \mathrm{APA} , \qquad \mathrm{GQA} ,
$$

the **symmetric plain algebra** of the Jordan product $\tilde q_1\bullet\tilde q_2=\tfrac12(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1)$, the **antisymmetric plain algebra** of the cross product $\tilde q_1\wedge\tilde q_2=\tfrac12(\tilde q_1\tilde q_2-\tilde q_2\tilde q_1)=\vec q_1\times\vec q_2$, and the **general quaternionic algebra** of the product $\tilde q_1^{\natural}\tilde q_2$. A zero divisor names its product, so the generic definition poses three questions, answered once here. The fourth structure of the space, the algebra product, is a division algebra and owns its element theory in the *Quaternions* category, in *Zero Divisors of the Quaternion Algebra*; the table below names it once for the contrast and cites it rather than restating it.

## The Empty Zero-Divisor Set

**Definition.** The **zero-divisor set of the general quaternionic product** is the vanishing set of the norm with the apex removed,

$$
\mathcal{Z}=\{\tilde q\in\mathbb{H}:\langle\tilde q\rangle_{\natural}=0\}\setminus\{0\}=\varnothing ,
$$

the norm being $\langle\tilde q\rangle_{\natural}=q_t^{2}+q_x^{2}+q_y^{2}+q_z^{2}$, the quaternion algebraic norm of *The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space*.

**Definition.** A subset of $\mathbb{H}$ is a **real cone** when it contains $\lambda\tilde q$ for every $\tilde q$ it contains and every $\lambda\in\mathbb{R}$. Its **apex** is the origin.

The vanishing set $\{N=0\}$ is the smallest real cone, the apex alone, of dimension zero and containing no ray; removing the apex leaves nothing.

### The Empty Set Is the Complement of the Group of Units

The elements of $\mathbb{H}$ fall into two classes, and there is no third. The invertible elements of the algebra product, the units, are exactly those of non-vanishing norm, $\mathbb{H}^{\times}=\{\tilde q:\langle\tilde q\rangle_{\natural}\neq0\}=\mathbb{H}\setminus\{0\}$ (*Zero Divisors of the Quaternion Algebra*); the origin is never a zero divisor; and an element of nonzero norm is invertible in the general quaternionic algebra as well, so it admits no annihilating partner there. Hence

$$
\boxed{\;\mathbb{H}=\{0\}\cup\mathbb{H}^{\times}\;}.
$$

So an element is a unit exactly when it lies off the vanishing set of the norm, and the zero-divisor set of the general quaternionic product is the complement of the group of units with the apex removed, which is empty.

## The Three Companion Structures and the Zero-Divisor Set

The algebra product splits into its symmetric and antisymmetric halves, and the two halves together with the general quaternionic product are the three companion structures (*The 6 Products of the Quaternioid Real Space*). A zero divisor names its product, so each of the three carries a zero-divisor set of its own; the table of §*Results* records them, the product written by its defining formula.

**Theorem (the empty set is the mark of the general quaternionic product).** Among the three companion structures the zero-divisor set is empty exactly for the general quaternionic product $\mathrm{GQA}$, and for no other. The two derived sets are strictly larger: the symmetric plain structure $\mathrm{SPA}$ has the punctured vector subspace $\mathrm{Vect}(\mathbb{H})\setminus\{0\}$ of real dimension three, and the antisymmetric plain structure $\mathrm{APA}$ has the whole punctured space $\mathbb{H}\setminus\{0\}$.

The three structures are read one by one below; each names the product, its zero-divisor set and the reason. The general quaternionic product is read first, the two derived structures after it in §*Results*.

**Corollary (the empty set is contained in every set).** The empty set is contained in the zero-divisor set of each of the three companion structures, and it is equal to the set of exactly one of them, the general quaternionic product.

*Proof.* Every row of the table of §*Results* contains the empty set; the general quaternionic row equals it, and the two derived rows are nonempty.

The ring-theoretic picture breaks on the derived structures: the element $\vec e_x$, whose norm is $1$, is a zero divisor of $\mathrm{SPA}$, because $\vec e_x\bullet \vec e_y=\tfrac12(\vec e_x\vec e_y+\vec e_y\vec e_x)=0$ for the Jordan product, and it is invertible, $\vec e_x\bullet(-\vec e_x)=\tfrac12(-\vec e_x^{2}-\vec e_x^{2})=e_t$. A zero divisor need not be a non-unit, and here the failure is not the absence of a unit, the element $e_t$ being a two-sided unit of $\mathrm{SPA}$: it is the absence of associativity, which the equivalence of the two notions needs, and which the symmetrised and antisymmetrised products lack.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde q_1^{\natural}\tilde q_2$, its conjugate is $\tilde q_1^{\natural}$, and the form of the product is

$$
\langle\tilde q_1,\tilde q_2\rangle_{\natural}=\mathrm{Sc}(\tilde q_1^{\natural}\tilde q_2)=q_{1t}q_{2t}+(\vec q_1,\vec q_2) ,
$$

the quaternion form of *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*. The norm is the form at the two equal arguments, $\langle\tilde q\rangle_{\natural}=q_t^{2}+q_x^{2}+q_y^{2}+q_z^{2}$; the natural conjugation sends $\vec q$ to $-\vec q$, so $\langle\tilde q^{\natural}\rangle_{\natural}=\langle\tilde q\rangle_{\natural}$.

**The zero-divisor set is empty.** The natural product is the algebra product with the natural conjugation in the first slot, so its left multiplication by $\tilde q$ is the left multiplication of the algebra by $\tilde q^{\natural}$; the kernel is $\{0\}$ for $\tilde q\neq0$ (*Zero Divisors of the Quaternion Algebra*). The element is invertible, with the two-sided solution $(\tilde q^{-1})^{\natural}$ of the inverse equations.

The element $e_t$ is a left unit alone, and every nonzero element has the two-sided solution $(\tilde q^{-1})^{\natural}$ of the inverse equations; the invertible elements are $\mathbb{H}\setminus\{0\}$, and the complement of the empty zero-divisor set is that set together with the origin, the whole space.

## Results

The three companion structures are tabulated against their zero-divisor sets, and the vanishing set of the norm is read in coordinates and on its two families.

### The Three Zero-Divisor Sets

Read against the empty set and against the whole space, the three sets are

| structure | the product | the zero-divisor set |
|---|---|---|
| $\mathrm{GQA}$ | $\tilde q_1^{\natural}\tilde q_2$ | $\varnothing$ |
| $\mathrm{SPA}$ | $\tfrac12(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1)$ | $\mathrm{Vect}(\mathbb{H})\setminus\{0\}$ |
| $\mathrm{APA}$ | $\tfrac12(\tilde q_1\tilde q_2-\tilde q_2\tilde q_1)$ | $\mathbb{H}\setminus\{0\}$ |

The general quaternionic product has the empty set. The symmetric plain structure has the punctured vector subspace, of real dimension three. The antisymmetric plain structure has the whole punctured space. The empty set is therefore the zero-divisor set of exactly one of the three companion structures, and it is contained in all three, so that it is the common core of the three. For the contrast, the algebra product of the same space has the empty zero-divisor set as well, and that statement is owned by *Zero Divisors of the Quaternion Algebra*. The sections that follow read the consequences.

### The General Quaternionic Product Has No Zero Divisor

**Theorem (the zero-divisor set is empty).** A nonzero element $\tilde q_1$ is a left, a right or a two-sided zero divisor of neither the general quaternionic product nor the algebra product. In symbols,

$$
\boxed{\;\{\tilde q_1\neq0:\tilde q_1\text{ admits an annihilating factor in }\star\}=\varnothing \qquad\text{for }\star=\tilde q_1^{\natural}\tilde q_2\text{ and }\star=\tilde q_1\tilde q_2\;}.
$$

*Proof.* The natural product is the algebra product with the natural conjugation in the first slot, so its left multiplication by $\tilde q_1$ is the left multiplication of the algebra by $\tilde q_1^{\natural}$, and the conjugation is a bijection that leaves the norm unchanged. The kernel of the algebra left multiplication by $\tilde q_1^{\natural}$ is $\{0\}$, the element $\tilde q_1^{\natural}$ being nonzero; hence a nonzero element admits no annihilating factor in the general quaternionic product. For the algebra product this is the division property itself: from $\tilde q_1\tilde q_2=0$ with $\tilde q_1\neq0$ one multiplies by $\tilde q_1^{-1}$ and gets $\tilde q_2=0$.

| product | left condition | right condition | the set |
|---|---|---|---|
| $\mathrm{GQA}$, $\tilde q_1^{\natural}\tilde q_2$ | $\langle\tilde q_1\rangle_{\natural}=0$ | $\langle\tilde q_1\rangle_{\natural}=0$ | $\varnothing$ |
| the algebra product, $\tilde q_1\tilde q_2$ | $\langle\tilde q_1\rangle_{\natural}=0$ | $\langle\tilde q_1\rangle_{\natural}=0$ | $\varnothing$ |

The two rows are identical, and that is the theorem: the general quaternionic product and the algebra product select one and the same subset of $\mathbb{H}$, the empty one. The algebra row is owned by *Zero Divisors of the Quaternion Algebra* and is repeated here for the contrast only. **The word is *coincide*, not *independent*.** The zero divisor is defined by an equation that names a product, so the notion belongs to the product and the two products are two definitions, not one; what the theorem says is that in the quaternion space the two definitions select the same subset.

### $\mathrm{SPA}$ and $\mathrm{APA}$, the Two Derived Structures

**The symmetric plain algebra.** The product is the Jordan product $\tilde q_1\bullet\tilde q_2=\tfrac12(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1)=(q_{1t}q_{2t}-(\vec q_1,\vec q_2))e_t+q_{1t}\vec q_2+q_{2t}\vec q_1$, the symmetrisation of the algebra product, so its form is the same,

$$
\langle\tilde q_1,\tilde q_2\rangle_{\natural}=\mathrm{Sc}(\tilde q_1^{\natural}\tilde q_2)=q_{1t}q_{2t}+(\vec q_1,\vec q_2) ,
$$

and the norm is $\langle\tilde q\rangle_{\natural}=q_t^{2}+q_x^{2}+q_y^{2}+q_z^{2}$. **The zero-divisor set is the punctured vector subspace $\mathrm{Vect}(\mathbb{H})\setminus\{0\}$, of real dimension three.** If $\tilde q_1$ is pure, $\tilde q_1=\vec q_a$, and the partner is pure, $\tilde q_2=\vec v$, the product is $\tilde q_1\bullet\tilde q_2=-(\vec q_a,\vec v)e_t$, which vanishes exactly when $\vec q_a$ and $\vec v$ are orthogonal; a nonzero pure element has a nonzero orthogonal vector in the three-dimensional vector subspace. If $\tilde q_1$ is not pure the left multiplication operator is nonsingular, of determinant

$$
\boxed{\;\det L^{\bullet}_{\tilde q_1}=q_{1t}^{2}\langle\tilde q_1\rangle_{\natural}\;},
$$

which does not vanish; the computation is in *The Multiplication Operators of the Symmetric Plain Algebra*. The plane $q_t=0$ of the pure elements is the zero-divisor set of the structure, and the regular elements are the non-pure ones together with the origin.

The unit $e_t$ is two-sided, and every nonzero element is invertible, $\vec e_x\bullet(-\vec e_x)=e_t$; but the invertible elements form no group, the product being non-associative, and the complement of the zero-divisor set is not the invertible set: the origin is a non-zero-divisor that is not invertible, and every nonzero pure element is invertible while lying in the zero-divisor set.

**The antisymmetric plain algebra.** The product is the commutator $\tilde q_1\wedge\tilde q_2=\tfrac12(\tilde q_1\tilde q_2-\tilde q_2\tilde q_1)=\vec q_1\times\vec q_2$. It is alternating, so at the two equal arguments it vanishes, $\tilde q\wedge\tilde q=0$; there is no form there and no norm. **The zero-divisor set is the whole punctured space $\mathbb{H}\setminus\{0\}$.** Every nonzero element is annihilated by itself. There is no unit, the values lying in the vector subspace, so there is no group of units and the complement of the zero-divisor set — the whole punctured space — is the origin alone.

### The Norm in Coordinates and the Absence of a Cone

Written on the coordinates, the vanishing set of the norm is one real equation in the four real coordinates,

$$
q_t^{2}+q_x^{2}+q_y^{2}+q_z^{2}=0 .
$$

**Proposition (the vanishing set is the apex alone).** The set $\{N=0\}$ is the origin; the norm is positive definite and anisotropic over $\mathbb{R}$, so it cuts no cone, and the zero-divisor set of the general quaternionic product is empty.

*Proof.* The norm is a sum of four squares of real numbers, which vanishes exactly when the four coordinates vanish. A vanishing set of one point contains no ray through the origin other than the apex, so it is a cone of dimension zero; removing the apex leaves the empty set.

### The Two Families

The scalar part cuts the space into two families, and the criterion of the symmetric plain structure, the one criterion of the three that is not constant, reads differently on each.

**Definition.** An element is **pure** when its scalar part vanishes, $q_t=0$, and **non-pure** when $q_t\neq0$.

On a pure element the Jordan criterion drops the scalar coordinate and becomes an orthogonality in the vector subspace; on a non-pure element no annihilating partner exists.

| | pure, $q_t=0$ | non-pure, $q_t\neq0$ |
|---|---|---|
| the criterion of $\mathrm{SPA}$ | a nonzero pure partner orthogonal to $\vec q$ | none |
| square in the algebra product | $\tilde q^{2}=-\langle\tilde q\rangle_{\natural}e_t$ | $\tilde q^{2}=2q_t\tilde q-\langle\tilde q\rangle_{\natural}e_t$ |
| structure | the zero divisors of $\mathrm{SPA}$ | the regular elements of $\mathrm{SPA}$ |
| real dimension | $3$ | $4$ |

The square of a pure element is a nonzero real multiple of $e_t$ and does not vanish, so the square does not detect the zero divisors of the symmetric structure; the vanishing is carried by the pair and not by the element. The two families are read in the remarkable subspaces in *Introduction to the Remarkable Subspaces of the Quaternions*: the pure family is the vector subspace, of real dimension three, and the non-pure family is its complement.

## The Empty Set against the Complex Case

The sets of this article are read over $\mathbb{R}$, where the norm is definite and the cone is the apex alone. The comparisons with the complex case isolate what the change of scalars supplies, and they are stated here because the real space is the base case on which the complex cone table rests.

**Proposition (over $\mathbb{R}$ the two squares vanish together).** The square of the algebra product and the natural square have the same vanishing set, the origin:

$$
\boxed{\;\tilde q^{2}=0\iff\tilde q=0,\qquad \tilde q\tilde q^{\natural}=\langle\tilde q\rangle_{\natural}e_t=0\iff\tilde q=0\;}.
$$

Over $\mathbb{C}$ the two separate: the sesquilinear square $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}$ still vanishes only at the origin, but the natural square $\tilde Q\tilde Q^{\natural}$ vanishes exactly on the zero-divisor cone (*The Squares and the Positive Cone of the Biquaternion Sesqualgebra*).

*Proof.* The norm is multiplicative, $\langle\tilde q_1\tilde q_2\rangle_{\natural}=\langle\tilde q_1\rangle_{\natural}\langle\tilde q_2\rangle_{\natural}$ (*The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space*), so $\langle\tilde q^{2}\rangle_{\natural}=\langle\tilde q\rangle_{\natural}^{2}$, and $\tilde q^{2}=0$ forces $\langle\tilde q\rangle_{\natural}=0$; the norm is a sum of four squares of real numbers, so $\tilde q=0$. The natural square is $\tilde q\tilde q^{\natural}=\langle\tilde q\rangle_{\natural}e_t$ and vanishes under the same condition. **The one equation that does not vanish off the origin is the pair**, which is the criterion of $\mathrm{SPA}$.

**The cone over $\mathbb{R}$ belongs to the plain form, not to the norm.** The plain bilinear form

$$
\langle\tilde q_1,\tilde q_2\rangle=\mathrm{Sc}(\tilde q_1\tilde q_2)=q_{1t}q_{2t}-(\vec q_1,\vec q_2)
$$

has signature $(1,3)$ (*The 2 Forms over the Quaternioid $\mathbb{R}$ Space*), and its vanishing set is a genuine real double cone, $q_t^{2}=\lvert\vec q\rvert^{2}$, of real dimension three, whose link on the unit sphere is the disjoint union $S^{2}\sqcup S^{2}$, one sphere per nappe (*The Topology of the Zero-Divisor Cone*). The norm's vanishing set is the apex alone. Of the two bilinear structures of the article, therefore, $\langle\cdot\rangle$ carries a cone and $\langle\cdot\rangle_{\natural}$ does not, and this is the sharp form of the contrast: over $\mathbb{R}$ the cone is a property of the signature and not of the algebra. The physics corpus reads this real cone on the material sector, where the fourth coordinate is $Q_t=iq'_t$ (*Introduction to the Remarkable Subspaces of the Quaternions*).

**The units are every nonzero element, and their group is a sphere.** The invertible elements are $\mathbb{H}^{\times}=\mathbb{H}\setminus\{0\}$, a group homeomorphic to $S^{3}$, simply connected, with $\pi_x(\mathbb{H}^{\times})=0$ and $\pi_z(\mathbb{H}^{\times})\cong\mathbb{Z}$ (*The Quaternion Unit Group as a Topological Group*). The complex case is different in exactly one place: $\mathbb{B}^{\times}\simeq S^{1}\times S^{3}$, with $\pi_x(\mathbb{B}^{\times})\cong\mathbb{Z}$, the extra circle coming from the punctured complex line that the vanishing set of the norm leaves in each direction (*The Biquaternion Unit Group as a Topological Group*). The integer the complex units carry and the real ones do not is the winding of the determinant.

**The split siblings show where the cone comes from.** Replace the quaternion algebra by a split one and the empty set fills. In the split-quaternion algebra the norm is indefinite of signature $(2,2)$ and the zero-divisor set is the punctured real cone, the null set of that indefinite norm (*Split-Quaternion Zero Divisors*); in the split-complex algebra the zero divisors are the two real lines, and the algebra is the product $\mathbb{R}\times\mathbb{R}$ (*Zero Divisors of the Split-Complex Algebra*). So the cone is not an accident of the multiplication: it appears exactly when the form that decides invertibility turns indefinite, and over $\mathbb{H}$ it is absent because that form is positive definite.

**The reading.** The quaternion space is the definite base case of the family: its zero-divisor set is empty, its units are everything nonzero, and its cone is the apex. Every cone of the corpus appears when the same norm is read on a form of non-definite signature, indefinite over the split siblings and complex over the biquaternions, where it becomes a complex cone of real dimension six. The empty set is the table's first row.

## The One-Sided Inverse Equations

Of the two structures with the empty zero-divisor set only the algebra product has a two-sided unit, so the classical equivalence *zero divisor if and only if not a unit* is available for it alone, and there it is exact: for a nonzero $\tilde q$ the statements *$\tilde q$ is a zero divisor of the algebra product*, *$\langle\tilde q\rangle_{\natural}=0$* and *$\tilde q$ is not invertible* are equivalent, and all three fail off the origin (*Zero Divisors of the Quaternion Algebra*). The substitute for the general quaternionic product, whose identity $e_t$ is a left unit alone, is the one-sided inverse criterion. The criteria of the two derived structures are read in their own articles. For the general quaternionic product it reads as follows.

**Theorem (the inverse equations).** Let $\star$ be the general quaternionic product and let $\tilde q\neq0$. Then $\tilde q$ admits no annihilating factor in $\star$, and the two equations

$$
\boxed{\;\tilde q\star\tilde q_3=e_t , \qquad \tilde q_3\star\tilde q=e_t\;}
$$

have the common solution $\tilde q_3=(\tilde q^{-1})^{\natural}$; equivalently, both have a solution exactly when $\langle\tilde q\rangle_{\natural}\neq0$, which is every nonzero element.

*Proof.* The quaternion norm is multiplicative, $\langle\tilde q_1\tilde q_2\rangle_{\natural}=\langle\tilde q_1\rangle_{\natural}\langle\tilde q_2\rangle_{\natural}$ (*The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space*). If the first equation has a solution, then $\langle\tilde q^{\natural}\rangle_{\natural}\langle\tilde q_3\rangle_{\natural}=1$ and $\langle\tilde q^{\natural}\rangle_{\natural}=\langle\tilde q\rangle_{\natural}$, so $\langle\tilde q\rangle_{\natural}\neq0$. Conversely, if $\langle\tilde q\rangle_{\natural}\neq0$ then $\tilde q_3=(\tilde q^{-1})^{\natural}$ solves both equations, because $\tilde q^{\natural}(\tilde q^{-1})^{\natural}=(\tilde q^{-1}\tilde q)^{\natural}=e_t$ and $(\tilde q^{-1})^{\natural}\tilde q^{\natural}=(\tilde q\tilde q^{-1})^{\natural}=e_t$. **The general quaternionic product has no zero divisor and the one-sided inverse equations hold at every nonzero element.**

The one-sided criterion is the substitute for the classical equivalence in the general quaternionic case, where the unit is one-sided; and it is a statement about invertibility and not a group law, the product being non-associative.

## Summary

A zero divisor is defined by an equation that names a product, so the three companion products of the quaternion space define three zero-divisor sets. The set of the general quaternionic product is empty: the norm $\langle\tilde q\rangle_{\natural}=q_t^{2}+q_x^{2}+q_y^{2}+q_z^{2}$ is positive definite, it vanishes at the origin alone, and every nonzero element has the two-sided solution $(\tilde q^{-1})^{\natural}$ of the inverse equations. The symmetric plain structure has the punctured vector subspace, the plane of the pure elements, of real dimension three, and the antisymmetric plain structure has the whole punctured space. The empty set is the zero-divisor set of the general quaternionic product alone among the three, and it is contained in all three, so that it is their common core; the same empty set is the zero-divisor set of the algebra product of the space, owned by *Zero Divisors of the Quaternion Algebra*.

Read against the complex case, the emptiness has one cause. The norm is positive definite over $\mathbb{R}$, so both the square of the algebra product and the natural square vanish at the origin alone, whereas over $\mathbb{C}$ the natural square vanishes on the whole zero-divisor cone. The cone over $\mathbb{R}$ belongs to the plain bilinear form $\langle\cdot,\cdot\rangle$ of signature $(1,3)$, a real double cone of real dimension three with link $S^{2}\sqcup S^{2}$, and not to the norm; the units are every nonzero element, a group homeomorphic to $S^{3}$ with $\pi_x=0$, against the complex units $S^{1}\times S^{3}$ with $\pi_x\cong\mathbb{Z}$; and the split siblings, whose norm is indefinite, have a punctured cone for a zero-divisor set. The cone is therefore a property of a non-definite signature rather than of the multiplication, and the quaternion space is the definite base case of the table.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\star$ | one of the three companion products of $\mathbb{H}$ |
| $\tilde q_1^{\natural}\tilde q_2$ | the general quaternionic product, the one with the empty zero-divisor set |
| $\tilde q_1\tilde q_2$ | the algebra product, of the *Quaternions* category, also without zero divisors |
| $\langle\tilde q_1,\tilde q_2\rangle_{\natural}=\mathrm{Sc}(\tilde q_1^{\natural}\tilde q_2)=q_{1t}q_{2t}+(\vec q_1,\vec q_2)$ | the quaternion form, positive definite, the polar form of the norm |
| $\langle\tilde q_1,\tilde q_2\rangle=\mathrm{Sc}(\tilde q_1\tilde q_2)=q_{1t}q_{2t}-(\vec q_1,\vec q_2)$ | the plain bilinear form, of signature $(1,3)$ |
| $\langle\tilde q\rangle_{\natural}=q_t^{2}+q_x^{2}+q_y^{2}+q_z^{2}$ | the norm, the quaternion algebraic norm, the scalar of the central square $\tilde q\tilde q^{\natural}=\langle\tilde q\rangle_{\natural}e_t$ |
| $\{N=0\}=\{0\}$ | the vanishing set of the norm, the apex alone; there is no cone |
| $\varnothing$ | the zero-divisor set of $\mathrm{GQA}$ |
| $\mathrm{Vect}(\mathbb{H})\setminus\{0\}$ | the zero-divisor set of $\mathrm{SPA}$, the pure cone, of real dimension three |
| $\mathbb{H}\setminus\{0\}$ | the zero-divisor set of $\mathrm{APA}$ |
| $q_t^{2}\langle\tilde q\rangle_{\natural}$ | the determinant of the left multiplication operator of $\mathrm{SPA}$ |
| $(\tilde q^{-1})^{\natural}$ | the two-sided solution of the inverse equations in the general quaternionic product |
| $(\vec q_1,\vec q_2)$ | the plain bilinear dot product of the two vector parts |
| $\mathrm{SPA},\mathrm{APA},\mathrm{GQA}$ | the three companion structures of the space |

## Further Reading

- [Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-quaternioid-r-space.html), for the general vocabulary: the zero divisor, the annihilator, the idempotent, the nilpotent and the rest, each stated once for a general product.
- [The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space](the-2-algebraic-norms-over-the-quaternioid-r-space.html), for the norm $\langle\cdot\rangle_{\natural}$ and the two algebraic norms read at the two equal arguments.
- [The 2 Forms over the Quaternioid $\mathbb{R}$ Space](the-2-forms-over-the-quaternioid-r-space.html), for the plain and the quaternion forms and their signatures, the plain form $\langle\cdot,\cdot\rangle$ of signature $(1,3)$ whose null set is the real double cone and the definite norm $\langle\cdot\rangle_{\natural}$ whose null set is the apex.
- [Zero Divisors of the Quaternion Algebra](zero-divisors-of-the-quaternion-algebra.html), in the *Quaternions* category, for the algebra-product criterion and the invertibility of the nonzero elements.
- [Comparison Between the Two General Products](comparison-between-the-two-general-products.html), for the property table, the unit entries, the square and the radical.
- [The 6 Products of the Quaternioid Real Space](the-6-products-of-the-quaternioid-real-space.html), for the two general products and their four symmetric and antisymmetric parts.
- [The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space](the-algebraic-structures-over-the-quaternioid-r-space.html), for the three companion names and the class of each.
- [Square Roots of One and the Idempotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space](square-roots-of-one-and-the-idempotents-in-the-algebraic-structures-over-the-quaternioid-r-space.html), for the roots of $+1$ and the idempotent sets of the three companion structures.
- [Square Roots of a General Element in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space](square-roots-of-a-general-element-in-the-algebraic-structures-over-the-quaternioid-r-space.html), for the root equation at a general central value.
- [Annihilators in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space](annihilators-in-the-algebraic-structures-over-the-quaternioid-r-space.html), for the one-sided annihilators of one element and the three-row table.
- [Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space](square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-quaternioid-r-space.html), for the square-zero sets, the roots of $0$ and the three-row reading.
- [The Multiplication Operators of the Symmetric Plain Algebra](the-multiplication-operators-of-the-symmetric-plain-algebra-of-quaternioid.html), for the operator and the determinant $q_t^{2}\langle\tilde q\rangle_{\natural}$.
- [Introduction to the Remarkable Subspaces of the Quaternions](introduction-to-the-remarkable-subspaces-of-the-quaternions.html), for the scalar and the vector subspaces, the pure family and its dimension.
- [Split-Quaternion Zero Divisors](split-quaternion-zero-divisors.html) and [Zero Divisors of the Split-Complex Algebra](zero-divisors-of-the-split-complex-algebra.html), for the split siblings whose indefinite norm refills the empty set.
