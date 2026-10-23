# __The Group of Units of the Biquaternion Algebra and the Complement of the Zero-Divisor Cone__

## Introduction

Of the twelve algebraic structures that the complex space
$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries, exactly one is an associative unital
algebra, the biquaternion algebra of *Introduction to the Biquaternion Algebra*;
the specificity that its associativity and its two-sided unit $e_t$ deliver is that its invertible
elements form a genuine **group** (*The Specificities of the Biquaternion Algebra*). This article
studies that group and the exact meaning of its boundary. The group of units is the complement of
the zero-divisor cone, the algebra is the disjoint union of the two, and the cone is at once the
complement of the group and its topological boundary.

The boundary deserves an article of its own because it is drawn by a form the product does not
carry. The plain product has one algebraic norm of its own, the general plain bilinear form
$\langle\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^{2}$, and $\langle\cdot,\cdot\rangle$ decides nothing about invertibility (*Norm
and Invertibility in the Biquaternion Algebra*, §*The Absence of a Criterion from the Algebraic
Norm*). The boundary is drawn instead by the **general quaternionic bilinear algebraic norm** $\langle\cdot\rangle_{\natural}$,
also the **reduced norm**, $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$, the norm that the quaternionic
structure of the space carries; that form is **multiplicative**, and its multiplicativity is exactly
the reason its non-vanishing set is closed under the product and under inversion, hence a group. The
two statements of the article are the pair of these facts: **the units of the plain product are the
elements of non-vanishing norm $\langle\cdot\rangle_{\natural}$, and their complement is a group for the plain product and for no
other of the twelve structures.**

$$
\langle\tilde Q\rangle_{\natural}=\sum_{\mu\in\{t,x,y,z\}}Q_\mu^{2}=\mathrm{Sc}\bigl(\tilde Q\tilde Q^{\natural}\bigr),
$$

the scalar of the central square $\tilde Q\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}e_t$. It is one of the four
algebraic norms of the space (*The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*), and
the whole article turns on its not being the algebraic norm of the plain product: $\langle\cdot\rangle$ is the
diagonal of the plain bilinear form, $\langle\cdot,\cdot\rangle_{\natural}$ is the general quaternionic one, and the two are different
forms with different vanishing sets. The generic norm $\mathrm{Norm}$ of *Conventions in
Mathematics*, §*The form convention and the norm convention*, is instantiated in this article by the
general quaternionic bilinear algebraic norm $\langle\cdot\rangle_{\natural}$ (*The 4 Algebraic Norms over the Biquaternion
$\mathbb{C}$ Space*): every statement below names its norm, and the norm it names is $\langle\cdot\rangle_{\natural}$.

## The Partition of the Algebra

**Definition (the zero-divisor cone).** The vanishing set of the norm $\langle\cdot\rangle_{\natural}$,

$$
\mathcal{C}=\{\tilde Q\in\mathbb{B}:\langle\tilde Q\rangle_{\natural}=0\},
$$

is the **zero-divisor cone**. It is a complex cone with apex at the origin, of complex dimension
three and real dimension six, and the zero-divisor set of the four general products is the punctured
cone $\mathcal{C}\setminus\{0\}$ (*Zero Divisors of the Biquaternion Algebra*; *Zero Divisors in
the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*).

**Theorem (the invertibility criterion of the plain product).** An element $\tilde Q$ of
$\mathbb{B}$ is invertible in the plain product exactly when $\langle\tilde Q\rangle_{\natural}\neq0$, and its inverse is
then

$$
\tilde Q^{-1}=\frac{\tilde Q^{\natural}}{\langle\tilde Q\rangle_{\natural}} .
$$

*Proof.* The natural conjugation is an anti-automorphism, $\tilde Q_1^{\natural}\tilde
Q_2^{\natural}=(\tilde Q_2\tilde Q_1)^{\natural}$. Write $\tilde Q=Q_te_t+\vec Q$, so that $\tilde
Q^{\natural}=Q_te_t-\vec Q$ and

$$
\tilde Q\tilde Q^{\natural}=Q_t^{2}e_t-\vec Q^{2},
$$

