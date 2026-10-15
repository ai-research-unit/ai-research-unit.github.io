# __Zero Divisors in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space__

## Introduction

Let $\star$ be a product on the quaternion algebra $\mathbb{H}$. A nonzero $\tilde p\in\mathbb{H}$ is a **zero divisor of $\star$** when it kills a nonzero partner: when $\tilde p\star\tilde q=0$ or $\tilde q\star\tilde p=0$ for some nonzero $\tilde q$. The first case makes it a left zero divisor, the second a right zero divisor, and an element of both kinds a two-sided zero divisor.

**The six names.** The space carries six products, so the generic definition poses six questions; this article answers them once for all six. Each of the six products has a three-letter code: the first letter is the operation, $\mathrm G$ the general product and $\mathrm S$, $\mathrm A$ its symmetric and antisymmetric parts; the second is the first slot, $\mathrm P$ plain and $\mathrm Q$ quaternionic; the third is the family, $\mathrm A$ the algebra over $\mathbb{R}$. The six are read in the three halves of *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space*,

| the half | the plain algebra | the quaternionic algebra |
|---|---|---|
| general | $\mathrm{GPA}$ | $\mathrm{GQA}$ |
| symmetric | $\mathrm{SPA}$ | $\mathrm{SQA}$ |
| antisymmetric | $\mathrm{APA}$ | $\mathrm{AQA}$ |

and every table of the article follows this order, half by half and, inside a half, the plain structure then the quaternionic one.

**Scope and owners.** The general vocabulary, the zero divisor, the annihilator, the idempotent and the nilpotent stated once for a general product, is *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*. The criteria of the four derived structures stay owned by their articles, cited one by one in §*The Six Structures and the Zero-Divisor Set*. The two general products and their four parts are *The 6 Products of the Quaternion Real Space* and *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, whose three-letter code is used throughout, and the two forms are *The 2 Forms over the Quaternion $\mathbb{R}$ Space*. The property table and the two unit entries are *Comparison Between the Two General Products*; the idempotents and the roots of $+1$ are *Square Roots of One and the Idempotents in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the roots of $0$, the square-zero sets and the nilpotents are *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the root equation at a general value is *Square Roots of a General Element in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; and the annihilators of one element are *Annihilators in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*. The space being real and the norm definite, the empty set is finally read against the complex case in §*The Empty Set against the Complex Case*.

## The Empty Zero-Divisor Set

**Definition.** The **zero-divisor set of the general products** is the vanishing set of the norm with the apex removed,

$$
\mathcal{Z}=\{\tilde p\in\mathbb{H}:N(\tilde p)=0\}\setminus\{0\}=\varnothing ,
$$

the norm being the quaternion norm $N(\tilde p)=p_0^{2}+p_1^{2}+p_2^{2}+p_3^{2}$ of *The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*. It is the common zero-divisor set of the two general products.

**Definition.** A subset of $\mathbb{H}$ is a **real cone** when it contains $\lambda\tilde p$ for every $\tilde p$ it contains and every $\lambda\in\mathbb{R}$. Its **apex** is the origin.

The vanishing set $\{N=0\}$ is the smallest real cone, the apex alone, of dimension zero and containing no ray; removing the apex leaves nothing.

### The Empty Set Is the Complement of the Group of Units

The elements of $\mathbb{H}$ fall into two classes, and there is no third. The invertible elements of the plain product, the units, are exactly those of non-vanishing norm, $\mathbb{H}^{\times}=\{\tilde p:N(\tilde p)\neq0\}=\mathbb{H}\setminus\{0\}$ (*Zero Divisors of the General Plain Algebra*); the origin is never a zero divisor; and the remaining elements, the zero divisors of the two general products, are none. Hence

$$
\mathbb{H}=\{0\}\cup\mathbb{H}^{\times} .
$$

So an element is a unit exactly when it lies off the vanishing set of the norm, and the zero-divisor set of the general products is the complement of the group of units with the apex removed, which is empty.

## The Six Structures and the Zero-Divisor Set

The two general products split into the six structures through the symmetrisation and the antisymmetrisation (*The 6 Products of the Quaternion Real Space*). A zero divisor names its product, so each of the six carries a zero-divisor set of its own; the table of §*Results* records them, one half to a block and, inside a block, the plain structure first, the product written by its defining formula.

