# __The Axis-Free Construction of the Quaternion Algebra__

## Introduction

**The claim.** The quaternion algebra is fixed by four units, one unit axiom, three equal squares, three anticommutations and three cyclic products. The three vector units enter that list in exactly the same way, so the construction names no direction, no base field and no imaginary unit.

**The route it improves on.** The doubling of *The Cayley–Dickson Construction of the Quaternion Algebra* builds the same algebra, correctly and completely. It also declares a base field $\mathbb{C}=\mathbb{R}[\vec e_z]$, then a doubling unit $\vec e_x$, and it computes the third unit, $\vec e_y=\vec e_z\vec e_x$. Three units that the algebra treats alike therefore enter the doubling in three different roles: one is a scalar field, one is a generator, one is an output. This article takes the other order. It declares the three alike and derives the table.

**Why the order is worth a separate article.** A construction is the page on which a reader learns what belongs to the object and what belongs to the way the object was reached. The doubling teaches that one direction is a field and another is a generator, and the algebra teaches no such thing. Nothing in the doubling is wrong. The cost is that the equality of the three squares, the cyclic symmetry of the table and the fact that the third unit carries no special role must all be re-derived, and a reader cannot tell from that page which features are the algebra's and which are the construction's. The axis-free route states them at the start, in the data.

**What is left over, and what it costs.** One bit. The table needs a cyclic order of the three units, and a cyclic order is an orientation, not a direction. §*What Is Free and What Is Fixed* shows that seven of the ten statements of the data are invariant under every permutation of the three units, that the remaining three are the cyclic ones, that the automorphisms of the algebra are exactly the rotations of the vector part, that a reflection is an anti-automorphism, and that the other cyclic order tabulates the opposite algebra, which the conjugation identifies with this one. The bit is therefore invisible.

**What the article contains.** §*The Data* states the four units and the two data on the vector part. §*The Product* gives the rule, first in the invariant form and then on the units, and states the ten equations the rule is equivalent to. §*The Table* prints the sixteen products and the three identities they satisfy. §*Associativity* proves associativity from the four left multipliers, which are signed permutation matrices of determinant one; that display is used as a proof and not as a picture. §*The First Properties* gives the unit, the centre, the conjugation, the norm, the inverse, the division property, the classes of element and the commutator. §*What Is Free and What Is Fixed* accounts for the symmetries. §*The Contrast with the Doubling* sets the two constructions side by side and states what each is good for.

**The overlap, declared.** The table and the list of properties below overlap *Quaternion Algebra* and the doubling article, and the overlap is deliberate. A construction must produce the object the other two articles use, and a reader who arrives from either of them must meet the same sixteen products. What is new here is the order of the argument, the associativity proof from the display, and the accounting of what is chosen and what is forced.

**Boundaries.** The algebra as an algebraic structure, with its vector subspaces and its Lie algebra, is *Quaternion Algebra*, above this article in this category. The doubling step, its nine derivations and the argument that fixes the twist are *The Cayley–Dickson Construction of the Quaternion Algebra*, beside this one. The classes of element are *The Specificities of the Quaternion Algebra*; the norm, its multiplicativity and the invertibility criterion it supplies are *Norm and Invertibility in the Quaternion Algebra*; the matrix models are *Quaternion Linear Representations* and *The Spin Group via $4\times4$ Real Matrices*. The same construction with the signs of two squares changed is *Split-Quaternion Algebra*, and the same construction on the biquaternion algebra is *The Axis-Free Construction of the Biquaternion Algebra*, in the Biquaternions category.

## The Data

### The Four Units

**One unit to a direction.** The algebra is written on a real vector space with four units, one for the scalar and one for each direction:

$$
e_t=1,\qquad \vec e_x,\qquad \vec e_y,\qquad \vec e_z .
$$

The scalar unit is $e_t$ and it is the number $1$. The three vector units are the quaternion units, the corpus's replacement for Hamilton's $i,j,k$. The arrow is the only mark that separates the scalar unit from a vector unit.

**The coefficients.** A coefficient carries the name of the direction it multiplies. The generic element is

$$
\tilde q=q_t e_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z=\sum_{\mu\in\{t,x,y,z\}} q_\mu e_\mu ,
$$

with the four coefficients real and the label on each coefficient naming the unit it multiplies. A pure element is one with $q_t=0$, and it is written $\vec q$.

**The names are labels and not data.** The letters $x,y,z$ name three directions of a three-dimensional space. Nothing in this article reads a physical direction into them, and §*What Is Free and What Is Fixed* proves that a permutation of the three labels produces the same algebra.

### The Vector Part and Its Two Data

**The splitting.** The underlying space is the direct sum

$$
\mathbb{H}=\mathbb{R}e_t\oplus V,\qquad V=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\},
$$

of real dimensions $1+3=4$. The scalar line and the vector part are the two objects the construction adds a product to, and the vector part carries the whole of the interest: the scalar line has one dimension and no choice in it.

**The first datum: an inner product.** The three units of $V$ are declared orthonormal,

$$
\vec e_\eta\cdot\vec e_\zeta=\delta_{\eta\zeta},
$$

and the inner product is extended bilinearly. It is the unit metric of *Algebra and Element Conventions*, positive definite, of inertia $(3,0)$ on $V$. This datum is invariant under every orthogonal map of $V$.

**The second datum: an orientation.** The cyclic order $x\to y\to z\to x$ is declared, equivalently the volume element $\vec e_x\wedge\vec e_y\wedge\vec e_z$, and the cross product is the one it defines,