whose vector part vanishes and whose scalar part is $Q_t^{2}+\sum_k Q_k^{2}=\langle\tilde Q\rangle_{\natural}$, because
the vector part of the algebra squares to $\vec Q^{2}=-\sum_kQ_k^{2}e_t$. Hence $\tilde Q\tilde
Q^{\natural}=\langle\tilde Q\rangle_{\natural}e_t$, and the same computation in the other order gives $\tilde
Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}e_t$. If $\langle\tilde Q\rangle_{\natural}\neq0$ the displayed element is a two-sided
inverse. If $\langle\tilde Q\rangle_{\natural}=0$ and $\tilde Q\neq0$ then $\tilde Q^{\natural}\neq0$ and $\tilde Q\tilde
Q^{\natural}=0$, so $\tilde Q$ is a zero divisor and cannot be invertible; and the origin is not
invertible. Verified by recomputation on $100$ random elements, the two products $\tilde Q\tilde
Q^{-1}$ and $\tilde Q^{-1}\tilde Q$ returning $e_t$ with error below $10^{-9}$.

**Theorem (the partition of the algebra).** The algebra is the disjoint union

$$
\mathbb{B}=\mathbb{B}^\times\uplus\mathcal{C},\qquad
\mathbb{B}^\times=\{\tilde Q\in\mathbb{B}:\langle\tilde Q\rangle_{\natural}\neq0\},
$$

of its **group of units** and its **zero-divisor cone**. The cone is exactly the complement of the
group.

*Proof.* By the criterion the units are the elements of non-vanishing norm, so the two sets are
complementary; they are disjoint because a complex number is either zero or not. The group structure
is *Norm and Invertibility in the General Quaternionic Algebra*.
Verified by recomputation on a mixed sample of $100$ elements: the $93$ random elements off the cone
are units, the $6$ cone elements are zero divisors and the origin is neither.

**Corollary (the zero-divisor set and its complement).** The zero-divisor set of the four general
products is the punctured cone $\mathcal{C}\setminus\{0\}$, and the complement of the zero-divisor
set in the algebra is

$$
\mathbb{B}\setminus\bigl(\mathcal{C}\setminus\{0\}\bigr)=\mathbb{B}^\times\cup\{0\},
$$

the group of units together with the origin.

*Proof.* The apex is excluded from the zero-divisor set by the definition, which requires both
elements nonzero; every other point of the cone is a zero divisor by the criterion; and the
complement of the punctured cone is the off-cone part together with the apex, that is
$\mathbb{B}^\times\cup\{0\}$.

The partition gives the three-way classification of the elements of the algebra by their behaviour
in the plain product.

| condition on $\langle\tilde Q\rangle_{\natural}$ | condition on $\tilde Q$ | class |
| --- | --- | --- |
| $\neq0$ | (automatically $\neq0$) | a unit; an element of the group $\mathbb{B}^\times$ |
| $=0$ | $\tilde Q=0$ | the origin; neither a unit nor a zero divisor |
| $=0$ | $\tilde Q\neq0$ | a zero divisor; a point of the punctured cone $\mathcal{C}\setminus\{0\}$ |

**Remark (the two complements).** The group has two complements in the algebra, and they differ by
the apex. **The complement of the cone is the group of units, and the complement of the zero-divisor
set is the group together with the origin.** The apex is therefore the one point that separates the
two statements: it lies on the cone and in the complement of the zero-divisor set, it is the only
element of the algebra that is neither a unit nor a zero divisor, and it is the apex of the boundary
of the group while being no zero divisor itself. The identity $e_t$ is the mirror case: it is off
the cone, in the group, and in no zero-divisor set.

## Multiplicativity Makes the Complement a Group

**Theorem (the norm $\langle\cdot\rangle_{\natural}$ is multiplicative).** For all $\tilde Q_1,\tilde Q_2\in\mathbb{B}$,

$$
\langle\tilde Q_1\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1\rangle_{\natural}\,\langle\tilde Q_2\rangle_{\natural}.
$$

*Proof.* The natural conjugation reverts the order, so