**Theorem (the empty set is the mark of the two general products).** Among the six structures the zero-divisor set is empty exactly for the two general structures $\mathrm{GPA}$ and $\mathrm{GQA}$, and for no other. The four derived sets are strictly larger: the symmetric plain structure $\mathrm{SPA}$ has the punctured vector subspace $\mathrm{Vect}(\mathbb{H})\setminus\{0\}$ of real dimension three, and the three remaining structures $\mathrm{SQA}$, $\mathrm{APA}$ and $\mathrm{AQA}$ have the whole punctured space $\mathbb{H}\setminus\{0\}$.

The six structures are read one by one below; each names the product, its zero-divisor set and the reason. The two general rows are read together in §*Results*.

**Corollary (the empty set is contained in every set).** The empty set is contained in the zero-divisor set of each of the six structures, and it is equal to the set of exactly two of them, the two general products.

*Proof.* Every row of the table of §*Results* contains the empty set; the two general rows equal it, and the four others are nonempty.

The ring-theoretic picture breaks on the derived structures: the element $e_1$, whose norm is $1$, is a zero divisor of $\mathrm{SPA}$, because $e_1\bullet e_2=\tfrac12(e_1e_2+e_2e_1)=0$ for the Jordan product, and it is invertible, $e_1\bullet(-e_1)=\tfrac12(-e_1^{2}-e_1^{2})=e_0$. A zero divisor need not be a non-unit, and here the failure is not the absence of a unit, the element $e_0$ being a two-sided unit of $\mathrm{SPA}$: it is the absence of associativity, which the equivalence of the two notions needs, and which the symmetrised and antisymmetrised products lack.

### $\mathrm{GPA}$, the general plain algebra

The product is $\tilde p\tilde q$, its conjugate is $\tilde p^{\natural}$, and the form of the product is

$$
N(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p^{\natural}\tilde q)=p_0q_0+(\vec p,\vec q) ,
$$

the quaternion form of *The 2 Forms over the Quaternion $\mathbb{R}$ Space*. The norm is the form at the two equal arguments, $N(\tilde p)=N(\tilde p,\tilde p)$, the scalar of the central element $\tilde p^{\natural}\tilde p$. Write $\tilde p=p_0e_0+\vec p$ with $\vec p=p_1e_1+p_2e_2+p_3e_3$ and $\tilde p^{\natural}=p_0e_0-\vec p$. Since $e_ke_l+e_le_k=0$ for $k\neq l$ and $e_k^{2}=-e_0$, the vector part squares to $\vec p^{2}=-(p_1^{2}+p_2^{2}+p_3^{2})e_0$, so

$$
\tilde p^{\natural}\tilde p=(p_0^{2}+p_1^{2}+p_2^{2}+p_3^{2})e_0 ,
$$

and its scalar is the norm.

**The zero-divisor set is empty.** The norm is positive definite, so it vanishes at the origin alone; every nonzero element has the two-sided inverse $\tilde p^{-1}=\tilde p^{\natural}/N(\tilde p)$, and no element admits an annihilating partner. The general plain algebra is a division algebra.

The units are the elements off the vanishing set of the norm, $\mathbb{H}^{\times}=\mathbb{H}\setminus\{0\}$, a group under the plain product with the two-sided inverse $\tilde p^{-1}=\tilde p^{\natural}/N(\tilde p)$; the complement of the empty zero-divisor set is that group together with the origin, the whole space.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde p^{\natural}\tilde q$, its conjugate is $\tilde p^{\natural}$, and the form of the product is

$$
N(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p^{\natural}\tilde q)=p_0q_0+(\vec p,\vec q) .
$$

The norm is the form at the two equal arguments, the reduced norm of §*The General Plain Algebra (GPA)*, $N(\tilde p)=p_0^{2}+p_1^{2}+p_2^{2}+p_3^{2}$; the natural conjugation sends $\vec p$ to $-\vec p$, so $N(\tilde p^{\natural})=N(\tilde p)$.

**The zero-divisor set is empty.** The natural product is the plain product with the natural conjugation in the first slot, so its left multiplication by $\tilde p$ is the plain left multiplication by $\tilde p^{\natural}$; the kernel is $\{0\}$ for $\tilde p\neq0$ by §*The General Plain Algebra (GPA)*. The element is invertible, with the two-sided inverse $(\tilde p^{-1})^{\natural}$.