$$
\vec e_x\times\vec e_y=\vec e_z,\qquad
\vec e_y\times\vec e_z=\vec e_x,\qquad
\vec e_z\times\vec e_x=\vec e_y,
$$

extended by antisymmetry and bilinearity. This datum is invariant under the rotations of $V$ and reverses under a reflection.

**Neither datum is a direction.** The inner product is one object and the orientation is another, and neither is a point of the unit sphere of $V$. A direction would be a unit vector, and naming one would be a datum of a different kind. The construction below names none.

### What the Data Do Not Contain

**No base field.** The construction does not begin with a subfield of the algebra other than the scalar line. In particular it does not begin with $\mathbb{C}=\mathbb{R}[\vec e_z]$, so no invertible element of $V$ is spent on a coefficient field.

**No imaginary unit and no doubling unit.** All three units of $V$ are declared at once, in one line, with the same square and the same relation to the other two. None is adjoined to another, and none is computed from another.

**No root of $-e_t$.** The roots of $-e_t$ in $\mathbb{H}$ are the unit sphere of $V$, a two-dimensional family, and the construction distinguishes no member of it. This is the sharp form of the claim of the article: the object that the doubling names at its first step, and that every frame of the corpus names later, is here a whole sphere.

**No array.** The construction is a product rule on four symbols. The display of the algebra appears only in §*Associativity*, where it is the instrument of a proof, and that display is the coefficient basis, whose diagonal is the four squares and which names no direction.

## The Product

### The Rule

**Definition.** For $\lambda,\mu\in\mathbb{R}$ and $\vec u,\vec v\in V$, the product is

$$
(\lambda e_t+\vec u)(\mu e_t+\vec v)=(\lambda\mu-\vec u\cdot\vec v)\,e_t+\lambda\vec v+\mu\vec u+\vec u\times\vec v ,
$$

with $\cdot$ the inner product and $\times$ the cross product of §*The Vector Part and Its Two Data*, extended to the whole algebra by bilinearity.

**The four terms, and what each is for.** The scalar term $\lambda\mu$ is the product of the scalar parts. The term $-\vec u\cdot\vec v$ is the collapse of two vector parts into the scalar line, and it is the only place the inner product is used. The two linear terms $\lambda\vec v+\mu\vec u$ say that the scalar line acts as the identity. The term $\vec u\times\vec v$ is the only place the orientation is used, and it is the reason the product is not commutative.

**Bilinearity.** The right side is linear in $(\lambda,\vec u)$ alone and in $(\mu,\vec v)$ alone, so the rule extends to a bilinear map $\mathbb{H}\times\mathbb{H}\to\mathbb{H}$, and by that extension it is defined on the whole algebra. Nothing else is assumed.

### The Rule on the Invertibles

**Proposition.** On two pure elements the rule reads

$$
\vec u\vec v=-\vec u\cdot\vec v\,e_t+\vec u\times\vec v ,
$$

so that the products of the four units are

$$
e_t e_\mu=e_\mu e_t=e_\mu,\qquad
\vec e_\eta^2=-e_t,\qquad
\vec e_\eta\vec e_\zeta=-\vec e_\zeta\vec e_\eta\ \ (\eta\neq\zeta),
$$

together with the three cyclic products $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$ and $\vec e_z\vec e_x=\vec e_y$.

*Proof.* The first display is the rule with $\lambda=\mu=0$, and it is the whole of the second: the inner product gives the square $\vec e_\eta\cdot\vec e_\eta=1$, hence $\vec e_\eta^2=-e_t$; it gives $\vec e_\eta\cdot\vec e_\zeta=0$ for distinct units, hence the product of two distinct units is pure; and the cross product of two distinct units is the third unit up to sign, antisymmetric in the pair. The cyclic products are the declared orientation. ∎

**The three squares are one equation written three times.** The data give $\vec e_\eta^2=-e_t$ for each of the three, and the three equations are the same equation with the label changed. This is the point the doubling cannot make at its start: there the three squares are three theorems, and they hold because the twist and the sign of the new unit happen to produce them.

### The Ten Statements

**The equivalence.** The product rule is equivalent to ten statements on the units: that $e_t$ is a two-sided unit; that each of the three vector units squares to $-e_t$; that each pair of distinct vector units anticommutes; and that the three cyclic products hold.

*Proof.* The rule gives the ten statements by evaluation on the pairs of invertibles, which is the proposition above. Conversely the ten statements fix all sixteen products: the seven involving $e_t$ by the unit axiom, the three squares, the six ordered products of distinct units by the three anticommutations and the three cyclic products. A bilinear map is fixed by its values on the sixteen pairs, so the ten statements fix the product. ∎

**Two of the four families are symmetric and two are not.** The unit axiom, the three squares and the three anticommutations are stated for the three units without distinction, and every permutation of the three leaves them unchanged. The three cyclic products are stated in one order, and they are invariant under the cyclic group of order three alone: a transposition turns $\vec e_x\vec e_y=\vec e_z$ into $\vec e_y\vec e_x=\vec e_z$, which is the negative of the anticommutation statement. The asymmetry of the table is exactly this, and it is nothing else.

### The Scalar–Vector Form

**Corollary.** For two general elements,

$$
\tilde q\tilde p=(q_tp_t-\vec q\cdot\vec p)\,e_t+q_t\vec p+p_t\vec q+\vec q\times\vec p ,
$$