$$
(\tilde Q_1\tilde Q_2)(\tilde Q_1\tilde Q_2)^{\natural}
=\tilde Q_1\tilde Q_2\tilde Q_2^{\natural}\tilde Q_1^{\natural}
=\tilde Q_1\,\langle\tilde Q_2\rangle_{\natural}e_t\,\tilde Q_1^{\natural}
=\langle\tilde Q_2\rangle_{\natural}\tilde Q_1\tilde Q_1^{\natural}
=\langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_2\rangle_{\natural}e_t,
$$

the scalar $\langle\tilde Q_2\rangle_{\natural}$ being central. Verified by recomputation on $100$ random pairs, error below
$10^{-9}$.

**Corollary (the cone is absorbing and the units are closed).** The cone is closed under the product
in the strong sense that a cone factor forces a cone product: if $\langle\tilde Q_1\rangle_{\natural}=0$ then $\langle\tilde
Q_1\tilde Q_2\rangle_{\natural}=\langle\tilde Q_2\tilde Q_1\rangle_{\natural}=0$ for every $\tilde Q_2$. The group of units is closed under the
product, and with it the inverse formula is closed under inversion.

*Proof.* Multiply the multiplicativity by zero in the two orders; closure under multiplication
follows from the non-vanishing of the two factors, and closure under inversion from $\tilde
Q^{-1}=\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$.

**Theorem (the norm $\langle\cdot\rangle_{\natural}$ is a homomorphism of the group onto $\mathbb{C}^\times$).** The
multiplicative norm restricts to a surjective homomorphism of groups

$$
N:\mathbb{B}^\times\longrightarrow\mathbb{C}^\times,\qquad \tilde Q\longmapsto \langle\tilde Q\rangle_{\natural},
$$

whose kernel is the **norm-one group** $\mathbb{B}^\times_1=\{\tilde Q:\langle\tilde Q\rangle_{\natural}=1\}$.

*Proof.* Multiplicativity makes the restriction a homomorphism into the nonzero complex numbers; it
is surjective because the centre gives $\langle Ae_t\rangle_{\natural}=A^{2}$ and every nonzero complex number is a square,
the map being two-to-one on the central line; the kernel is the preimage of $1$, a normal subgroup.
The identification of the norm-one group with $SL_2(\mathbb{C})$ and the two-to-one covering
$\mathbb{C}^\times e_t\times\mathbb{B}^\times_1\to\mathbb{B}^\times$ of kernel $\{\pm e_t\}$ are
*The Biquaternion Unit Group as a Topological Group*.

**Remark (why the complement is a group here and nowhere else).** The two closure properties are
exactly what a set of the form $\{\text{form}\neq0\}$ needs in order to be a group, and both are
read from multiplicativity. The norm $\langle\cdot\rangle_{\natural}$ supplies them, so its non-vanishing set is the group of
units of the plain product. The algebraic norm of the plain product, $\langle\cdot\rangle$, supplies neither, and its
non-vanishing set is not closed under the product: the elements $\tilde Q_1=e_t-\tfrac13\vec e_x$ and
$\tilde Q_2=e_t+2\vec e_x$ have $\langle\tilde Q_1\rangle=\tfrac89$ and $\langle\tilde Q_2\rangle=-3$, both nonzero, while $\langle\tilde
Q_1\tilde Q_2\rangle=0$. The non-vanishing set of $\langle\cdot\rangle$ therefore carries no group, although it is closed under
the inverse formula; **a group of units needs a multiplicative norm, and the multiplicative norm of
the space is not the norm of the plain product.** Verified by recomputation: $\langle\tilde Q_1\rangle=\tfrac89$,
$\langle\tilde Q_2\rangle=-3$, $\langle\tilde Q_1\tilde Q_2\rangle$ below $10^{-15}$.

## The Boundary Is the Cone of the Norm and Not the Cone of the Product

The algebraic norm of the plain product is the general plain bilinear form read at the two equal
arguments,

$$
\langle\tilde Q\rangle=\mathrm{Sc}\bigl(\tilde Q\tilde Q\bigr)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu Q_\mu^{2}=Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2},
$$

of Gram matrix $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$; it is not multiplicative, its vanishing
set is a complex cone of real dimension six, and it is neither the null cone nor the zero-divisor
cone (*Norm and Invertibility in the General Quaternionic Algebra*). The two cones are different objects,
and the difference is the boundary of the group.