The element $e_0$ is a left unit alone, and every nonzero element has the two-sided solution $(\tilde p^{-1})^{\natural}$ of the inverse equations; the invertible elements are $\mathbb{H}\setminus\{0\}$, and the complement of the empty zero-divisor set is that set together with the origin, the whole space.

### $\mathrm{SPA}$, the symmetric plain algebra

The product is the Jordan product $\tilde p\bullet\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)=(p_0q_0-(\vec p,\vec q))e_0+p_0\vec q+q_0\vec p$, the symmetrisation of the plain product, so its form is the same,

$$
N(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p^{\natural}\tilde q)=p_0q_0+(\vec p,\vec q) ,
$$

and the norm is the reduced norm $N(\tilde p)=p_0^{2}+p_1^{2}+p_2^{2}+p_3^{2}$ of §*The General Plain Algebra (GPA)*.

**The zero-divisor set is the punctured vector subspace $\mathrm{Vect}(\mathbb{H})\setminus\{0\}$, of real dimension three.** If $\tilde p$ is pure, $\tilde p=\vec u$, and the partner is pure, $\tilde q=\vec v$, the product is $\tilde p\bullet\tilde q=-(\vec u,\vec v)e_0$, which vanishes exactly when $\vec u$ and $\vec v$ are orthogonal; a nonzero pure element has a nonzero orthogonal vector in the three-dimensional vector subspace. If $\tilde p$ is not pure the left multiplication operator is nonsingular, of determinant

$$
\det L^{\bullet}_{\tilde p}=p_0^{2}N(\tilde p) ,
$$

which does not vanish; the computation is in *The Multiplication Operators of the Symmetric Plain Algebra*.

The plane $p_0=0$ of the pure elements is the zero-divisor set of the structure, and the regular elements are the non-pure ones together with the origin.

The unit $e_0$ is two-sided, and every nonzero element is invertible, $e_1\bullet(-e_1)=e_0$; but the invertible elements form no group, the product being non-associative, and the complement of the zero-divisor set is not the invertible set: the origin is a non-zero-divisor that is not invertible, and every nonzero pure element is invertible while lying in the zero-divisor set.

### $\mathrm{SQA}$, the symmetric quaternionic algebra

The product is $\tfrac12(\tilde p^{\natural}\tilde q+\tilde q^{\natural}\tilde p)=N(\tilde p,\tilde q)e_0$, central, and the form of the product is

$$
N(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p^{\natural}\tilde q)=p_0q_0+(\vec p,\vec q) ,
$$

the quaternion form of *The 2 Forms over the Quaternion $\mathbb{R}$ Space*; the norm is the reduced norm $N(\tilde p)=p_0^{2}+p_1^{2}+p_2^{2}+p_3^{2}$.

**The zero-divisor set is the whole punctured space $\mathbb{H}\setminus\{0\}$.** The value is the central read of the form, $N(\tilde p,\tilde q)e_0$. The form is nondegenerate, its Gram matrix being the identity in the four coordinates, so for $\tilde p\neq0$ the equation $N(\tilde p,\tilde q)=0$ is one real linear equation in the four components of $\tilde q$ and its solutions fill a hyperplane of nonzero vectors, of real dimension three.

There is no unit — the value is central and $e_0$ acts as $N(e_0,\tilde q)e_0=q_0e_0$, not as an identity — so there is no group of units and the complement of the zero-divisor set, the whole punctured space, is the origin alone.

### $\mathrm{APA}$, the antisymmetric plain algebra

The product is the commutator $\tilde p\wedge\tilde q=\tfrac12(\tilde p\tilde q-\tilde q\tilde p)=\vec p\times\vec q$. It is alternating, so at the two equal arguments it vanishes, $\tilde p\wedge\tilde p=0$; there is no form there and no norm.

**The zero-divisor set is the whole punctured space $\mathbb{H}\setminus\{0\}$.** Every nonzero element is annihilated by itself.

There is no unit, the values lying in the vector subspace, so there is no group of units and the complement of the zero-divisor set — the whole punctured space — is the origin alone.

### $\mathrm{AQA}$, the antisymmetric quaternionic algebra

The product is the commutator $\tilde p\wedge^{\natural}\tilde q=\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)$. It is alternating, $\tilde p\wedge^{\natural}\tilde p=0$, so at the two equal arguments there is no form and no norm.