and the scalar part of the product is symmetric in the two factors while the vector part is not.

*Proof.* Expand the rule with $\lambda=q_t$, $\vec u=\vec q$ and $\mu=p_t$, $\vec v=\vec p$. The scalar part is $q_tp_t-\vec q\cdot\vec p$ and the vector part is $q_t\vec p+p_t\vec q+\vec q\times\vec p$. ∎

**The reading.** The scalar part of a product of two elements carries the inner product of their vector parts, and the vector part carries the cross product. The two operations that a three-dimensional space supports are therefore not two structures imposed on the algebra: they are the two halves of one product. The square of a pure element, $\vec q^2=-\lvert\vec q\rvert^{2}e_t$, is the statement that a vector has no direction of its own, and it is the first thing the algebra says about the geometry of $V$.

## The Table

### The Sixteen Products

**The table.** The rows give the left factor and the columns the right factor.

| | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $-e_t$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $\vec e_y$ | $-\vec e_z$ | $-e_t$ | $\vec e_x$ |
| $\vec e_z$ | $\vec e_z$ | $\vec e_y$ | $-\vec e_x$ | $-e_t$ |

**The four blocks.** The table is one row and one column of the identity, one scalar diagonal $-e_t$ repeated three times, and a $3\times3$ block of the three vector units with signs. The block is antisymmetric, and the antisymmetry is the statement that the product is not commutative. No entry names a direction in a role another entry does not have: the three diagonal entries are equal, and the six off-diagonal entries are the three units in two signs each.

**The count.** Of the sixteen entries, one is $e_t$, six are the units themselves, three are $-e_t$, and six are invertible with a sign. The signs carry the whole of the asymmetry of the table.

### The Three Identities

**The product of the three units.** Multiplying the three vector units in cyclic order gives minus the identity,

$$
\vec e_x\vec e_y\vec e_z=-e_t ,
$$

and multiplying them out of cyclic order gives plus the identity, $\vec e_x\vec e_z\vec e_y=+e_t$.

*Proof.* $\vec e_x\vec e_y=\vec e_z$ and $\vec e_z\vec e_z=-e_t$. For the other order, $\vec e_x\vec e_y\vec e_z$ and $\vec e_x\vec e_z\vec e_y$ differ by the transposition of $\vec e_y$ and $\vec e_z$, which are distinct vector units and anticommute, so the second product is the negative of the first. ∎

**One equation for the four units.** The three squares and the triple product are one value,

$$
\vec e_x^2=\vec e_y^2=\vec e_z^2=\vec e_x\vec e_y\vec e_z=-e_t ,
$$

which is the compact statement of the table's scalar half. Every entry of the table is invertible with a sign, so the table is a statement about signs alone.

**The sign count.** The four scalar values above are the compact test of a table found in the literature: the three squares and the triple product must all equal $-e_t$, and the three cyclic products must hold in one cyclic order. A table that passes the first test and fails the second is the table of the opposite algebra, and a table with one square equal to $+e_t$ is the table of a split-quaternion algebra.

### What the Table Fixes and What It Leaves

**Fixed.** The sixteen products, hence the product of any two elements. The squares, hence the norm of a pure element and the sign that makes the algebra a division algebra. The anticommutations, hence the non-commutativity. The three cyclic products, hence the orientation.

**Left open.** The cyclic order, which is one bit. The names of the three units, which are labels. The signs of the three squares, which are not a labelling: with the three at $-e_t$ the algebra is this one, and with $\vec e_x^2=-e_t$ and $\vec e_y^2=\vec e_z^2=+e_t$ it is the split-quaternion algebra of *Split-Quaternion Algebra*, a different algebra and not a different tabulation of this one.

## Associativity

### The Four Left Multipliers

**The display.** Left multiplication by an element $\tilde q$ is the linear map $X\mapsto\tilde qX$. Read on the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, with the products $\tilde qe_\nu$ as columns, its matrix is

$$
L(\tilde q)=
\begin{pmatrix}
q_t&-q_x&-q_y&-q_z\\
q_x&q_t&-q_z&q_y\\
q_y&q_z&q_t&-q_x\\
q_z&-q_y&q_x&q_t
\end{pmatrix},
$$

the matrix $L_{\mathrm{axf}}(\tilde q)$ of *Matrix Representations Conventions*, and the four generators are

$$
L_x=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
L_y=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
L_z=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix},
$$

with $L_t=\mathrm I_4$. The display is the one of *The Spin Group via $4\times4$ Real Matrices*, and the proof below uses three of the properties that article records.

**Why this display and no other.** Each generator has exactly one nonzero entry in each row and each column, that entry $\pm1$, a zero diagonal and determinant $+1$. No generator is diagonal and no generator carries a direction: the three are the three signed permutations of one cycle, and a cyclic relabelling of the units permutes them. A display with a direction inside it would put one unit on the diagonal and two off it, and the proof would then be a proof about that unit. This one is not.

### The Display Is Multiplicative on the Basis

**Proposition.** The four generators satisfy

$$
L_x^2=L_y^2=L_z^2=-\mathrm I_4,\qquad
L_xL_y=L_z,\qquad L_yL_z=L_x,\qquad L_zL_x=L_y .
$$

*Proof.* Direct multiplication of the printed arrays. Each identity is an equality of four-by-four integer matrices, and each is checked entry by entry. ∎