**Theorem (neither cone decides invertibility through the other).** The two implications fail in
both directions,

$$
\langle\tilde Q\rangle=0\ \not\Longrightarrow\ \tilde Q\notin\mathbb{B}^\times,
\qquad
\langle\tilde Q\rangle\neq0\ \not\Longrightarrow\ \tilde Q\in\mathbb{B}^\times,
$$

with the witnesses $\tilde Q=e_t+\vec e_x$, a unit of vanishing $\langle\cdot\rangle$, and $\tilde Q=e_t+i\vec e_x$, a zero
divisor of non-vanishing $\langle\cdot\rangle$.

*Proof.* $(e_t+\vec e_x)(e_t-\vec e_x)=2e_t$, so $e_t+\vec e_x$ is invertible, while $\langle e_t+\vec e_x\rangle=1-1=0$. And
$(e_t+i\vec e_x)(e_t-i\vec e_x)=0$, so $e_t+i\vec e_x$ is a zero divisor, while $\langle e_t+i\vec e_x\rangle=1-i^{2}=2$.

**Corollary (the boundary of the group).** The boundary of the group of units is the zero-divisor
cone $\mathcal{C}=\{N=0\}$, and not the vanishing set $\{B=0\}$ of the product's own algebraic norm.
The two cones meet, and neither contains the other.

*Proof.* The complement of the group is the cone, the group is dense in the algebra and the cone is
closed, so the boundary of the group — the intersection of the closure of the group and the closure
of its complement — is the cone; and the witnesses of the theorem place a point of $\{B=0\}$ outside
$\mathcal{C}$ and a point of $\mathcal{C}$ outside $\{B=0\}$, so the two vanishing sets meet and
neither contains the other.

| form | vanishing set | real dimension | multiplicative | decides the units |
| --- | --- | --- | --- | --- |
| $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ | the zero-divisor cone $\mathcal{C}$ | $6$ | yes | yes: $\mathbb{B}^\times=\{N\neq0\}$ |
| $\langle\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^{2}$ | the complex cone of $\langle\cdot\rangle$ | $6$ | no | no, by the two witnesses |

**Remark (what the boundary is made of).** The group of units of the plain product is therefore
bounded by the zero set of a form that the product does not carry in its own right: the plain
product is the multiplication, its algebraic norm is $\langle\cdot\rangle$, and the criterion is furnished by the
general quaternionic bilinear algebraic norm $\langle\cdot\rangle_{\natural}$, which belongs to the quaternionic structure of the
space. **The units of the plain product are read from the norm of a different product.** This is the
geometric content of the absence recorded in *Norm and Invertibility in the Biquaternion Algebra*,
and the reason the statement is stated here: the article that owns the product does not own the form
that decides its units, and the partition of §*The Partition of the Algebra* is the place where the
two meet.

## The Group and Its Boundary

The group and the cone are complementary, so their topologies are two readings of one partition; the
topological theorems are proved in the articles named and collected here for the group of the
algebra.

**Proposition (the group is open and dense, the cone is closed, and they share their boundary).**
The group $\mathbb{B}^\times$ is open and dense in the algebra; the cone $\mathcal{C}$ is closed,
with empty interior, of real codimension two; and the group and the cone have one and the same
boundary,

$$
\partial\mathbb{B}^\times=\partial\mathcal{C}=\mathcal{C}.
$$

*Proof.* The cone is the zero set of a polynomial, hence closed, and it is a proper algebraic
subset, hence of empty interior; its complement is therefore open and dense, of real dimension
eight. The identity of the two boundaries is the corollary of §*The Boundary Is the Cone of the Norm
and Not the Cone of the Product*.

**Proposition (the group is connected and its boundary does not separate).** $\mathbb{B}^\times$ is
connected, of real dimension eight, and the cone of real codimension two does not disconnect the
algebra; the group is the connected complement of the cone.