**The zero-divisor set is the whole punctured space $\mathbb{H}\setminus\{0\}$.** Every nonzero element is annihilated by itself, and the left multiplication operator has rank three off the origin.

There is no unit, the values lying in the vector subspace, so there is no group of units and the complement of the zero-divisor set is the origin alone.

## Results

The two general products share one zero-divisor set, the empty set of §*The Empty Zero-Divisor Set*. The six structures are tabulated against it, the two that coincide are separated out, and the vanishing set of the norm is read in coordinates and on its two families.

### The Six Zero-Divisor Sets

Read against the empty set and against the whole space, the six sets are

| half | structure | the product | the zero-divisor set |
|---|---|---|---|
| the general products | $\mathrm{GPA}$ | $\tilde p\tilde q$ | $\varnothing$ |
| | $\mathrm{GQA}$ | $\tilde p^{\natural}\tilde q$ | $\varnothing$ |
| the symmetric products | $\mathrm{SPA}$ | $\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$ | $\mathrm{Vect}(\mathbb{H})\setminus\{0\}$ |
| | $\mathrm{SQA}$ | $\tfrac12(\tilde p^{\natural}\tilde q+\tilde q^{\natural}\tilde p)$ | $\mathbb{H}\setminus\{0\}$ |
| the antisymmetric products | $\mathrm{APA}$ | $\tfrac12(\tilde p\tilde q-\tilde q\tilde p)$ | $\mathbb{H}\setminus\{0\}$ |
| | $\mathrm{AQA}$ | $\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)$ | $\mathbb{H}\setminus\{0\}$ |

The two general products have one and the same set, the empty one. The symmetric plain structure has the punctured vector subspace, of real dimension three. The three remaining structures, the two antisymmetric ones and the scalar-valued symmetric one, have the whole punctured space. The empty set is therefore the zero-divisor set of exactly two of the six structures, and it is contained in all six, so that it is the common core of the six. The theorem below and §*The Six Structures and the Zero-Divisor Set* prove the table, and the sections that follow read its consequences.

### The Two General Products Coincide

**Theorem (the two zero-divisor sets coincide, and they are empty).** For the two general products the zero-divisor sets coincide, and they are empty. A nonzero element $\tilde p$ is a left, a right or a two-sided zero divisor of neither of the two general products. In symbols,

$$
\{\tilde p\neq0:\tilde p\text{ admits an annihilating factor in }\star\}=\varnothing \qquad\text{for each of the two general products }\star .
$$

*Proof.* The natural product is the plain product with the natural conjugation in the first slot, so its left multiplication by $\tilde p$ is the plain left multiplication by $\tilde p^{\natural}$, and the conjugation is a bijection that leaves the norm unchanged. The kernel of the plain left multiplication by $\tilde p^{\natural}$ is $\{0\}$, the element $\tilde p^{\natural}$ being nonzero; hence a nonzero element admits no annihilating factor in either general product. For the plain product this is the division property itself: from $\tilde p\tilde q=0$ with $\tilde p\neq0$ one multiplies by $\tilde p^{-1}$ and gets $\tilde q=0$.

| product | left condition | right condition | the set |
|---|---|---|---|
| $\mathrm{GPA}$, $\tilde p\tilde q$ | $N(\tilde p)=0$ | $N(\tilde p)=0$ | $\varnothing$ |
| $\mathrm{GQA}$, $\tilde p^{\natural}\tilde q$ | $N(\tilde p)=0$ | $N(\tilde p)=0$ | $\varnothing$ |

The two rows are identical, and that is the theorem. **The word is *coincide*, not *independent*.** The zero divisor is defined by an equation that names a product, so the notion belongs to the product and the two products are two definitions, not one. What the theorem says is that in the quaternion algebra the two definitions select one and the same subset of $\mathbb{H}$, the empty one; it does not say that they must, and it does not extend to the four derived structures of §*The Six Structures and the Zero-Divisor Set*.

### The Norm in Coordinates and the Absence of a Cone

Written on the coordinates, the vanishing set common to the two general products is one real equation in the four real coordinates,

$$
p_0^{2}+p_1^{2}+p_2^{2}+p_3^{2}=0 .
$$