**Corollary.** $L_{e_\mu}L_{e_\nu}=L_{e_\mu e_\nu}$ for all sixteen pairs of invertibles.

*Proof.* Seven pairs involve $L_t=\mathrm I_4$ and are trivial. Of the remaining nine, three are the squares and three are the cyclic products, which the proposition gives. The last three are the reverse-ordered products, and each is the negative of a cyclic product: $L_yL_x=-L_xL_y=-L_z=L_{yx}$, and likewise for $L_xL_z$ and $L_zL_y$. ∎

### Associativity

**Theorem.** The multiplication is associative, $(\tilde q_1\tilde q_2)\tilde q_3=\tilde q_1(\tilde q_2\tilde q_3)$.

*Proof.* The map $\tilde q\mapsto L(\tilde q)$ is linear, and on the basis it is multiplicative by the corollary, so it is multiplicative everywhere: for $\tilde q=\sum_\mu q_\mu e_\mu$ and $\tilde p=\sum_\nu p_\nu e_\nu$,

$$
L(\tilde q)L(\tilde p)=\sum_{\mu,\nu}q_\mu p_\nu L_{e_\mu}L_{e_\nu}=\sum_{\mu,\nu}q_\mu p_\nu L_{e_\mu e_\nu}=L(\tilde q\tilde p),
$$

the last equality because $\tilde q\tilde p$ is by definition the bilinear extension of the products of invertibles. Then $L(\tilde q\tilde p)$ is left multiplication by $\tilde q\tilde p$, so

$$
(\tilde q\tilde p)\tilde r=L(\tilde q\tilde p)\tilde r=L(\tilde q)L(\tilde p)\tilde r=L(\tilde q)(\tilde p\tilde r)=\tilde q(\tilde p\tilde r). 
$$

**What the proof uses.** The sixteen products of the table, the four printed arrays, and nothing else — no model, no array of a general element, no ideal, no root. The display of §*The Four Left Multipliers* is the axis-free display, and the fact that associativity is proved inside it is the reason that display is used throughout the corpus.

### The Check

**The sixty-four triples.** The two sides of the associativity identity were evaluated on the sixty-four triples of basis elements in integer arithmetic, so that no rounding enters: the number of mismatches is $0$.

**One hundred elements.** The same identity on one hundred random real elements gave a largest residual of $2.7\times10^{-15}$ in double precision, which is the rounding of the arithmetic and not a failure of the identity.

**The multiplicativity of the display.** The sixteen identities $L_{e_\mu}L_{e_\nu}=L_{e_\mu e_\nu}$ were checked as integer matrix equalities, again with no rounding and no mismatch, and the three cyclic relations and the three squares of the proposition were checked the same way. The four determinants of the generators are $+1$ exactly.

### The Algebra Axioms

**Theorem.** With this multiplication $\mathbb{H}$ is a four-dimensional associative unital non-commutative real algebra, and every nonzero element is invertible.

*Proof.* Associativity is the theorem above. The unit is $e_t$, by the first row and column of the table. Non-commutativity is $\vec e_x\vec e_y=\vec e_z\neq-\vec e_z=\vec e_y\vec e_x$. The dimension is four by the declared basis. Invertibility is the theorem of §*The Inverse and the Division Property*. ∎

**The four general products.** The corpus writes four general products on a quaternion algebra: the plain one, the two sesquilinear ones, and the pair of symmetrised and antisymmetrised halves. Only the plain one is associative with a unit, and it is the one tabulated above. The symmetrised half is commutative and not associative, since $(\vec e_x\bullet\vec e_x)\bullet\vec e_z=-\vec e_z$ while $\vec e_x\bullet(\vec e_x\bullet\vec e_z)=0$. The antisymmetrised half has no unit, since $[\tilde q,e_t]=0$ for every $\tilde q$. The two sesquilinear products fail associativity on the algebra as a whole. The comparison is *The Four General Products and Their Relations over the Biquaternion Algebra*, and it is not repeated here; what matters for this article is that the product built above is the algebra's own, and not a product chosen among several.

## The First Properties

### The Unit and the Centre

**Theorem.** The centre of $\mathbb{H}$ is the scalar line $\mathbb{R}e_t$.

*Proof.* The scalar line is central because $e_t$ is the unit. Conversely let $\tilde q=q_te_t+\vec q$ commute with every element. It commutes with each vector unit, and the commutator of two elements with vector parts $\vec q$ and $\vec e_\eta$ is

$$
[\tilde q,\vec e_\eta]=2\,\vec q\times\vec e_\eta ,
$$

whose scalar part vanishes and whose vector part is the cross product. So $\vec q\times\vec e_x=0$ and $\vec q\times\vec e_y=0$. A vector orthogonal to two independent vectors is zero, so $\vec q=0$. ∎

**The reading.** The centre is one-dimensional, so the algebra is not commutative and not of the form $M_n(K)$ for a field $K$ larger than $\mathbb{R}$: a matrix algebra carries its coefficient field as its centre. The centre of the group of invertibles is $\mathbb{R}^{\times}e_t$ by the same computation, and the two statements are one.

### The Conjugation and the Two Subspaces

**Definition.** The conjugation is the linear map that fixes $e_t$ and negates the three vector units,

$$
\tilde q^{\natural}=q_te_t-q_x\vec e_x-q_y\vec e_y-q_z\vec e_z .
$$