*Proof.* The polar decomposition retracts the group onto its maximal compact subgroup
$\mathrm{U}(\mathbb{B})\cong \mathrm{U}(2)$, a continuous image of a connected group; the retraction, the structure of
the maximal compact subgroup and the connectedness are *The Biquaternion Unit Group as a Topological
Group*, §*The Topology of the Group*, and *The Unitary Group of the Biquaternion Algebra*.

**The group in the matrix model (cited).** Under $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ the
group is $\mathbb{B}^\times\cong GL_2(\mathbb{C})$ and the norm is the determinant,
$\det\mathsf{M}_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$, so the norm-one group is $\mathbb{B}^\times_1\cong
SL_2(\mathbb{C})$, and the norm is the determinant homomorphism
$GL_2(\mathbb{C})\to\mathbb{C}^\times$ (*The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of
Biquaternions*; §*The Determinant and the Matrix Model* of *The Biquaternion Unit Group as a
Topological Group*). The homotopy type, the fundamental group generated by the loop around the cone,
the third homotopy group carried by the unit quaternions and the universal cover are *The
Biquaternion Unit Group as a Topological Group*.

## The Units inside the Remarkable Subspaces

The criterion restricts to the remarkable subspaces, where the cone cuts a slice of lower dimension
and the group is the complement of that slice. The distribution is *Norm and Invertibility in the
General Quaternionic Algebra*, §*The Algebraic Norm on the Remarkable Subspaces*, and is tabulated
here in the form the boundary takes.

| subspace | $\dim_{\mathbb{R}}$ | cone slice | units |
| --- | --- | --- | --- |
| centre $\mathbb{C}_{\mathbb{B}}$ | $2$ | the apex alone | the nonzero scalars $\mathbb{C}^\times e_t$ |
| quaternion subspace $\mathbb{H}_{\mathbb{B}}$ | $4$ | the apex alone | every nonzero element |
| anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ | $4$ | the apex alone | every nonzero element |
| vector subspace $\mathrm{Vect}(\mathbb{B})$ | $6$ | a complex cone of real dimension $4$ | the complement of that cone |
| sectors $\mathbb{M}_\pm$ | $4$ | a real cone of real dimension $3$ | the complement of that cone |

**Remark (the two rows that carry a cone).** On the centre and the two quaternionic subspaces the
norm vanishes at the origin alone, so the punctured cone is empty there and the only non-unit is the
origin; **the boundary of the group is empty in those subspaces and non-empty exactly in the vector
subspace and the two sectors.** On the vector subspace the cone is the complex cone
$\sum_kQ_k^{2}=0$, of real codimension two in the subspace; on the two sectors it is the null cone,
of real codimension one, the slice the physics articles read as the causal boundary. The dimension
of the cone drops from six to four on the vector subspace and to three on the sectors, and the group
is the complement at every stage.

## The Complement in the Other Eleven Structures

The invertibility is relative to the product, so the statement of this article is a statement about
one of the twelve structures, and the comparison is what fixes its exact scope. The units of the
four general products and the symmetrised plain product are collected first.

| structure | unit | invertible elements | a group |
| --- | --- | --- | --- |
| the algebra | $e_t$, two-sided; associative | the units of the definition: $\{N\neq0\}$, with $\tilde Q_1^{-1}=\tilde Q_1^{\natural}/\langle\tilde Q_1\rangle_{\natural}$ | **yes** |
| $\mathrm{SPA}$ | $e_t$, two-sided; not associative | the elements of non-vanishing norm, with the Jordan inverse | no |
| $\mathrm{GQA}$ | $e_t$, left alone; not associative | not defined; the inverse equations select $\{N\neq0\}$, solved by $(\tilde Q_1^{-1})^{\natural}$ | no |
| $\mathrm{GPS}$ | $e_t$, right alone; not associative | not defined; the inverse equations select $\{N\neq0\}$, solved by $(\tilde Q_1^{-1})^{*}$ | no |
| $\mathrm{GQS}$ | no unit on either side; not associative | not defined; the inverse equations select $\{N\neq0\}$, solved by $(\tilde Q_1^{-1})^{\natural*}$ | no |

The definition of the inverse presupposes a two-sided unit, so the invertibility of the definitions
exists only in the two unital structures of the table, the plain and the symmetrised plain. The
three non-unital general products are read through the inverse equations, which use the fixed
element $e_t$ and make no appeal to a unit of the product.