**Proposition (the vanishing set is the apex alone).** The set $\{N=0\}$ is the origin; the norm is positive definite and anisotropic over $\mathbb{R}$, so it cuts no cone, and the zero-divisor set of the two general products is empty.

*Proof.* The norm is a sum of four squares of real numbers, which vanishes exactly when the four coordinates vanish. A vanishing set of one point contains no ray through the origin other than the apex, so it is a cone of dimension zero; removing the apex leaves the empty set.

### The Two Families

The scalar part cuts the space into two families, and the criterion of the symmetric plain structure, the one criterion of the six that is not constant, reads differently on each.

**Definition.** An element is **pure** when its scalar part vanishes, $p_0=0$, and **non-pure** when $p_0\neq0$.

On a pure element the Jordan criterion drops the scalar coordinate and becomes an orthogonality in the vector subspace; on a non-pure element no annihilating partner exists.

| | pure, $p_0=0$ | non-pure, $p_0\neq0$ |
|---|---|---|
| the criterion of $\mathrm{SPA}$ | a nonzero pure partner orthogonal to $\vec p$ | none |
| square in the plain product | $\tilde p^{2}=-N(\tilde p)e_0$ | $\tilde p^{2}=2p_0\tilde p-N(\tilde p)e_0$ |
| structure | the zero divisors of $\mathrm{SPA}$ | the regular elements of $\mathrm{SPA}$ |
| real dimension | $3$ | $4$ |

The square of a pure element is a nonzero real multiple of $e_0$ and does not vanish, so the plain square does not detect the zero divisors of the symmetric structure; the vanishing is carried by the pair and not by the element. The two families are read in the remarkable subspaces in *Introduction to the Remarkable Subspaces of the Quaternions*: the pure family is the vector subspace, of real dimension three, and the non-pure family is its complement.

## The Empty Set against the Complex Case

The six sets of this article are read over $\mathbb{R}$, where the norm is definite and the cone is the apex alone. Four comparisons with the complex case isolate what the change of scalars supplies, and they are stated here because the real space is the base case on which the complex cone table rests.

**Proposition (over $\mathbb{R}$ the two squares vanish together).** The plain square and the natural square have the same vanishing set, the origin:

$$
\tilde p^{2}=0\iff\tilde p=0,\qquad \tilde p\tilde p^{\natural}=N(\tilde p)e_0=0\iff\tilde p=0 .
$$

Over $\mathbb{C}$ the two separate: the sesquilinear square $\tilde P\star\tilde P=\tilde P\tilde P^{*}$ still vanishes only at the origin, but the natural square $\tilde P\tilde P^{\natural}$ vanishes exactly on the zero-divisor cone (*The Squares and the Positive Cone of the Biquaternion Sesqualgebra*).

*Proof.* The norm is multiplicative, $N(\tilde p\tilde q)=N(\tilde p)N(\tilde q)$ (*The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*), so $N(\tilde p^{2})=N(\tilde p)^{2}$, and $\tilde p^{2}=0$ forces $N(\tilde p)=0$; the norm is a sum of four squares of real numbers, so $\tilde p=0$. The natural square is $\tilde p\tilde p^{\natural}=N(\tilde p)e_0$ and vanishes under the same condition. **The one equation that does not vanish off the origin is the pair**, which is the criterion of $\mathrm{SPA}$.

**The cone over $\mathbb{R}$ belongs to the plain form, not to the norm.** The plain bilinear form

$$
B(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p\tilde q)=p_0q_0-(\vec p,\vec q)
$$

has signature $(1,3)$ (*The 2 Forms over the Quaternion $\mathbb{R}$ Space*), and its vanishing set is a genuine real double cone, $p_0^{2}=\lvert\vec p\rvert^{2}$, of real dimension three, whose link on the unit sphere is the disjoint union $S^{2}\sqcup S^{2}$, one sphere per nappe (*Biquaternion Lorentzian and Conformal Geometry*). The norm's vanishing set is the apex alone. Of the two bilinear structures of the article, therefore, $B$ carries a cone and $N$ does not, and this is the sharp form of the contrast: over $\mathbb{R}$ the cone is a property of the signature and not of the algebra. The physics corpus's light cone is this real cone, read on the material sector where the time coordinate carries the factor $ict$ (*Introduction to the Remarkable Subspaces of the Quaternions*).