**Proposition.** The conjugation is an involution, it reverses the order of a product, and its fixed space is $\mathbb{R}e_t$ while its anti-fixed space is $V$.

*Proof.* The involution and the two fixed spaces are read from the definition. The order reversal is checked on the sixteen pairs of invertibles: each product is invertible with a sign, the conjugation negates the three vector units, and the two sides agree on every pair; bilinearity extends the identity to all elements. ∎

**The two subspaces, and the third conjugation.** The decomposition $\mathbb{H}=\mathbb{R}e_t\oplus V$ is the eigenspace decomposition of ${}^{\natural}$ for the eigenvalues $+1$ and $-1$, and the projections are $\tfrac12(\tilde q\pm\tilde q^{\natural})$. Two companion maps exist, $-\tilde q^{\natural}$ and $-\tilde q$, and with the identity they form a group of order four. The conjugation is the only member of that group that reverses the order of a product: negating the product is not an order reversal, and negating the conjugate is not one either. The catalogue of the four maps and of the classes of element they cut out is *The Specificities of the Quaternion Algebra*.

### The Norm

**Definition.** The quaternion norm is $\langle\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}$.

**Proposition.** $\langle\tilde q\rangle_{\natural}=\tilde q^{\natural}\tilde q=q_t^2+q_x^2+q_y^2+q_z^2$, a real scalar, non-negative, and zero only at $\tilde q=0$.

*Proof.* The product $\tilde q\tilde q^{\natural}$ is computed from the scalar–vector form: the scalar part is $q_t^2+\lvert\vec q\rvert^{2}$, and the vector part is $q_t(-\vec q)+q_t\vec q+\vec q\times(-\vec q)=0$. The other order agrees because the value is a real scalar and the scalar line is central. The sum of four squares is non-negative, and it vanishes only when the four coefficients do. ∎

**Theorem.** The norm is multiplicative, $\langle\tilde q_1\tilde q_2\rangle_{\natural}=\langle\tilde q_1\rangle_{\natural}\langle\tilde q_2\rangle_{\natural}$.

*Proof.* Using the order reversal of ${}^{\natural}$ and the centrality of the value,

$$
\langle\tilde q_1\tilde q_2\rangle_{\natural}
=\tilde q_1\tilde q_2(\tilde q_1\tilde q_2)^{\natural}
=\tilde q_1\tilde q_2\tilde q_2^{\natural}\tilde q_1^{\natural}
=\tilde q_1\langle\tilde q_2\rangle_{\natural}\tilde q_1^{\natural}
=\langle\tilde q_1\rangle_{\natural}\langle\tilde q_2\rangle_{\natural}. 
$$

**The check.** The identity on one hundred random real pairs gave a largest residual of $1.4\times10^{-14}$, and the sum-of-squares reading on one hundred random elements a largest residual of $4.4\times10^{-16}$.

### The Inverse and the Division Property

**Theorem.** Every nonzero element is invertible, with two-sided inverse

$$
\tilde q^{-1}=\frac{\tilde q^{\natural}}{\langle\tilde q\rangle_{\natural}} .
$$

*Proof.* The norm is a positive real number for $\tilde q\neq0$, so the quotient is defined, and $\tilde q\tilde q^{\natural}=\tilde q^{\natural}\tilde q=\langle\tilde q\rangle_{\natural}$ gives $\tilde q\tilde q^{-1}=\tilde q^{-1}\tilde q=e_t$. ∎

**Corollary.** $\mathbb{H}$ has no zero divisors, no nonzero nilpotent and no idempotent other than $0$ and $e_t$.

*Proof.* A zero divisor $\tilde q$ would have a nonzero annihilator, and multiplying $\tilde q\tilde p=0$ by $\tilde q^{\natural}$ gives $\langle\tilde q\rangle_{\natural}\tilde p=0$, hence $\tilde p=0$. A nilpotent has zero norm, because $\langle\tilde q^k\rangle_{\natural}=\langle\tilde q\rangle_{\natural}^{k}$. An idempotent satisfies $\langle\tilde\Pi_{\mathrm{id}}\rangle_{\natural}=\langle\tilde\Pi_{\mathrm{id}}^2\rangle_{\natural}=\langle\tilde\Pi_{\mathrm{id}}\rangle_{\natural}^{2}$, so its norm is $0$ or $1$, and the first case is $\tilde\Pi_{\mathrm{id}}=0$ while the second forces all three vector coefficients to vanish and $q_t^2=q_t$. ∎

**The check.** The inverse identity on one hundred random elements, both sides, gave a largest residual of $2.2\times10^{-16}$; one hundred random real elements were tested against the idempotent equation and none satisfied it, the two solutions of the corollary aside.

### The Classes of Element

**The roots of $-e_t$ are the unit sphere.** An element $\tilde\zeta=q_te_t+\vec q$ satisfies $\tilde\zeta^2=-e_t$ exactly when $q_t=0$ and $\lvert\vec q\rvert=1$, so the roots of minus the unit form the unit sphere of $V$, of real dimension two.

*Proof.* The square is $(q_t^2-\lvert\vec q\rvert^{2})e_t+2q_t\vec q$. The vector part vanishes when $q_t=0$ or $\vec q=0$; the second case would need $q_t^2=-1$, which has no real solution; the first needs $-\lvert\vec q\rvert^{2}=-1$. ∎