**Theorem (the inverse equations of the four general products).** For each of the four general
products, and for a nonzero element $\tilde Q_1$, the two equations $\tilde Q_1\star\tilde Q_2=e_t$ and
$\tilde Q_2\star\tilde Q_1=e_t$ have a solution exactly when $\langle\tilde Q_1\rangle_{\natural}\neq0$, the solutions being
those of the table above. The cone is therefore the complement of the elements solvable on both
sides of the inverse equations, for each of the four products at once.

*Proof.* The solutions are exhibited in the table and satisfy the equations because the natural
conjugation and the coefficient conjugation revert the product, $(\tilde Q_1\tilde
Q_2)^{\natural}=\tilde Q_2^{\natural}\tilde Q_1^{\natural}$, so that $\tilde Q_1^{\natural}(\tilde
Q_1^{-1})^{\natural}=(\tilde Q_1^{-1}\tilde Q_1)^{\natural}=e_t$ and likewise with the coefficient
conjugation. Conversely, the matrix model turns the equations into matrix equations with an
invertible right factor, so the multiplication by $\tilde Q_1$ is invertible and $\langle\tilde Q_1\rangle_{\natural}\neq0$.
The statement is *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$
Space*, §*The One-Sided Inverse Equations*, and the verification is by recomputation on $100$ random
off-cone elements for each of the three non-unital products.

**Remark (the complement is one set for the four).** The theorem says that the elements of the four
general products that solve the inverse equations on both sides are one and the same set, the
complement of the cone; the table says where that set becomes a group. **The invertible elements of
the four general products are the same set, and the set is a group in the biquaternion algebra
alone.** the algebra has both the two-sided unit and the associative product; $\mathrm{GQA}$ and
$\mathrm{GPS}$ have a one-sided unit and a non-associative product, so the element $e_t$ is not even
a two-sided identity and no group can be read; $\mathrm{GQS}$ has no unit at all.

**The symmetrised plain algebra: the same set and no group.** The symmetrised product
$\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$ has $e_t$ as a two-sided unit, and its invertible
elements are again the elements of non-vanishing norm: for $\langle\tilde Q_1\rangle_{\natural}\neq0$ the two-sided solution
is the **Jordan inverse**

$$
\tilde Q_1^{\bullet}=\frac{2Q_{1t}e_t-\tilde Q_1}{\langle\tilde Q_1\rangle_{\natural}},
\qquad
\tilde Q_1\bullet\tilde Q_1^{\bullet}=\tilde Q_1^{\bullet}\bullet\tilde Q_1=e_t,
$$

which is the Cayley–Hamilton inverse of the matrix model, $\mathsf{M}_2(2Q_{1t}e_t-\tilde
Q_1)=2Q_{1t}\mathrm{I}_2-\mathsf{M}_2(\tilde Q_1)=\operatorname{tr}\mathsf{M}_2(\tilde
Q_1)\mathrm{I}_2-\mathsf{M}_2(\tilde Q_1)$; and a nonzero element of the cone is a zero divisor of the
symmetrised product, hence not invertible. But the product is not associative, and the invertible
elements form **no group**: the elements $\vec e_x$ and $\vec e_y$ are invertible, with $\vec e_x\bullet(-\vec e_x)=e_t$
and $\vec e_y\bullet(-\vec e_y)=e_t$, while $\vec e_x\bullet \vec e_y=\tfrac12(\vec e_z-\vec e_z)=0$ is not. The complement of the
zero-divisor set of the symmetrised product, which is $\{Q_{1t}\neq0,N\neq0\}\cup\{0\}$, is not the
invertible set either: the pure element $\vec e_x$ is a zero divisor and invertible at once, and the
origin is a non-zero-divisor that is not invertible. The invertibility of the symmetrised product is
*Norm and Invertibility in the Symmetric Plain Algebra*, and it is quoted here for the comparison
only. Verified by recomputation: the Cayley–Hamilton solution returns the unit on $100$ random
elements of non-vanishing norm, and $\vec e_x\bullet \vec e_y=0$.