**The units are every nonzero element, and their group is a sphere.** The invertible elements are $\mathbb{H}^{\times}=\mathbb{H}\setminus\{0\}$, a group homeomorphic to $S^{3}$, simply connected, with $\pi_1(\mathbb{H}^{\times})=0$ and $\pi_3(\mathbb{H}^{\times})\cong\mathbb{Z}$ (*The Quaternion Unit Group as a Topological Group*). The complex case is different in exactly one place: $\mathbb{B}^{\times}\simeq S^{1}\times S^{3}$, with $\pi_1(\mathbb{B}^{\times})\cong\mathbb{Z}$, the extra circle coming from the punctured complex line that the vanishing set of the norm leaves in each direction (*The Biquaternion Unit Group as a Topological Group*). The integer the complex units carry and the real ones do not is the winding of the determinant.

**The split siblings show where the cone comes from.** Replace the quaternion algebra by a split one and the empty set fills. In the split-quaternion algebra the norm is indefinite of signature $(2,2)$ and the zero-divisor set is the punctured real cone, the null set of that indefinite norm (*Split-Quaternion Zero Divisors*); in the split-complex algebra the zero divisors are the two real lines, and the algebra is the product $\mathbb{R}\times\mathbb{R}$ (*Split-Complex Zero Divisors*). So the cone is not an accident of the multiplication: it appears exactly when the form that decides invertibility turns indefinite, and over $\mathbb{H}$ it is absent because that form is positive definite.

**The reading.** The quaternion space is the definite base case of the family: its zero-divisor set is empty, its units are everything nonzero, and its cone is the apex. Every cone of the corpus appears when the same norm is read on a form of non-definite signature, indefinite over the split siblings and complex over the biquaternions, where it becomes a complex cone of real dimension six. The empty set is the table's first row.

## The One-Sided Inverse Equations

Of the two general products only the plain one has a two-sided unit, so the classical equivalence *zero divisor if and only if not a unit* is available for it alone, and there it is exact: for a nonzero $\tilde p$ the statements *$\tilde p$ is a zero divisor of the plain product*, *$N(\tilde p)=0$* and *$\tilde p$ is not invertible* are equivalent, and all three fail off the origin (*Zero Divisors of the General Plain Algebra*). The substitute for the natural product, whose identity $e_0$ is a left unit alone, is the one-sided inverse criterion. The criteria of the four derived structures are read in their own articles. For the two general products it reads as follows.

**Theorem (the inverse equations).** Let $\star$ be one of the two general products and let $\tilde p\neq0$. Then $\tilde p$ is a zero divisor of $\star$ exactly when neither of the two equations

$$
\tilde p\star\tilde x=e_0 , \qquad \tilde x\star\tilde p=e_0
$$

has a solution; equivalently, both have a solution exactly when $N(\tilde p)\neq0$, which is every nonzero element.

*Proof.* The quaternion norm is multiplicative, $N(\tilde p\tilde q)=N(\tilde p)N(\tilde q)$ (*The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*). If the first equation has a solution, then $N(\tilde p)N(\tilde x)=N(e_0)=1$ for the plain product and $N(\tilde p^{\natural})N(\tilde x)=1$ for the natural one, and $N(\tilde p^{\natural})=N(\tilde p)$; in both cases $N(\tilde p)\neq0$. Conversely, if $N(\tilde p)\neq0$ the solutions are those of the table below, and then $\tilde p\star\tilde q=0$ forces $\tilde q=0$, by applying the solution of $\tilde x\star\tilde p=e_0$ on the left.

The solutions are written with the inverse $\tilde p^{-1}=\tilde p^{\natural}/N(\tilde p)$ of the algebra, which exists for $\tilde p\neq0$.

| product | $\tilde x$ with $\tilde p\star\tilde x=e_0$ | $\tilde x$ with $\tilde x\star\tilde p=e_0$ |
|---|---|---|
| $\tilde p\tilde q$ | $\tilde p^{-1}$ | $\tilde p^{-1}$ |
| $\tilde p^{\natural}\tilde q$ | $(\tilde p^{-1})^{\natural}$ | $(\tilde p^{-1})^{\natural}$ |

This criterion uses the fixed element $e_0$, invariant under the conjugation, and makes no appeal to a unit of the product; it reads the same in the two products, and it says that the zero-divisor set of the general products is empty.

## Summary