**This is the article's claim in one object.** There is a two-sphere of roots of $-e_t$ and no member of it is distinguished, because the automorphisms of the algebra act on that sphere transitively (§*The Automorphisms Are the Rotations*). The doubling enters the same sphere at one point, $\vec e_z$, and derives the other two directions from it.

**The roots of $+e_t$ are the two signs of the unit.** An element with square $+e_t$ is $\pm e_t$. The same computation gives $q_t^2-\lvert\vec q\rvert^{2}=1$ and $2q_t\vec q=0$; the second equation leaves $q_t=0$ or $\vec q=0$; the first then reads $-\lvert\vec q\rvert^{2}=1$ in the first case, which is impossible, and $q_t^2=1$ in the second.

**The classes, in one table.**

| class | equation | the set |
|---|---|---|
| units | $\langle\tilde q\rangle_{\natural}\neq0$ | the complement of the origin |
| zero divisors | $\langle\tilde q\rangle_{\natural}=0$ | none |
| idempotents | $\tilde q^2=\tilde q$ | $\{0,e_t\}$ |
| nilpotents | $\tilde q^2=0$ | $\{0\}$ |
| roots of $-e_t$ | $\tilde q^2=-e_t$ | the unit sphere of $V$ |
| roots of $+e_t$ | $\tilde q^2=+e_t$ | $\{\pm e_t\}$ |

**The check.** One hundred random unit vectors of $V$ squared to $-e_t$ with a largest residual of $4.4\times10^{-16}$, and a vector of length $1.3$ squared to $-1.69\,e_t$, so the condition on the length is not decorative.

### The Commutator and the Lie Algebra

**Proposition.** For two pure elements, $[\vec u,\vec v]=2\,\vec u\times\vec v$, and for two general elements,

$$
[\tilde q,\tilde p]=2\,\vec q\times\vec p .
$$

*Proof.* The commutator of the two products cancels the symmetric terms of the scalar–vector form and leaves twice the cross-product term. ∎

**The consequences.** The vector part is closed under the bracket, so it is a Lie subalgebra, and with the bracket it is $\mathfrak{so}(3)$: the cross product is the adjoint action, and the identity $\vec u\times(\vec v\times\vec w)=\vec v(\vec u\cdot\vec w)-\vec w(\vec u\cdot\vec v)$ is the Jacobi identity read on $V$. The bracket of an element with itself vanishes, and the scalar part never enters the bracket: the commutator is a map $V\wedge V\to V$ and nothing else.

**The check.** The identity was evaluated on one hundred random pairs of vectors, exact residual $0$, and on one hundred random pairs of general real elements, where the commutator agreed with $2\vec q\times\vec p$ to $2.2\times10^{-16}$.

### The Two-Sided Ideals

**Theorem.** $\mathbb{H}$ has no two-sided ideal other than $0$ and $\mathbb{H}$.

*Proof.* Let $I$ be a two-sided ideal and take $0\neq a\in I$. Then $a^{\natural}a=\langle a\rangle_{\natural}e_t\in I$, and the norm is a positive real number, so $e_t\in I$ and $I=\mathbb{H}$. ∎

**The reading.** The algebra is simple, and it is the only simple associative algebra of dimension four over $\mathbb{R}$ other than the matrix algebra $M_2(\mathbb{R})$. The two are distinguished by the division property, which is the next article's subject, and by the centre of the group of invertibles.

## What Is Free and What Is Fixed

### The Seven Statements Are Invariant

**The invariance.** Seven of the ten statements of §*The Ten Statements* are invariant under every permutation of the three vector units: the unit axiom, the three squares and the three anticommutations. A permutation that renames the three units therefore maps a tabulation of the algebra to a tabulation of the algebra, with the same sixteen products up to the renaming.

**What this buys.** A reader who is told that $\vec e_x$ is the diagonal one, or that $\vec e_z$ is the axis, is being told something about a page and not about the algebra. The seven statements cannot express such a distinction, and no consequence of them can either.

### The Tenth Statement Is the Orientation

**The residue.** The three cyclic products are the only asymmetric part of the data, and they are the two-valued choice of orientation of $V$. One bit.

**The comparison with a direction.** A direction would be a point of the unit sphere of $V$, and the sphere has two dimensions. An orientation has no continuous parameter. The choice the construction makes is therefore strictly smaller than the choice of a root of $-e_t$, and it is of a different kind: it is the choice of which of the two cyclic orders is written plus.

### The Automorphisms Are the Rotations

**Theorem.** The automorphisms of $\mathbb{H}$ are exactly the maps that fix $e_t$ and act on $V$ by a rotation, so $\operatorname{Aut}(\mathbb{H})\cong SO(3)$.

*Proof.* Let $\phi$ be an automorphism. It fixes $e_t$, because the unit is the unique two-sided identity. It preserves the property of being a negative multiple of $e_t$, so it maps $V=\{0\}\cup\{u:u^2\in\mathbb{R}_{<0}e_t\}$ to itself. On $V$ it preserves squares, hence the inner product read from $\vec u^2=-\lvert\vec u\rvert^{2}e_t$, and it preserves products, hence the cross product and the orientation. So $\phi|_V$ is a rotation. Conversely a rotation $R$ of $V$, extended by the identity on $e_t$, preserves the inner product and satisfies $Ru\times Rv=(\det R)\,R(u\times v)=R(u\times v)$, so it preserves the product rule and is an automorphism. ∎

**The corollary.** The automorphism group acts transitively on the unit sphere of $V$, so no root of $-e_t$ is an invariant of the algebra. A statement that names one is a statement about a frame.