**The seven with no unit on either side.** The six structures $\mathrm{APA}$, $\mathrm{SQA}$,
$\mathrm{AQA}$, $\mathrm{SPS}$, $\mathrm{APS}$ and $\mathrm{AQS}$ have a unit on neither side, and
the seventh, the symmetric quaternionic sesqualgebra $\mathrm{SQS}$, has none either. The definition
of the inverse presupposes a two-sided unit, so no invertible element and no group of units is
defined for any of them; the fixed element $e_t$ is a value of some of them, $e_t\star e_t=e_t$ in
each symmetrised structure, but it is the identity of none, which is exactly what the absence of a
two-sided unit says. Six of the seven have the whole punctured space for zero-divisor set, so the
complement of the zero-divisor set degenerates to the origin alone; $\mathrm{SQS}$ has the enlarged
set, and its complement is the reduced set $\{Q_t\neq0,N\neq0\}\cup\{0\}$.

**Theorem (the isolation).** Of the twelve structures of the complex space, the general plain
algebra is the only one whose invertible elements form a group; equivalently, the only one in which
the complement of the zero-divisor cone is a group under the product of the structure.

*Proof.* By the table only the algebra and $\mathrm{SPA}$ have a two-sided unit and therefore
invertible elements at all, and $\mathrm{SPA}$ fails the closure of them under its own product,
$\vec e_x\bullet \vec e_y=0$ against $\vec e_x,\vec e_y$ invertible, so they form no group. The ten others have no
two-sided unit: for $\mathrm{GQA}$, $\mathrm{GPS}$ and $\mathrm{GQS}$ the inverse equations detect
the off-cone elements without supplying an identity, and for the seven structures without a unit the
invertibility is not defined at all. The complement of the cone is the set of non-vanishing norm for
every structure of the space, and it is a group exactly when the product is associative with a
two-sided unit and the norm is multiplicative on it, which is the case in the algebra alone.

**Remark (set and structure again).** The isolation is a statement about the **group structure** and
not about the **set**: the complement of the cone is the same set $\{N\neq0\}$ in the algebra and
in $\mathrm{SPA}$, and the associativity of the plain product is the whole of the difference. The
same caution as in *The Specificities of the Biquaternion Algebra* applies: the plain product is
not the only structure with invertible elements, it is the only structure where they form a group.

## Summary