A zero divisor is defined by an equation that names a product, so the six products of the quaternion algebra define six zero-divisor sets. For the two general products the sets coincide: for each of them, and for a nonzero element, being a left zero divisor, being a right zero divisor and lying on the vanishing set of the norm are the same condition, the norm being $N(\tilde p)=p_0^{2}+p_1^{2}+p_2^{2}+p_3^{2}=\mathrm{Sc}(\tilde p^{\natural}\tilde p)$ of *The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*.

The common set is the empty set. The norm is a sum of four squares, its vanishing set is the origin alone, and every nonzero element is a unit with the two-sided inverse $\tilde p^{-1}=\tilde p^{\natural}/N(\tilde p)$; the space is the disjoint union $\mathbb{H}=\{0\}\cup\mathbb{H}^{\times}$, with no zero-divisor term. The scalar part cuts the space into the pure family, of real dimension three, which is the zero-divisor set of $\mathrm{SPA}$, and the non-pure family, of real dimension four, on which $\mathrm{SPA}$ has no zero divisor.

The annihilators of a fixed element are *Annihilators in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the square-zero sets and the roots of $0$ are *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*. The empty set is the zero-divisor set of the two general products alone: the symmetric plain structure has the punctured vector subspace, and the two antisymmetric structures together with the scalar-valued symmetric one have the whole punctured space. The empty set is contained in all six sets and is the largest subset on which they agree. What a product does not change is the detection of the units: an element of nonzero norm has the two-sided inverse $\tilde p^{-1}$ for the plain product and the one-sided solution $(\tilde p^{-1})^{\natural}$ for the natural one, and the one-sided inverse equations replace the classical equivalence for the natural product, which has no two-sided unit.