### A Reflection Is an Anti-Automorphism

**Proposition.** Let $T$ be a reflection of $V$, extended by the identity on $e_t$. Then $T(\tilde q\tilde p)=T(\tilde p)T(\tilde q)$ for all elements, and $T$ is not an automorphism.

*Proof.* For orthogonal $T$ and any two vectors, $Tu\times Tv=(\det T)\,T(u\times v)$, so a reflection reverses the cross product: $Tu\times Tv=-T(u\times v)$. In the product rule the scalar terms are unchanged and the only term that changes is the cross product, which changes sign; the same sign appears on the other side when the two factors are exchanged, because $Tv\times Tu=-T(v\times u)=+T(u\times v)$. The two sides therefore agree. A reflection fails to be an automorphism because $T(\vec e_x\vec e_y)=T(\vec e_z)$ while $T(\vec e_x)T(\vec e_y)=\vec e_y\vec e_x=-\vec e_z$. ∎

**The reading.** The symmetry group of the tabulation is the full orthogonal group: its rotations are automorphisms and its reflections are anti-automorphisms. A reflection is the operation that reverses the cyclic order, and the proposition says that reversing the cyclic order reverses the product and nothing else.

**The check.** A transposition of two units gave an anti-automorphism with a largest residual of $8.9\times10^{-16}$ over one hundred random pairs, and the same transposition read as an automorphism failed with a residual of $16.1$, so the two statements are not interchangeable.

### The Other Orientation Is the Opposite Algebra

**The proposition.** Tabulating with the other cyclic order, $\vec e_x\vec e_y=-\vec e_z$, produces the opposite algebra $\mathbb{H}^{\mathrm{op}}$, in which every product is the product of this article read backwards.

**Corollary.** The two tabulations give isomorphic algebras, and the isomorphism is the conjugation.

*Proof.* The conjugation reverses the order of a product and is an involution, so it is an isomorphism $\mathbb{H}\to\mathbb{H}^{\mathrm{op}}$ and an isomorphism back. ∎

**The consequence.** The one bit the construction leaves costs nothing: the algebra built from the other orientation is this algebra, with the labels read through ${}^{\natural}$. A construction that spends a direction cannot make that statement, because a direction is not absorbed by an anti-automorphism.

### No Axis, and No Root Distinguished

**The account.** The data are four units, one inner product and one orientation. The three vector units occur in the axioms in the same way, the seven symmetric statements cannot name one of them, the roots of $-e_t$ form a sphere on which the automorphism group acts transitively, and the only choice left is one bit that the conjugation absorbs.

**What this does not claim.** It does not claim that the algebra has no directions; it has three, and every element with a unit vector part names one. It claims that the construction does not name one, and that no statement derived from the construction can prefer one.

## The Contrast with the Doubling

### The Three Roles

**The doubling in one paragraph.** The doubling of *The Cayley–Dickson Construction of the Quaternion Algebra* begins with the complex algebra $\mathbb{C}=\mathbb{R}[\vec e_z]$, adjoins an invertible element $\vec e_x$ with the square $-e_t$ and the twisting rule $\vec e_xw=\bar w\vec e_x$, and reads the third unit off the product, $\vec e_y=\vec e_z\vec e_x$. The three units enter as a base field, a generator and an output.

**Why that is a defect of presentation and not of mathematics.** The doubling proves three things the axis-free route assumes: that the twist is forced by the absence of zero divisors, that the third unit is computed rather than chosen, and that the signs of the ordered products are not conventions. Those are results, and the axis-free route cannot supply them, because it takes the table as data. A reader who wants to know why the table has these signs and not others must read the doubling.

**The asymmetry, stated exactly.** The twisting rule mentions $\vec e_z$ inside $\bar w$ and $\vec e_x$ outside it, and it does not mention $\vec e_y$ at all. The axiom set of the doubling is therefore asymmetric by construction, and the symmetry of the resulting table is a theorem about that axiom set. The axis-free route begins with a symmetric axiom set and obtains the table directly.

### The One Bit

**The two choices, compared.**

| | the doubling | the axis-free construction |
|---|---|---|
| declared first | a base field $\mathbb{C}=\mathbb{R}[\vec e_z]$ | the four units and the product rule |
| the role of $\vec e_z$ | the imaginary unit of the base | one of three units |
| the role of $\vec e_x$ | the doubling unit | one of three units |
| the role of $\vec e_y$ | computed, $\vec e_z\vec e_x$ | one of three units |
| what is derived | the three squares, the anticommutations, the cycle | the table, from the ten statements |
| what is chosen | a root of $-e_t$, then a transverse unit | a cyclic order |
| the size of the choice | a point of the two-sphere, then a direction | one bit |
| what is proved | the twist is forced, the third unit is computed | associativity, division, the automorphism group |
| taken as data | the base field and the twist | the ten statements on the units |

**The reading of the table.** The two routes prove different things about the same object, and neither replaces the other. The doubling answers the question why the table is what it is. The axis-free construction answers the question what the table is, with the fewest and the most symmetric data, and it is the route to take when the table is the starting point rather than the conclusion.

### What the Doubling Is For

**The ladder.** The doubling is the only route that shows where the construction stops: the next rung gives the octonions, where associativity fails, and the rung after that gives zero divisors of a new kind. That ladder, its saturation and the Hurwitz theorem are *Quadratic Forms over Algebras and Norms*, §*The Cayley–Dickson Doubling*.