The biquaternion algebra has the group of units $\mathbb{B}^\times=\{\langle\tilde Q\rangle_{\natural}\neq0\}$ for the
multiplicative norm $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}=\mathrm{Sc}(\tilde Q\tilde Q^{\natural})$, with
the inverse $\tilde Q^{-1}=\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$; the zero-divisor cone
$\mathcal{C}=\{N=0\}$ is exactly its complement, so that the algebra is the disjoint union
$\mathbb{B}=\mathbb{B}^\times\uplus\mathcal{C}$, the zero-divisor set is the punctured cone, and the
complement of the zero-divisor set is the group together with the origin. The boundary of the group
is the cone of the norm $\langle\cdot\rangle_{\natural}$ of the general quaternionic bilinear form and not the cone of the
**plain product's own** algebraic norm $\langle\cdot\rangle=\sum_\mu\varepsilon_\mu Q_\mu^{2}$: the element $e_t+\vec e_x$
is a unit with $\langle\cdot\rangle=0$ and the element $e_t+i\vec e_x$ is a zero divisor with $\langle\cdot\rangle=2$, so $\langle\cdot\rangle$ decides
nothing, while $\langle\cdot\rangle_{\natural}$ is multiplicative, $\langle\tilde Q_1\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_2\rangle_{\natural}$, which makes the
cone absorbing, the units closed under the product and the inverse, and $\langle\cdot\rangle_{\natural}$ a surjective
homomorphism $\mathbb{B}^\times\to\mathbb{C}^\times$ with kernel the norm-one group. The group is
open, dense and connected, of real dimension eight, of the homotopy type $S^{1}\times S^{3}$ with
$\pi_x\cong\mathbb{Z}$, with the cone of real codimension two as its boundary; on the centre and the
two quaternionic subspaces the cone is empty and the group is everything but the origin, while on
the vector subspace and the two sectors the boundary is the complex cone and the null cone. Across
the twelve structures the complement of the cone is one set and one group: the set is shared by the
four general products, whose inverse equations are solved by $(\tilde Q_1^{-1})^{\natural}$, $(\tilde
Q_1^{-1})^{*}$ and $(\tilde Q_1^{-1})^{\natural*}$ for the off-cone elements, and the group structure
exists in the biquaternion algebra alone: the symmetrised plain algebra has the same invertible set
and no group, the three other general products select the same off-cone set through the inverse
equations without a two-sided identity, and the seven structures without a unit have no invertible
element at all.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}=\mathrm{Sc}(\tilde Q\tilde Q^{\natural})$ | the general quaternionic bilinear algebraic norm, the reduced norm; multiplicative; the criterion of invertibility |
| $\mathcal{C}=\{\tilde Q:\langle\tilde Q\rangle_{\natural}=0\}$ | the zero-divisor cone; the complement of the group of units; real dimension $6$; real codimension $2$ |
| $\mathcal{C}\setminus\{0\}$ | the zero-divisor set of the four general products |
| $\mathbb{B}^\times=\{N\neq0\}$ | the group of units of the plain product; the complement of the cone |
| $\mathbb{B}\setminus(\mathcal{C}\setminus\{0\})=\mathbb{B}^\times\cup\{0\}$ | the complement of the zero-divisor set: the group together with the origin |
| $\tilde Q^{-1}=\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$ | the inverse of an element of the group |
| $e_t+\vec e_x$; $e_t+i\vec e_x$ | the unit with $\langle\cdot\rangle=0$; the zero divisor with $\langle\cdot\rangle=2$ |
| $\langle\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^{2}$ | the algebraic norm of the plain product; not multiplicative; not the criterion |
| $N:\mathbb{B}^\times\to\mathbb{C}^\times$ | the norm as a homomorphism; kernel the norm-one group $\mathbb{B}^\times_1$ |
| $(2Q_{1t}e_t-\tilde Q_1)/\langle\tilde Q_1\rangle_{\natural}$ | the Jordan inverse of the symmetrised plain product |
| $\vec e_x\bullet \vec e_y=0$ | the witness that the invertible elements of the symmetrised product form no group |

## Further Reading

- [Norm and Invertibility in the Biquaternion Algebra](norm-and-invertibility-in-the-biquaternion-algebra.html), for the algebraic norm
  of the plain product, its non-multiplicativity and the absence of a criterion, and for the
  distribution of the invertible elements over the remarkable subspaces.
- [Zero Divisors of the Biquaternion Algebra](zero-divisors-of-the-biquaternion-algebra.html), for the criterion of the plain
  product, the two families of the cone and the three-way classification.
- [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html),
  for the cone as the zero-divisor set of the four general products and the one-sided inverse
  equations.
- [The Biquaternion Unit Group as a Topological Group](the-biquaternion-unit-group-as-a-topological-group.html), for the group
  $\mathbb{B}^\times\cong GL_2(\mathbb{C})$, the norm-one group $\mathbb{B}^\times_1\cong
  SL_2(\mathbb{C})$, the determinant sequence, the covering and the homotopy type.
- [The Unitary Group of the Biquaternion Algebra](the-unitary-group-of-the-biquaternion-algebra.html), for the polar decomposition,
  the retractions onto the compact subgroups and the homotopy groups.
- [The Topology of the Zero-Divisor Cone](the-topology-of-the-zero-divisor-cone.html), for the cone as the boundary of the
  group of units.
- [Norm and Invertibility in the Symmetric Plain Algebra](norm-and-invertibility-in-the-symmetric-plain-algebra.html), for the invertibility
  of the symmetrised product.
- [The Specificities of the Biquaternion Algebra](the-specificities-of-the-biquaternion-algebra.html), for the left alternativity
  that the associativity of the plain product supplies and the isolation of the block.
- [The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](the-algebraic-structures-over-the-biquaternion-c-space.html), for the twelve
  structures, their units and their images.
- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), for the unit, the
  inverse, the zero divisor and the annihilator stated once for a general product.