Read against the complex case, the emptiness has one cause. The norm is positive definite over $\mathbb{R}$, so both the plain square and the natural square vanish at the origin alone, whereas over $\mathbb{C}$ the natural square vanishes on the whole zero-divisor cone. The cone over $\mathbb{R}$ belongs to the plain bilinear form $B$ of signature $(1,3)$, a real double cone of real dimension three with link $S^{2}\sqcup S^{2}$, and not to the norm; the units are every nonzero element, a group homeomorphic to $S^{3}$ with $\pi_1=0$, against the complex units $S^{1}\times S^{3}$ with $\pi_1\cong\mathbb{Z}$; and the split siblings, whose norm is indefinite, have a punctured cone for a zero-divisor set. The cone is therefore a property of a non-definite signature rather than of the multiplication, and the quaternion space is the definite base case of the table.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\star$ | one of the six products of $\mathbb{H}$; the two general products in the theorems |
| $\tilde p\tilde q$, $\tilde p^{\natural}\tilde q$ | the two general products |
| $N(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p^{\natural}\tilde q)=p_0q_0+(\vec p,\vec q)$ | the quaternion form, positive definite, the polar form of the norm |
| $B(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p\tilde q)=p_0q_0-(\vec p,\vec q)$ | the plain bilinear form, of signature $(1,3)$ |
| $N(\tilde p)=p_0^{2}+p_1^{2}+p_2^{2}+p_3^{2}$ | the reduced norm, the quaternion bilinear algebraic norm, the scalar of the central square $\tilde p\tilde p^{\natural}=N(\tilde p)e_0$ |
| $\{N=0\}=\{0\}$ | the vanishing set of the norm, the apex alone; there is no cone |
| $\varnothing$ | the zero-divisor set of the two general products |
| $\mathrm{Vect}(\mathbb{H})\setminus\{0\}$ | the zero-divisor set of $\mathrm{SPA}$, the pure cone, of real dimension three |
| $\mathbb{H}\setminus\{0\}$ | the zero-divisor set of $\mathrm{SQA}$, $\mathrm{APA}$ and $\mathrm{AQA}$ |
| $p_0^{2}N(\tilde p)$ | the determinant of the left multiplication operator of $\mathrm{SPA}$ |
| $\tilde p^{-1}=\tilde p^{\natural}/N(\tilde p)$ | the inverse of a nonzero element |
| $(\vec p,\vec q)$ | the plain bilinear dot product of the two vector parts |
| $\mathrm{GPA},\dots,\mathrm{AQA}$ | the six structures of the space: the two general products and their four symmetric and antisymmetric parts |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternion-r-space.md`), for the general vocabulary: the zero divisor, the annihilator, the idempotent, the nilpotent and the rest, each stated once for a general product.
- *The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-2-algebraic-norms-over-the-quaternion-r-space.md`), for the norm $N$ and the two algebraic norms read at the two equal arguments.
- *The 2 Forms over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternion-r-space.md`), for the plain and the quaternion forms and their signatures, the plain form $B$ of signature $(1,3)$ whose null set is the real double cone and the definite norm $N$ whose null set is the apex.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra-of-quaternions.md`), for the plain-product criterion and the invertibility of the nonzero elements.
- *Comparison Between the Two General Products* (`articles_maths/comparison-between-the-two-general-products.md`), for the property table, the unit entries, the square and the radical.
- *The 6 Products of the Quaternion Real Space* (`articles_maths/the-6-products-of-the-quaternion-real-space.md`), for the two general products and their four symmetric and antisymmetric parts.
- *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-algebraic-structures-over-the-quaternion-r-space.md`), for the six names, the three letters of each and the class of each.
- *Square Roots of One and the Idempotents in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/square-roots-of-one-and-the-idempotents-in-the-algebraic-structures-over-the-quaternion-r-space.md`), for the roots of $+1$ and the idempotent sets of the six structures.
- *Square Roots of a General Element in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/square-roots-of-a-general-element-in-the-algebraic-structures-over-the-quaternion-r-space.md`), for the root equation at a general central value.
- *Annihilators in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/annihilators-in-the-algebraic-structures-over-the-quaternion-r-space.md`), for the one-sided annihilators of one element and the six-row table.
- *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-quaternion-r-space.md`), for the square-zero sets, the roots of $0$ and the six-row reading.
- *The Multiplication Operators of the Symmetric Plain Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-plain-algebra-of-quaternions.md`), for the operator and the determinant $p_0^{2}N(\tilde p)$.
- *Zero Divisors of the Symmetric Plain Algebra* (`articles_maths/zero-divisors-of-the-symmetric-plain-algebra-of-quaternions.md`), for the criterion $p_0=0$ and the annihilator planes.
- *Zero Divisors of the Symmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the scalar-valued product and its hyperplane annihilators.
- *Zero Divisors of the Antisymmetric Plain Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-plain-algebra-of-quaternions.md`) and *Zero Divisors of the Antisymmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-quaternionic-algebra-of-quaternions.md`), for the two alternating structures whose zero-divisor set is the whole punctured space.
- *Zero Divisors of the General Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-algebra-of-quaternions.md`), for the natural product's criterion and the coincidence of its two annihilators.
- *Introduction to the Remarkable Subspaces of the Quaternions* (`articles_maths/introduction-to-the-remarkable-subspaces-of-the-quaternions.md`), for the scalar and the vector subspaces, the pure family and its dimension.
- *The Isotropic Structure of the General Quaternionic Algebra* (`articles_maths/the-isotropic-structure-of-the-general-quaternionic-algebra-of-quaternions.md`), for the isotropic cones of the plain and the quaternion forms, which are not the vanishing set of the norm.
- *The Squares and the Positive Cone of the Biquaternion Sesqualgebra* (`articles_maths/the-squares-and-the-positive-cone-of-the-biquaternion-sesqualgebra.md`), for the complex separation of the two squares that this article sees coincide over $\mathbb{R}$.
- *Biquaternion Lorentzian and Conformal Geometry* (`articles_maths/biquaternion-lorentzian-and-conformal-geometry.md`), for the Minkowski slice, its light cone and its link $S^{2}\sqcup S^{2}$, of which the real cone of $B$ is the coordinate form.
- *The Quaternion Unit Group as a Topological Group* (`articles_maths/the-quaternion-unit-group-as-a-topological-group.md`), for $\mathbb{H}^{\times}\simeq S^{3}$ and its homotopy groups.
- *The Biquaternion Unit Group as a Topological Group* (`articles_maths/the-biquaternion-unit-group-as-a-topological-group.md`), for the complex units $S^{1}\times S^{3}$, the covering and the generator of $\pi_1\cong\mathbb{Z}$.
- *Split-Quaternion Zero Divisors* (`articles_maths/split-quaternion-zero-divisors.md`) and *Split-Complex Zero Divisors* (`articles_maths/split-complex-zero-divisors.md`), for the two split siblings in which the indefinite norm fills the empty set with a punctured cone.