**The zero divisors.** The doubling is also the route that exhibits the alternative: with the plain rule instead of the twist, the element $\vec e_z\vec e_x$ squares to $+e_t$ and the algebra carries two non-zero orthogonal idempotents. That argument is the doubling article's, and it has no counterpart here, because the axis-free construction never has the plain rule in view.

**The division property.** The doubling proves it from the norm of a doubled element; this article proves it from the norm of the element itself, in one line, because the norm is a sum of four squares by construction. The two proofs are the same proof read at different depths.

## Summary

The quaternion algebra is fixed by four units and ten statements: that $e_t$ is a two-sided unit, that each of the three vector units squares to $-e_t$, that distinct vector units anticommute, and that the three cyclic products hold. The product rule in the invariant form uses an inner product and an orientation on the three-dimensional vector part, and it reads

$$
(\lambda e_t+\vec u)(\mu e_t+\vec v)=(\lambda\mu-\vec u\cdot\vec v)\,e_t+\lambda\vec v+\mu\vec u+\vec u\times\vec v .
$$

The three vector units enter the data in the same way, so the construction names no direction. Seven of the ten statements are invariant under every permutation of the three units, and the three cyclic products are the orientation, one bit. The automorphisms are the rotations of the vector part, a reflection is an anti-automorphism, and the other cyclic order tabulates the opposite algebra, which the conjugation identifies with this one. The bit therefore costs nothing.

Associativity is proved inside the coefficient display. The four left multipliers are signed permutation matrices of determinant one, with zero diagonal, and they satisfy $L_x^2=L_y^2=L_z^2=-\mathrm I_4$ and $L_xL_y=L_z$ cyclically; from those sixteen identities the display is multiplicative, and multiplicativity of the display is associativity of the product. The proof uses no model, no ideal and no root.

The first properties follow in a few lines each: the centre is the scalar line, the conjugation reverses the order and splits the algebra into the scalars and the vector part, the norm is the sum of four squares and is multiplicative, every nonzero element is invertible with inverse $\tilde q^{\natural}/\langle\tilde q\rangle_{\natural}$, the algebra has no zero divisors, no nonzero nilpotent and no idempotent beyond $0$ and $e_t$, the commutator of two elements is twice the cross product of their vector parts, and the algebra is simple. The roots of $-e_t$ form the unit sphere of the vector part, a two-sphere with no distinguished point. That sphere is the object the doubling enters at a single point, and it is the sharpest statement of what this construction does not choose.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}=\mathbb{R}e_t\oplus V$ | the quaternion algebra, as a scalar line plus a three-dimensional vector part |
| $e_t=1$ | the scalar unit, the two-sided identity |
| $\vec e_x,\vec e_y,\vec e_z$ | the three vector units, orthonormal and positively oriented |
| $\tilde q=q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ | the generic quaternion, coefficients real |
| $\vec q$ | the vector part, a pure element |
| $\vec u\cdot\vec v$ | the inner product of the vector part, the unit metric |
| $\vec u\times\vec v$ | the cross product the orientation fixes |
| the ten statements | the unit axiom, the three squares, the three anticommutations, the three cyclic products |
| the seven symmetric statements | the ten less the three cyclic products; invariant under every permutation of the three units |
| $\tilde q^{\natural}=q_te_t-q_x\vec e_x-q_y\vec e_y-q_z\vec e_z$ | the conjugation, an order-reversing involution |
| $\langle\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}=q_t^2+q_x^2+q_y^2+q_z^2$ | the quaternion norm |
| $L(\tilde q)$, $L_x,L_y,L_z$ | left multiplication and its three generators, the axis-free display |
| $\operatorname{Aut}(\mathbb{H})\cong SO(3)$ | the automorphisms, the rotations of the vector part |
| $T$ | a reflection of $V$, an anti-automorphism of the algebra |
| $\mathbb{H}^{\mathrm{op}}$ | the opposite algebra, tabulated by the other cyclic order |

## Further Reading

- [Quaternion Algebra](quaternion-algebra.html), for the algebra as a structure, the three conjugations, the three fixed-point subspaces and the Lie algebra of the vector part.
- [The Cayley–Dickson Construction of the Quaternion Algebra](the-cayley-dickson-construction-of-the-quaternion-algebra.html), for the doubling route, the nine derivations of the table and the argument that fixes the twist.
- [The Specificities of the Quaternion Algebra](the-specificities-of-the-quaternion-algebra.html), for the classes of element and the Frobenius and Hurwitz theorems.
- [Norm and Invertibility in the Quaternion Algebra](norm-and-invertibility-in-the-quaternion-algebra.html), for the norm as a quadratic form, its polarisation and the group of invertibles.
- [The Spin Group via $4\times4$ Real Matrices](the-spin-group-via-4x4-real-matrices.html), for the left regular display, the four properties of its generators and the group they generate.
- [Matrix Representations Conventions](matrix-representations-conventions.html), for the axis-free array and the reason the coefficient basis is the one that names no direction.
- [Split-Quaternion Algebra](split-quaternion-algebra.html), for the same construction with one square changed, and the three idempotents it then carries.
- [The Axis-Free Construction of the Biquaternion Algebra](the-axis-free-construction-of-the-biquaternion-algebra.html), in the Biquaternions category, for the same route taken with complex coefficients.
- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original table and the words the corpus keeps.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the doubling ladder and the classification of the real division algebras.
